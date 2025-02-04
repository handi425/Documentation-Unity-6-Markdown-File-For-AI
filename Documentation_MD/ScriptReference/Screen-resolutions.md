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

#  [Screen](Screen.html).resolutions

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

public static Resolution[] resolutions;

### Description

Returns all full-screen resolutions that the monitor supports (Read Only).

Unity returns the resolutions the monitor supports and sorts them by width and
then by ascending resolution. **Important:** When you use
[FullScreenMode.ExclusiveFullScreen](FullScreenMode.ExclusiveFullScreen.html)
you should use `Screen.resolutions` to determine which resolution to pass to
[Screen.SetResolution](Screen.SetResolution.html) because
`FullScreenMode.ExclusiveFullScreen` only works with supported resolutions. If
you pass a non-supported resolution, it has a severe impact on performance.
All other fullscreen modes support arbitrary resolutions without performance
penalties.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Resolution](Resolution.html)[] resolutions = [Screen.resolutions](Screen-resolutions.html);  
      
            // Print the resolutions
            foreach (var res in resolutions)
            {
                [Debug.Log](Debug.Log.html)(res.width + "x" + res.height + " : " + res.refreshRateRatio);
            }
        }
    }
    

**Note:** On MacOS devices that have a notch area, the resolution array
contains resolutions that don't fit under the notch area and will be resized
when applied.  
  
Additional resources: [Resolution](Resolution.html) structure,
[SetResolution](Screen.SetResolution.html).

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

