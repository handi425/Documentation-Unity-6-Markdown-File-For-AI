[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/linux-il2cpp-crosscompiler.html)
  * [中文](/cn/current/Manual/linux-il2cpp-crosscompiler.html)
  * [日本語](/ja/current/Manual/linux-il2cpp-crosscompiler.html)
  * [한국어](/kr/current/Manual/linux-il2cpp-crosscompiler.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/linux-il2cpp-crosscompiler.html)
  * [中文](/cn/current/Manual/linux-il2cpp-crosscompiler.html)
  * [日本語](/ja/current/Manual/linux-il2cpp-crosscompiler.html)
  * [한국어](/kr/current/Manual/linux-il2cpp-crosscompiler.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Scripting backends](scripting-backends.html)
  * [IL2CPP Overview](scripting-backends-il2cpp.html)
  * Linux IL2CPP cross-compiler

[](handling-il2cpp-additional-args.html)

Handling platform specific settings for IL2CPP additional arguments

[](il2cpp-windows-runtime-support.html)

Windows Runtime support

# Linux IL2CPP cross-compiler

The Linux **IL2CPP** A Unity-developed scripting back-end which you can use as
an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) cross-compiler is a set of sysroot and
toolchain packages that allow you to build Linux IL2CPP Players on any
Standalone platform without needing to use the Linux Unity Editor or rely on
Mono.

If you meet the prerequisites, Unity automatically installs these packages for
you when you choose the Linux build target. If you want to opt out of this
process and use your own sysroot and toolchain packages, go to **Edit** >
**Project Settings** > **Toolchain Management** and disable the **Install
Toolchain package automatically** checkbox. If you already have these
installed, you also need to remove them from the package manager.

**Warning:** Setting additional IL2CPP arguments might affect your project
compilation. For more information, refer to [Handling platform specific
settings for IL2CPP additional arguments](handling-il2cpp-additional-
args.html).

![Build settings window with Linux build target
selected](../uploads/Main/linuxBuildSettings.png) Build settings window with
Linux build target selected

## Prerequisites

Unity needs the following to install the IL2CPP cross-compiler packages:

  * Unity 2019.4 or above.
  * Enough available disk space for your chosen Linux toolchain package. For further information, refer to the Required disk space for Linux toolchain packages.
  * Scripting backend set to IL2CPP. To set the scripting backend to IL2CPP: Go to **Edit** > **Project** **Setting** > **Player** **Settings** > **Setting** **for** **PC, Mac and Linux Standalone** > **Other Settings** > **Configuration.** Set the **Scripting Backend to** **IL2CPP**.
  * IL2CPP module. For information on how to install the IL2CPP module, follow the steps documented on [Adding modules](https://docs.unity3d.com/hub/manual/AddModules.html).

## Linux sysroot package

A Linux sysroot package is a directory which includes all the headers and
libraries you need to build for Linux.

Every operating system (OS) has its own build systems which vary from one to
another. If you build using the headers and libraries of a particular OS, the
built Player might not run on other operating systems. To address this, Unity
provides a sysroot to build with which works on all supported Linux platforms.

## Linux toolchain packages

Unity provides toolchain packages for macOS, Windows, and Linux. Each of these
platforms builds for Linux in a unique way.

A Linux toolchain package is a set of tools (including the compiler and
linker) that Unity needs to build for Linux from each of these operating
systems.

## Required disk space for Linux toolchain packages

Make sure you have enough disk space to account for the package download,
decompression, and use.

In the rare instances where you are unsure whether you have enough space,
define a UNITY_SYSROOT_CACHE environment variable and use it to store the
uncompressed sysroots and toolchain packages. An environment variable is a
variable that you set outside of Unity which is available for Unity to
reference. In this case, you set a cache that Unity can reference when
decompressing the sysroot and toolchain packages. Environment variables are
specific to your operating system, so you need to follow your system’s
guidelines to set them.

The table below shows the total disk space requirements for each toolchain
package.

Toolchain package | Required disk space  
---|---  
com.unity.toolchain.linux-x86_64 | 462MB  
com.unity.toolchain.macos-x86_64-linux-x86_64 | 2GB  
com.unity.toolchain.win-x86_64-linux-x86_64 | 2GB  
  
## Using the Linux IL2CPP cross-compiler

If you meet all the prerequisites on this page, you can build your project as
a Linux Player. Unity automatically uses the Linux IL2CPP cross-compiler at
build time.

To build a Linux Player, follow these steps:

  1. Open the **Build Settings** (menu: **File** > **Build Settings).**
  2. Select the **Windows, Mac, Linux** option.
  3. Set the **Build Target** option to **Linux**.
  4. Click the **Switch Platform** button.
  5. Build your Player. From Unity’s main menu, go to **File** and select either **Build** or **Build and Run**.

## Additional resources

  * [How to add modules in the Unity Editor](https://docs.unity3d.com/hub/manual/AddModules.html)
  * [Linux Build Settings](Buildsettings-linux.html) platform docs.
  * [Linux Player Settings](PlayerSettings-linux.html)

[](handling-il2cpp-additional-args.html)

Handling platform specific settings for IL2CPP additional arguments

[](il2cpp-windows-runtime-support.html)

Windows Runtime support

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

