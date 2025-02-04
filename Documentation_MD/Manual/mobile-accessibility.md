[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/mobile-accessibility.html)
  * [中文](/cn/current/Manual/mobile-accessibility.html)
  * [日本語](/ja/current/Manual/mobile-accessibility.html)
  * [한국어](/kr/current/Manual/mobile-accessibility.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/mobile-accessibility.html)
  * [中文](/cn/current/Manual/mobile-accessibility.html)
  * [日本語](/ja/current/Manual/mobile-accessibility.html)
  * [한국어](/kr/current/Manual/mobile-accessibility.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Accessibility for mobile applications

[](BuildPlayerPipeline.html)

Build Player Pipeline

[](UnityRemote5.html)

Unity Remote

# Accessibility for mobile applications

Use the [Accessibility module
APIs](../ScriptReference/UnityEngine.AccessibilityModule.html) to create
mobile applications that are accessible to a wider audience, including people
with disabilities.

## Requirements and compatibility

The Accessibility module APIs are available only for iOS and Android devices,
with the following minimum requirements:

**Platform** | **Operating system version**  
---|---  
**Android** | Android 8.0 (API level 26)  
**iOS** | iOS 13  
  
## Screen reader support

Android and iOS devices have built-in screen readers that describe what
appears on the screen out loud. These screen readers are designed to help
users who are blind or have low vision to navigate and interact with their
mobile devices without needing to see the screen.

**Platform** | **Screen reader**  
---|---  
**Android** | [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover)  
**iOS** | [TalkBack](https://support.google.com/accessibility/android/topic/10601571?hl=en-GB&ref_topic=3529932)  
  
Use Unity’s [Assistive Support
API](../ScriptReference/Accessibility.AssistiveSupport.html) to enable screen
reader capabilities for your application. The `AssistiveSupport` class stores
the active accessibility hierarchy that you create, allows your application to
notify the screen reader of changes in your UI, and notifies your application
of events based on user actions. Use the **Accessibility Hierarchy Viewer**
(menu: **Window** > **Accessibility** > **Accessibility Hierarchy Viewer**)
during Play mode to view the active accessibility hierarchy and its nodes in
real-time.

## System settings

Use Unity’s [Accessibility Settings
API](../ScriptReference/Accessibility.AccessibilitySettings.html) to configure
your **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) to interact with native font scaling, bold
text, and closed captions. This improves the readability and visibility of
your application’s UI for all your users.

## Additional resources

  * [Accessibility Public Sample: LetterSpell](https://github.com/Unity-Technologies/a11y-public-sample) on GitHub
  * [Accessibility module](../ScriptReference/UnityEngine.AccessibilityModule.html) API documentation
  * [Mobile screen reader support in Unity](https://unity.com/blog/engine-platform/mobile-screen-reader-support-in-unity)
  * [Unity Discussions: Accessibility](https://discussions.unity.com/tag/Accessibility)
  * [User interfaces roadmap](https://unity.com/roadmap/unity-platform/ui)

[](BuildPlayerPipeline.html)

Build Player Pipeline

[](UnityRemote5.html)

Unity Remote

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

