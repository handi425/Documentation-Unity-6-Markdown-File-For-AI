[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-dual-thread-allocator.html)
  * [中文](/cn/current/Manual/performance-dual-thread-allocator.html)
  * [日本語](/ja/current/Manual/performance-dual-thread-allocator.html)
  * [한국어](/kr/current/Manual/performance-dual-thread-allocator.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-dual-thread-allocator.html)
  * [中文](/cn/current/Manual/performance-dual-thread-allocator.html)
  * [日本語](/ja/current/Manual/performance-dual-thread-allocator.html)
  * [한국어](/kr/current/Manual/performance-dual-thread-allocator.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Native memory](performance-native-memory.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)
  * Dual thread allocator example

[](performance-native-memory-allocator-examples.html)

Native memory allocator examples

[](performance-dynamic-heap-allocator.html)

Dynamic heap allocator example

# Dual thread allocator example

## Prerequisites

The examples use the memory usage reports that Unity writes to the log when
you close the Player or Unity Editor. To create these reports, use the `-log-
memory-performance-stats` command line argument. To find your project’s log
files, follow the instructions on [the log files page](log-files.html).

## Customize block size

You can customize the block sizes of the two dynamic heap allocators:

![Main Allocator, with a custom value for Shared Thread Block
Size](../uploads/Main/Main_Allocator.png) Main Allocator, with a custom value
for Shared Thread Block Size

## Usage report example

The usage report contains information for all three parts of the allocator.
For example:

    
    
    [ALLOC_DEFAULT] Dual Thread Allocator
      Peak main deferred allocation count 135
        [ALLOC_BUCKET]
          Large Block size 4.0 MB
          Used Block count 1
          Peak Allocated bytes 3.3 MB
        [ALLOC_DEFAULT_MAIN]
          Peak usage frame count: [16.0 MB-32.0 MB]: 8283 frames, [32.0 MB-64.0 MB]: 1 frames
          Requested Block Size 16.0 MB
          Peak Block count 2
          Peak Allocated memory 53.3 MB
          Peak Large allocation bytes 40.2 MB
        [ALLOC_DEFAULT_THREAD]
          Peak usage frame count: [64.0 MB-128.0 MB]: 8284 frames
          Requested Block Size 16.0 MB
          Peak Block count 2
          Peak Allocated memory 78.3 MB
          Peak Large allocation bytes 47.3 MB
    

**Note** : The **Peak main deferred allocation count** is the number of items
in a deletion queue. The main thread must delete any allocation it made. If
another thread deletes an allocation, Unity adds that allocation to a queue.
The allocation waits in the queue for the main thread to delete it. It’s then
counted as a deferred allocation.

## Additional resources

  * [Native memory allocators](performance-native-allocators.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)

[](performance-native-memory-allocator-examples.html)

Native memory allocator examples

[](performance-dynamic-heap-allocator.html)

Dynamic heap allocator example

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

