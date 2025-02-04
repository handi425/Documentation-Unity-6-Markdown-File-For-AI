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

#
[CullingResults](Rendering.CullingResults.html).ComputeDirectionalShadowMatricesAndCullingPrimitives

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

public bool ComputeDirectionalShadowMatricesAndCullingPrimitives(int
activeLightIndex, int splitIndex, int splitCount, [Vector3](Vector3.html)
splitRatio, int shadowResolution, float shadowNearPlaneOffset, out
[Matrix4x4](Matrix4x4.html) viewMatrix, out [Matrix4x4](Matrix4x4.html)
projMatrix, out [Rendering.ShadowSplitData](Rendering.ShadowSplitData.html)
shadowSplitData);

### Parameters

activeLightIndex | The index into the active light array.  
---|---  
splitIndex | The cascade index.  
splitCount | The number of cascades.  
splitRatio | The cascade ratios.  
shadowResolution | The resolution of the shadowmap.  
shadowNearPlaneOffset | The near plane offset for the light.  
viewMatrix | The computed view matrix.  
projMatrix | The computed projection matrix.  
shadowSplitData | The computed cascade data.  
  
### Returns

**bool** If false, the shadow map for this cascade does not need to be
rendered this frame.

### Description

Calculates the view and projection matrices and shadow split data for a
directional light.

Additional resources: [ShadowSplitData](Rendering.ShadowSplitData.html).

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

