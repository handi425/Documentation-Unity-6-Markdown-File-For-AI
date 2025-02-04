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

#  [Camera](Camera.html).CopyStereoDeviceProjectionMatrixToNonJittered

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
CopyStereoDeviceProjectionMatrixToNonJittered([Camera.StereoscopicEye](Camera.StereoscopicEye.html)
eye);

### Parameters

eye | Specifies the stereoscopic eye whose non-jittered projection matrix will be sourced from the VR SDK.  
---|---  
  
### Description

Sets the non-jittered projection matrix, sourced from the VR SDK.

With traditional rendering, the application is responsible for generating the
non-jittered and jittered projection matrices. However, in VR rendering, the
projection matrices are sourced from the VR SDK. Therefore, if the intention
is to jitter the VR projection matrices, that would indicate the non-jittered
projection matrices are the ones provided by the VR SDK. This API provides
this functionality by copying the VR SDK projection matrices directly into the
non-jittered stereo projection matrix set.  
  
Use Camera.GetNonJitteredStereoProjectionMatrix to get the non-jittered stereo
projection matrices.  
  
Use [Camera.SetStereoProjectionMatrix](Camera.SetStereoProjectionMatrix.html)
and [Camera.GetStereoProjectionMatrix](Camera.GetStereoProjectionMatrix.html)
to set and get the jittered stereo projection matrices, respectively.  
  
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

