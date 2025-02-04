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

#  [ModelImporter](ModelImporter.html).skinWeights

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

public [ModelImporterSkinWeights](ModelImporterSkinWeights.html) skinWeights;

### Description

Skin weights import options.

To import more than 4 bone weights per vertex, set this property to
[ModelImporterSkinWeights.Custom](ModelImporterSkinWeights.Custom.html) and
set [ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html) to
the required number. You may also limit the number of bones to less than 4, or
set a threshold for the weights via
[ModelImporter.minBoneWeight](ModelImporter-minBoneWeight.html).  
  
Note that [QualitySettings.skinWeights](QualitySettings-skinWeights.html) and
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html) can limit the
number of bone weights that Unity uses for skinning. Ensure that these values
are set to Auto, if you want to use more than 4 bone weights per vertex.  
  
Additional resources: [ModelImporter.maxBonesPerVertex](ModelImporter-
maxBonesPerVertex.html), [ModelImporter.minBoneWeight](ModelImporter-
minBoneWeight.html),[QualitySettings.skinWeights](QualitySettings-
skinWeights.html), [SkinnedMeshRenderer.quality](SkinnedMeshRenderer-
quality.html).

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

