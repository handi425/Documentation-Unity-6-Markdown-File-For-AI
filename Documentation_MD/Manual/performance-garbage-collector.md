[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-garbage-collector.html)
  * [中文](/cn/current/Manual/performance-garbage-collector.html)
  * [日本語](/ja/current/Manual/performance-garbage-collector.html)
  * [한국어](/kr/current/Manual/performance-garbage-collector.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-garbage-collector.html)
  * [中文](/cn/current/Manual/performance-garbage-collector.html)
  * [日本語](/ja/current/Manual/performance-garbage-collector.html)
  * [한국어](/kr/current/Manual/performance-garbage-collector.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Managed memory](performance-managed-memory.html)
  * Garbage collector overview

[](performance-managed-memory-introduction.html)

Managed memory introduction

[](performance-incremental-garbage-collection.html)

Garbage collection modes

# Garbage collector overview

Unity uses a [garbage collector](https://docs.microsoft.com/en-
us/dotnet/standard/garbage-collection/fundamentals) to reclaim memory from
objects that your application and Unity are no longer using. When a script
tries to make an allocation on the managed heap but there isn’t enough free
heap memory to accommodate the allocation, Unity runs the garbage collector.

When the garbage collector runs, it examines all objects in [the managed
heap](performance-managed-memory-introduction.html), and marks for deletion
any objects that your application no longer references. Unity then deletes the
unreferenced objects, which frees up memory. Ideally the freed memory can then
accommodate the new allocation, and if it can’t, the heap grows and Unity
allocates additional memory blocks for it.

## When the garbage collector reallocates memory

The garbage collector handles subsequent requests in the same way until
there’s no free area large enough to allocate the required block size. In this
situation, it’s unlikely that all allocated memory is still in use. Unity’s
**scripting backends** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) can only access a reference
item on the heap as long as there are still reference variables that can
locate it.

To determine which heap blocks are no longer in use, the garbage collector
searches through all active reference variables and marks the blocks of memory
that they refer to as live. At the end of the search, the garbage collector
considers any space between the live blocks empty and marks them for use for
subsequent allocations. The process of locating and freeing up unused memory
is called **garbage collection** (GC).

**Note:** The garbage collector works differently on the Web platform. For
more information, refer to [Memory in web garbage collection
considerations](webgl-memory.html#garbagecollection).

## Temporary allocations

It’s common for an application to allocate temporary data to the [managed
heap](performance-managed-memory-introduction.html) in each frame but
temporary allocations can affect the performance of the application.

For example, if a program allocates 1 KB of temporary memory each frame, and
it runs at 60 **frames per second** The frequency at which consecutive frames
are displayed in a running game. [More info](RenderingStatistics.html)  
See in [Glossary](Glossary.html#framespersecond), then it must allocate 60 KB
of temporary memory per second. Over the course of a minute, this adds up to
3.6 MB of memory available to the garbage collector.

Invoking the garbage collector once per second has a negative effect on
performance. If it has to clean up 3.6 MB spread across thousands of
individual allocations, that might result in significant garbage collection
times.

Loading operations have an impact on performance. If your application
generates a lot of temporary objects during a heavy asset-loading operation,
and Unity references those objects until the operation completes, then the
garbage collector can’t release those temporary objects. This means that the
managed heap needs to expand, even though Unity releases a lot of the objects
that it contains a short time later.

To avoid managed heap expansion, reduce the amount of frequent managed heap
allocations as possible: ideally to 0 bytes per frame, or as close to zero as
you can get. For information on how to optimize for managed heap allocations,
refer to [Optimizing your code for managed memory](performance-optimizing-
code-managed-memory.html).

## Additional resources

  * [Garbage collection modes](performance-incremental-garbage-collection.html)
  * [Configuring garbage collection](performance-disabling-garbage-collection.html)
  * [Optimizing your code for managed memory](performance-optimizing-code-managed-memory.html)

[](performance-managed-memory-introduction.html)

Managed memory introduction

[](performance-incremental-garbage-collection.html)

Garbage collection modes

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

