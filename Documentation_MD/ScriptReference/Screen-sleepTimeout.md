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

#  [Screen](Screen.html).sleepTimeout

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

public static int sleepTimeout;

### Description

A power saving setting, allowing the screen to dim some time after the last
active user interaction.

Most useful for handheld devices, allowing OS to preserve battery life in most
efficient ways. Does nothing on non-handheld devices.  
  
sleepTimeout is measured in seconds. The default value varies from platform to
platform, generally being non-zero.  
  
On mobile devices it would be useful to set sleepTimeout to
[SleepTimeout.NeverSleep](SleepTimeout.NeverSleep.html) for games using
accelerometer as the main source of input. However, such games should allow
screen dimming while in menu or paused. Currently you will only be able to set
this property to one of the values predefined in
[SleepTimeout](SleepTimeout.html) class. A get will return either one of the
predefined values, or the actual number of seconds until screen gets dimmed,
as specified in system preferences of the device.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Disable screen dimming
            [Screen.sleepTimeout](Screen-sleepTimeout.html) = [SleepTimeout.NeverSleep](SleepTimeout.NeverSleep.html);
        }
    }
    

Additional resources: [SleepTimeout](SleepTimeout.html).

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

