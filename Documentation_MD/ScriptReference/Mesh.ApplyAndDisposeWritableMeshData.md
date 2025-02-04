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

#  [Mesh](Mesh.html).ApplyAndDisposeWritableMeshData

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

public static void
ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](Mesh.MeshDataArray.html)
data, [Mesh](Mesh.html) mesh,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public static void
ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](Mesh.MeshDataArray.html)
data, Mesh[] meshes,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

## Declaration

public static void
ApplyAndDisposeWritableMeshData([Mesh.MeshDataArray](Mesh.MeshDataArray.html)
data, List<Mesh> meshes,
[Rendering.MeshUpdateFlags](Rendering.MeshUpdateFlags.html) flags);

### Parameters

data | The mesh data array, see [MeshDataArray](Mesh.MeshDataArray.html).  
---|---  
mesh | The destination Mesh. Mesh data array must be of size 1.  
meshes | The destination Meshes. Must match the size of mesh data array.  
flags | The mesh data update flags, see [MeshUpdateFlags](Rendering.MeshUpdateFlags.html).  
  
### Description

Applies data defined in `MeshData` structs to Mesh objects.

`ApplyAndDisposeWritableMeshData` takes a
[MeshDataArray](Mesh.MeshDataArray.html) containing writeable `MeshData`
structs, and applies the vertex buffer, index buffer, and sub-mesh data to
[Mesh](Mesh.html) objects. Use this to create new Meshes using the C# Job
System and Burst.  
  
After `ApplyAndDisposeWritableMeshData` is called, the `MeshDataArray` struct
is disposed and can no longer be used.  
  
Additional resources:
[AllocateWritableMeshData](Mesh.AllocateWritableMeshData.html),
[MeshDataArray](Mesh.MeshDataArray.html), [MeshData](Mesh.MeshData.html).

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

