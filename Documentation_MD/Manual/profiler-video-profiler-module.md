[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-video-profiler-module.html)
  * [中文](/cn/current/Manual/profiler-video-profiler-module.html)
  * [日本語](/ja/current/Manual/profiler-video-profiler-module.html)
  * [한국어](/kr/current/Manual/profiler-video-profiler-module.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-video-profiler-module.html)
  * [中文](/cn/current/Manual/profiler-video-profiler-module.html)
  * [日本語](/ja/current/Manual/profiler-video-profiler-module.html)
  * [한국어](/kr/current/Manual/profiler-video-profiler-module.html)

  * [Video and cutscenes](Video.html)
  * Video Profiler module

[](VideoPanoramic.html)

Panoramic video

[](scripting.html)

Scripting

# Video Profiler module

The Video **Profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module displays information about
what resources the video in your application is using, such as memory,
buffering, and number of [video clips](class-VideoClip.html). You can use this
to determine how efficiently your application plays back and buffers videos on
your selected platforms. You can also use the CPU Usage Profiler module to
assess where Unity spends time on video. For more information, see the [CPU
Usage Profiler module](ProfilerCPU.html) documentation.

To open the Profiler window, go to menu: **Window > Analysis > Profiler**.

![The Video Profiler module](../uploads/Main/video-profiler-module.png) The
Video Profiler module

## Chart categories

The Video Profiler module’s chart is divided into four categories. To change
the order of the categories in the chart, you can drag and drop them in the
chart’s legend. You can also click a category’s colored legend to toggle its
display. For more information on how to use the Profiler window, see the
documentation on [Getting started with the Profiler
window](ProfilerWindow.html).

**Chart** | **Description**  
---|---  
**Total Video Sources** | The total number of video sources in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).  
**Playing Video Sources** | The number of video sources playing in your Scene.  
**Pre-buffered frames** | The total number of pre-buffered frames.  
**Total Video Memory** | The amount of system memory the video in your application is using.  
  
## Module details pane

When you select a frame in the Video Profiler module, the module details pane
at the bottom of the Profiler window displays further detailed information on
the video playback in your Scene. The following information is available:

**Detail** | **Description**  
---|---  
**Total Video Sources** | The number of video sources in your Scene.  
**Playing Video Sources** | The number of video sources playing in your Scene.  
**Paused Video Sources** | The number of video sources that are paused.  
**Software Video Playback** | The number of videos playing that the platform doesn’t natively support.  
**Pre-buffered frames** | The total number of pre-buffered frames.  
**Pre-buffered frame limit** | The pre-buffered frame limit. Unity buffers up to 16 frames per clip.  
**Total frames dropped** | Number of frames that Unity had to skip in order to maintain real time. This might happen when your application runs slowly and cannot produce frames fast enough to play in real time.  
**Video Clip Count** | The number of video clips in your Scene.  
**Total Video Memory** | The amount of system memory the video in your application is using.  
  
## Additional resources

  * [Profiler window introduction](ProfilerWindow.html)
  * [Profiling your application](profiler-profiling-applications.html)

[](VideoPanoramic.html)

Panoramic video

[](scripting.html)

Scripting

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

