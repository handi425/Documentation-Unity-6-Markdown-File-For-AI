[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-optimizing-code-managed-memory.html)
  * [中文](/cn/current/Manual/performance-optimizing-code-managed-memory.html)
  * [日本語](/ja/current/Manual/performance-optimizing-code-managed-memory.html)
  * [한국어](/kr/current/Manual/performance-optimizing-code-managed-memory.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-optimizing-code-managed-memory.html)
  * [中文](/cn/current/Manual/performance-optimizing-code-managed-memory.html)
  * [日本語](/ja/current/Manual/performance-optimizing-code-managed-memory.html)
  * [한국어](/kr/current/Manual/performance-optimizing-code-managed-memory.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Managed memory](performance-managed-memory.html)
  * Optimizing your code for managed memory

[](performance-track-garbage-collection.html)

Tracking garbage collection allocations

[](performance-reference-types.html)

Reference type management

# Optimizing your code for managed memory

C#’s automatic memory management reduces the risk of memory leaks and other
programming errors, in comparison to other programming languages like C++,
where you must manually track and free all the memory you allocate.

Automatic memory management allows you to write code quickly and with few
errors. However, this convenience might have performance implications. To
optimize your code for performance, you must avoid situations where your
application triggers the [garbage collector](performance-garbage-
collector.html) a lot. This section outlines some common issues and workflows
that affect when your application triggers the garbage collector.

**Topic** | **Description**  
---|---  
**[Reference type management](performance-reference-types.html)** | Optimize how you use reference types in your code.  
**[Creating reusable code](performance-reusable-code.html)** | Reuse code to optimize the performance of your application.  
**[Optimizing arrays](performance-optimizing-arrays.html)** | Optimize when and how you use arrays in your code.  
  
## Additional resources

  * [Managed memory introduction](performance-managed-memory-introduction.html)
  * [Garbage collector introduction](performance-garbage-collector.html)

[](performance-track-garbage-collection.html)

Tracking garbage collection allocations

[](performance-reference-types.html)

Reference type management

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

