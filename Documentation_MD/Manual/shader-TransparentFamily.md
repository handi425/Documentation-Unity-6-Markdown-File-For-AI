[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransparentFamily.html)
  * [中文](/cn/current/Manual/shader-TransparentFamily.html)
  * [日本語](/ja/current/Manual/shader-TransparentFamily.html)
  * [한국어](/kr/current/Manual/shader-TransparentFamily.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransparentFamily.html)
  * [中文](/cn/current/Manual/shader-TransparentFamily.html)
  * [日本語](/ja/current/Manual/shader-TransparentFamily.html)
  * [한국어](/kr/current/Manual/shader-TransparentFamily.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Transparent Shader Family

[](shader-NormalDiffuseDetail.html)

Diffuse Detail

[](shader-TransVertexLit.html)

Transparent Vertex-Lit

# Transparent Shader Family

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces these **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

The Transparent shaders are used for fully- or semi-transparent objects. Using
the alpha channel of the **Base** texture, you can determine areas of the
object which can be more or less transparent than others. This can create a
great effect for glass, HUD interfaces, or sci-fi effects.

## [Transparent Vertex-Lit](shader-TransVertexLit.html)

![shader-TransVertexLit](../uploads/Shaders/Thumb-TransVertex.jpg) shader-
TransVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

[» More details](shader-TransVertexLit.html)

## [Transparent Diffuse](shader-TransDiffuse.html)

![shader-TransDiffuse](../uploads/Shaders/Thumb-TransDiffuse.jpg) shader-
TransDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

[» More details](shader-TransDiffuse.html)

## [Transparent Specular](shader-TransSpecular.html)

![shader-TransSpecular](../uploads/Shaders/Thumb-TransSpec.jpg) shader-
TransSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map

**Note:** One limitation of this shader is that the **Base** texture’s alpha
channel doubles as a Specular Map for the Specular shaders in this family.

[» More details](shader-TransSpecular.html)

## [Transparent Normal mapped](shader-TransBumpedDiffuse.html)

![shader-TransBumpedDiffuse](../uploads/Shaders/Thumb-TransBump.jpg) shader-
TransBumpedDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) normal map, no alpha channel
required

[» More details](shader-TransBumpedDiffuse.html)

## [Transparent Normal mapped Specular](shader-TransBumpedSpecular.html)

![shader-TransBumpedSpecular](../uploads/Shaders/Thumb-TransBumpSpec.jpg)
shader-TransBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map, no alpha channel required

**Note:** One limitation of this shader is that the **Base** texture’s alpha
channel doubles as a Specular Map for the Specular shaders in this family.

[» More details](shader-TransBumpedSpecular.html)

## [Transparent Parallax](shader-TransParallaxDiffuse.html)

![shader-TransParallaxDiffuse](../uploads/Shaders/Thumb-TransParallaxBump.jpg)
shader-TransParallaxDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** normal map with alpha channel for Parallax Depth

[» More details](shader-TransParallaxDiffuse.html)

## [Transparent Parallax Specular](shader-TransParallaxSpecular.html)

![shader-TransParallaxSpecular](../uploads/Shaders/Thumb-
TransParallaxBumpSpec.jpg) shader-TransParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map with alpha channel for Parallax Depth

**Note:** One limitation of this shader is that the **Base** texture’s alpha
channel doubles as a Specular Map for the Specular shaders in this family.

[» More details](shader-TransParallaxSpecular.html)

TransparentFamily

[](shader-NormalDiffuseDetail.html)

Diffuse Detail

[](shader-TransVertexLit.html)

Transparent Vertex-Lit

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

