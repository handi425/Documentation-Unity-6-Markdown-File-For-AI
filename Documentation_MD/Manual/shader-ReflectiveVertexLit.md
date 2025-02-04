[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-ReflectiveVertexLit.html)
  * [中文](/cn/current/Manual/shader-ReflectiveVertexLit.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveVertexLit.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveVertexLit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-ReflectiveVertexLit.html)
  * [中文](/cn/current/Manual/shader-ReflectiveVertexLit.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveVertexLit.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveVertexLit.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Reflective Shader Family](shader-ReflectiveFamily.html)
  * Reflective Vertex-Lit

[](shader-ReflectiveFamily.html)

Reflective Shader Family

[](shader-ReflectiveDiffuse.html)

Reflective Diffuse

# Reflective Vertex-Lit

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-ReflVertex.jpg)

## Reflective Properties

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this shader.

This shader will simulate reflective surfaces such as cars, metal objects etc.
It requires an environment **Cubemap** A collection of six square textures
that can represent the reflections in an environment or the skybox drawn
behind your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](class-
Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) which will define what exactly is
reflected. The main texture’s alpha channel defines the strength of reflection
on the object’s surface. Any **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) lights will add illumination on top of
what is reflected.

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

Generally, this shader is not too expensive to render. For more details,
please view the [Shader Peformance page](shader-Performance.html).

ReflectiveVertexLit

[](shader-ReflectiveFamily.html)

Reflective Shader Family

[](shader-ReflectiveDiffuse.html)

Reflective Diffuse

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

