[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-touch-input.html)
  * [中文](/cn/current/Manual/qnx-touch-input.html)
  * [日本語](/ja/current/Manual/qnx-touch-input.html)
  * [한국어](/kr/current/Manual/qnx-touch-input.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-touch-input.html)
  * [中文](/cn/current/Manual/qnx-touch-input.html)
  * [日本語](/ja/current/Manual/qnx-touch-input.html)
  * [한국어](/kr/current/Manual/qnx-touch-input.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Develop for QNX](qnx-develop.html)
  * Support touch input for QNX

[](qnx-autodetect-plugins.html)

Autodetect plug-ins for QNX

[](qnx-optional-features.html)

Enable optional features for QNX

# Support touch input for QNX

The Unity QNX Player supports input via touch devices. To enable this, make
sure you meet the following prerequisites and operating system configuration
requirements.

## Prerequisites

  * QNX Image has the required touch libraries and utilities installed.
  * Touch configuration is set up for touch devices ([QNX 7.0 doc](https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.screen/topic/manual/mtouch_config.html) / [QNX 7.1 doc](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/mtouch_config.html)).
  * `mtouch` ([QNX 7.0 doc](https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.screen/topic/manual/mtouch.html) / [QNX 7.1 doc](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/mtouch.html)) service is running.

## Configure QNX touch scaling

As the QNX Unity player requires the touch coordinates to be in screen
coordinates, configure the following setup in the `scaling.conf` file:

  1. Configure the QNX `scaling.conf` ([QNX 7.0](https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.screen/topic/manual/mtouch_scaling_config.html)/[QNX 7.1](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/mtouch_scaling_config.html)) file to use screen coordinates. For example, if you have a `1366x768` display, set `mode:scale` for the display resolution to `scaling.conf: 1366x768:mode=scale`.
  2. Restart the `mtouch` service.

## Verify your setup

If you have installed the `events` ([QNX
7.0](https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.screen/topic/manual/events_binary.html)/[QNX
7.1](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/events_binary.html))
utility on the QNX image, you can use it to verify if the touch service is set
up correctly. The reported coordinates (`pos`) should be in the range `[(0,0),
(DisplayWidth, DisplayHeight)]`.

If the coordinates are outside the range, check if the scaling mode in
`scaling.conf` is correct and the touch device specific parameters in the
`mtouch.conf` ([QNX
7.0](https://www.qnx.com/developers/docs/7.0.0/#com.qnx.doc.screen/topic/manual/mtouch_config.html)/[QNX
7.1](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/mtouch_config.html))
file are matching the used device.

## Additional resources

  * [Autodetect plug-ins for QNX](qnx-autodetect-plugins.html)
  * [Optional features](qnx-optional-features.html)

[](qnx-autodetect-plugins.html)

Autodetect plug-ins for QNX

[](qnx-optional-features.html)

Enable optional features for QNX

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

