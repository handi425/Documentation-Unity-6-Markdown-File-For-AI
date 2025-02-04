[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/embedded-linux-deploy.html)
  * [中文](/cn/current/Manual/embedded-linux-deploy.html)
  * [日本語](/ja/current/Manual/embedded-linux-deploy.html)
  * [한국어](/kr/current/Manual/embedded-linux-deploy.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/embedded-linux-deploy.html)
  * [中文](/cn/current/Manual/embedded-linux-deploy.html)
  * [日本語](/ja/current/Manual/embedded-linux-deploy.html)
  * [한국어](/kr/current/Manual/embedded-linux-deploy.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [Embedded Linux](embedded-linux.html)
  * [Build and deliver for Embedded Linux](embedded-linux-build-and-deliver.html)
  * Deploy an Embedded Linux project

[](embedded-linux-build-command-line.html)

Build for Embedded Linux from the command line

[](qnx.html)

QNX

# Deploy an Embedded Linux project

On the Embedded Linux player, Unity uses SDL2 to handle keyboard, mouse, and
gamepad input to interact with the Player window. Depending on the graphics
API used, it requires SDL to dynamically load `libEGL` and `libGLESv2` for
OpenGL ES, or `libvulkan` for Vulkan from the user space.

## Setup for [Wayland](https://wiki.archlinux.org/title/Wayland)

Although this setup assumes that you’re using
[weston](https://gitlab.freedesktop.org/wayland/weston) (the reference Wayland
server), you can use the same setup with slight modifications for another
compositor.

## Prerequisites

This assumes that you have a Wayland compositor (weston) running, which
exports the wayland socket in the directory that the environment variable
`XDG_RUNTIME_DIR` is linked to.

### Setup on Desktop shell

To deploy your project on desktop shell:

  1. Verify that the environment variable `XDG_RUNTIME_DIR` is set to the correct directory. If not, then run `export XDG_RUNTIME_DIR=/run/user/1000/` with the correct directory (`/run/user/1000/`is the default for a weston installation).
  2. Run Unity Player.

### Additional information

By default, Unity creates surfaces of the same size as the physical displays.
If you want to use surfaces other than physical displays, such as rendering
multiple surfaces to one screen, use `UNITY_IVI_EXPORT_DISPLAYS` as the
environment variable.

For example, with the setting `export`
`UNITY_IVI_EXPORT_DISPLAYS=1024x768@60,1920x1080@60` Unity uses a surface size
of _1024x768_ for Unity Display 1, and a surface size of _1920x1080_ for Unity
Display 2.

You can omit `@60` and use `export
UNITY_IVI_EXPORT_DISPLAYS=1024x768,1920x1080`because `@60` is automatically
assumed.

[](embedded-linux-build-command-line.html)

Build for Embedded Linux from the command line

[](qnx.html)

QNX

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

