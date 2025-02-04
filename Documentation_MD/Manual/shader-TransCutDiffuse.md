[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransCutDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransCutDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransCutDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransCutDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransCutDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransCutDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransCutDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransCutDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](shader-TransparentCutoutFamily.html)
  * Transparent Cutout Diffuse

[](shader-TransCutVertexLit.html)

Transparent Cutout Vertex-Lit

[](shader-TransCutSpecular.html)

Transparent Cutout Specular

# Transparent Cutout Diffuse

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransCutoutDiffuse.jpg)

## Transparent Cutout Properties

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this shader.

Cutout shader is an alternative way of displaying transparent objects.
Differences between Cutout and regular [Transparent](shader-
TransparentFamily.html) shaders are:

  * This shader cannot have partially transparent areas. Everything will be either fully opaque or fully transparent.
  * Objects using this shader can cast and receive shadows!
  * The graphical sorting problems normally associated with Transparent shaders do not occur when using this shader.

This shader uses an alpha channel contained in the **Base** Texture to
determine the transparent areas. If the alpha contains a blend between
transparent and opaque areas, you can manually determine the cutoff point for
the which areas will be shown. You change this cutoff by adjusting the **Alpha
Cutoff** slider.

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the
surface decreases as the angle between it and the light decreases. The
lighting depends only on this angle, and does not change as the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) moves or rotates around.

## Performance

Generally, this shader is cheap to render. For more details, please view the
[Shader Peformance page](shader-Performance.html).

TransCutDiffuse

[](shader-TransCutVertexLit.html)

Transparent Cutout Vertex-Lit

[](shader-TransCutSpecular.html)

Transparent Cutout Specular

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

