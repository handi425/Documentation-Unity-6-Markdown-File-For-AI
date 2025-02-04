[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-SelfIllumFamily.html)
  * [中文](/cn/current/Manual/shader-SelfIllumFamily.html)
  * [日本語](/ja/current/Manual/shader-SelfIllumFamily.html)
  * [한국어](/kr/current/Manual/shader-SelfIllumFamily.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-SelfIllumFamily.html)
  * [中文](/cn/current/Manual/shader-SelfIllumFamily.html)
  * [日本語](/ja/current/Manual/shader-SelfIllumFamily.html)
  * [한국어](/kr/current/Manual/shader-SelfIllumFamily.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Self-Illuminated Shader Family

[](shader-TransCutBumpedSpecular.html)

Transparent Cutout Bumped Specular

[](shader-SelfIllumVertexLit.html)

Self-Illuminated Vertex-Lit

# Self-Illuminated Shader Family

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces these **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

The **Self-Illuminated** shaders will emit light only onto themselves based on
an attached alpha channel. They do not require any Lights to shine on them to
emit this light. Any vertex lights or **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) lights will simply add more light on
top of the self-illumination.

This is mostly used for light emitting objects. For example, parts of the wall
texture could be self-illuminated to simulate lights or displays. It can also
be useful to light power-up objects that should always have consistent
lighting throughout the game, regardless of the lights shining on it.

## [Self-Illuminated Vertex-Lit](shader-SelfIllumVertexLit.html)

![shader-SelfIllumVertexLit](../uploads/Shaders/Thumb-IllumVertex.jpg) shader-
SelfIllumVertexLit

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Illumination** texture with alpha channel for Illumination Map

[» More details](shader-SelfIllumVertexLit.html)

## [Self-Illuminated Diffuse](shader-SelfIllumDiffuse.html)

![shader-SelfIllumDiffuse](../uploads/Shaders/Thumb-IllumDiffuse.jpg) shader-
SelfIllumDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Illumination** texture with alpha channel for Illumination Map

[» More details](shader-SelfIllumDiffuse.html)

## [Self-Illuminated Specular](shader-SelfIllumSpecular.html)

![shader-SelfIllumSpecular](../uploads/Shaders/Thumb-IllumSpec.jpg) shader-
SelfIllumSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Illumination** texture with alpha channel for Illumination Map

[» More details](shader-SelfIllumSpecular.html)

## [Self-Illuminated Bumped](shader-SelfIllumBumpedDiffuse.html)

![shader-SelfIllumBumpedDiffuse](../uploads/Shaders/Thumb-IllumBump.jpg)
shader-SelfIllumBumpedDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) normal map with alpha channel for
Illumination

[» More details](shader-SelfIllumBumpedDiffuse.html)

## [Self-Illuminated Bumped Specular](shader-SelfIllumBumpedSpecular.html)

![shader-SelfIllumBumpedSpecular](../uploads/Shaders/Thumb-IllumBumpSpec.jpg)
shader-SelfIllumBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map** normal map with alpha channel for Illumination Map

[» More details](shader-SelfIllumBumpedSpecular.html)

## [Self-Illuminated Parallax](shader-SelfIllumParallaxDiffuse.html)

![shader-SelfIllumParallaxDiffuse](../uploads/Shaders/Thumb-
IllumParallaxBump.jpg) shader-SelfIllumParallaxDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map** normal map with alpha channel for Illumination Map & Parallax Depth combined

**Note:** One consideration of this shader is that the **Bumpmap** texture’s
alpha channel doubles as a Illumination and the Parallax Depth.

[» More details](shader-SelfIllumParallaxDiffuse.html)

## [Self-Illuminated Parallax Specular](shader-SelfIllumParallaxSpecular.html)

![shader-SelfIllumParallaxSpecular](../uploads/Shaders/Thumb-
IllumParallaxBumpSpec.jpg) shader-SelfIllumParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map** normal map with alpha channel for Illumination Map & Parallax Depth combined

**Note:** One consideration of this shader is that the **Bumpmap** texture’s
alpha channel doubles as a Illumination and the Parallax Depth.

[» More details](shader-SelfIllumParallaxSpecular.html)

SelfIllumFamily

[](shader-TransCutBumpedSpecular.html)

Transparent Cutout Bumped Specular

[](shader-SelfIllumVertexLit.html)

Self-Illuminated Vertex-Lit

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

