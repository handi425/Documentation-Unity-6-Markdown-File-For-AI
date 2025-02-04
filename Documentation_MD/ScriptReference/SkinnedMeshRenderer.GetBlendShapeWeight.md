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

#  [SkinnedMeshRenderer](SkinnedMeshRenderer.html).GetBlendShapeWeight

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

[Switch to Manual](../Manual/class-SkinnedMeshRenderer.html "Go to
SkinnedMeshRenderer Component in the Manual")

## Declaration

public float GetBlendShapeWeight(int index);

### Parameters

index | The index of the BlendShape whose weight you want to retrieve. Index must be smaller than the [Mesh.blendShapeCount](Mesh-blendShapeCount.html) of the Mesh attached to this Renderer.  
---|---  
  
### Returns

**float** The weight of the BlendShape.

### Description

Returns the weight of a BlendShape for this Renderer.

The weight of a BlendShape represents how much the Mesh has been blended (or
morphed) from its original shape to a target BlendShape (another Mesh
containing the same topology, but with different vertex positions than the
original). The BlendShape weight range includes values between the minimum and
the maximum weights defined in the model.  
  
Additional resources:
[SetBlendShapeWeight](SkinnedMeshRenderer.SetBlendShapeWeight.html).

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

