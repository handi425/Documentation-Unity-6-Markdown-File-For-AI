[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaders.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaders.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaders.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaders.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaders.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaders.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaders.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * Introduction to surface shaders in the Built-In Render Pipeline

[](writing-surface-shaders.html)

Writing Surface Shaders

[](SL-SurfaceShaders-output.html)

Surface Shader output structures in the Built-In Render Pipeline

# Introduction to surface shaders in the Built-In Render Pipeline

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), Surface **Shaders** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) are a streamlined way of writing
shaders that interact with lighting.

## Render pipeline compatibility

**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Surface Shaders** | No  
  
For a streamlined way of creating Shader objects in URP, see [Shader Graph](shader-graph.html). | No  
  
For a streamlined way of creating Shader objects in HDRP, see [Shader Graph](shader-graph.html). | No | Yes  
  
## Overview

Writing shaders that interact with lighting is complex. There are different
light types, different shadow options, different **rendering paths** The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) (forward and deferred
rendering), and the shader should somehow handle all that complexity.

Surface Shaders is a code generation approach that makes it much easier to
write lit shaders than using low level [vertex/pixel shader programs](writing-
shader-writing-shader-programs-hlsl.html).

For some examples, take a look at [Surface Shader Examples](SL-
SurfaceShaderExamples.html).

## How it works

You define a “surface function” that takes any UVs or data you need as input,
and fills in output structure `SurfaceOutput`. SurfaceOutput basically
describes _properties of the surface_ (its albedo color, normal, emission,
specularity etc.). You write this code in HLSL.

Surface Shader compiler then figures out what inputs are needed, what outputs
are filled and so on, and generates actual [vertex&pixel shaders](writing-
shader-writing-shader-programs-hlsl.html), as well as rendering passes to
handle forward and deferred rendering.

## Surface Shaders and DirectX 11 HLSL syntax

Currently some parts of **surface shader** compilation pipeline do not
understand [DirectX 11](UsingDX11GL3Features.html)-specific HLSL syntax, so if
you’re using HLSL features like StructuredBuffers, RWTextures and other non-
DX9 syntax, you have to wrap it into a DX11-only preprocessor macro.

See [Platform Specific Differences](SL-PlatformDifferences.html) and [Using
HLSL](writing-shader-writing-shader-programs-hlsl.html) pages for details.

## Additional resources

  * [Writing custom shaders in URP](urp/writing-custom-shaders-urp.html)

[](writing-surface-shaders.html)

Writing Surface Shaders

[](SL-SurfaceShaders-output.html)

Surface Shader output structures in the Built-In Render Pipeline

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

