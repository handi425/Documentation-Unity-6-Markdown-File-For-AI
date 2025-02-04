[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GPUInstancing.html)
  * [中文](/cn/current/Manual/GPUInstancing.html)
  * [日本語](/ja/current/Manual/GPUInstancing.html)
  * [한국어](/kr/current/Manual/GPUInstancing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GPUInstancing.html)
  * [中文](/cn/current/Manual/GPUInstancing.html)
  * [日本語](/ja/current/Manual/GPUInstancing.html)
  * [한국어](/kr/current/Manual/GPUInstancing.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Optimizing draw calls](reduce-draw-calls-landing.html)
  * [GPU instancing](GPUInstancing-landing.html)
  * Introduction to GPU instancing

[](GPUInstancing-landing.html)

GPU instancing

[](gpu-instancing-enable.html)

Enable GPU instancing

# Introduction to GPU instancing

GPU instancing is a [draw call optimization](optimizing-draw-calls.html)
method that renders multiple copies of a **mesh** The main graphics primitive
of Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) with the same material in a single draw
call. Each copy of the mesh is called an instance. This is useful for drawing
things that appear multiple times in a **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), for example, trees or bushes.

GPU instancing renders identical meshes in the same draw call. To add
variation and reduce the appearance of repetition, each instance can have
different properties, such as **Color** or **Scale**. Draw calls that render
multiple instances appear in the [Frame Debugger](FrameDebugger.html) as
**Render Mesh (instanced)**.

## Requirements and compatibility

This section includes information about the platform, **render pipeline** A
series of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), and SRP Batcher compatibility
of GPU instancing.

### Platform compatibility

GPU instancing is available on every platform. However, the performance
benefits of GPU instancing depend on the platform and the GPU you’ve chosen.
For example, the performance benefits are more prominent on mobile platforms
than on desktop platforms.

### Render pipeline compatibility

**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**GPU instancing** | Yes (1) | Yes (1) | Yes (1) | Yes  
  
**Notes** :

  1. Only if the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) isn’t compatible with the [SRP
Batcher](SRPBatcher.html). Refer to [Make materials incompatible with the SRP
Batcher](SRPBatcher-Incompatible.html) for more information.

### Lighting

GPU instancing supports Unity’s [Baked Global Illumination
system](progressive-lightmapper.html). Unity Standard Shaders and **surface
shaders** A streamlined way of writing shaders for the Built-in Render
Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) in the Built-In Render Pipeline
support GPU instancing and Unity’s Baked **Global Illumination** A group of
techniques that model both direct and indirect lighting to provide realistic
lighting results.  
See in [Glossary](Glossary.html#globalillumination) system by default.

Each GPU instance supports global illumination from one of the following
sources:

  * Any number of [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).

  * One [lightmap](Lightmapping.html)A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap).  
**Note** : An instance can use multiple atlas regions in the lightmap.

  * One [Light Probe Proxy Volume](class-LightProbeProxyVolume.html)A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](class-LightProbeProxyVolume.html)  
See in [Glossary](Glossary.html#LightProbeProxyVolume)(LPPV) component.  
**Note** : You must bake the LPPV for the space volume that contains all the
instances.

GPU instancing automatically works with:

  * Dynamic [Mesh Renderers](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) affected by Light Probes.

  * Static Mesh Renderers you bake to the same lightmap texture. A Mesh Renderer is static in this context if it includes **Contribute GI** in its [Static Editor Flags](StaticObjects.html).

[](GPUInstancing-landing.html)

GPU instancing

[](gpu-instancing-enable.html)

Enable GPU instancing

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

