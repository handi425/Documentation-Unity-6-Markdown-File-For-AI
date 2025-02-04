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

#  [Mesh](Mesh.html).GetBoneWeights

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

public void GetBoneWeights(List<BoneWeight> boneWeights);

### Parameters

boneWeights | A list of [BoneWeight](BoneWeight.html) structs to populate.  
---|---  
  
### Description

Gets the bone weights for the Mesh.

Use this method instead of [Mesh.boneWeights](Mesh-boneWeights.html) if you
want to avoid allocating a new array with every access.  
  
The [BoneWeight](BoneWeight.html) at each index corresponds to the vertex with
the same index if this mesh has bone weights defined. Otherwise the list will
be empty.  
  
Note that this property uses [BoneWeight](BoneWeight.html) structs, which
represent exactly 4 bone weights per vertex. The newer
[BoneWeight1](BoneWeight1.html) struct describes a single bone weight, and it
can be used with the associated
[Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.SetBoneWeights](Mesh.SetBoneWeights.html) and
[Mesh.GetBonesPerVertex](Mesh.GetBonesPerVertex.html) APIs to describe up to
255 bone weights per vertex. It is preferable to use
[BoneWeight1](BoneWeight1.html) and its associated APIs; they offer more
flexibility, and might result in small performance benefits as Unity does not
have to perform unnessary conversion operations.  
  
Additional resources: [Mesh.boneWeights](Mesh-boneWeights.html),
[Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.SetBoneWeights](Mesh.SetBoneWeights.html),
[Mesh.GetBonesPerVertex](Mesh.GetBonesPerVertex.html),
[ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html),
[QualitySettings.skinWeights](QualitySettings-skinWeights.html),
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html).

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

