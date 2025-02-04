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

#  [Mesh](Mesh.html).SetIndexBufferData

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

public void SetIndexBufferData(NativeArray<T> data, int dataStart, int
meshBufferStart, int count,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetIndexBufferData(T[] data, int dataStart, int meshBufferStart,
int count, [Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public void SetIndexBufferData(List<T> data, int dataStart, int
meshBufferStart, int count,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

### Parameters

data | Index buffer data array.  
---|---  
dataStart | The first element in the data to copy from.  
meshBufferStart | The first element in the mesh index buffer to receive the data.  
count | Count of indices to copy.  
flags | Flags controlling the function behavior, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Sets the data of the index buffer of the Mesh.

Note: This method is designed for advanced users aiming for maximum
performance because it operates on the underlying mesh data structures that
primarily work on raw index buffers, vertex buffers and mesh subset data.
Using this method, Unity performs very little data validation, so you must
ensure your data is valid.  
  
In particular, you must ensure that the SubMesh index range and topology are
updated via [SetSubMesh](Mesh.SetSubMesh.html).  
  
By default, the index buffer `data` array is checked for out-of-bounds
indices. `flags` parameter can be set to
[MeshUpdateFlags.DontValidateIndices](Rendering.MeshUpdateFlags.DontValidateIndices.html)
to turn the validation off for performance reasons.  
  
For information about the difference between the simpler and more advanced
methods of assigning data to a Mesh from script, see the notes on the
[Mesh](Mesh.html) page.  
  
General usage pattern is:

    
    
    var mesh = new [Mesh](Mesh.html)();  
      
    // setup vertex buffer data
    mesh.vertices = ...;  
      
    // set index buffer
    mesh.SetIndexBufferParams(...);
    mesh.SetIndexBufferData(...);  
      
    // setup information about mesh subsets
    mesh.subMeshCount = ...;
    mesh.SetSubMesh(index, ...);
    

Additional resources: [SetIndexBufferParams](Mesh.SetIndexBufferParams.html),
[subMeshCount](Mesh-subMeshCount.html), [SetSubMesh](Mesh.SetSubMesh.html),
[SetVertexBufferData](Mesh.SetVertexBufferData.html),
[MeshUpdateFlags](Rendering.MeshUpdateFlags.html),
[AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).

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

