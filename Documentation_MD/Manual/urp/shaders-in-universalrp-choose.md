[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shaders-in-universalrp-choose.html)
  * [中文](/cn/current/Manual/urp/shaders-in-universalrp-choose.html)
  * [日本語](/ja/current/Manual/urp/shaders-in-universalrp-choose.html)
  * [한국어](/kr/current/Manual/urp/shaders-in-universalrp-choose.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shaders-in-universalrp-choose.html)
  * [中文](/cn/current/Manual/urp/shaders-in-universalrp-choose.html)
  * [日本語](/ja/current/Manual/urp/shaders-in-universalrp-choose.html)
  * [한국어](/kr/current/Manual/urp/shaders-in-universalrp-choose.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * Choose a prebuilt shader in URP

[](../urp/shading-model.html)

Shading models in URP

[](../urp/shaders-in-universalrp-select.html)

Assign a shader to a material in URP

# Choose a prebuilt shader in URP

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) implements Physically Based
Rendering (PBR).

The pipeline provides pre-built **shaders** A program that runs on the GPU.
[More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) that can simulate real world
materials.

PBR materials provide a set of parameters that let artists achieve consistency
between different material types and under different lighting conditions.

## Complex Lit Shader

The [Complex Lit shader](shader-complex-lit.html) is suitable for simulating
advanced materials that require more complex lighting evaluation, such as the
clear coat effect.

The Complex Lit Shader contains all the functionality of the Lit shader and
adds advanced material features. Some features in this shader might be
considerably more resource-intensive and require [Unity Shader Model
4.5](https://docs.unity3d.com/Manual/SL-ShaderCompileTargets.html) hardware.

In the Deferred **Rendering Path** The technique that a render pipeline uses
to render graphics. Choosing a different rendering path affects how lighting
and shading are calculated. Some rendering paths are more suited to different
platforms and hardware than others. [More info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath), URP renders objects that
have the Complex Lit shader using the **Forward Rendering** A rendering path
that renders each object in one or more passes, depending on lights that
affect the object. Lights themselves are also treated differently by Forward
Rendering, depending on their settings and intensity. [More
info](../RenderTech-ForwardRendering.html)  
See in [Glossary](../Glossary.html#ForwardRendering) Path. If the hardware of
the target platform does not support features in the Complex Lit shader, URP
uses the Lit shader instead.

## Lit Shader

The URP [Lit shader](lit-shader.html) is suitable for modeling most of the
real world materials.

The Lit Shader lets you render real-world surfaces like stone, wood, glass,
plastic, and metals in photo-realistic quality. Your light levels and
reflections look lifelike and react properly across various lighting
conditions, for example bright sunlight, or a dark cave. This Shader uses the
most computationally heavy [shading model](shading-model.html) in the
Universal Render Pipeline (URP).

For examples of how to use the Lit Shader, refer to the [Shaders samples in
URP Package Samples](package-sample-urp-package-samples.html#shaders).

## Simple Lit Shader

URP provides the [Simple Lit shader](simple-lit-shader.html) as a helper to
convert non-PBR projects made with the Built-in Render Pipeline to URP. This
shader is non-PBR and is not supported by Shader Graph.

Use this Shader when performance is more important than photorealism. This
Shader uses a simple approximation for lighting. Because this Shader [does not
calculate for physical correctness and energy conservation](shading-
model.html#simple-shading), it renders quickly.

## Baked Lit Shader

If you don’t need real-time lighting, or would rather only use [baked
lighting](https://docs.unity3d.com/Manual/LightMode-Baked.html) and sample
**global illumination** A group of techniques that model both direct and
indirect lighting to provide realistic lighting results.  
See in [Glossary](../Glossary.html#globalillumination), choose a Baked Lit
Shader.

In the Universal Render Pipeline (URP), use this Shader for stylised games or
apps that only require [baked
lighting](https://docs.unity3d.com/Manual/LightMode-Baked.html)via
[lightmaps](https://docs.unity3d.com/Manual/Lightmapping.html)A pre-rendered
texture that contains the effects of light sources on static objects in the
scene. Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](../Lightmapping.html)  
See in [Glossary](../Glossary.html#Lightmap) and [Light
Probes](https://docs.unity3d.com/Manual/LightProbes.html)Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe). This shader does not use
[Physically Based Shading](shading-model.html#physically-based-shading)An
advanced lighting model that simulates the interactions between materials and
light in a way that mimics reality. [More info](../shader-StandardShader.html)  
See in [Glossary](../Glossary.html#PhysicallyBasedShading) and has no real-
time lighting, so all real-time relevant shader keywords and variants are
[stripped](shader-stripping.html) from the Shader code, which makes it faster
to calculate.

## Unlit Shader

If you don’t need lighting on a Material at all, you can choose the Unlit
Shader.

Use this Shader for effects or unique objects in your visuals that don’t need
lighting. Because there are no time-consuming lighting calculations or
lookups, this Shader is optimal for lower-end hardware. The Unlit Shader uses
the most simple [shading model](shading-model.html) in URP.

## Particle shaders

URP provides the following particle shaders:

  * Particles Lit Shader - makes particles appear almost photorealistic, for example for camp fire particles, rain drops or torch smoke. This Shader produces lifelike visuals but uses the most computationally heavy [shading model](shading-model.html) in URP, which can impact performance.
  * Particles Simple Lit shader - for particles where performance is more important than photorealism. This Shader uses a simple approximation for lighting. Because this Shader [does not calculate for physical correctness and energy conservation](shading-model.html#simple-shading), it renders quickly.
  * Particles Unlit Shader - for particles that don’t need lighting. Because there are no time-consuming lighting calculations or lookups, this Shader is optimal for lower-end hardware. The Unlit Shader uses the most simple [shading model](shading-model.html) in the Universal Render Pipeline (URP).

[](../urp/shading-model.html)

Shading models in URP

[](../urp/shaders-in-universalrp-select.html)

Assign a shader to a material in URP

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

