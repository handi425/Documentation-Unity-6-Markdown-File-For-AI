[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scripting-backends-mono.html)
  * [中文](/cn/current/Manual/scripting-backends-mono.html)
  * [日本語](/ja/current/Manual/scripting-backends-mono.html)
  * [한국어](/kr/current/Manual/scripting-backends-mono.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scripting-backends-mono.html)
  * [中文](/cn/current/Manual/scripting-backends-mono.html)
  * [日本語](/ja/current/Manual/scripting-backends-mono.html)
  * [한국어](/kr/current/Manual/scripting-backends-mono.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Scripting backends](scripting-backends.html)
  * Mono overview

[](scripting-backends.html)

Scripting backends

[](scripting-backends-il2cpp.html)

IL2CPP Overview

# Mono overview

The **Mono**scripting backend** A framework that powers scripting in Unity.
Unity supports three different scripting backends depending on target
platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports
only two: .NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend)** compiles code at runtime,
with a technique called just-in-time compilation (JIT). Unity uses a
[fork](https://github.com/Unity-Technologies/mono) of the open source [Mono
project](https://www.mono-project.com/).

Some platforms don’t support JIT compilation, so the Mono backend doesn’t work
on every platform. Other platforms support JIT and Mono but not ahead-of-time
compilation (AOT), and so can’t support the [IL2CPP backend](./scripting-
backends-il2cpp.html). When a platform can support both backends, Mono is the
default. For more information, see [Scripting restrictions](scripting-
restrictions.html).

Mono supports the debugging of managed code. For more information, see
[Debugging C# code in Unity](managed-code-debugging.html).

## Building a project using Mono

You can change the scripting backend Unity uses to build your application in
one of two ways:

  * Through the ****Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings)** menu in the Editor. Perform
the following steps to change the scripting backend through the **Player**
settings menu:

    1. Go to **Edit** > **Project Settings**.
    2. Select **Player** to open the [Player](class-PlayerSettings.html) settings for the current platform in the [Inspector](UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

    3. Under the **Other Settings** sub-menu, navigate to **Configuration** > **Scripting Backend**.
    4. Select **Mono**.
  * Through the Editor scripting API. Use the [PlayerSettings.SetScriptingBackend](../ScriptReference/PlayerSettings.SetScriptingBackend.html) property to change the scripting backend that Unity uses.

![The Configuration section of the Player settings](../uploads/Main/backend-
mono.png) The **Configuration** section of the **Player** settings

To start the build process, open the **Build Profiles** window (Menu: **File**
> **Build Profiles**) and select **Build**.

Both the Mono and **IL2CPP** A Unity-developed scripting back-end which you
can use as an alternative to Mono when building projects for some platforms.
[More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) scripting backends require a new build
for each platform you want to target. For example, to support both the Android
and iOS platforms, you need to build your application twice and produce two
binary files, one for Android and one for iOS.

## Additional resources

  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * [Build profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)

[](scripting-backends.html)

Scripting backends

[](scripting-backends-il2cpp.html)

IL2CPP Overview

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

