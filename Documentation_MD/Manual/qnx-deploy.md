[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-deploy.html)
  * [中文](/cn/current/Manual/qnx-deploy.html)
  * [日本語](/ja/current/Manual/qnx-deploy.html)
  * [한국어](/kr/current/Manual/qnx-deploy.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-deploy.html)
  * [中文](/cn/current/Manual/qnx-deploy.html)
  * [日本語](/ja/current/Manual/qnx-deploy.html)
  * [한국어](/kr/current/Manual/qnx-deploy.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Build and deliver for QNX](qnx-build-and-deliver.html)
  * Deploy a QNX project

[](qnx-build-command-line.html)

Build for QNX from the command line

[](iphone.html)

iOS

# Deploy a QNX project

Unity uses EGL handled by SDL2, which requires SDL to dynamically load
`libEGL` and `libGLESv2` from the `graphics.conf file`. Unity does not parse
the `conf` file but instead uses environment variables to locate these
libraries.

## Setup

Use the following instructions to deploy QNX.

  1. Use one of the methods to locate the `graphics.conf` file that your screen loads:

     * Start `screen` with the `-c [path/to/graphics.conf]` option.
     * Let your `screen` automatically find the `graphics.conf` file in the folder inside `GRAPHICS_ROOT`.
  2. Make sure the folder that contains `graphics.conf` is part of `LD_LIBRARY_PATH`.

  3. Locate `begin egl display 1` in `graphics.conf`:

     * The line starting with `egl-dlls`should contain `libEGL[-_tag].so`, which is the required `libEGL` (for example, `libEGL_viv.so`).
     * The line starting with `glesv2-dlls` should contain `libGLESv2[-_tag]`, which is the `libGLESv2` (for example, `libGLESv2_viv.so`).
     * Both libraries should be in the same folder as `graphics.conf`.
     * Both library file names must be set up as environment variables.
  4. If you are using `ksh`, set the following environment variables.
    
        SDL_VIDEO_EGL_DRIVER=[name_of_libEGL_in_graphics_conf].so (e.g., run export SDL_VIDEO_EGL_DRIVER=libEGL_viv.so)
    SDL_VIDEO_GL_DRIVER=[name_of_libGLESv2_in_graphics_conf].so (e.g., run export SDL_VIDEO_GL_DRIVER=libGLESv2_viv.so)
    

  5. If you are on `sh`, you need to set the environment with the unity player start. For example, `run SDL_VIDEO_EGL_DRIVER=libEGL_viv.so SDL_VIDEO_GL_DRIVER=libGLESv2_viv.so ./qnxplayer`.

  6. Start the Unity Player.

[](qnx-build-command-line.html)

Build for QNX from the command line

[](iphone.html)

iOS

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

