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

#  [Mesh](Mesh.html).SetSubMeshes

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

## Declaration

public void SetSubMeshes(SubMeshDescriptor[] desc, int start, int count,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetSubMeshes(SubMeshDescriptor[] desc,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetSubMeshes(List<SubMeshDescriptor> desc, int start, int count,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetSubMeshes(List<SubMeshDescriptor> desc,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetSubMeshes(NativeArray<T> desc, int start, int count,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetSubMeshes(NativeArray<T> desc,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

### Parameters

desc | An array or list of sub-mesh data descriptors.  
---|---  
start | Index of the first element to take from the array or list in `desc`.  
count | Number of elements to take from the array or list in `desc`.  
flags | (Optional) Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Sets information defining all sub-meshes in this [Mesh](Mesh.html), replacing
any existing sub-meshes.

Note that [SetSubMeshes](Mesh.SetSubMeshes.html),
[SetSubMesh](Mesh.SetSubMesh.html),
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html), and
[SetIndexBufferData](Mesh.SetIndexBufferData.html) are designed for maximum
performance. These functions operate on the underlying mesh data structures
involving raw index buffers, vertex buffers and mesh subset data. When you use
these methods, Unity performs very little data validation, so you must ensure
your data is valid.  
  
In particular, you must ensure that the
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html) index ranges and
[SubMeshDescriptor.topology](Rendering.SubMeshDescriptor-topology.html) values
are set to correct values. SubMesh indices, both indexStart and indexCount,
must not overlap with any other SubMesh indices.  
  
For information about the difference between the simpler and more advanced
methods of assigning data to a Mesh from script, see [Mesh](Mesh.html).  
  
The [SubMeshDescriptor-bounds](Rendering.SubMeshDescriptor-bounds.html),
[SubMeshDescriptor-firstVertex](Rendering.SubMeshDescriptor-firstVertex.html)
and [SubMeshDescriptor-vertexCount](Rendering.SubMeshDescriptor-
vertexCount.html) values of
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html) are calculated
automatically by `SetSubMeshes`, unless
[MeshUpdateFlags.DontRecalculateBounds](Rendering.MeshUpdateFlags.DontRecalculateBounds.html)
flag is passed. Note that this only applies to the bounds of the SubMesh. You
must call [Mesh.RecalculateBounds](Mesh.RecalculateBounds.html) to recalculate
the bounds of the Mesh itself.  
  
General usage pattern is:

    
    
    var mesh = new [Mesh](Mesh.html)();  
      
    // setup vertex buffer data
    mesh.vertices = ...;  
      
    // set index buffer
    mesh.SetIndexBufferParams(...);
    mesh.SetIndexBufferData(...);  
      
    // setup information about mesh subsets
    [SubMeshDescriptor](Rendering.SubMeshDescriptor.html)[] sm = new [SubMeshDescriptor](Rendering.SubMeshDescriptor.html)[] {...}
    mesh.SetSubMeshes(sm);  
      
    // update bounds of the mesh
    mesh.RecalculateBounds();

For details on what data to set up for each sub-mesh, see
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html).  
  
Additional resources: [subMeshCount](Mesh-subMeshCount.html),
[GetSubMesh](Mesh.GetSubMesh.html), [SetSubMesh](Mesh.SetSubMesh.html),
[SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[SetIndexBufferData](Mesh.SetIndexBufferData.html),
[MeshUpdateFlags](Rendering.MeshUpdateFlags.html).

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

