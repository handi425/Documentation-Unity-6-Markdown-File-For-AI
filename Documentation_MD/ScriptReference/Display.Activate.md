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

#  [Display](Display.html).Activate

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

public void Activate();

### Description

Activates an external display. For example, a secondary monitor connected to
the system.

Creates a window with screen width and screen height, and with the default
refresh rate.  
  
Displays have the following indices in the [Display.displays](Display-
displays.html) array:

  * The primary display is `0`.
  * Secondary displays are `1` to `7`.

Make sure an external display is connected before you activate it.  
  
This method works only on desktop platforms.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Check the number of monitors connected.
            if (Display.displays.Length > 1)
            {
                // Activate the display 1 (second monitor connected to the system).
                [Display.displays](Display-displays.html)[1].Activate();
            }
        }
    }
    

* * *

## Declaration

public void Activate(int width, int height, [RefreshRate](RefreshRate.html)
refreshRate);

### Parameters

width | Windows platforms only. Width of the window to open.  
---|---  
height | Windows platforms only. Height of the window to open.  
refreshRate | Refresh Rate of the window to open.  
  
### Description

Windows platforms only. Activates an external display with a specific width,
height and refresh rate. For example, a secondary monitor connected to the
system.

This method only works fully on Windows platforms. If you use this method on
Linux or macOS platforms, the display uses the screen width and height.  
  
Displays have the following indices in the [Display.displays](Display-
displays.html) array:

  * The primary display is `0`.
  * Secondary displays are `1` to `7`.

Make sure an external display is connected before you activate it.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Check the number of monitors connected.
            if (Display.displays.Length > 1)
            {
                // Activate the display 1 (second monitor connected to the system).
                [Display.displays](Display-displays.html)[1].Activate(0, 0, new [RefreshRate](RefreshRate.html)() { numerator = 60, denominator = 1 });
            }
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

