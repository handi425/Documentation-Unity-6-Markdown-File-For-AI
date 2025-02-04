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

#  [ScreenOrientation](ScreenOrientation.html).AutoRotation

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

Autorotates the screen as necessary toward any of the enabled orientations.

When you assign ScreenOrientation.AutoRotation to the
[Screen.orientation](Screen-orientation.html) property, the screen autorotates
so that the bottom of the image points downwards. To set permitted
orientations, use the following properties:

  * [Screen.autorotateToLandscapeLeft](Screen-autorotateToLandscapeLeft.html)
  * [Screen.autorotateToLandscapeRight](Screen-autorotateToLandscapeRight.html)
  * [Screen.autorotateToPortrait](Screen-autorotateToPortrait.html)
  * [Screen.autorotateToPortraitUpsideDown](Screen-autorotateToPortraitUpsideDown.html)

You can set a combination of orientations. For example, you can set
[Screen.autorotateToPortrait](Screen-autorotateToPortrait.html) and
[Screen.autorotateToPortraitUpsideDown](Screen-
autorotateToPortraitUpsideDown.html) to true whilst setting
[Screen.autorotateToLandscapeLeft](Screen-autorotateToLandscapeLeft.html) and
[Screen.autorotateToLandscapeRight](Screen-autorotateToLandscapeRight.html) to
false. In this case, the autorotation never chooses either of the landscape
options.  
  
**Note** : On Android and iOS platforms, you must set at least one orientation
property for autorotation to true. Make sure to set the remaining properties
to false.  
  
WebGL builds only support autorotation on the mobile Chrome browser, and only
allows orienting to a subset of combinations, these are:

  * Individual orientations
  * Opposite pairs of orientations
  * All four of the above orientations.

If another combination is set, autorotation defaults to all four orientations.  
**Note:** Autorotation on WebGL only works in full-screen mode.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Screen.autorotateToPortrait](Screen-autorotateToPortrait.html) = true;  
      
            [Screen.autorotateToPortraitUpsideDown](Screen-autorotateToPortraitUpsideDown.html) = true;  
      
            [Screen.autorotateToLandscapeLeft](Screen-autorotateToLandscapeLeft.html) = false;  
      
            [Screen.autorotateToLandscapeRight](Screen-autorotateToLandscapeRight.html) = false;  
      
            [Screen.orientation](Screen-orientation.html) = [ScreenOrientation.AutoRotation](ScreenOrientation.AutoRotation.html);
        }
    }
    

Additional resources: [Screen.orientation](Screen-orientation.html).

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

