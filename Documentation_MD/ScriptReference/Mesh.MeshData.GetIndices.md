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

#  [Mesh.MeshData](Mesh.MeshData.html).GetIndices

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

public void GetIndices(NativeArray<ushort> outIndices, int submesh, bool
applyBaseVertex = true);

## Declaration

public void GetIndices(NativeArray<int> outIndices, int submesh, bool
applyBaseVertex = true);

### Parameters

outIndices | The destination indices array.  
---|---  
submesh | The index of the sub-mesh to get the indices for. See [subMeshCount](Mesh.MeshData-subMeshCount.html).  
applyBaseVertex | If true, Unity will apply base vertex offset to the returned indices. The default value is true.  
  
### Description

Populates an array with the indices for a given sub-mesh from the `MeshData`.

The destination array must have enough elements to hold the index buffer of
the given sub-mesh. See [GetSubMesh](Mesh.MeshData.GetSubMesh.html) and
[SubMeshDescriptor.indexCount](Rendering.SubMeshDescriptor-indexCount.html).
Additional resources: [Mesh.GetIndices](Mesh.GetIndices.html),
[subMeshCount](Mesh.MeshData-subMeshCount.html),
[GetSubMesh](Mesh.MeshData.GetSubMesh.html).

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

