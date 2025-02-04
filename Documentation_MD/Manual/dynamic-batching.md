[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dynamic-batching.html)
  * [中文](/cn/current/Manual/dynamic-batching.html)
  * [日本語](/ja/current/Manual/dynamic-batching.html)
  * [한국어](/kr/current/Manual/dynamic-batching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dynamic-batching.html)
  * [中文](/cn/current/Manual/dynamic-batching.html)
  * [日本語](/ja/current/Manual/dynamic-batching.html)
  * [한국어](/kr/current/Manual/dynamic-batching.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * [Batching moving GameObjects](dynamic-batching-landing.html)
  * Introduction to dynamic batching

[](dynamic-batching-landing.html)

Batching moving GameObjects

[](dynamic-batching-meshes.html)

How Unity batches moving GameObjects

# Introduction to dynamic batching

Dynamic batching is a [draw call batching](DrawCallBatching.html) method that
batches moving **GameObjects** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to reduce [draw calls](optimizing-
draw-calls.html). **Dynamic batching** An automatic Unity process which
attempts to render multiple meshes as if they were a single mesh for optimized
graphics performance. The technique transforms all of the GameObject vertices
on the CPU and groups many similar vertices together. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) works differently between
meshes and geometries that Unity generates dynamically at runtime, such as
[particle systems](ParticleSystems.html)A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem). For information about the
internal differences between meshes and dynamic geometries, see [Dynamic
batching for meshes](dynamic-batching-meshes.html) and [Dynamic batching for
dynamically generated geometries](dynamic-batching-meshes.html#dynamic-
batching-dynamic-geometry).

**Note** : Dynamic batching for meshes was designed to optimize performance on
old low-end devices. On modern consumer hardware, the work dynamic batching
does on the CPU can be greater than the overhead of a draw call. This
negatively affects performance. For more information, see [Dynamic batching
for meshes](dynamic-batching-meshes.html).

## Requirements and compatibility

This section includes information about the **render pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) compatibility of dynamic
batching.

### Render pipeline compatibility

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Dynamic Batching** | Yes | No | Yes | Yes  
  
### Limitations

In the following scenarios, Unity either can’t use dynamic batching at all or
can only apply dynamic batching to a limited extent:

  * Unity can’t apply dynamic batching to meshes that contain more than 900 vertex attributes and 300 vertices. This is because dynamic batching for meshes has an overhead per vertex. For example, if your **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) uses vertex position, vertex normal,
and a single UV, then Unity can batch up to 300 vertices. However, if your
shader uses vertex position, vertex normal, UV0, UV1, and vertex tangent, then
Unity can only batch 180 vertices.

  * If GameObjects use different material instances, Unity can’t batch them together, even if they are essentially the same. The only exception to this is shadow caster rendering.
  * GameObjects with lightmaps have additional renderer parameters. This means that, if you want to batch lightmapped GameObjects, they must point to the same **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) location.

  * Unity can’t fully apply dynamic batching to GameObjects that use multi-pass shaders. 
    * Almost all Unity shaders support several lights in **forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering). To achieve this, they
process an additional render pass for each light. Unity only batches the first
render pass. It can’t batch the draw calls for the additional per-pixel
lights.

[](dynamic-batching-landing.html)

Batching moving GameObjects

[](dynamic-batching-meshes.html)

How Unity batches moving GameObjects

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

