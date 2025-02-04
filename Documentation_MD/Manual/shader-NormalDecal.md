[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalDecal.html)
  * [中文](/cn/current/Manual/shader-NormalDecal.html)
  * [日本語](/ja/current/Manual/shader-NormalDecal.html)
  * [한국어](/kr/current/Manual/shader-NormalDecal.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalDecal.html)
  * [中文](/cn/current/Manual/shader-NormalDecal.html)
  * [日本語](/ja/current/Manual/shader-NormalDecal.html)
  * [한국어](/kr/current/Manual/shader-NormalDecal.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Normal Shader Family](shader-NormalFamily.html)
  * Decal

[](shader-NormalParallaxSpecular.html)

Parallax Bumped Specular

[](shader-NormalDiffuseDetail.html)

Diffuse Detail

# Decal

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-NormalDecal.jpg)

## Decal Properties

This shader is a variation of the VertexLit shader. All lights that shine on
it will be rendered as vertex lights by this shader. In addition to the main
texture, this shader makes use of a second texture for additional details. The
second “Decal” texture uses an alpha channel to determine visible areas of the
main texture. The decal texture should be supplemental to the main texture.
For example, if you have a brick wall, you can tile the brick texture as the
main texture, and use the decal texture with alpha channel to draw graffiti at
different places on the wall.

## Performance

This shader is approximately equivalent to the VertexLit shader. It is
marginally more expensive due to the second decal texture, but will not have a
noticeable impact.

NormalDecal

[](shader-NormalParallaxSpecular.html)

Parallax Bumped Specular

[](shader-NormalDiffuseDetail.html)

Diffuse Detail

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

