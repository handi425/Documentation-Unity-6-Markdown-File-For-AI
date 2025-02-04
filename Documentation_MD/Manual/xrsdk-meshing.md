[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-meshing.html)
  * [中文](/cn/current/Manual/xrsdk-meshing.html)
  * [日本語](/ja/current/Manual/xrsdk-meshing.html)
  * [한국어](/kr/current/Manual/xrsdk-meshing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-meshing.html)
  * [中文](/cn/current/Manual/xrsdk-meshing.html)
  * [日本語](/ja/current/Manual/xrsdk-meshing.html)
  * [한국어](/kr/current/Manual/xrsdk-meshing.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * [Subsystems](xrsdk-subsystems-landing.html)
  * XR SDK Meshing subsystem

[](xrsdk-display.html)

XR SDK Display subsystem

[](xrsdk-pre-init-interface.html)

XR SDK PreInit interface

# XR SDK Meshing subsystem

The Meshing subsystem extracts **mesh** The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) data from an external Provider and
converts it to a [UnityEngine.Mesh](../ScriptReference/Mesh.html). It can also
generate an optional
[UnityEngine.MeshCollider](../ScriptReference/MeshCollider.html) without
incurring any main thread stalls.

The main use case for the Meshing subsystem is to surface procedurally-
generated meshes, generally from a **spatial mapping** The process of mapping
real-world surfaces into the virtual world.  
See in [Glossary](Glossary.html#SpatialMapping) algorithm like the one
generated from a depth **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). There is no limit on the size of the
mesh, or the frequency of updates.

Mesh generation occurs asynchronously on a background thread, so extracting
data from an external provider doesn’t block the main thread to, for example,
bake the mesh **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).

## Control flow

The Meshing subsystem has two basic queries:

  * Get the state of all tracked meshes (for example, New, Changed, Unchanged, Removed).
  * Generate a particular mesh. Meshes are identified using the [MeshId](../ScriptReference/XR.MeshId.html) identifier.

### Getting MeshInfos

C# users can get the mesh infos from the `XRMeshSubsystem` instance method:

    
    
    public bool TryGetMeshInfos(List<MeshInfo> meshInfosOut);
    

This maps directly to the C call to `UnityXRMeshProvider::GetMeshInfos` and is
typically called once per frame to obtain the current list of tracked meshes.

The following C implementation can use the provided `allocator` object to
allocate an array of `UnityXRMeshInfo`s which it should then fill out:

    
    
    UnitySubsystemErrorCode(UNITY_INTERFACE_API * GetMeshInfos)(
            UnitySubsystemHandle handle, void* pluginData, UnityXRMeshInfoAllocator * allocator);
    

The allocated memory is owned by Unity (typically using a stack allocator, so
allocations are very fast):

    
    
    typedef struct UnityXRMeshInfo
    {
        UnityXRMeshId meshId;
        bool updated;
        int priorityHint;
    } UnityXRMeshInfo;
    

If nothing has changed since the last call to
[TryGetMeshInfos](../ScriptReference/XR.XRMeshSubsystem.TryGetMeshInfos.html),
you can return false to avoid filling out the array each frame.

**Field** | **Description**  
---|---  
**meshId** | A 128-bit unique identifier. The Provider generates these values, which can be a pointer to mesh data, but you need to be able to generate a specific mesh by its ID.  
**updated** | The only state Unity needs is whether the mesh has been updated since the last time it was generated. Determining whether the mesh was added or removed is done automatically; reporting the existence of a mesh that Unity doesn’t know about is surfaced as Added, while not reporting a mesh that was previously reported marks the mesh as Removed.  
**priorityHint** | C# interprets this value, but you might want to, for example, provide a C# component that prioritizes which mesh to generate based on it. Unity doesn’t use this value.  
  
In C#,
[TryGetMeshInfos](../ScriptReference/XR.XRMeshSubsystem.TryGetMeshInfos.html)
populates a `List<MeshInfo>`, which includes the [mesh
state](../ScriptReference/XR.MeshChangeState.html):

    
    
    public enum MeshChangeState
    {
        Added,
        Updated,
        Removed,
        Unchanged
    }
    

Based on the mesh change state and the priority hint value, a C# component can
then decide which mesh(es) to generate next.

### Mesh generation

From C#, you can generate a specific mesh asynchronously using the
[XRMeshSubsystem](../ScriptReference/XR.XRMeshSubsystem.GenerateMeshAsync.html)
instance method:

    
    
    public extern void GenerateMeshAsync(
        MeshId meshId,
        Mesh mesh,
        MeshCollider meshCollider,
        MeshVertexAttributes attributes,
        Action<MeshGenerationResult> onMeshGenerationComplete);
    

This enqueues a mesh for generation. You can enqueue as many meshes as you
need, but you might want to limit the number of meshes that are concurrently
generated to a few at a time.

Unity always calls the provided `onMeshGenerationComplete` delegate, even if
an error occurs.

Meshes are generated in two phases, following an acquire and release model:

![](../uploads/Main/acquire_release.png)

    
    
    UnitySubsystemErrorCode(UNITY_INTERFACE_API * AcquireMesh)(
        UnitySubsystemHandle handle,
        void* pluginData,
        const UnityXRMeshId * meshId,
        UnityXRMeshDataAllocator * allocator);
    

