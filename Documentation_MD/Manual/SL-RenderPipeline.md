[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-RenderPipeline.html)
  * [中文](/cn/current/Manual/SL-RenderPipeline.html)
  * [日本語](/ja/current/Manual/SL-RenderPipeline.html)
  * [한국어](/kr/current/Manual/SL-RenderPipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-RenderPipeline.html)
  * [中文](/cn/current/Manual/SL-RenderPipeline.html)
  * [日本語](/ja/current/Manual/SL-RenderPipeline.html)
  * [한국어](/kr/current/Manual/SL-RenderPipeline.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * Surface Shaders and rendering paths in the Built-In Render Pipeline

[](SL-SurfaceShaders-output.html)

Surface Shader output structures in the Built-In Render Pipeline

[](SL-SurfaceShader-create.html)

Create a surface shader in the Built-In Render Pipeline

# Surface Shaders and rendering paths in the Built-In Render Pipeline

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), when using a Surface
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), how lighting is applied and which
[Passes](SL-Pass.html) of the shader are used depends on which [rendering
path](RenderingPaths.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) is used. Each pass in a shader
communicates its lighting type via [Pass Tags](SL-PassTags.html).

## Render pipeline compatibility

**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Surface Shaders** | No  
  
For a streamlined way of creating Shader objects in URP, see [Shader Graph](shader-graph.html). | No  
  
For a streamlined way of creating Shader objects in HDRP, see [Shader Graph](shader-graph.html). | No | Yes  
  
## Rendering paths

  * In [Forward Rendering](RenderTech-ForwardRendering.html)A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering), `ForwardBase` and
`ForwardAdd` passes are used.

  * In [Deferred Shading](RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading), `Deferred` pass is used.

  * In [legacy Vertex Lit](RenderTech-VertexLit.html), `Vertex`, `VertexLMRGBM` and `VertexLM` passes are used.
  * In any of the above, to render [Shadows](Shadows.html)A UI component that adds a simple outline effect to graphic components such as Text or Image. It must be on the same GameObject as the graphic component. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Shadow.html)  
See in [Glossary](Glossary.html#Shadow) or a depth texture, `ShadowCaster`
pass is used.

## Forward Rendering path

`ForwardBase` pass renders ambient, **lightmaps** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), main directional light and not
important (vertex/SH) lights at once. `ForwardAdd` pass is used for any
additive per-pixel lights; one invocation per object illuminated by such light
is done. See [Forward Rendering](RenderTech-ForwardRendering.html) for
details.

If forward rendering is used, but a shader does not have forward-suitable
passes (i.e. neither `ForwardBase` nor `ForwardAdd` pass types are present),
then that object is rendered just like it would in Vertex Lit path, see below.

## Deferred Shading path

`Deferred` pass renders all information needed for lighting (in built-in
shaders: diffuse color, specular color, smoothness, world space normal,
emission). It also adds lightmaps, reflection probes and ambient lighting into
the emission channel. See [Deferred Shading](RenderTech-DeferredShading.html)
for details.

## Legacy Vertex Lit Rendering path

Since vertex lighting is most often used on platforms that do not support
programmable shaders, Unity can’t create multiple shader variants internally
to handle lightmapped vs. non-lightmapped cases. So to handle lightmapped and
non-lightmapped objects, multiple passes have to be written explicitly.

  * `Vertex` pass is used for non-lightmapped objects. All lights are rendered at once, using a fixed function OpenGL/Direct3D lighting model ([Blinn-Phong](http://en.wikipedia.org/wiki/Blinn-Phong_shading))
  * `VertexLMRGBM` pass is used for lightmapped objects, when lightmaps are RGBM encoded (PC and consoles). No real-time lighting is applied; pass is expected to combine textures with a lightmap.
  * `VertexLM` pass is used for lightmapped objects, when lightmaps are double-LDR encoded (mobile platforms). No real-time lighting is applied; pass is expected to combine textures with a lightmap.

[](SL-SurfaceShaders-output.html)

Surface Shader output structures in the Built-In Render Pipeline

[](SL-SurfaceShader-create.html)

Create a surface shader in the Built-In Render Pipeline

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

