[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalFamily.html)
  * [中文](/cn/current/Manual/shader-NormalFamily.html)
  * [日本語](/ja/current/Manual/shader-NormalFamily.html)
  * [한국어](/kr/current/Manual/shader-NormalFamily.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalFamily.html)
  * [中文](/cn/current/Manual/shader-NormalFamily.html)
  * [日本語](/ja/current/Manual/shader-NormalFamily.html)
  * [한국어](/kr/current/Manual/shader-NormalFamily.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * Normal Shader Family

[](shader-Performance.html)

Usage and Performance of Built-in Shaders

[](shader-NormalVertexLit.html)

Vertex-Lit

# Normal Shader Family

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces these **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

These shaders are the basic shaders in Unity. They are not specialized in any
way and should be suitable for most opaque objects. They are not suitable if
you want your object to be transparent, emitting light etc.

## [Vertex Lit](shader-NormalVertexLit.html)

![shader-NormalVertexLit](../uploads/Shaders/Thumb-NormalVertex.jpg) shader-
NormalVertexLit

**Assets needed:**

  * One **Base** texture, no alpha channel required

## [Diffuse](shader-NormalDiffuse.html)

![shader-NormalDiffuse](../uploads/Shaders/Thumb-NormalDiffuse.jpg) shader-
NormalDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required

## [Specular](shader-NormalSpecular.html)

![shader-NormalSpecular](../uploads/Shaders/Thumb-NormalSpec.jpg) shader-
NormalSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map

## [Normal mapped](shader-NormalBumpedDiffuse.html)

![shader-NormalBumpedDiffuse](../uploads/Shaders/Thumb-NormalBump.jpg) shader-
NormalBumpedDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap)

## [Normal mapped Specular](shader-NormalBumpedSpecular.html)

![shader-NormalBumpedSpecular](../uploads/Shaders/Thumb-NormalBumpSpec.jpg)
shader-NormalBumpedSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map**

## [Parallax](shader-NormalParallaxDiffuse.html)

![shader-NormalParallaxDiffuse](../uploads/Shaders/Thumb-
NormalParallaxBump.jpg) shader-NormalParallaxDiffuse

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Normal map**
  * One **Height** texture with Parallax Depth in the alpha channel

## [Parallax Specular](shader-NormalParallaxSpecular.html)

![shader-NormalParallaxSpecular](../uploads/Shaders/Thumb-
NormalParallaxBumpSpec.jpg) shader-NormalParallaxSpecular

**Assets needed:**

  * One **Base** texture with alpha channel for Specular Map
  * One **Normal map**
  * One **Height** texture with Parallax Depth in the alpha channel

## [Decal](shader-NormalDecal.html)

![shader-NormalDecal](../uploads/Shaders/Thumb-NormalDecal.jpg) shader-
NormalDecal

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Decal** texture with alpha channel for Decal transparency

## [Diffuse Detail](shader-NormalDiffuseDetail.html)

![shader-NormalDiffuseDetail](../uploads/Shaders/Thumb-
NormalDiffuseDetail.jpg) shader-NormalDiffuseDetail

**Assets needed:**

  * One **Base** texture, no alpha channel required
  * One **Detail** grayscale texture; with 50% gray being neutral color

NormalFamily

[](shader-Performance.html)

Usage and Performance of Built-in Shaders

[](shader-NormalVertexLit.html)

Vertex-Lit

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

