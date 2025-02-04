[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dynamic-batching-enable.html)
  * [中文](/cn/current/Manual/dynamic-batching-enable.html)
  * [日本語](/ja/current/Manual/dynamic-batching-enable.html)
  * [한국어](/kr/current/Manual/dynamic-batching-enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dynamic-batching-enable.html)
  * [中文](/cn/current/Manual/dynamic-batching-enable.html)
  * [日本語](/ja/current/Manual/dynamic-batching-enable.html)
  * [한국어](/kr/current/Manual/dynamic-batching-enable.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * [Batching moving GameObjects](dynamic-batching-landing.html)
  * Enable dynamic batching

[](dynamic-batching-meshes.html)

How Unity batches moving GameObjects

[](combining-meshes.html)

Combine meshes manually

# Enable dynamic batching

Unity always uses **dynamic batching** An automatic Unity process which
attempts to render multiple meshes as if they were a single mesh for optimized
graphics performance. The technique transforms all of the GameObject vertices
on the CPU and groups many similar vertices together. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) for dynamic geometry such as
Particle Systems

To use dynamic batching for meshes:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Dynamic Batching**.

If your project uses URP, the [Scriptable Render Pipeline (SRP)
batcher](SRPBatcher.html) is enabled by default. To enable dynamic batching
instead, go to the [URP
Asset](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@17.0/manual/universalrp-asset.html#rendering) and enable
**Dynamic Batching**.

Unity automatically batches moving meshes into the same draw call if they
fulfill the criteria described in the [common usage
information](DrawCallBatching-Enable.html).

[](dynamic-batching-meshes.html)

How Unity batches moving GameObjects

[](combining-meshes.html)

Combine meshes manually

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

