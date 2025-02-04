[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-tls-stack-allocator.html)
  * [中文](/cn/current/Manual/performance-tls-stack-allocator.html)
  * [日本語](/ja/current/Manual/performance-tls-stack-allocator.html)
  * [한국어](/kr/current/Manual/performance-tls-stack-allocator.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-tls-stack-allocator.html)
  * [中文](/cn/current/Manual/performance-tls-stack-allocator.html)
  * [日本語](/ja/current/Manual/performance-tls-stack-allocator.html)
  * [한국어](/kr/current/Manual/performance-tls-stack-allocator.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Native memory](performance-native-memory.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)
  * Thread Local Storage stack allocator example

[](performance-bucket-allocator.html)

Bucket allocator example

[](performance-threadsafe-linear-allocator.html)

Thread-safe linear allocator example

# Thread Local Storage stack allocator example

## Prerequisites

The examples use the memory usage reports that Unity writes to the log when
you close the Player or Unity Editor. To create these reports, use the `-log-
memory-performance-stats` command line argument. To find your project’s log
files, follow the instructions on [the log files page](log-files.html).

## TLS stack allocator usage reports

If a thread’s stack allocator is full, allocations fall back to the
[threadsafe linear allocator](performance-threadsafe-linear-allocator.html). A
few overflow allocations are fine: 1 to 10 in a frame, or a few hundred during
load. However, if the numbers grow every frame, you can increase the block
sizes.

![Main Thread Block Size custom value in the Fast Per Thread Temporary
Allocators](../uploads/Main/Per_Thread.png) Main Thread Block Size custom
value in the Fast Per Thread Temporary Allocators

To increase the block size, set the value in the Editor, or use the command
line arguments. For more information, refer to [Customizing native memory
allocators](memory-allocator-customization.html).

The information in the usage report can help you select a block size that’s
appropriate for your application. For example, in the following main thread
usage report, the load peaks at 2.7 MB, but the remaining frames are under 64
KB. You can reduce the block size from 4 MB to 64 KB and allow the loading
frame to spill over the allocations:

    
    
    [ALLOC_TEMP_TLS] TLS Allocator
      StackAllocators :
        [ALLOC_TEMP_MAIN]
          Peak usage frame count: [16.0 KB-32.0 KB]: 802 frames, [32.0 KB-64.0 KB]: 424 frames, [2.0 MB-4.0 MB]: 1 frames
          Initial Block Size 4.0 MB
          Current Block Size 4.0 MB
          Peak Allocated Bytes 2.7 MB
          Overflow Count 0
        [ALLOC_TEMP_Job.Worker 18]
    

In the following example, the worker thread isn’t used for large temporary
allocations. To save memory, you can reduce the worker’s block size to 32 KB.
This is useful on a multi-core machine, where each worker thread has its own
stack:

    
    
    [ALLOC_TEMP_Job.Worker 14]
          Initial Block Size 256.0 KB
          Current Block Size 256.0 KB
          Peak Allocated Bytes 18.6 KB
          Overflow Count 0
    

## Additional resources

  * [Native memory allocators](performance-native-allocators.html)
  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)

[](performance-bucket-allocator.html)

Bucket allocator example

[](performance-threadsafe-linear-allocator.html)

Thread-safe linear allocator example

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

