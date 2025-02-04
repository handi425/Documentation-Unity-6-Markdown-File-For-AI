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

#  [QualitySettings](QualitySettings.html).vSyncCount

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

public static int vSyncCount;

### Description

Represents the number of vertical syncs that should pass between each frame.

An integer in the range of 0-4. By default, it is set to 1.  
  
**Desktop and Web**  
  
`vSyncCount` specifies the number of screen refreshes your game allows to pass
between frames. In the Unity Editor, this corresponds to the **VSync Count**
property under **Project Settings > Quality > Other**.  
  
\- If `vSyncCount > 0`, then the field
[Application.targetFrameRate](Application-targetFrameRate.html) is ignored,
and the effective frame rate is the native refresh rate of the display divided
by `vSyncCount`. If `vSyncCount == 1`, rendering is synchronized to the
vertical refresh rate of the display.  
  
\- If `vSyncCount` is set to 0, Unity does not synchronize rendering to
vertical sync, and the field [Application.targetFrameRate](Application-
targetFrameRate.html) is instead used to pace the rendered frames.  
  
For example, if you're running the Editor on a 60 Hz display and `vSyncCount
== 2`, then the target frame rate is 30 frames per second.  
  
**Android and iOS:** The `vSyncCount` field is always ignored because mobile
devices do not allow unsynchronized rendering. Use the
[Application.targetFrameRate](Application-targetFrameRate.html) field instead
to control the frame rate.  
  
**VR platforms:** Both `vSyncCount` and
[Application.targetFrameRate](Application-targetFrameRate.html) are ignored.
Instead, the VR SDK controls the frame rate.  
  
**Note** : You can use [Resolution.refreshRateRatio](Resolution-
refreshRateRatio.html) in the [Screen.currentResolution](Screen-
currentResolution.html) property to query the screen's refresh rate for most
platforms.  
  
**Varying display native refresh rate**  
  
While historically the native refresh rate for displays often stayed fixed,
the new generation mobile devices, laptops, and desktop devices today can
influence the native refresh rate of the display to change dynamically at
runtime. For example:

  * **Desktop** : When user drags a game window from primary monitor over to a secondary monitor, or changes the monitor refresh rate in Display Properties while the game is running, the native display refresh rate can change on the fly.
  * **Laptops** : A gaming laptop with a high refresh rate display might only run at 144 H, for example, when the laptop is powered to a wall charger. When unplugged, the display caps to 60 Hz.
  * **Mobile** : A mobile phone might restrict the display refresh rate to 60 Hz when the mobile phone battery is being charged, to throttle and prevent overheating due to simultaneous heat buildup from the battery being recharged.
  * **Web** : Any of the above conditions might occur, depending on which form factor device the user is browsing on.

Therefore, it is recommended to not hardcode anywhere in the game logic with
an assumption that the display refresh rate that is seen at the game startup
will persist throughout the lifetime of the application.  
  
Additional resources: [Application.targetFrameRate](Application-
targetFrameRate.html)

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Render at half the refresh rate of the display (Desktop and Web platforms)
            [QualitySettings.vSyncCount](QualitySettings-vSyncCount.html) = 2;
        }
    }
    

Additional resources: [Quality Settings](../Manual/class-
QualitySettings.html).

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

