[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DrawCallBatching-landing.html)
  * [中文](/cn/current/Manual/DrawCallBatching-landing.html)
  * [日本語](/ja/current/Manual/DrawCallBatching-landing.html)
  * [한국어](/kr/current/Manual/DrawCallBatching-landing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DrawCallBatching-landing.html)
  * [中文](/cn/current/Manual/DrawCallBatching-landing.html)
  * [日本語](/ja/current/Manual/DrawCallBatching-landing.html)
  * [한국어](/kr/current/Manual/DrawCallBatching-landing.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * Batching draw calls

[](gpu-instancing-troubleshoot.html)

Troubleshooting GPU instancing

[](DrawCallBatching.html)

Introduction to batching draw calls

# Batching draw calls

Resources and approaches for improving performance by combining static
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or moving GameObjects into fewer
draw calls.

**Page** | **Description**  
---|---  
[Introduction to batching draw calls](DrawCallBatching.html) | Understand how Unity creates batches of static and dynamic GameObjects to reduce draw calls.  
[Enable draw call batching](DrawCallBatching-Enable.html) | Make sure GameObjects are compatible with **static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching) and **dynamic batching** An
automatic Unity process which attempts to render multiple meshes as if they
were a single mesh for optimized graphics performance. The technique
transforms all of the GameObject vertices on the CPU and groups many similar
vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching).  
[Batching static GameObjects](static-batching-landing.html) | Resources for combining static GameObjects into fewer draw calls.  
[Batching moving GameObjects](dynamic-batching-landing.html) | Resources for combining moving GameObjects into fewer draw calls.  
  
[](gpu-instancing-troubleshoot.html)

Troubleshooting GPU instancing

[](DrawCallBatching.html)

Introduction to batching draw calls

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

