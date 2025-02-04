[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-managed-memory-introduction.html)
  * [中文](/cn/current/Manual/performance-managed-memory-introduction.html)
  * [日本語](/ja/current/Manual/performance-managed-memory-introduction.html)
  * [한국어](/kr/current/Manual/performance-managed-memory-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-managed-memory-introduction.html)
  * [中文](/cn/current/Manual/performance-managed-memory-introduction.html)
  * [日本語](/ja/current/Manual/performance-managed-memory-introduction.html)
  * [한국어](/kr/current/Manual/performance-managed-memory-introduction.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Managed memory](performance-managed-memory.html)
  * Managed memory introduction

[](performance-managed-memory.html)

Managed memory

[](performance-garbage-collector.html)

Garbage collector overview

# Managed memory introduction

Unity’s managed memory system is part of the C# scripting environment provided
by either the [Mono or IL2CPP Virtual Machines (VM)](scripting-backends.html).
The benefit of the managed memory system is that it manages the release of
memory, so you don’t need to manually request the release of memory through
your code. These VM offer a controlled memory environment consisting of the
following parts:

  * **The managed heap** : A section of memory that the VM automatically controls with a [garbage collector](performance-garbage-collector.html). The memory allocated on the managed heap is referred to as **GC Allocation** , and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) records any occurrence of such an
allocation as a **GC.Alloc** sample.

  * **The scripting stack** : This is a fixed-size memory region allocated at the start of each thread. It tracks temporary data like variables and execution flow as your application moves in and out of code blocks.
  * **Native VM memory** : Contains memory related to the execution and management of Unity’s scripting VM. You don’t have direct access to it and the normal execution of your code influences it indirectly. It’s useful to know that it includes memory related to the executable code that your code generates, in particular memory used for [generics](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/types/generics), type meta data used for [reflection](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/reflection), and the memory required to run the VM.

## Automatic memory management

Unity’s managed memory system uses a [garbage collector](performance-garbage-
collector.html) and a managed heap to automatically free memory allocations
when your **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) no longer hold any references to
those allocations. This helps protect against memory leaks, which happen when
allocated memory is never freed because the reference required to free it
manually has been lost.

Unity’s memory management system guards memory access, which means that you
can’t access memory that has been freed, or that was never valid for your code
to access. However, this memory management process impacts runtime
performance, because allocating managed memory is time-consuming for the CPU.
Garbage collection might also stop the CPU from doing other work until it
completes.

In the following diagram, the blue box represents a quantity of memory that
Unity allocates to the managed heap. The white boxes within it represent data
values that Unity stores within the managed heap’s memory space. When
additional data values are needed, Unity allocates them the free space from
the managed heap (annotated A).

![A quantity of memory. Marked A on the diagram is some free
memory.](../uploads/Main/managed-heap.jpg) A quantity of memory. Marked A on
the diagram is some free memory.

### Types allocated to the heap

When a method is called, the scripting back end copies the values of its
parameters to an area of memory reserved for that specific call, in a data
structure called a call stack. The scripting back end can quickly copy data
types that occupy a few bytes. However, it’s common for objects, strings, and
arrays to be much larger, and it’s inefficient for the scripting back end to
copy these types of data on a regular basis.

All non-null [reference-type objects](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/builtin-types/reference-types) and all
[boxed value-typed objects](https://docs.microsoft.com/en-
us/dotnet/csharp/programming-guide/types/boxing-and-unboxing) in managed code
must be allocated on the managed heap.

It’s important that you’re familiar with value and reference types, so that
you can effectively manage your code. For more information, refer to
Microsoft’s documentation on [value types](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/builtin-types/value-types), and [reference
types](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/keywords/reference-types).

### Memory fragmentation and heap expansion

When Unity releases an object, the memory that the object occupied is freed
up. However, the free space doesn’t become part of a single large pool of free
memory.

The objects on either side of the released object might still be in use.
Because of this, the freed space is a gap between other segments of memory.
Unity can only use this gap to store data of identical or lesser size than the
released object. This situation is called memory fragmentation, and the
following diagram shows an example of this:

