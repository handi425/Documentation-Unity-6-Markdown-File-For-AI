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

#  [MeshUtility](MeshUtility.html).AcquireReadOnlyMeshData

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

## Declaration

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AcquireReadOnlyMeshData([Mesh](Mesh.html) mesh);

## Declaration

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AcquireReadOnlyMeshData(Mesh[] meshes);

## Declaration

public static [Mesh.MeshDataArray](Mesh.MeshDataArray.html)
AcquireReadOnlyMeshData(List<Mesh> meshes);

### Parameters

mesh | The input mesh.  
---|---  
meshes | The input meshes.  
  
### Returns

**MeshDataArray** Returns a read-only snapshot of Mesh data. See
[MeshDataArray](Mesh.MeshDataArray.html) and [MeshData](Mesh.MeshData.html).

### Description

Gets a snapshot of Mesh data for read-only access in the Unity Editor.

This method retrieves the same data as
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html).  
  
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html) only
retrieves data from meshes where [Mesh.isReadable](Mesh-isReadable.html) is
`true`. In the Editor, all meshes are readable, even when
[Mesh.isReadable](Mesh-isReadable.html) is set to `false`. This Editor-only
method skips the `isReadable` check, and retrieves data whether
[Mesh.isReadable](Mesh-isReadable.html) is `true` or `false`.  
  
Additional resources:
[Mesh.AcquireReadOnlyMeshData](Mesh.AcquireReadOnlyMeshData.html),
[MeshDataArray](Mesh.MeshDataArray.html), [MeshData](Mesh.MeshData.html)

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

