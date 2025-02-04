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

# ShadowSplitData

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

Describes the culling information for a given shadow split (e.g. directional
cascade).

### Static Properties

[maximumCullingPlaneCount](Rendering.ShadowSplitData-
maximumCullingPlaneCount.html)| The maximum number of culling planes.  
---|---  
  
### Properties

[cullingMatrix](Rendering.ShadowSplitData-cullingMatrix.html)| The model view
projection matrix Unity uses to cull objects it renders into this shadow map.  
---|---  
[cullingNearPlane](Rendering.ShadowSplitData-cullingNearPlane.html)| The near
plane distance that Unity uses to cull objects. Unity transforms the objects
with ShadowSplitData.cullingMatrix, and then culls the ones that are farther
than the near plane distance.  
[cullingPlaneCount](Rendering.ShadowSplitData-cullingPlaneCount.html)| The
number of culling planes.  
[cullingSphere](Rendering.ShadowSplitData-cullingSphere.html)| The culling
sphere. The first three components of the vector describe the sphere center,
and the last component specifies the radius.  
[shadowCascadeBlendCullingFactor](Rendering.ShadowSplitData-
shadowCascadeBlendCullingFactor.html)|  A multiplier applied to the radius of
the culling sphere.Values must be in the range 0 to 1. With higher values,
Unity culls more objects. Lower makes the cascades share more rendered
objects. Using lower values allows blending between different cascades as they
then share objects.  
  
### Public Methods

[GetCullingPlane](Rendering.ShadowSplitData.GetCullingPlane.html)| Gets a
culling plane.  
---|---  
[SetCullingPlane](Rendering.ShadowSplitData.SetCullingPlane.html)| Sets a
culling plane.  
  
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

