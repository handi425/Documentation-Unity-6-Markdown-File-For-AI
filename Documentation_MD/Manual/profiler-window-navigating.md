[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-window-navigating.html)
  * [中文](/cn/current/Manual/profiler-window-navigating.html)
  * [日本語](/ja/current/Manual/profiler-window-navigating.html)
  * [한국어](/kr/current/Manual/profiler-window-navigating.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-window-navigating.html)
  * [中文](/cn/current/Manual/profiler-window-navigating.html)
  * [日本語](/ja/current/Manual/profiler-window-navigating.html)
  * [한국어](/kr/current/Manual/profiler-window-navigating.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * Navigating the Profiler window

[](profiler-deep-profiling.html)

Instrument all function calls

[](profiler-adding-information-code.html)

Adding profiling information to your code

# Navigating the Profiler window

To open the Profiler, go to **Window > Analysis > Profiler** or use the
keyboard shortcut Ctrl+7 (Command+7 on macOS). Use the [Profiler module
charts](profiler-modules-introduction.html) to inspect and analyze Profiler
data.

## Selecting and inspecting a frame

To select and inspect a frame:

  1. Click on the area of a **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module’s chart that you want to
inspect. A white line appears, which highlights one frame of your application.

  2. To navigate between frames, use the [transport controls](ProfilerWindow.html) in the **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) of the Profiler window, or the arrow
keys on your keyboard.

Unity then displays more details about the frame in the panel in the bottom
half of the Profiler window. The type of detail in this window changes
depending on which Profile module you select. For more information about the
specific details that each module displays in this area, refer to the
individual documentation for the [Profiler modules](ProfilerWindow.html).

Unity manages the vertical scale of the charts automatically, and the charts
attempt to fill the vertical space of the window. To inspect a chart in more
detail, drag the splitter between the charts and the details pane to increase
the screen area of the charts.

## Customizing metric views

Hide or display metrics in a module’s chart, or reorder the metrics, to
identify the causes of spikes, or make more prominent metrics visible. To
customize the metrics displayed in a chart:

  1. Click the colored square next to the metric’s label in its module to hide or display the metric.
  2. Click and drag the handle icon (═) next to a metric to recorder it in stacked charts such as the [CPU Usage](ProfilerCPU.html) chart.

## Increasing frame count

By default, the Profiler records and keeps the last 300 frames of your
application, and displays detailed information about every frame. To increase
the default frame count:

  1. Open the Preferences window (**Unity > Settings**)
  2. Select the Profiler preferences (**Analysis > Profiler**)
  3. Enter a value for the **Frame Count** , up to 2,000 frames.

**Note:** If you increase this setting to a large number, the Profiler’s
overhead and memory usage might become more performance intensive.

## Additional resources

  * [Profiler introduction](profiler-introduction.html)
  * [Profiler modules introduction](profiler-modules-introduction.html)
  * [Profiler window reference](ProfilerWindow.html)
  * [Profiling your application](profiler-profiling-applications.html)

[](profiler-deep-profiling.html)

Instrument all function calls

[](profiler-adding-information-code.html)

Adding profiling information to your code

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

