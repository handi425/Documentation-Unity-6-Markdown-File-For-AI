[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RenderingPaths.html)
  * [中文](/cn/current/Manual/RenderingPaths.html)
  * [日本語](/ja/current/Manual/RenderingPaths.html)
  * [한국어](/kr/current/Manual/RenderingPaths.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RenderingPaths.html)
  * [中文](/cn/current/Manual/RenderingPaths.html)
  * [日本語](/ja/current/Manual/RenderingPaths.html)
  * [한국어](/kr/current/Manual/RenderingPaths.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Render pipelines](render-pipelines.html)
  * [Using the Built-In Render Pipeline](built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](built-in-rendering-paths.html)
  * Introduction to rendering paths in the Built-In Render Pipeline

[](built-in-rendering-paths.html)

Rendering paths in the Built-In Render Pipeline

[](RenderTech-ForwardRendering.html)

Forward rendering path in the Built-In Render Pipeline

# Introduction to rendering paths in the Built-In Render Pipeline

Unity’s Built-In **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) supports different rendering
paths. A **rendering path** is a series of operations related to lighting and
shading. Different rendering paths have different capabilities and performance
characteristics. Deciding on which rendering path is most suitable for your
Project depends on the type of Project, and on the target hardware.

You can choose the rendering path that your Project uses in the
[Graphics](class-GraphicsSettings.html) window, and you can override that path
for each [Camera](class-Camera.html)A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

If the GPU on the device running your Project does not support the rendering
path that you have selected, Unity automatically uses a lower fidelity
rendering path. For example, on a GPU that does not handle **Deferred
Shading** A rendering path in the Built-in Render Pipeline that places no
limit on the number of Lights that can affect a GameObject. All Lights are
evaluated per-pixel, which means that they all interact correctly with normal
maps and so on. Additionally, all Lights can have cookies and shadows. [More
info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading), Unity uses **Forward
Rendering** A rendering path that renders each object in one or more passes,
depending on lights that affect the object. Lights themselves are also treated
differently by Forward Rendering, depending on their settings and intensity.
[More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering).

  * [Forward](RenderTech-ForwardRendering.html) is the default rendering path in the Built-in Render Pipeline. It is a general-purpose rendering path.
  * [Deferred](RenderTech-DeferredShading.html) is the rendering path with the most lighting and shadow fidelity in the Built-in Render Pipeline.
  * [Legacy Vertex Lit](RenderTech-VertexLit.html) is the rendering path with the lowest lighting fidelity and no support for real-time shadows. It is a subset of the Forward rendering path.

## Rendering Path comparison

| **_Deferred_** | **_Forward_** | **_Vertex Lit_**  
---|---|---|---  
**Features** |  |  |   
Per-pixel lighting (normal maps, light cookies) | Yes | Yes | -  
Real-time shadows | Yes | With caveats | -  
**Reflection Probes** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) | Yes | Yes | -  
Depth & Normal Buffers | Yes | Additional render passes | -  
**Soft Particles** Particles that create semi-transparent effects like smoke,
fog or fire. Soft particles fade out as they approach an opaque object, to
prevent intersections with the geometry. [More info](shader-
StandardParticleShaders.html)  
See in [Glossary](Glossary.html#SoftParticles) | Yes | - | -  
Semi-transparent objects | - | Yes | Yes  
Anti-Aliasing | - | Yes | Yes  
Light **Culling Masks** Allows you to include or omit objects to be rendered
by a Camera, by Layer.  
See in [Glossary](Glossary.html#CullingMask) | Limited | Yes | Yes  
Lighting Fidelity | All per-pixel | Some per-pixel | All per-vertex  
**Performance** |  |  |   
Cost of a per-pixel Light | Number of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) it illuminates | Number of pixels * Number of objects it illuminates | -  
Number of times objects are normally rendered | 1 | Number of per-pixel lights | 1  
Overhead for simple **Scenes** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) | High | None | None  
**Platform Support** |  |  |   
PC (Windows/Mac) | **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) Model 3.0+ & MRT | All | All  
Mobile (iOS/Android) | OpenGL ES 3.0 & MRT, Metal | All | All  
Consoles | XB1, PS4 | All | -  
  
[](built-in-rendering-paths.html)

Rendering paths in the Built-In Render Pipeline

[](RenderTech-ForwardRendering.html)

Forward rendering path in the Built-In Render Pipeline

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

