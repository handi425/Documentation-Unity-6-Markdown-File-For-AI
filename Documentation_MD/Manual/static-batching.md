[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/static-batching.html)
  * [中文](/cn/current/Manual/static-batching.html)
  * [日本語](/ja/current/Manual/static-batching.html)
  * [한국어](/kr/current/Manual/static-batching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/static-batching.html)
  * [中文](/cn/current/Manual/static-batching.html)
  * [日本語](/ja/current/Manual/static-batching.html)
  * [한국어](/kr/current/Manual/static-batching.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [Batching draw calls](DrawCallBatching-landing.html)
  * [Batching static GameObjects](static-batching-landing.html)
  * Introduction to static batching

[](static-batching-landing.html)

Batching static GameObjects

[](static-batching-enable.html)

Enable static batching

# Introduction to static batching

Static batching is a [draw call batching](DrawCallBatching.html) method that
combines meshes that don’t move to reduce [draw calls](optimizing-draw-
calls.html). It transforms the combined meshes into world space and builds one
shared vertex and index buffer for them. Then Unity performs a single draw
call that uses this combined **mesh** The main graphics primitive of Unity.
Meshes make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) to draw all objects in the batch at
once. **Static batching** A technique Unity uses to draw GameObjects on the
screen that combines static (non-moving) GameObjects into big Meshes, and
renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching) can significantly reduce the
number of draw calls.

Static batching is more efficient than [dynamic batching](dynamic-
batching.html)An automatic Unity process which attempts to render multiple
meshes as if they were a single mesh for optimized graphics performance. The
technique transforms all of the GameObject vertices on the CPU and groups many
similar vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) because static batching
doesn’t transform vertices on the CPU. For more information about the
performance implications for static batching, see Performance implications.

## Requirements and compatibility

This section includes information about the **render pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) compatibility of static
batching.

### Render pipeline compatibility

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
  
## Performance implications

Using static batching requires additional CPU memory to store the combined
geometry. If multiple GameObjects use the same mesh, Unity creates a copy of
the mesh for each **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), and inserts each copy into the
combined mesh. This means that the same geometry appears in the combined mesh
multiple times. Unity does this regardless of whether you use the
[editor](static-batching-enable.html#editor) or [runtime API](static-batching-
enable.html#runtime) to prepare the GameObjects for static batching. If you
want to keep a smaller memory footprint, you might have to sacrifice rendering
performance and avoid static batching for some GameObjects. For example,
marking trees as static in a dense forest environment can have a serious
memory impact.

**Note** : There are limits to the number of vertices a static batch can
include. Each static batch can include up to 64000 vertices. If there are
more, Unity creates another batch.

[](static-batching-landing.html)

Batching static GameObjects

[](static-batching-enable.html)

Enable static batching

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

