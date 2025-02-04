[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-ReflectiveBumpedUnlit.html)
  * [中文](/cn/current/Manual/shader-ReflectiveBumpedUnlit.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveBumpedUnlit.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveBumpedUnlit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-ReflectiveBumpedUnlit.html)
  * [中文](/cn/current/Manual/shader-ReflectiveBumpedUnlit.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveBumpedUnlit.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveBumpedUnlit.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Reflective Shader Family](shader-ReflectiveFamily.html)
  * Reflective Normal Mapped Unlit

[](shader-ReflectiveParallaxSpecular.html)

Reflective Parallax Specular

[](shader-ReflectiveBumpedVertexLit.html)

Reflective Normal mapped Vertex-lit

# Reflective Normal Mapped Unlit

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-ReflBumpUnlit.jpg)

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

## Normal mapped Properties

This shader does not use normal-mapping in the traditional way. The **normal
map** A type of Bump Map texture that allows you to add surface detail such as
bumps, grooves, and scratches to a model which catch the light as if they are
represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) does not affect any lights shining
on the object, because the shader does not use lights at all. The normal map
will only distort the reflection map.

## Special Properties

This shader is special because it does not respond to lights at all, so you
don’t have to worry about performance reduction from use of multiple lights.
It simply displays the reflection cube map on the model. The reflection is
distorted by the normal map, so you get the benefit of detailed reflection.
Because it does not respond to lights, it is quite cheap. It is somewhat of a
specialized use case, but in those cases it does exactly what you want as
cheaply as possible.

## Performance

Generally, this shader is quite cheap to render. For more details, please view
the [Shader Peformance page](shader-Performance.html).

ReflectiveBumpedUnlit

[](shader-ReflectiveParallaxSpecular.html)

Reflective Parallax Specular

[](shader-ReflectiveBumpedVertexLit.html)

Reflective Normal mapped Vertex-lit

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

