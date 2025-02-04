[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalDiffuseDetail.html)
  * [中文](/cn/current/Manual/shader-NormalDiffuseDetail.html)
  * [日本語](/ja/current/Manual/shader-NormalDiffuseDetail.html)
  * [한국어](/kr/current/Manual/shader-NormalDiffuseDetail.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalDiffuseDetail.html)
  * [中文](/cn/current/Manual/shader-NormalDiffuseDetail.html)
  * [日本語](/ja/current/Manual/shader-NormalDiffuseDetail.html)
  * [한국어](/kr/current/Manual/shader-NormalDiffuseDetail.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Normal Shader Family](shader-NormalFamily.html)
  * Diffuse Detail

[](shader-NormalDecal.html)

Decal

[](shader-TransparentFamily.html)

Transparent Shader Family

# Diffuse Detail

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-NormalDiffuseDetail.jpg)

## Diffuse Detail Properties

This shader is a version of the regular Diffuse shader with additional data.
It allows you to define a second “Detail” texture that will gradually appear
as the **camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) gets closer to it. It can be used on
**terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain), for example. You can use a base low-
resolution texture and stretch it over the entire terrain. When the camera
gets close the low-resolution texture will get blurry, and we don’t want that.
To avoid this effect, create a generic Detail texture that will be tiled over
the terrain. This way, when the camera gets close, the additional details
appear and the blurry effect is avoided.

The Detail texture is put “on top” of the base texture. Darker colors in the
detail texture will darken the main texture and lighter colors will brighten
it. Detail texture are usually gray-ish.

## Performance

This shader is pixel-lit, and approximately equivalent to the Diffuse shader.
It is marginally more expensive due to additional texture.

NormalDiffuseDetail

[](shader-NormalDecal.html)

Decal

[](shader-TransparentFamily.html)

Transparent Shader Family

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

