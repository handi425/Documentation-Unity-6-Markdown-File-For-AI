[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/build-for-linux.html)
  * [中文](/cn/current/Manual/build-for-linux.html)
  * [日本語](/ja/current/Manual/build-for-linux.html)
  * [한국어](/kr/current/Manual/build-for-linux.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/build-for-linux.html)
  * [中文](/cn/current/Manual/build-for-linux.html)
  * [日本語](/ja/current/Manual/build-for-linux.html)
  * [한국어](/kr/current/Manual/build-for-linux.html)

  * [Platform development ](PlatformSpecific.html)
  * [Linux](linux.html)
  * Build a Linux application

[](Buildsettings-linux.html)

Linux Build Settings reference

[](linux-editor-troubleshooting.html)

Troubleshooting the Linux Editor issues

# Build a Linux application

To build your Unity application on the Linux platform, use the following
steps:

  1. Open the [Build Profiles window](BuildSettings.html) from **File** > **Build Profiles**.
  2. Select **Add**Build Profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)** to open the **Platform
Browser** window.

  3. Select **Linux** from the list of available platforms and set the required build settings. If **Linux** isn’t an option, select **Install with Unity Hub** and follow the installation instructions. For information on how to install modules, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).
  4. Select **Switch Profile** to set the new build profile as the active profile.
  5. Select **Build** or **Build And Run**. For more information on these options, refer to [Build your application](build-profiles-reference.html#build-your-application).
  6. In the Linux file chooser window, select the destination for Unity to place the build.
  7. In the **Name** field, enter an appropriate name for the build.
  8. Select **Save**. This starts the build process.

## Linux Player build binaries

When you build a Unity application on the Linux platform, Unity produces the
following files, where `ProjectName` is the name of your application:

  * `ProjectName.x86_64`: This is the project executable file for your application. It contains the program entry point that initiates the Unity engine when launched.
  * `UnityPlayer.so`: This `.so` file contains all the native Unity engine code. It’s signed with the Unity Technologies certificate allowing you to verify that no malicious entities have tampered with your engine code.
  * `*.pdb` files: These are symbol files you can use to debug managed (C#) code. Unity copies these files to the build directory if you enable ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)** in the [Build
Settings](Buildsettings-linux.html) window.

  * `*_s.debug` files: These are symbol files you can use to debug native (C/C++) code. Unity copies these files to the build directory if you enable **Development Build** in the [Build Settings](Buildsettings-linux.html) window.
  * `ProjectName_Data` folder: This folder contains all the data needed to run your application.
  * `libdecor-0.so.0`: This `.so` file is a Linux shared library used by Wayland clients to manage client-side window decorations. It ensures consistent window behavior and appearance across various compositors.
  * `libdecor-cairo.so`: This `.so` file is a Linux shared library that integrates Cairo graphics with `libdecor`. It renders client-side decorations in Wayland to enhance visual consistency and performance.

If you’re using the **IL2CPP** A Unity-developed scripting back-end which you
can use as an alternative to Mono when building projects for some platforms.
[More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) **scripting backend** A framework that
powers scripting in Unity. Unity supports three different scripting backends
depending on target platform: Mono, .NET and IL2CPP. Universal Windows
Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-
backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend), your application Player
build also includes the following file and folder:

  * `GameAssembly.so`: This `.so` file contains all managed (C#) game logic and **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) converted into native code (C/C++)
for enhanced performance.

  * `ProjectName_BackUpThisFolder_ButDontShipItWithYourGame` folder: This folder contains intermediate files generated during IL2CPP builds that are useful for debugging rather than distribution.

## Additional resources

  * [Linux Build Settings reference](Buildsettings-linux.html)

[](Buildsettings-linux.html)

Linux Build Settings reference

[](linux-editor-troubleshooting.html)

Troubleshooting the Linux Editor issues

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

