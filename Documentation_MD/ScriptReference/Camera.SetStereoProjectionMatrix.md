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

#  [Camera](Camera.html).SetStereoProjectionMatrix

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void
SetStereoProjectionMatrix([Camera.StereoscopicEye](Camera.StereoscopicEye.html)
eye, [Matrix4x4](Matrix4x4.html) matrix);

### Parameters

eye | Specifies the stereoscopic eye whose projection matrix needs to be set.  
---|---  
matrix | The matrix to be set.  
  
### Description

Sets a custom projection matrix for a specific stereoscopic eye.

In general it is recommended to stick with the projection matrices provided by
the VR SDK to ensure accurate stereoscopic rendering. However for some
specific scenarios it can be useful to override the projection matrices to
achieve specific effects. For example, custom projection matrices would be
required to implement binoculars in VR. In order to process custom projection
matrix per eye, [RenderingPath](RenderingPath.html) has to be set to Multi
Pass in player settings.  
  
Calling
[Camera.ResetStereoProjectionMatrices](Camera.ResetStereoProjectionMatrices.html)
will revert the camera to using projection matrices provided by the VR SDK.

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