`AcquireMesh` is called on a background thread, so you can do as much
processing in this method as you like, including computationally-intensive
work such as generating the mesh itself. This function can return immediately
or span several frames.

If you provide a `MeshCollider` to `GenerateMeshAsync`, Unity also computes
the MeshCollider’s acceleration structure (“Bake Physics” in the above
diagram). This can be time-consuming for large meshes, so it also occurs on
the worker thread.

Finally, when the data is ready, Unity writes it to the `UnityEngine.Mesh`
and/or `UnityEngine.MeshCollider` on the main thread. Afterwards, Unity calls
`ReleaseMesh`, also on the main thread:

    
    
    UnitySubsystemErrorCode(UNITY_INTERFACE_API * ReleaseMesh)(
        UnitySubsystemHandle handle,
        void* pluginData,
        const UnityXRMeshId * meshId,
        const UnityXRMeshDescriptor * mesh,
        void* userData);
    

Because`ReleaseMesh` is called on the main thread, it should return quickly.
Typically, this is used to free resources allocated during `AcquireMesh`.

### Memory management

`AcquireMesh` offers two means of providing mesh data to Unity: Unity-managed
and provider-managed.

#### Unity-managed memory

To let Unity manage the memory, use:

    
    
    UnityXRMeshDescriptor* (UNITY_INTERFACE_API * MeshDataAllocator_AllocateMesh)(
        UnityXRMeshDataAllocator * allocator,
        size_t vertexCount,
        size_t indexCount,
        UnityXRIndexFormat indexFormat,
        UnityXRMeshVertexAttributeFlags attributes,
        UnityXRMeshTopology topology);
    

This returns a struct with pointers to buffers based on an intersection of
these `attributes` and the vertex attributes requested from C#. The provider
should then copy the appropriate data to the buffers.

When you use this paradigm, you don’t have to free the memory, because Unity
will recycle the memory after the call to `ReleaseMesh`.

#### Provider-managed memory

Instead of letting Unity manage the memory, you can point it at your own data.
The data must remain valid until `ReleaseMesh` is called.

Use `MeshDataAllocator_SetMesh` to provide your own `UnityXRMeshDescriptor`
whose non-null pointers point to valid data:

    
    
    void(UNITY_INTERFACE_API * MeshDataAllocator_SetMesh)(
        UnityXRMeshDataAllocator * allocator, const UnityXRMeshDescriptor * meshDescriptor);
    

#### User data

Your `AcquireMesh` implementation can call:

    
    
    void(UNITY_INTERFACE_API * MeshDataAllocator_SetUserData)(
        UnityXRMeshDataAllocator * allocator, void* userData);
    

Unity passes the `userData` pointer back to your `ReleaseMesh` implementation.
This is particularly useful when you’re using provider-managed memory.

## Example C# component

    
    
    void Update()
    {
        if (s_MeshSubsystem.TryGetMeshInfos(s_MeshInfos))
        {
            foreach (var meshInfo in s_MeshInfos)
            {
                switch (meshInfo.ChangeState)
                {
                    case MeshChangeState.Added:
                    case MeshChangeState.Updated:
                        AddToQueueIfNecessary(meshInfo);
                        break;
    
                    case MeshChangeState.Removed:
                        RaiseMeshRemoved(meshInfo.MeshId);
    
                        // Remove from processing queue
                        m_MeshesNeedingGeneration.Remove(meshInfo.MeshId);
    
                        // Destroy the GameObject
                        GameObject meshGameObject;
                        if (meshIdToGameObjectMap.TryGetValue(meshInfo.MeshId, out meshGameObject))
                        {
                            Destroy(meshGameObject);
                            meshIdToGameObjectMap.Remove(meshInfo.MeshId);
                        }
    
                        break;
    
                    default:
                        break;
                }
            }
        }
    
        // ...
    
        while (m_MeshesBeingGenerated.Count < meshQueueSize && m_MeshesNeedingGeneration.Count > 0)
        {
            // Get the next mesh to generate. Could be based on the mesh's
            // priorityHint, whether it is new vs updated, etc.
            var meshId = GetNextMeshToGenerate();
    
            // Gather the necessary Unity objects for the generation request
            var meshGameObject = GetOrCreateGameObjectForMesh(meshId);
            var meshCollider = meshGameObject.GetComponent<MeshCollider>();
            var mesh = meshGameObject.GetComponent<MeshFilter>().mesh;
            var meshAttributes = shouldComputeNormals ? MeshVertexAttributes.Normals : MeshVertexAttributes.None;
    
            // Request generation
            s_MeshSubsystem.GenerateMeshAsync(meshId, mesh, meshCollider, meshAttributes, OnMeshGenerated);
    
            // Update internal state
            m_MeshesBeingGenerated.Add(meshId, m_MeshesNeedingGeneration[meshId]);
            m_MeshesNeedingGeneration.Remove(meshId);
        }
    }
    
    void OnMeshGenerated(MeshGenerationResult result)
    {
        if (result.Status != MeshGenerationStatus.Success)
        {
            // Handle error, regenerate, etc.
        }
    
        m_MeshesBeingGenerated.Remove(result.MeshId);
    }
    

[](xrsdk-display.html)

XR SDK Display subsystem

[](xrsdk-pre-init-interface.html)

XR SDK PreInit interface

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

