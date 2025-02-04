[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# MeshData

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

### Description

A struct containing Mesh data for C# Job System access.

Use a `MeshData` struct to access, process and create Meshes in the C# Job
System. There are two types of `MeshData` struct: read-only `MeshData` structs
that allow read-only access to Mesh data from the C# Job System, and writeable
`MeshData` structs that allow you to create Meshes from the C# Job System.  
  
**Read-only MeshData**  
  
When you pass one or more Meshes to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html), Unity
returns a [MeshDataArray](Mesh.MeshDataArray.html) of read-only `MeshData`
structs. You can access the resulting `MeshDataArray` and `MeshData` structs
from any thread. Creating a `MeshDataArray` has some overhead for memory
tracking and safety reasons, so it is more efficient to make a single call to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and request
multiple `MeshData` structs in the same `MeshDataArray` than it is to make
multiple calls to
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).  
  
Each `MeshData` struct contains a read-only snapshot of data for a given Mesh.
You can use [GetIndexData](Mesh.MeshData.GetIndexData.html) and
[GetVertexData](Mesh.MeshData.GetVertexData.html) to access the raw read-only
Mesh data without any memory allocations, data copies or format conversions.
You need to know the exact Mesh data layout to do this: for instance, the
presence and formats of all the mesh vertex attributes. You can use
[GetColors](Mesh.MeshData.GetColors.html),
[GetIndices](Mesh.MeshData.GetIndices.html),
[GetNormals](Mesh.MeshData.GetNormals.html),
[GetTangents](Mesh.MeshData.GetTangents.html),
[GetUVs](Mesh.MeshData.GetUVs.html), and
[GetVertices](Mesh.MeshData.GetVertices.html) to copy the read-only Mesh data
into pre-existing arrays. These methods also perform data format conversions
if needed. For example, if the read-only `MeshData` struct uses
[VertexAttributeFormat.Float16](Rendering.VertexAttributeFormat.Float16.html)
normals and you call [GetNormals](Mesh.MeshData.GetNormals.html), the normals
will be converted into [Vector3](Vector3.html) normals in the destination
array.  
  
You must dispose of the `MeshDataArray` once you have finished working with
it. Calling [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)
does not cause any memory allocations or data copies by default, as long as
you dispose of the `MeshDataArray` before modifying the Mesh. However, if you
call [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and
then modify the Mesh while the `MeshDataArray` exists, Unity must copy the
`MeshDataArray` into a new memory allocation. In addition to this, if you call
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) and then
modify the Mesh, your modifications are not reflected in the `MeshData`
structs.  
  
Use [Dispose](Mesh.MeshDataArray.Dispose.html) to dispose of the
`MeshDataArray`, or use the C# `using` pattern to do this automatically:

    
    
    using Unity.Collections;
    using UnityEngine;
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new[] {[Vector3.one](Vector3-one.html), [Vector3.zero](Vector3-zero.html)};
            using (var dataArray = [Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html)(mesh))
            {
                var data = dataArray[0];
                // prints "2"
                [Debug.Log](Debug.Log.html)(data.vertexCount);
                var gotVertices = new NativeArray<[Vector3](Vector3.html)>(mesh.vertexCount, [Allocator.TempJob](Unity.Collections.Allocator.TempJob.html));
                data.GetVertices(gotVertices);
                // prints "(1.0, 1.0, 1.0)" and "(0.0, 0.0, 0.0)"
                foreach (var v in gotVertices)
                    [Debug.Log](Debug.Log.html)(v);
                gotVertices.Dispose();
            }
        }
    }
    

**Writeable MeshData**  
  
Use [Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html) to
obtain a [MeshDataArray](Mesh.MeshDataArray.html) of writeable `MeshData`
structs. You can access the resulting `MeshDataArray` and `MeshData` structs
from any thread. Creating a `MeshDataArray` has some overhead for memory
tracking and safety reasons, so it is more efficient to make a single call to
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html) and
request multiple `MeshData` structs in the same `MeshDataArray` than it is to
make multiple calls to
[Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html).  
  
You can populate writeable `MeshData` structs with data to create new Meshes.
Use
[Mesh.MeshData.SetVertexBufferParams](Mesh.MeshData.SetVertexBufferParams.html)
to set the vertex buffer size and layout, and then write to the array returned
by [Mesh.MeshData.GetVertexData](Mesh.MeshData.GetVertexData.html) to set the
vertices. Use
[Mesh.MeshData.SetIndexBufferParams](Mesh.MeshData.SetIndexBufferParams.html)
to set the index buffer size and format, and then write to the array returned
by [Mesh.MeshData.GetIndexData](Mesh.MeshData.GetIndexData.html) to set the
indices. Write to [Mesh.MeshData.subMeshCount](Mesh.MeshData-
subMeshCount.html) to set the number of sub meshes, and then use
[Mesh.MeshData.SetSubMesh](Mesh.MeshData.SetSubMesh.html) to set sub mesh
data.  
  
