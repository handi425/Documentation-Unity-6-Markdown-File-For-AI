[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ProfilerGPU.html)
  * [中文](/cn/current/Manual/ProfilerGPU.html)
  * [日本語](/ja/current/Manual/ProfilerGPU.html)
  * [한국어](/kr/current/Manual/ProfilerGPU.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ProfilerGPU.html)
  * [中文](/cn/current/Manual/ProfilerGPU.html)
  * [日本語](/ja/current/Manual/ProfilerGPU.html)
  * [한국어](/kr/current/Manual/ProfilerGPU.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Profile rendering](profile-rendering.html)
  * GPU Usage Profiler module

[](ProfilerRendering.html)

Rendering Profiler module

[](graphics-performance-and-profiling-in-urp.html)

Graphics performance and profiling in URP

# GPU Usage Profiler module

The GPU Usage **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module displays where your
application spends time in the GPU. You can only use the GPU Profiler in [Play
mode](profiling-play-mode.html), or for builds of your application. You can’t
use it to profile the Unity Editor.

By default, the GPU Usage Profiler module isn’t enabled. To enable it, refer
to [Activating Profiler modules](profiler-modules-activate.html).

**Note:** If you have **Graphics Jobs** enabled in the **Player Settings** ,
GPU profiling isn’t supported. For more information, refer to the
documentation on [Player Settings](class-PlayerSettings.html)Settings that let
you set various player-specific options for the final game built by Unity.
[More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings). Additionally, on macOS, you
can profile the GPU only on Mavericks 10.9 and later.

## Chart categories

The GPU Usage Profiler module’s chart has several different categories that
you can use to investigate GPU timings:

**Chart** | **Description**  
---|---  
**Opaque** | Built-in rendering pipeline’s time to render opaque objects.  
**Transparent** | Built-in rendering pipeline’s time to render transparent objects.  
**Shadows/Depth** | Built-in rendering pipeline’s time to render shadow maps.  
**Deferred Geometry** | Built-in deferred rendering pipeline’s time to render geometry.  
**Deferred Lighting** | Built-in deferred rendering pipeline’s time to render lighting.  
**PostProcess** | Built-in rendering pipeline’s time to process post processing effects.  
**Other** | Rendering time to process other things such as Scriptable Rendering Pipelines  
  
## Module details pane

When you select the GPU Usage module, the details pane displays a breakdown of
where the application spent time in the selected frame.

### Views dropdown

You can display the timing data as a hierarchical table. To change the table
views, use the top-left dropdown in the details pane (set to Hierarchy by
default). The views available are:

**Value** | **Description**  
---|---  
**Hierarchy** | Groups the timing data by its internal hierarchical structure. This option displays the elements that your application called in a descending list format, ordered by the time spent by default. You can also order the information by the total amount of GPU time, or the number of calls. To change the column that orders the table, click the table column’s header.  
**Raw Hierarchy** | Displays the timing data in a hierarchical structure that is similar to the call stacks where the timing occurred. Unity lists each call stack separately in this mode instead of merging them, as it does in Hierarchy view.  
  
### Table statistics

The table views have the following columns:

**Value** | **Description**  
---|---  
**Total** | The total amount of time Unity spent on a particular function, as a percentage.  
**DrawCalls** | The number of calls made to this function in this frame.  
**GPU ms** | The total amount of time Unity spent on a particular function, in milliseconds.  
  
## GPU profiling support

The following table lists the platforms that the GPU Usage Profiler module
supports:

**Platform** | **Graphics API** | **Status**  
---|---|---  
**Windows** | DirectX 11, DirectX 12, OpenGL | Supported  
| Vulkan | Not supported  
**macOS** | OpenGL | Supported.  
**Note:** Apple has deprecated support of OpenGL.  
| Metal | Not supported. Use XCode’s GPU Frame Debugger **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) instead.  
**Linux** | OpenGL core | Supported  
| Vulkan | Not supported  
**Web** | All **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) | Not supported  
**Android** | OpenGL | Supported on devices running NVIDIA or Intel GPUs.  
| Vulkan | Not supported  
**iOS, tvOS** | Metal | Not supported. Use XCode’s GPU Frame Debugger UI instead.  
**Tizen** | OpenGL | Not supported.  
  
On Windows, Unity supports Play mode profiling in the Editor with Direct3D 11
and Direct3D 12 APIs only. This is convenient for quick profiling, because it
means you don’t need to build the Player. However, the overhead of running the
Unity Editor affects the Profiler, which might make the profiling results less
accurate.

## Additional resources

  * [Activating Profiler modules](profiler-modules-activate.html)
  * [Connecting the Profiler to a data source](profiler-profiling-applications.html)
  * [Profiler window reference](ProfilerWindow.html)

[](ProfilerRendering.html)

Rendering Profiler module

[](graphics-performance-and-profiling-in-urp.html)

Graphics performance and profiling in URP

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

