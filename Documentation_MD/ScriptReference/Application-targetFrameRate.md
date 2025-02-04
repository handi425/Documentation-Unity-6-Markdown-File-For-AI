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

#  [Application](Application.html).targetFrameRate

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

public static int targetFrameRate;

### Description

Specifies the target frame rate at which Unity tries to render your game.

An integer > 0, or special value -1 (default).  
  
**Desktop and Web** : If [QualitySettings.vSyncCount](QualitySettings-
vSyncCount.html) is set to 0, then `Application.targetFrameRate` chooses a
target frame rate for the game. If `vSyncCount != 0`, then `targetFrameRate`
is ignored.  
  
**Android and iOS** : Mobile platforms always ignore
[QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) and instead use
`Application.targetFrameRate` to choose a target frame rate for the game. Use
`targetFrameRate` to control the frame rate of your game. This is useful for
capping your game's frame rate to make sure your game displays smoothly and
consistently under heavy rendering workloads. You can also reduce your game's
frame rate to conserve battery life and avoid overheating on mobile devices.  
  
When `QualitySettings.vSyncCount = 0` and `Application.targetFrameRate = -1`:  
  
\- **Desktop** : Content is rendered unsynchronized as fast as possible.  
  
\- **Web** : Content is rendered at the native display refresh rate.  
  
\- **Android and iOS** : Content is rendered at **fixed 30 fps** to conserve
battery power, independent of the native refresh rate of the display.  
  
**Desktop and Web** : It is recommended to use `QualitySettings.vSyncCount`
over `Application.targetFrameRate` because `vSyncCount` implements a hardware-
based synchronization mechanism, whereas `targetFrameRate`, which is a
software-based timing method is subject to microstuttering. In other words, on
Desktop and Web platforms, setting `vSyncCount = 0` and using
`targetFrameRate` will not produce a completely stutter-free output. Always
use `vSyncCount > 0` when smooth frame pacing is needed.  
  
**Web, Android and iOS** : Rendering is always limited by the maximum refresh
rate of the display. Setting `vSyncCount = 0` and `targetFrameRate` to an
arbitrary high value will not exceed the display's native refresh rate, even
if the rendering workload is sufficiently low.  
  
**Android and iOS** : To render at the native refresh rate of the display, set
`Application.targetFrameRate` to the value from the
[Resolution.refreshRateRatio](Resolution-refreshRateRatio.html) field of the
[Screen.currentResolution](Screen-currentResolution.html) property.  
  
**iOS** : The native refresh rate of the display is controlled by the Apple
**ProMotion** feature. When ProMotion is disabled in the project (default for
new projects), the native refresh rate is 60 Hz. When ProMotion is enabled,
the native refresh rate is 120 Hz on the iOS displays that support ProMotion,
60 Hz otherwise.  
  
**Android and iOS** : If the specified rate does not evenly divide the current
refresh rate of the display, then the value of `Application.targetFrameRate`
is rounded down to the nearest number that does. For example, when running on
a 60Hz Android display, and `Application.targetFrameRate = 25`, then content
is effectively rendered at 20fps, since 20 is the highest number below 25 that
divides 60 evenly.  
  
**VR platforms**  
  
VR platforms ignore both [QualitySettings.vSyncCount](QualitySettings-
vSyncCount.html) and `Application.targetFrameRate` and instead, the VR SDK
controls the frame rate.  
  
**Unity Editor**  
  
In the Editor, `Application.targetFrameRate` affects only the Game view. It
has no effect on other Editor windows.  
  
Additional resources: [QualitySettings.vSyncCount](QualitySettings-
vSyncCount.html), [Screen.currentResolution](Screen-currentResolution.html).

    
    
    using UnityEngine;  
      
    public class Example
    {
        void Start()
        {
            // Limit framerate to cinematic 24fps.
            [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) = 0; // Set vSyncCount to 0 so that using .targetFrameRate is enabled.
            [Application.targetFrameRate](Application-targetFrameRate.html) = 24;
        }
    }
    

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

