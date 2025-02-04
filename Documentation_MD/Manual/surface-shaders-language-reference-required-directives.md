[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/surface-shaders-language-reference-required-directives.html)
  * [中文](/cn/current/Manual/surface-shaders-language-reference-required-directives.html)
  * [日本語](/ja/current/Manual/surface-shaders-language-reference-required-directives.html)
  * [한국어](/kr/current/Manual/surface-shaders-language-reference-required-directives.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/surface-shaders-language-reference-required-directives.html)
  * [中文](/cn/current/Manual/surface-shaders-language-reference-required-directives.html)
  * [日本語](/ja/current/Manual/surface-shaders-language-reference-required-directives.html)
  * [한국어](/kr/current/Manual/surface-shaders-language-reference-required-directives.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader language reference for the Built-In Render Pipeline](surface-shaders-language-reference.html)
  * Surface Shader required directives reference for the Built-In Render Pipeline

[](surface-shaders-language-reference.html)

Surface Shader language reference for the Built-In Render Pipeline

[](surface-shaders-language-reference-optional-directives.html)

Surface Shader optional directives reference for the Built-In Render Pipeline

# Surface Shader required directives reference for the Built-In Render
Pipeline

  * `surfaceFunction` \- which Cg function has surface **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code. The function should have the
form of `void surf (Input IN, inout SurfaceOutput o)`, where Input is a
structure you have defined. Input should contain any texture coordinates and
extra automatic variables needed by surface function.

  * `lightModel` \- lighting model to use. Built-in ones are physically based `Standard` and `StandardSpecular`, as well as simple non-physically based `Lambert` (diffuse) and `BlinnPhong` (specular). See [Custom Lighting Models](SL-SurfaceShaderLighting.html) page for how to write your own. 
    * `Standard` lighting model uses `SurfaceOutputStandard` output struct, and matches the Standard (metallic workflow) shader in Unity.
    * `StandardSpecular` lighting model uses `SurfaceOutputStandardSpecular` output struct, and matches the Standard (specular setup) shader in Unity.
    * `Lambert` and `BlinnPhong` lighting models are not physically based (coming from Unity 4.x), but the shaders using them can be faster to render on low-end hardware.

[](surface-shaders-language-reference.html)

Surface Shader language reference for the Built-In Render Pipeline

[](surface-shaders-language-reference-optional-directives.html)

Surface Shader optional directives reference for the Built-In Render Pipeline

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

