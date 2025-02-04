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

#  [Screen](Screen.html).orientation

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

public static [ScreenOrientation](ScreenOrientation.html) orientation;

### Description

Specifies logical orientation of the screen.

The default value is taken from the [Default Orientation](PlayerSettings-
defaultInterfaceOrientation.html) property in [Player
Settings](../Manual/class-PlayerSettings.html). Currently screen orientation
is only relevant on mobile platforms. For example, if a mobile device has a
resolution of 480x320, the horizontal orientation is treated as 480x320
resolution and vertical orientation is 320x480.  
  
**Note:** The logical orientation affects not only screen orientation, but
also touch coordinates. You should expect drastic changes in the touch
positions after changing logical orientation, because touch positions are
rotated clockwise or counter-clockwise to match screen coordinates.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Start in landscape mode
        void Start()
        {
            [Screen.orientation](Screen-orientation.html) = [ScreenOrientation.LandscapeLeft](ScreenOrientation.LandscapeLeft.html);
        }
    }
    

If the value is set to
[ScreenOrientation.AutoRotation](ScreenOrientation.AutoRotation.html) then the
screen selects from any of the options (enabled by
[autorotateToPortrait](Screen-autorotateToPortrait.html), etc) automatically
as the device orientation changes.  
  
Additional resources: [ScreenOrientation](ScreenOrientation.html).

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

