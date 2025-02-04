[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-managed-memory.html)
  * [中文](/cn/current/Manual/performance-managed-memory.html)
  * [日本語](/ja/current/Manual/performance-managed-memory.html)
  * [한국어](/kr/current/Manual/performance-managed-memory.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-managed-memory.html)
  * [中文](/cn/current/Manual/performance-managed-memory.html)
  * [日本語](/ja/current/Manual/performance-managed-memory.html)
  * [한국어](/kr/current/Manual/performance-managed-memory.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * Managed memory

[](performance-memory-overview.html)

Memory in Unity introduction

[](performance-managed-memory-introduction.html)

Managed memory introduction

# Managed memory

Unity’s managed memory system is a C# scripting environment based on the Mono
or **IL2CPP** A Unity-developed scripting back-end which you can use as an
alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) Virtual Machines (VMs). The benefit of
the managed memory system is that it manages the release of memory, so you
don’t need to manually request the release of memory through your code. It
makes use of a garbage collector to automatically free memory allocations.

**Topic** | **Description**  
---|---  
**[Managed memory introduction](performance-managed-memory-introduction.html)** | Automatically manage the release and allocation of memory in your application.  
**[Garbage collector introduction](performance-garbage-collector.html)** | Reclaim unused memory in your application.  
**[Garbage collection modes](performance-incremental-garbage-collection.html)** | Overview of the different ways that the garbage collector runs.  
**[Configuring garbage collection](performance-disabling-garbage-collection.html)** | Set up the garbage collector in your project.  
**[Tracking garbage collection allocations](performance-track-garbage-collection.html)** | Monitor when your application performed garbage collection.  
**[Optimizing your code for managed memory](performance-optimizing-code-managed-memory.html)** | Approaches for optimizing your code to work with managed memory.  
  
## Additional resources

  * [Memory in Unity introduction](performance-memory-overview.html)
  * [Memory performance data](profiler-memory.html)

[](performance-memory-overview.html)

Memory in Unity introduction

[](performance-managed-memory-introduction.html)

Managed memory introduction

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

