[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiling-collect-data-introduction.html)
  * [中文](/cn/current/Manual/profiling-collect-data-introduction.html)
  * [日本語](/ja/current/Manual/profiling-collect-data-introduction.html)
  * [한국어](/kr/current/Manual/profiling-collect-data-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiling-collect-data-introduction.html)
  * [中文](/cn/current/Manual/profiling-collect-data-introduction.html)
  * [日本語](/ja/current/Manual/profiling-collect-data-introduction.html)
  * [한국어](/kr/current/Manual/profiling-collect-data-introduction.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * Collect performance data introduction

[](profiler-collect-data.html)

Collect performance data

[](profiler-profiling-applications.html)

Connecting the Profiler to a data source

# Collect performance data introduction

Collect performance data related to your application with the Profiler.

To collect data, you must connect the Profiler to a data source. You also must
enable any [Profiler modules](profiler-modules-introduction.html) that you
want to collect data for.

You can collect data with the [Profiler](profiler-introduction.html)A window
that helps you to optimize your game. It shows how much time is spent in the
various areas of your game. For example, it can report the percentage of time
spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) from the following sources:

  * Profile your application in a player on a target platform
  * Profile your application in Play mode
  * Profile the Unity Editor

The Profiler collects data only for the Profiler modules you have enabled. For
more information, refer to [Activating Profiler modules](profiler-modules-
activate.html).

## Collect performance data on a target platform

The best way to get accurate timings about your application is to [profile it
on the end platform](profiling-target-device.html) you intend to publish it
on. This gives you accurate timings about what impacts the performance of your
application.

## Collect performance data in Play mode

It can be time-consuming to build your application every time you want to
improve elements of its performance. To quickly assess the performance of your
application you can [profile it directly in Play mode](profiling-play-
mode.html) in the Editor. The Profiler’s default target is Play mode.

Play mode runs in the same application and main thread as the Editor which
means that the Editor’s systems such as the **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), **Inspectors** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view rendering, and asset management
affect the performance and memory measurements you get when profiling in Play
mode.

Profiling in Play mode doesn’t give you an accurate reflection of what the
performance of your application looks like on a real device. It’s useful to
test out changes without having to rebuild a player, and to identify areas to
investigate further.

To effectively profile in Play mode, build your application often and deploy
it to a range of target devices, and test and profile your application on
these devices. If you identify performance issues with your application on
these devices, narrow down the area that needs the most attention.

You can then profile your application in Play mode and quickly iterate over
any changes you make to your application. Once you’re satisfied with your
changes, build and deploy your application to the target devices again to
validate your changes.

## Collect performance data about the Unity Editor

The Editor might affect the performance of your application, because it uses
the same resources as your application when it’s running in Play mode. You can
[profile the Editor](profiling-edit-mode.html) separately to find out what
resources it uses. This is useful if you have designed your application to
work only in Play mode, such as for movie making.

You can also profile in Play mode or profile the Editor to identify issues
unrelated to the performance of your application. For example, to investigate
if long load times or an unresponsive Editor slows down iteration time, or if
your application’s performance is poor in Play mode.

## Additional resources

  * [Connecting the Profiler to your application](profiler-profiling-applications.html)
  * [Profiler modules introduction](profiler-modules-introduction.html)
  * [Profiler window reference](ProfilerWindow.html)

[](profiler-collect-data.html)

Collect performance data

[](profiler-profiling-applications.html)

Connecting the Profiler to a data source

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

