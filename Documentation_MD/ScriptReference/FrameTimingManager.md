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

# FrameTimingManager

class in UnityEngine

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

The FrameTimingManager allows the user to capture and access FrameTiming data
for multiple frames.

The FrameTimingManager is always active on Development Player builds. To use
this feature for other build types, go to **Edit** > **Project Settings** >
**Player** and enable the **Frame Timing Stats** property. The
FrameTimingManager also depends on the **Dynamic Resolution** feature and so
is only supported on platforms that support **Dynamic Resolution**.

### Static Methods

[CaptureFrameTimings](FrameTimingManager.CaptureFrameTimings.html)| This
function triggers the FrameTimingManager to capture a snapshot of
FrameTiming's data, that can then be accessed by the user.  
---|---  
[GetCpuTimerFrequency](FrameTimingManager.GetCpuTimerFrequency.html)| This
returns the frequency of CPU timer on the current platform, used to interpret
timing results. If the platform does not support returning this value it will
return 0.  
[GetGpuTimerFrequency](FrameTimingManager.GetGpuTimerFrequency.html)| This
returns the frequency of GPU timer on the current platform, used to interpret
timing results. If the platform does not support returning this value it will
return 0.  
[GetLatestTimings](FrameTimingManager.GetLatestTimings.html)| Allows the user
to access the currently captured FrameTimings.  
[GetVSyncsPerSecond](FrameTimingManager.GetVSyncsPerSecond.html)| This returns
the number of vsyncs per second on the current platform, used to interpret
timing results. If the platform does not support returning this value it will
return 0.  
[IsFeatureEnabled](FrameTimingManager.IsFeatureEnabled.html)| Check if frame
timing statistics are enabled.  
  
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

