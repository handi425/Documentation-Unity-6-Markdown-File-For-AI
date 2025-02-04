[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-environment-setup.html)
  * [中文](/cn/current/Manual/qnx-environment-setup.html)
  * [日本語](/ja/current/Manual/qnx-environment-setup.html)
  * [한국어](/kr/current/Manual/qnx-environment-setup.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-environment-setup.html)
  * [中文](/cn/current/Manual/qnx-environment-setup.html)
  * [日本語](/ja/current/Manual/qnx-environment-setup.html)
  * [한국어](/kr/current/Manual/qnx-environment-setup.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Get started with QNX](qnx-get-started.html)
  * Set up your environment for QNX

[](qnx-install-editor.html)

Install the platform package for QNX

[](qnx-player-settings.html)

QNX Player settings reference

# Set up your environment for QNX

Set up your environment to develop with QNX.

To create a Unity application for QNX, you first need to set up your Unity
project to support QNX. To support QNX, a Unity project requires certain
environment variables and dependencies.

**Note** : You must install the QNX platform package before you can set up
your environment. For more information, refer to [Install the platform package
for QNX](qnx-install-editor.html).

## Set the environment variables

After you have installed the Unity Editor, you will need to set the
environment variables. Open a terminal window and run one of the following
commands to set the environment variables in the local shell and start the
Editor from there.

  * `qnxsdp-env.bat` (Windows)
  * `source path/qnxsdp-env.sh` (Linux and macOS)

Alternatively, you can set the environment variables `QNX_TARGET` and
`QNX_HOST` either locally in a terminal or globally, and then run the Editor.

These are the environment variables you need to set:

  * `QNX_TARGET=/path/to/target/qnx7`
  * `QNX_HOST=/path/to/host/platform/arch`
  * `MAKEFLAGS=-I$QNX_TARGET/usr/include` (for QNX 7.0 only)
  * Add to `PATH:` `$QNX_HOST/usr/bin` (for QNX 7.1 only)

## Dependencies

QNX must provide direct and **indirect dependencies** An **indirect** , or
transitive dependency occurs when your project requests a package which itself
“depends on” another package. For example, if your project depends on the
`alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package,
then your project has an direct dependency on Alembic and an indirect
dependency on Timeline. [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) so Unity can run
correctly.

### Direct dependencies

Direct dependencies load at the application startup.

  * `libm.so.3`
  * `libgcc_s.so.1`
  * `libc.so.5`
  * `libsocket.so.3`
  * `libasound.so.3`
  * `libscreen.so.1`

### Indirect dependencies

Indirect dependencies load when needed during the application runtime, as a
shared library.

**Type** | **Dependencies**  
---|---  
**Webcam** | `libcamapi.so`  
**OpenGL ES** |  `libEGL.so.1` `libGLESv2.so.2`  
**Devices** | `libudev.so.1`  
  
## Troubleshooting

If you notice one of the following issues in the **Build Profiles** A set of
customizable configuration settings to use when creating a build for your
target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window, then the QNX SDP
Environment isn’t set up correctly:

  * **Unable to find QNX_TARGET in Environment.**
  * **The build environment does not fit the selected QNX Version.**
  * **The build environment does not contain the selected QNX Architecture.**

Before starting the Editor, always check that you have the QNX SDP Environment
set up correctly for the Editor to register it. For more information, refer to
[QNX Software
Center](https://www.qnx.com/download/group.html?programid=29178).

## Additional resources

  * [QNX product documentation](http://www.qnx.com/developers/docs/index.html)

[](qnx-install-editor.html)

Install the platform package for QNX

[](qnx-player-settings.html)

QNX Player settings reference

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

