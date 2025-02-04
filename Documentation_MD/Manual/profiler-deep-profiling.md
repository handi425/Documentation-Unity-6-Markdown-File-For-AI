[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-deep-profiling.html)
  * [中文](/cn/current/Manual/profiler-deep-profiling.html)
  * [日本語](/ja/current/Manual/profiler-deep-profiling.html)
  * [한국어](/kr/current/Manual/profiler-deep-profiling.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-deep-profiling.html)
  * [中文](/cn/current/Manual/profiler-deep-profiling.html)
  * [日本語](/ja/current/Manual/profiler-deep-profiling.html)
  * [한국어](/kr/current/Manual/profiler-deep-profiling.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * Instrument all function calls

[](profiler-play-edit-samples.html)

Play mode and Editor profile samples

[](profiler-window-navigating.html)

Navigating the Profiler window

# Instrument all function calls

The **Profiler** A window that helps you to optimize your game. It shows how
much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) only profiles code timings that are
explicitly wrapped in [Profiler markers](profiler-markers.html)Placed in code
to describe a CPU or GPU event that is then displayed in the Unity Profiler
window. Added to Unity code by default, or you can use [ProfilerMarker
API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-
guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#Profilermarker). This includes the first call
stack depth of invocations from Unity’s native code into your scripting code,
such as `MonoBehaviour.Start`, `MonoBehaviour.Update`, or similar methods.

The only samples you can visualize as child samples of your scripting code are
those that call back into Unity’s API, if that API is instrumented, or any of
your own code which has explicit Profiler marker instrumentation. Most API
calls that carry a performance overhead are instrumented. For example,
accessing the main **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) through the `Camera.main` API
registers as a `FindMainCamera` sample.

## Deep profiling

If you want to get data about all function calls to find out where your code
impacts on your application’s performance, you can use the **Deep Profile**
setting. When you enable the Deep Profile setting, the Profiler injects
profiler instrumentation into all your script methods to record all function
calls, including at least the first call stack depth into any Unity API.

Deep Profiling is resource-intensive and uses a lot of memory. As a result,
your application runs significantly slower while it’s profiling. Deep
Profiling works best for small games with simple scripting. If you use complex
script code, your application might not be able to use Deep Profiling, and for
many larger applications, Deep Profiling might make Unity run out of memory.

### Enabling Deep Profiling

You can enable Deep Profiling if you’re collecting performance data from a
connected application, or if you’re collecting data in the Unity Editor.

To enable Deep Profiling for a built application:

  1. Open the **Build Profiles** window (**File** > **Build Profiles**)
  2. Select your application’s target platform
  3. Enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)** setting

  4. Enable **Deep Profiling**

To enable Deep Profiling when you collect data in the Editor:

  1. Open the Profiler window (**Window** > **Analysis** > **Profiler**)
  2. Select **Deep Profile** from the [Profiler toolbar](ProfilerWindow.html).

The Profiler then instruments all function calls when you start a profiling
session.

## Additional resources

  * [Build Profiles Profile settings reference](profiler-build-settings-reference.html)
  * [Profiler markers introduction](profiler-markers.html)
  * [Collect performance data introduction](profiling-collect-data-introduction.html)

[](profiler-play-edit-samples.html)

Play mode and Editor profile samples

[](profiler-window-navigating.html)

Navigating the Profiler window

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

