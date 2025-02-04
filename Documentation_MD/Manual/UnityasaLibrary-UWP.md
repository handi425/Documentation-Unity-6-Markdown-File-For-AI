[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnityasaLibrary-UWP.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-UWP.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-UWP.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-UWP.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnityasaLibrary-UWP.html)
  * [中文](/cn/current/Manual/UnityasaLibrary-UWP.html)
  * [日本語](/ja/current/Manual/UnityasaLibrary-UWP.html)
  * [한국어](/kr/current/Manual/UnityasaLibrary-UWP.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Introduction to Universal Windows Platform](uwp-introducing.html)
  * Integrate Unity into UWP applications

[](uwp-requirements-and-compatibility.html)

UWP requirements and compatibility

[](uwp-getting-started.html)

Get started with Universal Windows Platform

# Integrate Unity into UWP applications

You can use the Unity as a Library feature to integrate the Unity Runtime
Library in Universal Windows Platform (UWP) applications. The Unity Runtime
Library exposes API controls to manage when and how to load, activate, and
unload content within another UWP application.

This integration enables you to include Unity-powered features in your UWP
application, such as:

  * 3D/2D real-time rendering
  * **AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) experience

  * 3D model interaction
  * 2D mini-games

To integrate the Unity Runtime Library into a UWP application, complete these
steps:

  1. Open **File > Build Settings**.
  2. In the **Universal Windows Platform** tab, select **Build Type > XAML**.
  3. Build your project.

As a result, Unity creates a Visual Studio project, which you can use to embed
the Unity Runtime Library into another UWP application. The project is a
general XAML UWP project in the form of a `MainPage.xaml` file which contains
a SwapChainPanel setup to load the Unity project. You can extend or replace
this project with any other non-Unity application business logic.

**Note:** The `MainPage.xaml` file is present only if you’re building a UWP
app using the **XAML** build type from the Unity editor.

When using a SwapchainPanel, Unity renders over other elements. This enables
you to render a small object with a transparent background on top of other
non-Unity application content. To do this, enable the [PlayerSettings.WSA-
transparentSwapchain](../ScriptReference/PlayerSettings.WSA-
transparentSwapchain.html) option. You can unload the Unity engine to reclaim
resources when Unity loads up with
[Application.Unload](../ScriptReference/Application.Unload.html).

## Limitations

If you use another application to host your Unity build, Unity won’t control
the runtime lifecycle, so your build might not work. You should also be aware
of the following limitations:

  * You can’t load or integrate more than one instance of the Unity runtime.
  * You might need to adapt your [native](plug-ins-native.html) and [managed](plug-ins-managed.html) **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) to work properly.

## Additional resources

  * [Using Unity as a Library in other applications](UnityasaLibrary.html)

[](uwp-requirements-and-compatibility.html)

UWP requirements and compatibility

[](uwp-getting-started.html)

Get started with Universal Windows Platform

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

