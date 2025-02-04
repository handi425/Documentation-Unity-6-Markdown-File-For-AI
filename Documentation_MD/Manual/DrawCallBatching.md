[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DrawCallBatching.html)
  * [中文](/cn/current/Manual/DrawCallBatching.html)
  * [日本語](/ja/current/Manual/DrawCallBatching.html)
  * [한국어](/kr/current/Manual/DrawCallBatching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DrawCallBatching.html)
  * [中文](/cn/current/Manual/DrawCallBatching.html)
  * [日本語](/ja/current/Manual/DrawCallBatching.html)
  * [한국어](/kr/current/Manual/DrawCallBatching.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * Introduction to batching draw calls

[](DrawCallBatching-landing.html)

Batching draw calls

[](DrawCallBatching-Enable.html)

Enable draw call batching

# Introduction to batching draw calls

Draw call batching is a [draw call optimization](optimizing-draw-calls.html)
method that combines meshes so that Unity can render them in fewer draw calls.
Unity provides two built-in draw call batching methods:

  * [Static batching](static-batching.html): For [static](StaticObjects.html) **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Unity combines them and renders
them together.

  * [Dynamic batching](dynamic-batching.html): For small enough meshes, this transforms their vertices on the CPU, groups similar vertices together, and renders them in one draw call.

Unity’s built-in draw call batching has several advantages over manually
merging meshes; most notably, Unity can still cull meshes individually.
However, it also has some downsides; static batching incurs memory and storage
overhead, and dynamic batching incurs some CPU overhead.

## Render pipeline compatibility

**Feature** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
**Dynamic Batching** | Yes | No | Yes | Yes   
  
## Limitations

Transparent **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) often require Unity to render meshes
in back-to-front order. To batch transparent meshes, Unity first orders them
from back to front and then tries to batch them. Since Unity must render the
meshes back-to-front, it often can’t batch as many transparent meshes as
opaque meshes.

Unity can’t apply dynamic batching to GameObjects that contain mirroring in
their **Transform component** A Transform component determines the Position,
Rotation, and Scale of each object in the scene. Every GameObject has a
Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent). For example, if one
GameObject has a scale of **1** and another GameObject has a scale of **–1** ,
Unity can’t batch them together.

If you are not able to use draw call batching, manually combining meshes that
are close to each other can be a good alternative. For more information on
combining meshes, see [Combining meshes](combining-meshes.html).

**Warning** : When you access shared material properties from a C# script,
make sure to use [Renderer.sharedMaterial](../ScriptReference/Renderer-
sharedMaterial.html) and not [Renderer.material](../ScriptReference/Renderer-
material.html). `Renderer.material` creates a copy of the material and assigns
the copy back to the Renderer. This stops Unity from batching the draw calls
for that Renderer.

[](DrawCallBatching-landing.html)

Batching draw calls

[](DrawCallBatching-Enable.html)

Enable draw call batching

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

