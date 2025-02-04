[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/reduce-draw-calls-landing.html)
  * [中文](/cn/current/Manual/reduce-draw-calls-landing.html)
  * [日本語](/ja/current/Manual/reduce-draw-calls-landing.html)
  * [한국어](/kr/current/Manual/reduce-draw-calls-landing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/reduce-draw-calls-landing.html)
  * [中文](/cn/current/Manual/reduce-draw-calls-landing.html)
  * [日本語](/ja/current/Manual/reduce-draw-calls-landing.html)
  * [한국어](/kr/current/Manual/reduce-draw-calls-landing.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * Optimizing draw calls

[](OptimizingGraphicsPerformance.html)

Reduce rendering work on the CPU or GPU

[](optimizing-draw-calls.html)

Introduction to optimizing draw calls

# Optimizing draw calls

There are several methods you can use in Unity to optimize and reduce draw
calls and render-state changes. Some methods are more suited for certain
**scenes** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) than others.

**Page** | **Description**  
---|---  
[Introduction to optimizing draw calls](optimizing-draw-calls.html) | Learn about why reducing draw calls improves rendering time, and how Unity prioritizes optimization methods.  
[GPU instancing](GPUInstancing-landing.html) | Resources and techniques for rendering multiple copies of the same **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) at the same time.  
[Batching draw calls](DrawCallBatching-landing.html) | Combine meshes to reduce draw calls, for either static or moving **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).  
[Combine meshes manually](combining-meshes.html) | Merge multiple meshes into a single mesh that Unity can render in a single draw call.  
  
## Additional resources

Refer to the following if your project uses the Universal **Render Pipeline**
A series of operations that take the contents of a Scene, and displays them on
a screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) or the High Definition
Render Pipeline (HDRP):

  * [Scriptable Render Pipeline (SRP) Batcher in URP](SRPBatcher-landing.html)
  * [BatchRendererGroup in URP](batch-renderer-group.html)
  * [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)

[](OptimizingGraphicsPerformance.html)

Reduce rendering work on the CPU or GPU

[](optimizing-draw-calls.html)

Introduction to optimizing draw calls

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

