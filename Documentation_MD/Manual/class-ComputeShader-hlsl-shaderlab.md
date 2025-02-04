[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [中文](/cn/current/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-hlsl-shaderlab.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [中文](/cn/current/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-hlsl-shaderlab.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-hlsl-shaderlab.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Compute shaders](class-ComputeShader.html)
  * Use HLSL and ShaderLab in a compute shader

[](class-ComputeShader-create.html)

Create a compute shader

[](class-ComputeShader-run.html)

Run a compute shader

# Use HLSL and ShaderLab in a compute shader

## Use texture samplers

Textures and samplers aren’t separate objects in Unity, so to use them in
compute **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) you must follow one of the following
Unity-specific rules:

  * Use the same name as the Texture name, with `sampler` at the beginning (for example, `Texture2D MyTex`; `SamplerState samplerMyTex`). In this case, the sampler is initialized to that Texture’s filter/wrap/aniso settings.

  * Use a predefined sampler. For this, the name has to have `Linear` or `Point` (for filter mode) and `Clamp` or `Repeat` (for wrap mode). For example, `SamplerState MyLinearClampSampler` creates a sampler that has Linear filter mode and Clamp wrap mode.

For more information, see documentation on [Sampler States](SL-
SamplerStates.html).

## Use keywords

You can use keywords to produce multiple variants of compute shaders, the same
as you can for graphics shaders.

For general information on variants, see [Shader variants](shader-
variants.html)A verion of a shader program that Unity generates according to a
specific combination of shader keywords and their status. A Shader object can
contain multiple shader variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant). For information on how to
implement these features in compute shaders, see [Declaring and using shader
keywords in HLSL](SL-MultipleProgramVariants.html) and the [ComputeShader API
documentation](../ScriptReference/ComputeShader.html).

## HLSL-only or GLSL-only compute shaders

Usually, compute shader files are written in
[HLSL](https://en.wikipedia.org/wiki/High-Level_Shading_Language), and
compiled or translated into all necessary platforms automatically. However, it
is possible to either prevent translation to other languages (that is, only
keep HLSL platforms), or to write
[GLSL](https://en.wikipedia.org/wiki/OpenGL_Shading_Language) compute code
manually.

The following information only applies to HLSL-only or GLSL-only compute
shaders, not cross-platform builds. This is because this information can
result in compute shader source being excluded from some platforms.

  * Compute shader source surrounded by `CGPROGRAM` and `ENDCG` keywords is not processed for non-HLSL platforms.

  * Compute shader source surrounded by `GLSLPROGRAM` and `ENDGLSL` keywords is treated as GLSL source, and emitted verbatim. This only works when targeting OpenGL or GLSL platforms. You should also note that while automatically translated shaders follow HLSL data layout on buffers, manually written GLSL shaders follow GLSL layout rules.

[](class-ComputeShader-create.html)

Create a compute shader

[](class-ComputeShader-run.html)

Run a compute shader

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

