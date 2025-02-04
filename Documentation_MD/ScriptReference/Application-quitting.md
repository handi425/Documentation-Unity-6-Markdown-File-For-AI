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

#  [Application](Application.html).quitting

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

Unity raises this event when the Player application is quitting.

Add an event handler to this event to receive a notification that the
application is quitting.  
  
**Note** : The `Application.quitting` event is raised when the quitting
process cannot be cancelled. Examples of when this event is not raised are:
when the Player is forced to quit or if there is a crash.  
  
**Android** : When an Android application is paused, the
`Application.quitting` event doesn't get detected. This is because in the
[paused
state](https://developer.android.com/guide/components/activities/activity-
lifecycle#onpause), the `activity` is no longer visible. As an alternative
approach, consider using
[OnApplicationFocus(bool)](MonoBehaviour.OnApplicationFocus.html) or
[OnApplicationPause(bool)](MonoBehaviour.OnApplicationPause.html).
`OnApplicationFocus(bool)` is called when the application loses or gains
focus. `OnApplicationPause(bool)` is called when the application pauses on
losing focus or resumes on regaining focus.  
  
**iOS** : iOS applications are usually suspended as they don't quit like
applications on other platforms. Use `OnApplicationPause` to capture these
events.  
  
**UWP** : On UWP apps, there's no application quit event; therefore, consider
using `OnApplicationFocus` event when `focusStatus` equals false.  
  
To prevent the Player application from quitting, refer to the
[Application.wantsToQuit](Application-wantsToQuit.html) event.  
  
Additional resources: [The activity
lifecycle](https://developer.android.com/guide/components/activities/activity-
lifecycle)

    
    
    using UnityEngine;  
      
    public class PlayerQuitExample
    {
        static void Quit()
        {
            [Debug.Log](Debug.Log.html)("Quitting the Player");
        }  
      
        [RuntimeInitializeOnLoadMethod]
        static void RunOnStart()
        {
            [Application.quitting](Application-quitting.html) += Quit;
        }
    }
    

Additional resources: [Application.wantsToQuit](Application-wantsToQuit.html).

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

