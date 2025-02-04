[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransCutVertexLit.html)
  * [中文](/cn/current/Manual/shader-TransCutVertexLit.html)
  * [日本語](/ja/current/Manual/shader-TransCutVertexLit.html)
  * [한국어](/kr/current/Manual/shader-TransCutVertexLit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransCutVertexLit.html)
  * [中文](/cn/current/Manual/shader-TransCutVertexLit.html)
  * [日本語](/ja/current/Manual/shader-TransCutVertexLit.html)
  * [한국어](/kr/current/Manual/shader-TransCutVertexLit.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](shader-TransparentCutoutFamily.html)
  * Transparent Cutout Vertex-Lit

[](shader-TransparentCutoutFamily.html)

Transparent Cutout Shader Family

[](shader-TransCutDiffuse.html)

Transparent Cutout Diffuse

# Transparent Cutout Vertex-Lit

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransCutoutVertex.jpg)

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

## Vertex-Lit Properties

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this shader.

This shader is **Vertex-Lit** , which is one of the simplest shaders. All
lights shining on it are rendered in a single pass and calculated at vertices
only.

Because it is vertex-lit, it won’t display any pixel-based rendering effects,
such as light cookies, normal mapping, or shadows. This shader is also much
more sensitive to tesselation of the models. If you put a point light very
close to a cube using this shader, the light will only be calculated at the
corners. Pixel-lit shaders are much more effective at creating a nice round
highlight, independent of tesselation. If that’s an effect you want, you may
consider using a pixel-lit shader or increase tesselation of the objects
instead.

## Performance

Generally, this shader is very cheap to render. For more details, please view
the [Shader Peformance page](shader-Performance.html).

TransCutVertexLit

[](shader-TransparentCutoutFamily.html)

Transparent Cutout Shader Family

[](shader-TransCutDiffuse.html)

Transparent Cutout Diffuse

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

