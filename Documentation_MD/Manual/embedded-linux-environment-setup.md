[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/embedded-linux-environment-setup.html)
  * [中文](/cn/current/Manual/embedded-linux-environment-setup.html)
  * [日本語](/ja/current/Manual/embedded-linux-environment-setup.html)
  * [한국어](/kr/current/Manual/embedded-linux-environment-setup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/embedded-linux-environment-setup.html)
  * [中文](/cn/current/Manual/embedded-linux-environment-setup.html)
  * [日本語](/ja/current/Manual/embedded-linux-environment-setup.html)
  * [한국어](/kr/current/Manual/embedded-linux-environment-setup.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [Embedded Linux](embedded-linux.html)
  * [Get started with Embedded Linux](embedded-linux-get-started.html)
  * Set up your environment for Embedded Linux

[](embedded-linux-install-editor.html)

Install the platform package for Embedded Linux

[](embedded-linux-player-settings.html)

Embedded Linux Player settings

# Set up your environment for Embedded Linux

Set up your environment to develop with Embedded Linux.

To create a Unity application for Embedded Linux, you first need to set up
your Unity project to support Embedded Linux. To support Embedded Linux, a
Unity project requires certain packages and dependencies.

**Note:** You must install the Embedded Linux platform package before you can
set up your environment. For more information, refer to [Install the platform
package for Embedded Linux](embedded-linux-install-editor.html).

## Install the toolchain and SDK packages

After you create a new project with Unity, you must install the following
toolchain and SDK packages for your operating system and target architecture.
To install a Unity package for Embedded Linux toolchain and SDK, refer to
[Install a UPM package by name](upm-ui-quick.html).

Toolchain packages:

**Operating system** | **Package**  
---|---  
**Windows** | `com.unity.toolchain.win-x86_64-embeddedlinux`  
**MacOS** | `com.unity.toolchain.macos-x86_64-embeddedlinux`  
**Linux** | `com.unity.toolchain.linux-x86_64-embeddedlinux`  
  
SDK packages:

**Target architecture** | **Package**  
---|---  
**aarch64** | `com.unity.sdk.embeddedlinux-aarch64`  
**x86_64** | `com.unity.sdk.embeddedlinux-x86_64`  
**arm32** | `com.unity.sdk.embeddedlinux-arm32`  
**x86** | `com.unity.sdk.embeddedlinux-x86`  
  
After you’ve installed the packages, the Package Manager window displays the
toolchain and SDK packages that are installed for Embedded Linux.

![Package Manager window with Embedded Linux toolchain
package](../uploads/Main/embedded-linux-proj-setup-1.png) Package Manager
window with Embedded Linux toolchain package

### Automated packages installation

You can also install the required Embedded Linux packages automatically from
the Build Settings window.

To initiate the automatic installation of packages:

  1. Go to **File** > **Build Profiles** from Unity’s main menu.
  2. In the **Build Profiles** window, select **Add**Build Profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)** to open the **Platform
Browser** window.

  3. In the **Platform Browser** window, select **Embedded Linux** and then click **Add Build Profile**.
  4. Go to **Edit** > **Project Settings** from Unity’s main menu.

If the Unity Editor has the **Install toolchain packages automatically**
option enabled by default, then the required packages such as the toolchain
and SDKs for installed architectures are installed automatically. After the
package installation process is complete, you can check which packages are
installed in the **Toolchain Management (Embedded Linux)** tab in **Project
Settings** A broad collection of settings which allow you to configure how
Physics, Audio, Networking, Graphics, Input and many other areas of your
project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings).

![Installed packages in Toolchain Management \(Embedded
Linux\)](../uploads/Main/embedded-linux-proj-setup-3.png) Installed packages
in Toolchain Management (Embedded Linux)

If the option to automatically install packages is disabled, you can switch to
the **Toolchain Management (Embedded Linux)** tab and click **Install sdk and
toolchain packages**.

After you’ve installed the packages, the Package Manager window displays the
list of all the toolchain packages that are installed for Embedded Linux.

![Install sdk and toolchain packages button in Toolchain Management \(Embedded
Linux\)](../uploads/Main/embedded-linux-proj-setup-2.png) Install sdk and
toolchain packages button in Toolchain Management (Embedded Linux)

## Dependencies

Embedded Linux must provide direct and **indirect dependencies** An
**indirect** , or transitive dependency occurs when your project requests a
package which itself “depends on” another package. For example, if your
project depends on the `alembic@1.0.7` package which in turn depends on the
`timeline@1.0.0` package, then your project has an direct dependency on
Alembic and an indirect dependency on Timeline. [More info](upm-
dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) so Unity can run
correctly.

### Direct dependencies

Direct dependencies load at the application startup.

  * `libm.so.6`
  * `libgcc_s.so.1`
  * `libpthread.so.0`
  * `libc.so.6`
  * `libdl.so.2`
  * `librt.so.1`

### Indirect dependencies

Indirect dependencies load when needed during the application runtime as a
shared library.

**Type** | **Dependencies**  
---|---  
**Audio** |  `libpulse-simple.so.0` `libpulse.so.0` `libesd.so.0` `libasound.so or libasound.so.2`  
**Wayland** |  `libwayland-client.so.0` `libwayland-egl.so.1` `libwayland-cursor.so.0` `libxkbcommon.so.0`  
**X11** |  `libX11.so.6` `libXext.so.6` `libXcursor.so.1` `libXinerama.so.1` `libXi.so.6` `libXrandr.so.2` `libXss.so.1` `libXxf86vm.so.1`  
**OpenGL ES** |  `libEGL.so.1` `libGLESv2.so.2`  
**Vulkan** | `libvulkan.so.1`  
**Devices** | `libudev.so.1`  
  
## Additional resources

  * [System requirements](system-requirements.html)
  * [Develop for Embedded Linux](embedded-linux-develop.html)

[](embedded-linux-install-editor.html)

Install the platform package for Embedded Linux

[](embedded-linux-player-settings.html)

Embedded Linux Player settings

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

