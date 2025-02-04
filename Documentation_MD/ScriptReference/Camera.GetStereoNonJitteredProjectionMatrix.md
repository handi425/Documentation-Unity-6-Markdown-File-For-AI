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

#  [Camera](Camera.html).GetStereoNonJitteredProjectionMatrix

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

public [Matrix4x4](Matrix4x4.html)
GetStereoNonJitteredProjectionMatrix([Camera.StereoscopicEye](Camera.StereoscopicEye.html)
eye);

### Parameters

eye | Specifies the stereoscopic eye whose non-jittered projection matrix needs to be returned.  
---|---  
  
### Returns

**Matrix4x4** The non-jittered projection matrix of the specified stereoscopic
eye.

### Description

Gets the non-jittered projection matrix of a specific left or right
stereoscopic eye.

If you have configured the non-jittered stereo projection matrices with
[Camera.CopyStereoDeviceProjectionMatrixToNonJittered](Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html),
this function will return the VR device's original stereo projection matrices.
If you have not used
[Camera.CopyStereoDeviceProjectionMatrixToNonJittered](Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html),
this will return the same matrix as
[Camera.GetStereoProjectionMatrix](Camera.GetStereoProjectionMatrix.html).  
  
Use [Camera.GetStereoProjectionMatrix](Camera.GetStereoProjectionMatrix.html)
to get the jittered stereo projection matrices.  
  
For descriptions of jittered projection rendering see:
[Camera.nonJitteredProjectionMatrix](Camera-nonJitteredProjectionMatrix.html).

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

