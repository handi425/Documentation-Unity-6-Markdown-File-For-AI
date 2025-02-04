[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-memory-introduction.html)
  * [中文](/cn/current/Manual/profiler-memory-introduction.html)
  * [日本語](/ja/current/Manual/profiler-memory-introduction.html)
  * [한국어](/kr/current/Manual/profiler-memory-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-memory-introduction.html)
  * [中文](/cn/current/Manual/profiler-memory-introduction.html)
  * [日本語](/ja/current/Manual/profiler-memory-introduction.html)
  * [한국어](/kr/current/Manual/profiler-memory-introduction.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Memory performance data](profiler-memory.html)
  * Memory Profiler module introduction

[](profiler-memory.html)

Memory performance data

[](profiler-memory-counters-players.html)

Accessing memory counters in players

# Memory Profiler module introduction

The Memory **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module visualizes counters that
represent the total allocated memory in your application. You can use the
memory module to visualize where Unity allocated memory, and in what
categories it spent memory.

The built-in Memory Profiler module displays a basic overview of memory
allocations in your application.

![Profiler window with the Memory module selected](../uploads/Main/profiler-
memory-module.png) Profiler window with the Memory module selected

To view a detailed breakdown of memory usage in your application, use [the
Memory Profiler
package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest).
The package adds an additional Memory Profiler window to the Unity Editor,
which you can then use to analyze memory usage in your application in more
detail than the Memory Profiler module. You can store and compare snapshots to
find memory leaks, or view the memory layout to find memory fragmentation
issues. For more information about the Memory Profiler package, refer to the
[Memory Profiler package
documentation](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest).

## Memory profiling in the Unity Editor

When you [profile your application in Play mode](profiling-play-mode.html),
the Memory Profiler module reports higher data use than a similar profile of
the application built on a target device. This is because the Unity Editor
uses specific objects that take up memory, and the Editor window itself uses
extra memory.

Part of the extra memory use is because Unity treats objects like textures as
read/write enabled in the Editor and keeps an extra copy of each texture on
the CPU. This effectively doubles the reported memory use of textures in the
Editor. For a more accurate idea of memory use by textures, [profile a built
version of your application running on the target platform](profiling-target-
device.html).

Unity can’t cleanly separate the memory that the Profiler itself takes up from
the Play mode’s memory, so memory that the Profiler process uses is also
displayed in the Profiler window.

To remind you of this, a warning displays at the top of the Memory Profiler
module details pane whenever you have the Profiler target set to Play mode or
Editor. For more precise numbers and memory usage for your application,
profile your application on the target device and operating system you intend
it to run on. For more information, refer to [Profiling your
application](profiler-profiling-applications.html).

## Additional resources

  * [Memory Profiler module reference](ProfilerMemory.html)
  * [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
  * [Profiling your application](profiler-profiling-applications.html)
  * [Memory in Unity](performance-memory-overview.html)

[](profiler-memory.html)

Memory performance data

[](profiler-memory-counters-players.html)

Accessing memory counters in players

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

