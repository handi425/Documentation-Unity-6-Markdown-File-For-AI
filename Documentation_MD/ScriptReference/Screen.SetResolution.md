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

#  [Screen](Screen.html).SetResolution

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

public static void SetResolution(int width, int height, bool fullscreen);

## Declaration

public static void SetResolution(int width, int height,
[FullScreenMode](FullScreenMode.html) fullscreenMode);

## Declaration

public static void SetResolution(int width, int height,
[FullScreenMode](FullScreenMode.html) fullscreenMode,
[RefreshRate](RefreshRate.html) preferredRefreshRate);

### Description

Switches the screen resolution.

A `width` by `height` resolution is used. If no matching resolution is
supported, the closest one is used.  
  
If `preferredRefreshRate` is 0 (default) Unity switches to the highest refresh
rate that the monitor supports.  
If `preferredRefreshRate` is not 0 Unity uses it if the monitor supports it,
otherwise it chooses the highest supported one. Changing refresh rate is only
supported when using exclusive full-screen mode.  
  
On Android `fullscreen` controls the `SYSTEM_UI_FLAG_LOW_PROFILE` flag to
`View.setSystemUiVisibility`.  
  
To set a specific full-screen mode on a desktop platform, use the method
overload that accepts the FullScreenMode parameter. Exclusive full-screen mode
is only supported on Windows standalone player.  
  
If you use [multi-display](../Manual/MultiDisplay.html), you can only use
`Screen.SetResolution` to set the resolution of the primary screen.  
  
A resolution switch does not happen immediately; it happens when the current
frame is finished.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // [Switch](PlayerSettings.Switch.html) to 640 x 480 full-screen
            [Screen.SetResolution](Screen.SetResolution.html)(640, 480, true);
        }
    }
    

Another example:

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // [Switch](PlayerSettings.Switch.html) to 640 x 480 full-screen at 60 hz
            [Screen.SetResolution](Screen.SetResolution.html)(640, 480, [FullScreenMode.ExclusiveFullScreen](FullScreenMode.ExclusiveFullScreen.html), new [RefreshRate](RefreshRate.html)() { numerator = 60, denominator = 1 });
        }
    }
    

Another example:

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // [Switch](PlayerSettings.Switch.html) to 800 x 600 windowed
            [Screen.SetResolution](Screen.SetResolution.html)(800, 600, false);
        }
    }
    

Additional resources: [resolutions](Screen-resolutions.html) property.

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