![A quantity of memory, with some objects released represented by grey dashed
lines.](../uploads/Main/managed-heap-removed-objects.jpg) A quantity of
memory, with some objects released represented by grey dashed lines.

Memory fragmentation happens when there’s a large amount of memory available
in the heap, but it’s only available in the memory gaps between objects. Even
though there’s enough total space for a large memory allocation, the managed
heap can’t find a large enough single block of contiguous memory to assign to
the allocation.

If a large object is allocated and there’s insufficient contiguous free space
to accommodate it, the Unity memory manager performs two operations:

  1. The garbage collector runs, if it hasn’t already done so. This attempts to free up enough space to fulfill the allocation request.
  2. If, after the garbage collector runs, there’s still not enough contiguous space to fit the requested amount of memory, the heap must expand. The specific amount that the heap expands is platform-dependent. On most platforms, when the heap expands, it expands by double the amount of the previous expansion. If the requested allocation size is bigger than that, Unity performs an out-of-cycle expansion to fit that allocation and continue from the previous regular expansion size as a basis for the next expansion.

Unity doesn’t release the memory allocated to the managed heap when it expands
regularly. Instead, it retains the expanded heap, even if a large section of
the heap is empty. This prevents the need to re-expand the heap if further
large allocations occur.

On most platforms, Unity eventually releases the memory that the empty
portions of the managed heap uses back to the operating system. The interval
at which this happens isn’t guaranteed and is unreliable. This requires these
portions to consist of one or more full memory pages (4 KB on most platforms).

## Managed heap and native memory

The garbage collector doesn’t clear out [native memory objects](performance-
native-allocators.html) or other native allocations. Unity only clears native
memory in the following situations:

  * When [`Resources.UnloadUnusedAssets`](../ScriptReference/Resources.UnloadUnusedAssets.html) is called. You can manually call `UnloadUnusedAssets`, or Unity calls it automatically when unloading a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) due to a loading a new scene in
[`LoadSceneMode.Single`](../ScriptReference/SceneManagement.LoadSceneMode.Single.html).
For asynchronous scene unloads you can request assets that were dynamically
created and embedded in the scene at build-time with the parameters of
[`SceneManager.UnloadSceneAsync`](../ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html)
and the option
[`UnloadSceneOptions.UnloadAllEmbeddedSceneObjects`](../ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html).
Calling `SceneManager.UnloadSceneAsync` with
`UnloadSceneOptions.UnloadAllEmbeddedSceneObjects` doesn’t unload regular
assets that Unity loaded to use in the scene, or dynamically and run-time
created assets.

  * When `Destroy` is called on an object.

`Resources.UnloadUnusedAssets` unloads all native objects that no longer have
any references pointing to them. If you want to free the memory earlier, for
example if you have full screen `RenderTexture` instances on platforms with
low RAM, call `Destroy` on the objects.

If you want to have more control over the assets that stay in memory, use
[AssetBundles](AssetBundlesIntro.html) and Addressables.

**Important:** Calling `UnloadUnusedAssets` or `GC.Collect` is a CPU-intensive
process. In large projects it might take several seconds to complete

Before calling `UnloadUnusedAssets`, make sure you’re not holding managed
references to the native objects you want to be cleaned up, or the native
objects won’t be unloaded. Static fields and events are common ways to hold on
to these objects without meaning to. For more information on how to analyze
these issues with the Memory Profiler, refer to [Managed shell
objects](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@1.1/manual/managed-
shell-objects.html) in the Memory Profiler package documentation.

## Additional resources

  * [Garbage collector introduction](performance-garbage-collector.html)
  * [`Resources.UnloadUnusedAssets` API reference](../ScriptReference/Resources.UnloadUnusedAssets.html)
  * [Optimizing your code for managed memory](performance-optimizing-code-managed-memory.html)

[](performance-managed-memory.html)

Managed memory

[](performance-garbage-collector.html)

Garbage collector overview

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

