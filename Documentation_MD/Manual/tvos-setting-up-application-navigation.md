[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tvos-setting-up-application-navigation.html)
  * [中文](/cn/current/Manual/tvos-setting-up-application-navigation.html)
  * [日本語](/ja/current/Manual/tvos-setting-up-application-navigation.html)
  * [한국어](/kr/current/Manual/tvos-setting-up-application-navigation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tvos-setting-up-application-navigation.html)
  * [中文](/cn/current/Manual/tvos-setting-up-application-navigation.html)
  * [日本語](/ja/current/Manual/tvos-setting-up-application-navigation.html)
  * [한국어](/kr/current/Manual/tvos-setting-up-application-navigation.html)

  * [Platform development ](PlatformSpecific.html)
  * [tvOS](tvOS-introducing.html)
  * [Developing for tvOS](tvOS-developing.html)
  * Setting up app navigation from the Unity UI

[](tvos-supporting-input-devices.html)

Supporting input devices on tvOS

[](tvos-debugging.html)

Debugging Your Application

# Setting up app navigation from the Unity UI

You must provide custom visual resources to the Apple Game Center for its
native leaderboard ****UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI)**. Here’s how to set them up in Xcode:

  1. Open the [Input](class-InputManager.html) window in the Unity Editor. Find the first occurrence of the **Submit** virtual input, expand it, and change its **Alt Positive Button** to [**joystick button 14**](ios-handle-game-controller-input.html#InputMapping).
  2. Select the EventSystem appObject in your ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)**. In the ****Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)**, find the EventSystem component,
and set a reference to the UI appObject that should receive initial focus in
the **First Selected** property. You might need to enable the **Force input
module** property in the **Standalone Input Module** component.#

**Note** : Apple TV Remote navigation doesn’t work while your app is running
in the TV Simulator.

[](tvos-supporting-input-devices.html)

Supporting input devices on tvOS

[](tvos-debugging.html)

Debugging Your Application

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

