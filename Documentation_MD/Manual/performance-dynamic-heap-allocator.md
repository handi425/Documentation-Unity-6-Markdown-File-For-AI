[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-dynamic-heap-allocator.html)
  * [中文](/cn/current/Manual/performance-dynamic-heap-allocator.html)
  * [日本語](/ja/current/Manual/performance-dynamic-heap-allocator.html)
  * [한국어](/kr/current/Manual/performance-dynamic-heap-allocator.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-dynamic-heap-allocator.html)
  * [中文](/cn/current/Manual/performance-dynamic-heap-allocator.html)
  * [日本語](/ja/current/Manual/performance-dynamic-heap-allocator.html)
  * [한국어](/kr/current/Manual/performance-dynamic-heap-allocator.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Native memory](performance-native-memory.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)
  * Dynamic heap allocator example

[](performance-dual-thread-allocator.html)

Dual thread allocator example

[](performance-bucket-allocator.html)

Bucket allocator example

# Dynamic heap allocator example

## Prerequisites

The examples use the memory usage reports that Unity writes to the log when
you close the Player or Unity Editor. To create these reports, use the `-log-
memory-performance-stats` command line argument. To find your project’s log
files, follow the instructions on [the log files page](log-files.html).

## Example usage report

An example usage report for the dynamic heap allocator is as follows:

    
    
    [ALLOC_DEFAULT_MAIN]
    Peak usage frame count: [16.0 MB-32.0 MB]: 497 frames, [32.0 MB-64.0 MB]: 1 frames
    Requested Block Size 16.0 MB
    Peak Block count 2
    Peak Allocated memory 54.2 MB
    Peak Large allocation bytes 40.2 MB
    

In this example, the [Two Level Segregated Fit (TLSF) block size](performance-
native-allocators.html#dynamic-heap) is 16 MB, and Unity has allocated two
blocks. The peak usage of the allocator was 54.2 MB. Of those 52.4 MB, 40.2 MB
weren’t allocated in the TLSF block, and instead fell back to virtual memory.
Most frames had 16 to 32 MB of allocated memory, while one frame, which was
likely the loading frame, peaked at 32 to 64 MB of memory.

If you increased the block size the large allocation stays in the dynamic heap
rather than fall back into virtual memory. However, that block size might lead
to memory waste, because the blocks might not be fully used.

The type tree and file cache allocators use dynamic heap allocation. To save
the memory blocks they might otherwise use under this algorithm, you can set
the type tree block size and file cache block size to 0. Allocations that
would have used typetree and cache fall back to the main allocator instead.

However, reducing the block size to 0 has a risk of increased native memory
fragmentation. Refer to [Customize allocators](memory-allocator-
customization.html) for how to set these block sizes.

## Additional resources

  * [Native memory allocators](performance-native-allocators.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)

[](performance-dual-thread-allocator.html)

Dual thread allocator example

[](performance-bucket-allocator.html)

Bucket allocator example

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

