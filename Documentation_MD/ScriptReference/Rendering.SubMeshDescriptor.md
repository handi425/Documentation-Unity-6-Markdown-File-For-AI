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

# SubMeshDescriptor

struct in UnityEngine.Rendering

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

[ ]()

### Description

Contains information about a single sub-mesh of a [Mesh](Mesh.html).

Simple usage of [Mesh](Mesh.html) scripting API involves using functions like
[Mesh.triangles](Mesh-triangles.html), [Mesh.vertices](Mesh-vertices.html) and
so on.  
  
For advanced use cases that require maximum performance, you can use the
advanced API, which has functions like
[Mesh.SetSubMesh](Mesh.SetSubMesh.html),
[Mesh.SetIndexBufferParams](Mesh.SetIndexBufferParams.html), and
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html). This advanced API
gives access to the underlying mesh data structures that primarily work on raw
index buffers, vertex buffers and mesh subset data.  
  
A single sub-mesh represents part of the Mesh that is using one material. Many
Meshes use just one material, but some might use more. Information in a sub-
mesh is composed of:

  * [indexStart](Rendering.SubMeshDescriptor-indexStart.html) \- starting point inside the whole Mesh index buffer where the face index data of this subset is found. See [Mesh.SetIndexBufferParams](Mesh.SetIndexBufferParams.html) and [Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html).
  * [indexCount](Rendering.SubMeshDescriptor-indexCount.html) \- index count for this sub-mesh. For example, in meshes with triangle topology, each triangle needs three indices.
  * [topology](Rendering.SubMeshDescriptor-topology.html) \- topology of this sub-mesh, most often [MeshTopology.Triangles](MeshTopology.Triangles.html).
  * [baseVertex](Rendering.SubMeshDescriptor-baseVertex.html) \- offset that is added to each value in the index buffer, to compute the final vertex index.
  * [bounds](Rendering.SubMeshDescriptor-bounds.html) \- bounding box of vertices in local space.
  * [firstVertex](Rendering.SubMeshDescriptor-firstVertex.html) and [vertexCount](Rendering.SubMeshDescriptor-vertexCount.html) \- range of vertices that are referenced by the index buffer of this sub-mesh.

The [bounds](Rendering.SubMeshDescriptor-bounds.html),
[firstVertex](Rendering.SubMeshDescriptor-firstVertex.html) and
[vertexCount](Rendering.SubMeshDescriptor-vertexCount.html) values are
calculated automatically by [Mesh.SetSubMesh](Mesh.SetSubMesh.html), unless
[MeshUpdateFlags.DontRecalculateBounds](Rendering.MeshUpdateFlags.DontRecalculateBounds.html)
flag is passed.  
  
Additional resources: [Mesh.SetSubMesh](Mesh.SetSubMesh.html),
[Mesh.GetSubMesh](Mesh.GetSubMesh.html),
[Mesh.SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[Mesh.SetIndexBufferData](Mesh.SetIndexBufferData.html).

### Properties

[baseVertex](Rendering.SubMeshDescriptor-baseVertex.html)| Offset that is
added to each value in the index buffer, to compute the final vertex index.  
---|---  
[bounds](Rendering.SubMeshDescriptor-bounds.html)| Bounding box of vertices in
local space.  
[firstVertex](Rendering.SubMeshDescriptor-firstVertex.html)| First vertex in
the index buffer for this sub-mesh.  
[indexCount](Rendering.SubMeshDescriptor-indexCount.html)| Index count for
this sub-mesh face data.  
[indexStart](Rendering.SubMeshDescriptor-indexStart.html)| Starting point
inside the whole Mesh index buffer where the face index data is found.  
[topology](Rendering.SubMeshDescriptor-topology.html)| Face topology of this
sub-mesh.  
[vertexCount](Rendering.SubMeshDescriptor-vertexCount.html)| Number of
vertices used by the index buffer of this sub-mesh.  
  
### Constructors

[SubMeshDescriptor](Rendering.SubMeshDescriptor-ctor.html)| Create a submesh
descriptor.  
---|---  
  
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

