[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/DrawCallBatching-Enable.html)
  * [中文](/cn/current/Manual/DrawCallBatching-Enable.html)
  * [日本語](/ja/current/Manual/DrawCallBatching-Enable.html)
  * [한국어](/kr/current/Manual/DrawCallBatching-Enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/DrawCallBatching-Enable.html)
  * [中文](/cn/current/Manual/DrawCallBatching-Enable.html)
  * [日本語](/ja/current/Manual/DrawCallBatching-Enable.html)
  * [한국어](/kr/current/Manual/DrawCallBatching-Enable.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * Enable draw call batching

[](DrawCallBatching.html)

Introduction to batching draw calls

[](static-batching-landing.html)

Batching static GameObjects

# Enable draw call batching

[Mesh Renderers](class-MeshRenderer.html)A mesh component that takes the
geometry from the Mesh Filter and renders it at the position defined by the
object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer), [Trail Renderers](class-
TrailRenderer.html)A visual effect that lets you to make trails behind
GameObjects in the Scene as they move. [More info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer), [Line Renderers](class-
LineRenderer.html)A component that takes an array of two or more points in 3D
space and draws a straight line between each one. You can use a single Line
Renderer component to draw anything from a simple straight line to a complex
spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer), [Particle Systems](class-
ParticleSystem.html)A component that simulates fluid entities such as liquids,
clouds and flames by generating and animating large numbers of small 2D images
in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem), and [Sprite
Renderers](sprite/renderer/renderer-landing.html)A component that lets you
display images as Sprites for use in both 2D and 3D scenes. [More
info](sprite/renderer/renderer-landing.html)  
See in [Glossary](Glossary.html#SpriteRenderer) are supported for draw call
batching. Other types of rendering components, including Skinned **Mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderers Cloth, are not supported.
Unity only batches Renderers with other Renderers of the same type; for
example, Mesh Renderers with Mesh Renderers.

Unity batches draw calls of **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that use the same material. This
means to get the best results from draw call batching, share materials among
as many GameObjects as possible. If you have two material assets that are
identical apart from their textures, you can combine the textures into a
single, larger texture. This process is called texture atlasing. For more
information, see the [Wikipedia
article](http://en.wikipedia.org/wiki/Texture_atlas) on texture atlasing. When
textures are in the same atlas, you can use a single material asset instead.

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), you can use a
[MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html) to
change material properties without breaking draw call batching. The CPU still
needs to make some render-state changes, but using a `MaterialPropertyBlock`
is faster than using multiple materials. If your project uses a Scriptable
Render Pipeline, don’t use a `MaterialPropertyBlock` because they remove SRP
Batcher compatibility for the material.

[](DrawCallBatching.html)

Introduction to batching draw calls

[](static-batching-landing.html)

Batching static GameObjects

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

