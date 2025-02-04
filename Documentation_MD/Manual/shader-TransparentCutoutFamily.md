[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransparentCutoutFamily.html)
  * [中文](/cn/current/Manual/shader-TransparentCutoutFamily.html)
  * [日本語](/ja/current/Manual/shader-TransparentCutoutFamily.html)
  * [한국어](/kr/current/Manual/shader-TransparentCutoutFamily.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransparentCutoutFamily.html)
  * [中文](/cn/current/Manual/shader-TransparentCutoutFamily.html)
  * [日本語](/ja/current/Manual/shader-TransparentCutoutFamily.html)
  * [한국어](/kr/current/Manual/shader-TransparentCutoutFamily.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Transparent Cutout Shader Family

[](shader-TransParallaxSpecular.html)

Transparent Parallax Specular

[](shader-TransCutVertexLit.html)

Transparent Cutout Vertex-Lit

# Transparent Cutout Shader Family

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces these **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

The Transparent Cutout shaders are used for objects that have fully opaque and
fully transparent parts (no partial transparency). Things like chain fences,
trees, grass, etc.

## [Transparent Cutout Vertex-Lit](shader-TransCutVertexLit.html)

![shader-TransCutVertexLit](../uploads/Shaders/Thumb-TransCutoutVertex.jpg)
shader-TransCutVertexLit

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

[» More details](shader-TransCutVertexLit.html)

## [Transparent Cutout Diffuse](shader-TransCutDiffuse.html)

![shader-TransCutDiffuse](../uploads/Shaders/Thumb-TransCutoutDiffuse.jpg)
shader-TransCutDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map

[» More details](shader-TransCutDiffuse.html)

## [Transparent Cutout Specular](shader-TransCutSpecular.html)

![shader-TransCutSpecular](../uploads/Shaders/Thumb-TransCutoutSpec.jpg)
shader-TransCutSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map

**Note:** One limitation of this shader is that the **Base** texture’s alpha
channel doubles as a Specular Map for the Specular shaders in this family.

[» More details](shader-TransCutSpecular.html)

## [Transparent Cutout Bumped](shader-TransCutBumpedDiffuse.html)

![shader-TransCutBumpedDiffuse](../uploads/Shaders/Thumb-TransCutoutBump.jpg)
shader-TransCutBumpedDiffuse

**Assets needed:**

  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) normal map, no alpha channel
required

[» More details](shader-TransCutBumpedDiffuse.html)

## [Transparent Cutout Bumped Specular](shader-TransCutBumpedSpecular.html)

![shader-TransCutBumpedSpecular](../uploads/Shaders/Thumb-
TransCutoutBumpSpec.jpg) shader-TransCutBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map, no alpha channel required

**Note:** One limitation of this shader is that the **Base** texture’s alpha
channel doubles as a Specular Map for the Specular shaders in this family.

[» More details](shader-TransCutBumpedSpecular.html)

TransparentCutoutFamily

[](shader-TransParallaxSpecular.html)

Transparent Parallax Specular

[](shader-TransCutVertexLit.html)

Transparent Cutout Vertex-Lit

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

