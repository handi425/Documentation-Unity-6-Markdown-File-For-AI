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

#  [VideoCapture](Windows.WebCam.VideoCapture.html).StartVideoModeAsync

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

public void
StartVideoModeAsync([Windows.WebCam.CameraParameters](Windows.WebCam.CameraParameters.html)
setupParams,
[Windows.WebCam.VideoCapture.AudioState](Windows.WebCam.VideoCapture.AudioState.html)
audioState,
[Windows.WebCam.VideoCapture.OnVideoModeStartedCallback](Windows.WebCam.VideoCapture.OnVideoModeStartedCallback.html)
onVideoModeStartedCallback);

### Parameters

setupParams | The various settings that should be applied to the web camera.  
---|---  
audioState | Indicates how audio should be recorded.  
onVideoModeStartedCallback | This callback will be invoked once video mode has been activated.  
  
### Description

Asynchronously starts video mode.

Activates the web camera with the settings specified in
[CameraParameters](Windows.WebCam.CameraParameters.html). Only one
VideoCapture instance can start the video mode at any given time. After
starting the video mode, you can record videos via
[VideoCapture.StartRecordingAsync](Windows.WebCam.VideoCapture.StartRecordingAsync.html).
Video mode can impact performance, so make sure to call
[VideoCapture.StopVideoModeAsync](Windows.WebCam.VideoCapture.StopVideoModeAsync.html)
when you are done recording.

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

