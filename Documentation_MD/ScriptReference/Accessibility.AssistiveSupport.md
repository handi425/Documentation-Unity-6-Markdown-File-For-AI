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

# AssistiveSupport

class in UnityEngine.Accessibility

/

Implemented
in:[UnityEngine.AccessibilityModule](UnityEngine.AccessibilityModule.html)

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

Access point to assistive technology support APIs.

The currently supported platforms are:

  * [RuntimePlatform.Android](RuntimePlatform.Android.html) (requires at least API level 26)
  * [RuntimePlatform.IPhonePlayer](RuntimePlatform.IPhonePlayer.html)

This class contains static methods that allow users to support assistive
technologies in the operating system (for example, the screen reader).

### Static Properties

[activeHierarchy](Accessibility.AssistiveSupport-activeHierarchy.html)|  The
active AccessibilityHierarchy for the screen reader. May be null if no
hierarchy is active. You need an active accessibility hierarchy to present any
content to the user through the screen reader.If the screen reader is off,
there is no active hierarchy. If the screen reader is turned off on the device
while an active hierarchy is set, the active hierarchy is automatically set to
null.For all the supported platforms, refer to AssistiveSupport.  
---|---  
[isScreenReaderEnabled](Accessibility.AssistiveSupport-
isScreenReaderEnabled.html)|  Whether the screen reader is enabled on the
operating system. For all the supported platforms, refer to AssistiveSupport.  
[notificationDispatcher](Accessibility.AssistiveSupport-
notificationDispatcher.html)|  Service used to send accessibility
notifications to the screen reader. For all the supported platforms, refer to
AssistiveSupport.  
  
### Events

[nodeFocusChanged](Accessibility.AssistiveSupport-nodeFocusChanged.html)|
Event that is invoked on the main thread when the screen reader focus changes.
For all the supported platforms, refer to AssistiveSupport.  
---|---  
[screenReaderStatusChanged](Accessibility.AssistiveSupport-
screenReaderStatusChanged.html)|  Event that is invoked on the main thread
when the screen reader is enabled or disabled. For all the supported
platforms, refer to AssistiveSupport.  
  
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

