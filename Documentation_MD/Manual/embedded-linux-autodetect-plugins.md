[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/embedded-linux-autodetect-plugins.html)
  * [中文](/cn/current/Manual/embedded-linux-autodetect-plugins.html)
  * [日本語](/ja/current/Manual/embedded-linux-autodetect-plugins.html)
  * [한국어](/kr/current/Manual/embedded-linux-autodetect-plugins.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/embedded-linux-autodetect-plugins.html)
  * [中文](/cn/current/Manual/embedded-linux-autodetect-plugins.html)
  * [日本語](/ja/current/Manual/embedded-linux-autodetect-plugins.html)
  * [한국어](/kr/current/Manual/embedded-linux-autodetect-plugins.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [Embedded Linux](embedded-linux.html)
  * [Develop for Embedded Linux](embedded-linux-develop.html)
  * Autodetect plug-ins for Embedded Linux

[](embedded-linux-develop.html)

Develop for Embedded Linux

[](embedded-linux-optional-features.html)

Enable optional features for Embedded Linux

# Autodetect plug-ins for Embedded Linux

Unity automatically detects plug-ins for Embedded Linux. When you import plug-
ins, Unity creates metadata files for each **plug-in** A set of code created
outside of Unity that creates functionality in Unity. There are two kinds of
plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies
created with tools like Visual Studio) and Native plug-ins (platform-specific
native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in). For example, a `.so` for shared
objects and shared libraries and an `.a` for archive files. These metadata
files contain the plug-in information, such as the target architecture and
platform. The Unity build system refers to these metadata files for tracking
which files to copy over during the build process.

You can have several shared libraries with the same name in a project. For
example, you can have a `libFoo.so` for x86_64 and a `libFoo.so` for ARM64 in
the same project as Unity detects the correct `libFoo.so` for your build
target and copies it across to the Player build.

You can edit these files manually in the Unity Editor. However, you don’t need
to manually add plug-ins to the `Plugins` folder in your project. Instead, you
can place them in special folders located under the project’s
`Assets/Plugins/EmbeddedLinux` folder in the project directory so Unity
automatically detects and sets their platform and architecture for you when
importing.

## Auto detection rules

Unity automatically detects plug-ins for Embedded Linux based on the following
rules:

  * **Architecture-specific folders** : Place plug-ins under `Assets/Plugins/EmbeddedLinux/<arch>`, where `<arch>` is x86, x86_64, ARM, or ARM64. Unity copies them only when building an app for the respective target architecture. For example, if you place a plug-in under `Assets/Plugins/EmbeddedLinux/x86_64`, Unity copies it to the Player build only when building for x86_64.

  * **Plugins with no architecture** : Place plug-ins with no architecture under `Assets/Plugins/EmbeddedLinux` and ensure that they’re checked for the target architecture through their respective ELF headers and that the appropriate architecture is assigned.

[](embedded-linux-develop.html)

Develop for Embedded Linux

[](embedded-linux-optional-features.html)

Enable optional features for Embedded Linux

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

