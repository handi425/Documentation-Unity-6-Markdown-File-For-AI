[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityasaLibrary.html)
  * [中文](/cn/current/Manual/UnityasaLibrary.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityasaLibrary.html)
  * [中文](/cn/current/Manual/UnityasaLibrary.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Using Unity as a Library in other applications

[](CrossPlatformConsiderations.html)

Troubleshooting common cross-platform issues

[](deep-linking.html)

Deep linking

# Using Unity as a Library in other applications

Unity as a Library is intended for specialist users who use native platform
technologies such as Java/Android, Objective C/iOS, or Windows Win32/UWP, and
want to include Unity-powered features in their games or applications.

This documentation assumes that you have experience with developing for native
platform technologies such as Java/Android, Objective C/iOS, or Windows
Win32/UWP, and that you are familiar with the structure of the project,
language features and specific platform configuration options (for example,
user permissions).

You can use Unity as a Library in other applications by integrating your
content and the Unity runtime components in a native platform project. This
enables you to embed content that uses 3D or 2D real-time rendering, like
**AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) experiences, interaction with 3D models,
and 2D mini-games. The Unity Runtime Library exposes ways to manage loading,
activating, and unloading within the native application.

The following platforms currently support Unity as a Library:

  * [Android](UnityasaLibrary-Android.html)
  * [iOS](UnityasaLibrary-iOS.html)
  * [Windows](UnityasaLibrary-Windows.html) and [Universal Windows Platform](UnityasaLibrary-UWP.html)

To determine platform versions and other dependencies, see the [system
requirements](system-requirements.html) page.

## Limitations

When hosted by another application, Unity doesn’t control the runtime
lifecycle, so it might not work in all scenarios. Known limitations include:

  * On Android and iOS: 
    * Only full-screen rendering is supported. However, if you are a Unity Industry customer, the limitations and features might differ.
    * When Unity is in an unloaded state (after calling [`Application.Unload`](../ScriptReference/Application.Unload.html)), it retains some amount of memory (between 80–180Mb) to be able to instantly switch back and run again in the same process. The amount of memory that’s not released largely depends on the device’s graphics resolution.
  * On iOS, if the Unity runtime quits entirely (after calling [`Application.Quit`](../ScriptReference/Application.Quit.html)), it’s not possible to reload Unity again in the same app session.
  * You can’t load more than one instance of the Unity runtime, or integrate more than one Unity runtime.
  * You might need to adapt your [native](plug-ins-native.html) and [managed](plug-ins-managed.html) **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) to work properly.

[](CrossPlatformConsiderations.html)

Troubleshooting common cross-platform issues

[](deep-linking.html)

Deep linking

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

