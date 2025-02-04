[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/frame-timing-manager-enable.html)
  * [中文](/cn/current/Manual/frame-timing-manager-enable.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-enable.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/frame-timing-manager-enable.html)
  * [中文](/cn/current/Manual/frame-timing-manager-enable.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-enable.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-enable.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Timing Manager](frame-timing-manager-landing.html)
  * Enable the FrameTimingManager

[](frame-timing-manager.html)

Introduction to the Frame Timing Manager

[](frame-timing-manager-get-timing-data.html)

Get frame timing data

# Enable the FrameTimingManager

**Tip** : FrameTimingManager is always active for Development Player builds.

To enable the FrameTimingManage for Release builds and in the Unity Editor:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , navigate to the **Rendering** heading.
  3. Enable the **Frame Timing Stats** property.

If you use the OpenGL platform, you also need to enable the
**OpenGL:**Profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) GPU Recorders** property to measure
GPU usage. To do this:

  1. Go to **Edit** > **Project** > **Settings** > **Player**.
  2. In **Other Settings** , navigate to the **Rendering** heading.
  3. Enable the **OpenGL: Profiler GPU** property.

Note: In Unity versions 2021.2 and earlier, the **OpenGL Profiler GPU
Recorder** disables the **Frame Timing Stats** property, so you can’t use them
together.

To access data that the FrameTimingManager records, use one of the following
methods:

  * [Retrieve timestamp data from the FrameTimingManager C# API](frame-timing-manager-get-timing-data.html).
  * [View frame time data in a Custom Profiler module](frame-timing-manager-get-timing-data.html#ViewFrameTimeDataCustomProfilerModule).
  * [Record data through specific profiler counters.](frame-timing-manager-record-timing-data.html)

[](frame-timing-manager.html)

Introduction to the Frame Timing Manager

[](frame-timing-manager-get-timing-data.html)

Get frame timing data

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

