[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-optional-features.html)
  * [中文](/cn/current/Manual/qnx-optional-features.html)
  * [日本語](/ja/current/Manual/qnx-optional-features.html)
  * [한국어](/kr/current/Manual/qnx-optional-features.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-optional-features.html)
  * [中文](/cn/current/Manual/qnx-optional-features.html)
  * [日本語](/ja/current/Manual/qnx-optional-features.html)
  * [한국어](/kr/current/Manual/qnx-optional-features.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Develop for QNX](qnx-develop.html)
  * Enable optional features for QNX

[](qnx-touch-input.html)

Support touch input for QNX

[](qnx-troubleshooting.html)

Troubleshooting the QNX Player

# Enable optional features for QNX

You can launch the Unity QNX Player from the command line and pass arguments
to change how the Player executes.

**Important** : All command line arguments have precedence over the Unity
Editor and `boot.config` settings.

Command | Details  
---|---  
`-log-startup-times-and-quit` | [Deprecated] Quit player after rendering the first frame.  
`-platform-hmi-force-srgb-blit` | Configure the path to the `graphics.conf` to override [auto detection](qnx-autodetect-plugins.html).  
`-platform-hmi-quit-after-frame` | Enable logging. Refer to [**Player Settings**](qnx-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-log-startup-times` | Enable logging. Refer to [**Player Settings**](qnx-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-force-vsync-count [C]` | The number of vertical syncs that are allowed to pass between each frame. Where, setting 0 disables **vsync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](Glossary.html#VSync) completely, –1 will use the value set
in `QualitySettings`.  
  
## Startup time logging

Startup time logging is the length of time that it takes an application to
start up. It’s often used as a critical metric for system safety and
regulatory requirements.

Startup time logging in QNX devices include the duration or total time from
the time the application launches. There are two types of Startup time
logging:

  * **Real:** This is the actual wall or clock time, similar to a stopwatch used for calculating the time.
  * **User:** This is the time an application or one of its threads has spent on a CPU core. This can be higher than the Real time if multiple threads are busy when an application is starting up.

### Example output

    
    
    [TIMING::STARTUP] Initial probing done: Real: 19 ms | User: 11 ms
    [TIMING::STARTUP] SDL Initialized: Real: 64 ms | User: 54 ms
    [TIMING::STARTUP] Scripting runtime loaded: Real: 97 ms | User: 86 ms
    [TIMING::STARTUP] Plugins loaded: Real: 97 ms | User: 87 ms
    [TIMING::STARTUP] Engine initialized (nogfx): Real: 104 ms | User: 94 ms
    [TIMING::STARTUP] Player Prefs loaded: Real: 104 ms | User: 94 ms
    [TIMING::STARTUP] Screen initialized: Real: 139 ms | User: 112 ms
    [TIMING::STARTUP] Engine initialized (gfx): Real: 187 ms | User: 161 ms
    [TIMING::STARTUP] Gfx initialized: Real: 190 ms | User: 163 ms
    [TIMING::STARTUP] Input initialized: Real: 190 ms | User: 163 ms
    [TIMING::STARTUP] SPLASH - Begin: Real: 190 ms | User: 164 ms
    [TIMING::STARTUP] SPLASH - Primary scene assets loaded (async): Real: 2197 ms | User: 1670 ms
    [TIMING::STARTUP] SPLASH - All engine initial states established: Real: 2197 ms | User: 1670 ms
    

Output from a custom event using the Script API

`[TIMING::STARTUP] HELLO!!: Real: 2198 ms | User: 1671 ms`

When you specify `platform-hmi-quit-after-frame` in `boot.config` output, then
the following will be in the log up until frame number `X`. Where, `X` is the
number provided for the boot configuration value.

`[TIMING::STARTUP] Frame 1 rendered: Real: 2209 ms | User: 1687 ms`

`[TIMING::STARTUP] Frame 2 rendered: Real: 2210 ms | User: 1692 ms`

## Webcam

**Note:** Unity’s support for Webcam in QNX is currently experimental.

#### Prerequisites

  * QNX 7.1
  * `libcamapi` and its dependencies installed on the system (will be loaded dynamically)
  * **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) supporting `NV12` format

[Webcam](../ScriptReference/WebCamTexture.html) usage is optional in QNX and
it’s only supported on QNX 7.1. For more information, refer to the
[Webcam](../ScriptReference/WebCamTexture.html) documentation.

## Additional resources

  * [Autodetect plug-ins for QNX](qnx-autodetect-plugins.html)
  * [Support touch input for QNX](qnx-touch-input.html)

[](qnx-touch-input.html)

Support touch input for QNX

[](qnx-troubleshooting.html)

Troubleshooting the QNX Player

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

