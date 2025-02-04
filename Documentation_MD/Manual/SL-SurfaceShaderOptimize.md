[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderOptimize.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderOptimize.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderOptimize.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderOptimize.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderOptimize.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderOptimize.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderOptimize.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderOptimize.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * Optimize Surface Shaders

[](SL-SurfaceShaderLighting.html)

Set the lighting model in a Surface Shader in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples.html)

Surface Shader examples in the Built-In Render Pipeline

# Optimize Surface Shaders

[Surface Shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders
for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) are great for writing
**shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that interact with lighting. However,
their default options are tuned to cover a broad number of general cases.
Tweak these for specific situations to make shaders run faster or at least be
smaller:

  * The `halfasview` for Specular shader types is even faster. The half-vector (halfway between lighting direction and view vector) is computed and normalized per vertex, and the [lighting function](SL-SurfaceShaderLighting.html) receives the half-vector as a parameter instead of the view vector.
  * `noforwardadd` makes a shader fully support one-directional light in **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) only. The rest of the lights
can still have an effect as per-vertex lights or spherical harmonics. This is
great to make your shader smaller and make sure it always renders in one pass,
even with multiple lights present.

  * `noambient` disables ambient lighting and spherical harmonics lights on a shader. This can make performance slightly faster.

## Additional resources

  * [Optimize shader runtime performance](SL-ShaderPerformance.html)

[](SL-SurfaceShaderLighting.html)

Set the lighting model in a Surface Shader in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples.html)

Surface Shader examples in the Built-In Render Pipeline

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

