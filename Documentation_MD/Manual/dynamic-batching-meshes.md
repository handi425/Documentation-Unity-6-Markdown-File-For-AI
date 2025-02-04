[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dynamic-batching-meshes.html)
  * [中文](/cn/current/Manual/dynamic-batching-meshes.html)
  * [日本語](/ja/current/Manual/dynamic-batching-meshes.html)
  * [한국어](/kr/current/Manual/dynamic-batching-meshes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dynamic-batching-meshes.html)
  * [中文](/cn/current/Manual/dynamic-batching-meshes.html)
  * [日本語](/ja/current/Manual/dynamic-batching-meshes.html)
  * [한국어](/kr/current/Manual/dynamic-batching-meshes.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * [Batching moving GameObjects](dynamic-batching-landing.html)
  * How Unity batches moving GameObjects

[](dynamic-batching.html)

Introduction to dynamic batching

[](dynamic-batching-enable.html)

Enable dynamic batching

# How Unity batches moving GameObjects

Dynamic batching for meshes works by transforming all vertices into world
space on the CPU, rather than on the GPU. This means **dynamic batching** An
automatic Unity process which attempts to render multiple meshes as if they
were a single mesh for optimized graphics performance. The technique
transforms all of the GameObject vertices on the CPU and groups many similar
vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) is only an optimization if
the transformation work is less resource intensive than doing a draw call.

The resource requirements of a draw call depend on many factors, primarily the
graphics API. For example, on consoles or modern APIs like Apple Metal, the
draw call overhead is generally much lower, and often dynamic batching doesn’t
produce a gain in performance. To determine whether it’s beneficial to use
dynamic batching in your application, [profile](Profiler.html) your
application with and without dynamic batching.

Unity can use dynamic batching for shadows casters, even if their materials
are different, as long as the material values Unity needs for the shadow pass
are the same. For example, multiple crates can use materials that have
different textures. Although the material assets are different, the difference
is irrelevant for the shadow caster pass and Unity can batch shadows for the
crate **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the shadow render step.

## Dynamic batching for dynamically generated geometries

The following renderers dynamically generate geometries, such as particles and
lines, that you can optimize using dynamic batching:

  * [Built-in Particle Systems](PartSysUsage.html)
  * [Line Renderers](class-LineRenderer.html)A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer)

  * [Trail Renderers](class-TrailRenderer.html)A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer)

Dynamic batching for dynamically generated geometries works differently than
it does for meshes:

  1. For each renderer, Unity builds all dynamically batchable content into one large vertex buffer.
  2. The renderer sets up the material state for the batch.
  3. Unity then binds the vertex buffer to the GPU.
  4. For each Renderer in the batch, Unity updates the offset in the vertex buffer and submits a new draw call.

This approach is similar to how Unity submits draw calls for [static
batching](static-batching.html)A technique Unity uses to draw GameObjects on
the screen that combines static (non-moving) GameObjects into big Meshes, and
renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching).

[](dynamic-batching.html)

Introduction to dynamic batching

[](dynamic-batching-enable.html)

Enable dynamic batching

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

