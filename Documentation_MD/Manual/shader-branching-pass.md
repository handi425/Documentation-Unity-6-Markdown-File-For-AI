[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-branching-pass.html)
  * [中文](/cn/current/Manual/shader-branching-pass.html)
  * [日本語](/ja/current/Manual/shader-branching-pass.html)
  * [한국어](/kr/current/Manual/shader-branching-pass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-branching-pass.html)
  * [中文](/cn/current/Manual/shader-branching-pass.html)
  * [日本語](/ja/current/Manual/shader-branching-pass.html)
  * [한국어](/kr/current/Manual/shader-branching-pass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html)
  * [Branching in shaders](shader-branching.html)
  * [Branch in a shader via built-in macros](shader-branching-built-in-macros.html)
  * Branch based on shader pass or shader stage

[](shader-branching-unity-version.html)

Branch based on Unity version

[](shader-keywords-landing.html)

Shader keywords

# Branch based on shader pass or shader stage

## Shader stage being compiled

Preprocessor macros `SHADER_STAGE_VERTEX`, `SHADER_STAGE_FRAGMENT`,
`SHADER_STAGE_DOMAIN`, `SHADER_STAGE_HULL`, `SHADER_STAGE_GEOMETRY`,
`SHADER_STAGE_COMPUTE` are defined when compiling each **Shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) stage. Typically they are useful when
sharing Shader code between **pixel** The smallest unit in a computer image.
Pixel size depends on your screen resolution. Pixel lighting is calculated at
every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) Shaders and compute Shaders, to handle
cases where some things have to be done slightly differently.

## Surface Shader pass

When [Surface Shaders](SL-SurfaceShaders.html)A streamlined way of writing
shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) are compiled, they generate a
lot of code for various passes to do lighting. When compiling each pass, one
of the following macros is defined:

**Macro:** | **Use:**  
---|---  
`UNITY_PASS_FORWARDBASE` | **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) base pass (main directional
light, lightmaps, SH).  
`UNITY_PASS_FORWARDADD` | Forward rendering additive pass (one light per pass).  
`UNITY_PASS_DEFERRED` | **Deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading) pass (renders G-buffer).  
`UNITY_PASS_SHADOWCASTER` | Shadow caster and depth Texture rendering pass.  
  
## Additional resources

  * [HLSL pragma directives reference](SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](SL-Pragma-target.html)
  * [HLSL pragma require command reference](SL-Pragma-require.html)

[](shader-branching-unity-version.html)

Branch based on Unity version

[](shader-keywords-landing.html)

Shader keywords

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

