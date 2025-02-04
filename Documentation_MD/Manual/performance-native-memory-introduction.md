[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/performance-native-memory-introduction.html)
  * [中文](/cn/current/Manual/performance-native-memory-introduction.html)
  * [日本語](/ja/current/Manual/performance-native-memory-introduction.html)
  * [한국어](/kr/current/Manual/performance-native-memory-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/performance-native-memory-introduction.html)
  * [中文](/cn/current/Manual/performance-native-memory-introduction.html)
  * [日本語](/ja/current/Manual/performance-native-memory-introduction.html)
  * [한국어](/kr/current/Manual/performance-native-memory-introduction.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Native memory](performance-native-memory.html)
  * Native memory introduction

[](performance-native-memory.html)

Native memory

[](performance-native-allocators.html)

Native memory allocators

# Native memory introduction

The Unity engine’s internal C/C++ core has its own memory management system,
called native memory. In most situations, you can’t directly access or modify
this memory type.

Native memory isn’t automatically managed or subject to [garbage
collection](performance-garbage-collector.html). This means it’s difficult to
profile and handle in a way that doesn’t cause memory leaks.

Unity uses different memory allocator types, which all use different
algorithms to organize memory. Unity’s memory manager uses these allocator
types in different areas to organize the memory in your application
effectively.

To get greater control over how Unity allocates native memory, you can adjust
the size of each allocation for each area. You can adjust the size of
allocations either through the [Player settings](class-
PlayerSettings.html)Settings that let you set various player-specific options
for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) window in the Unity Editor, or
through the command line. For more information, refer to [Customizing
allocators](memory-allocator-customization.html).

## Additional resources

  * [Memory in Unity introduction](performance-memory-overview.html)
  * [Native allocators introduction](performance-native-allocators.html)
  * [Customizing allocators](memory-allocator-customization.html)

[](performance-native-memory.html)

Native memory

[](performance-native-allocators.html)

Native memory allocators

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