When you have populated the writeable `MeshData` struct with your data, use
[Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html)
to apply the data to [Mesh](Mesh.html) objects and automatically dispose of
the `MeshDataArray`.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using Unity.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([MeshFilter](MeshFilter.html)))]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Allocate mesh data for one mesh.
            var dataArray = [Mesh.AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html)(1);
            var data = dataArray[0];  
      
            // Tetrahedron vertices with positions and normals.
            // 4 faces with 3 unique vertices in each -- the faces
            // don't share the vertices since normals have to be
            // different for each face.
            data.SetVertexBufferParams(12,
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Position](Rendering.VertexAttribute.Position.html)),
                new [VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)([VertexAttribute.Normal](Rendering.VertexAttribute.Normal.html), stream: 1));  
      
            // Four tetrahedron vertex positions:
            var sqrt075 = [Mathf.Sqrt](Mathf.Sqrt.html)(0.75f);
            var p0 = new [Vector3](Vector3.html)(0, 0, 0);
            var p1 = new [Vector3](Vector3.html)(1, 0, 0);
            var p2 = new [Vector3](Vector3.html)(0.5f, 0, sqrt075);
            var p3 = new [Vector3](Vector3.html)(0.5f, sqrt075, sqrt075 / 3);  
      
            // The first vertex buffer data stream is just positions;
            // fill them in.
            NativeArray<[Vector3](Vector3.html)> pos = data.GetVertexData<[Vector3](Vector3.html)>();
            pos[0] = p0; pos[1] = p1; pos[2] = p2;
            pos[3] = p0; pos[4] = p2; pos[5] = p3;
            pos[6] = p2; pos[7] = p1; pos[8] = p3;
            pos[9] = p0; pos[10] = p3; pos[11] = p1;  
      
            // Note: normals will be calculated later in RecalculateNormals.
            // Tetrahedron index buffer: 4 triangles, 3 indices per triangle.
            // All vertices are unique so the index buffer is just a
            // 0,1,2,...,11 sequence.
            data.SetIndexBufferParams(12, [IndexFormat.UInt16](Rendering.IndexFormat.UInt16.html));
            NativeArray<ushort> indexBuffer = data.GetIndexData<ushort>();
            for (ushort i = 0; i < indexBuffer.Length; ++i)
                indexBuffer[i] = i;  
      
            // One sub-mesh with all the indices.
            data.subMeshCount = 1;
            data.SetSubMesh(0, new [SubMeshDescriptor](Rendering.SubMeshDescriptor.html)(0, indexBuffer.Length));
            
            // Create the mesh and apply data to it:
            var mesh = new [Mesh](Mesh.html)();
            mesh.name = "Tetrahedron";
            [Mesh.ApplyAndDisposeWritableMeshData](Mesh.ApplyAndDisposeWritableMeshData.html)(dataArray, mesh);
            mesh.RecalculateNormals();
            mesh.RecalculateBounds();
            GetComponent<[MeshFilter](MeshFilter.html)>().mesh = mesh;
        }
    }
    

### Properties

[indexFormat](Mesh.MeshData-indexFormat.html)| Gets the format of the index
buffer data in the MeshData. (Read Only)  
---|---  
[subMeshCount](Mesh.MeshData-subMeshCount.html)| The number of sub-meshes in
the MeshData.  
[vertexBufferCount](Mesh.MeshData-vertexBufferCount.html)| Gets the number of
vertex buffers in the MeshData. (Read Only)  
[vertexCount](Mesh.MeshData-vertexCount.html)| Gets the number of vertices in
the MeshData. (Read Only)  
  
### Public Methods

[GetColors](Mesh.MeshData.GetColors.html)| Populates an array with the vertex
colors from the MeshData.  
---|---  
[GetIndexData](Mesh.MeshData.GetIndexData.html)| Gets raw data from the index
buffer of the MeshData.  
[GetIndices](Mesh.MeshData.GetIndices.html)| Populates an array with the
indices for a given sub-mesh from the MeshData.  
[GetNormals](Mesh.MeshData.GetNormals.html)| Populates an array with the
vertex normals from the MeshData.  
[GetSubMesh](Mesh.MeshData.GetSubMesh.html)| Gets data about a given sub-mesh
in the MeshData.  
[GetTangents](Mesh.MeshData.GetTangents.html)| Populates an array with the
vertex tangents from the MeshData.  
[GetUVs](Mesh.MeshData.GetUVs.html)| Populates an array with the UVs from the
MeshData.  
[GetVertexAttributeDimension](Mesh.MeshData.GetVertexAttributeDimension.html)|
Gets the dimension of a given vertex attribute in the MeshData.  
[GetVertexAttributeFormat](Mesh.MeshData.GetVertexAttributeFormat.html)| Gets
the format of a given vertex attribute in the MeshData.  
[GetVertexAttributeOffset](Mesh.MeshData.GetVertexAttributeOffset.html)| Gets
the offset within a vertex buffer stream of a given vertex data attribute on
this MeshData.  
[GetVertexAttributeStream](Mesh.MeshData.GetVertexAttributeStream.html)| Get
the vertex buffer stream index of a specific vertex data attribute on this
MeshData.  
[GetVertexBufferStride](Mesh.MeshData.GetVertexBufferStride.html)| Get the
vertex buffer stream stride in bytes.  
[GetVertexData](Mesh.MeshData.GetVertexData.html)| Gets raw data for a given
vertex buffer stream format in the MeshData.  
[GetVertices](Mesh.MeshData.GetVertices.html)| Populates an array with the
vertex positions from the MeshData.  
[HasVertexAttribute](Mesh.MeshData.HasVertexAttribute.html)| Checks if a given
vertex attribute exists in the MeshData.  
[SetIndexBufferParams](Mesh.MeshData.SetIndexBufferParams.html)| Sets the
index buffer size and format of the Mesh that Unity creates from the MeshData.  
[SetSubMesh](Mesh.MeshData.SetSubMesh.html)| Sets the data for a sub-mesh of
the Mesh that Unity creates from the MeshData.  
[SetVertexBufferParams](Mesh.MeshData.SetVertexBufferParams.html)| Sets the
vertex buffer size and layout of the Mesh that Unity creates from the
MeshData.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

