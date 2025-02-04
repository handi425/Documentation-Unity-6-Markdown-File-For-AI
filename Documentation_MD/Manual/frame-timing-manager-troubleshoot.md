[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/frame-timing-manager-troubleshoot.html)
  * [中文](/cn/current/Manual/frame-timing-manager-troubleshoot.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-troubleshoot.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-troubleshoot.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/frame-timing-manager-troubleshoot.html)
  * [中文](/cn/current/Manual/frame-timing-manager-troubleshoot.html)
  * [日本語](/ja/current/Manual/frame-timing-manager-troubleshoot.html)
  * [한국어](/kr/current/Manual/frame-timing-manager-troubleshoot.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * [Frame Timing Manager](frame-timing-manager-landing.html)
  * Troubleshooting the Frame Time Manager

[](frame-timing-manager-record-timing-data.html)

Record frame timing data

[](ProfilerRendering.html)

Rendering Profiler module

# Troubleshooting the Frame Time Manager

For GPUs that use tile-based deferred rendering architecture, such as Metal
GPUs in Apple devices, the reported GPU Time might be larger than the reported
frame time.

This can happen when the GPU is under heavy load, or when the GPU pipeline is
full. In these cases, the GPU might defer execution of some rendering phases.
Because the FrameTimingManager measures the time between the beginning and end
of the frame rendering, any gaps between phases increase the reported GPU
time.

In the example below, no GPU resources are available, because the GPU passes a
job from the Vertex queue to the Fragment queue. The GPU’s graphics API
therefore defers the execution of the next phase. When this happens, the GPU
time measurement includes phase work time and any gap in between. The result
is that the FrameTimingManager reports a higher GPU time measurement than
expected.

![Diagram showing how the discrepancy in reported GPU time can happen in the
Metal API](../uploads/Main/frame-timing-manager-deferred-rendering-
diagram.png) Diagram showing how the discrepancy in reported GPU time can
happen in the Metal API

[](frame-timing-manager-record-timing-data.html)

Record frame timing data

[](ProfilerRendering.html)

Rendering Profiler module

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

