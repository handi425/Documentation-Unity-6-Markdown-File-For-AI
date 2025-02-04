[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-track-garbage-collection.html)
  * [中文](/cn/current/Manual/performance-track-garbage-collection.html)
  * [日本語](/ja/current/Manual/performance-track-garbage-collection.html)
  * [한국어](/kr/current/Manual/performance-track-garbage-collection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-track-garbage-collection.html)
  * [中文](/cn/current/Manual/performance-track-garbage-collection.html)
  * [日本語](/ja/current/Manual/performance-track-garbage-collection.html)
  * [한국어](/kr/current/Manual/performance-track-garbage-collection.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Managed memory](performance-managed-memory.html)
  * Tracking garbage collection allocations

[](performance-disabling-garbage-collection.html)

Configuring garbage collection

[](performance-optimizing-code-managed-memory.html)

Optimizing your code for managed memory

# Tracking garbage collection allocations

Unity has the following tools to keep track of memory allocations:

  * [The CPU Usage Profiler module](profiler-cpu.html): Provides details of the garbage allocation per frame.
  * [The Memory Profiler module](ProfilerMemory.html): Provides high-level memory usage frame by frame.
  * [The Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest): A separate Unity package which provides detailed information about memory usage at specific points in time during in your application.

## Tracking allocations with the CPU Usage module

To track garbage collection allocations with the [CPU Usage Profiler
module](profiler-cpu.html), perform the following steps:

  1. Open the [Profiler window](ProfilerWindow.html) (**Window** > **Analysis** > **Profiler**).
  2. [Collect some performance data](profiling-collect-data-introduction.html).
  3. Select a frame in the CPU Usage **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module.

  4. In the module details pane, open the [Hierarchy view](ProfilerCPU.html), and inspect the **GC.Alloc** column.

The **GC.Alloc** column displays the number of bytes that Unity allocated on
the managed heap for the selected frame and thread.

Allocations can occur on all threads so you might want to use the thread
selection drop down to check out other threads than the main thread. You can
also use the [Timeline view](ProfilerCPU.html) and keep an eye out for the
`GC.Alloc` samples, which are colored bright magenta.

**Tip:** Use the [Call Stacks mode](profiler-cpu-navigating.html#call-stacks)
to enable the full call stack traces for `GC.Alloc` samples. Call stacks give
you precise details of where the garbage collector made the allocation without
needing to use [Deep Profiling](profiler-deep-profiling.html) mode, which
might impact performance.

## Tracking allocations with the Memory module

You can use the [Memory Profiler module](profiler-memory-introduction.html) to
track garbage collection memory allocations, but it only provides a high-level
overview of where Unity allocated memory. For detailed information on memory
usage in your application, use the [Memory Profiler
package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest).

To track garbage collection memory allocations with the Memory Profiler
module, perform the following steps:

  1. Open the [Profiler window](ProfilerWindow.html) (**Window** > **Analysis** > **Profiler**).
  2. [Collect some performance data](profiling-collect-data-introduction.html).
  3. Select a frame in the Memory Profiler module.
  4. In the module details pane, inspect the **GC allocated in frame** statistic.

The **Managed Heap** statistic displays the amount of memory that the garbage
collector managed, and it includes memory that Unity might have allocated and
reused in subsequent frames. This means that the sum of the `GC.Alloc` samples
over all frames doesn’t total how much the managed memory grew in that time.

The **GC allocated in frame** statistic diplays the amount of memory that was
allocated in this frame. This amount might be higher than the CPU Usage module
displays in the **GC.Alloc** column of the Hierarchy view. This is because the
`GC.Alloc` statistic includes allocations made across all threads and also
within [Editor only samples](profiler-play-edit-samples.html), or as part of
the `EditorLoop`. The Hierarchy view only displays one thread at a time and
hides the allocations made in Editor only samples by default and collapses the
code running as part of the `EditorLoop` unless the [profiler targets the
Editor](profiling-edit-mode.md) and not Play mode.

**Important:** To get the most accurate information, [profile your
application](profiler-profiling-applications.html) on a **development build**
A development build includes debug symbols and enables the Profiler. [More
info](https://docs.unity.com/devops/en/manual/build-target-
configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild) on the target platform or
device you want to build to. The Unity Editor works in a different way to a
build, and this affects the profiling data. For example, the `GetComponent`
method always allocates memory when it’s executed in the Editor, but not in a
built project.

## Additional resources

  * [Managed memory introduction](performance-managed-memory-introduction.html)
  * [Garbage collector introduction](performance-garbage-collector.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)

[](performance-disabling-garbage-collection.html)

Configuring garbage collection

[](performance-optimizing-code-managed-memory.html)

Optimizing your code for managed memory

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

