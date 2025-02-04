[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-ReflectiveSpecular.html)
  * [中文](/cn/current/Manual/shader-ReflectiveSpecular.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveSpecular.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveSpecular.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-ReflectiveSpecular.html)
  * [中文](/cn/current/Manual/shader-ReflectiveSpecular.html)
  * [日本語](/ja/current/Manual/shader-ReflectiveSpecular.html)
  * [한국어](/kr/current/Manual/shader-ReflectiveSpecular.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Reflective Shader Family](shader-ReflectiveFamily.html)
  * Reflective Specular

[](shader-ReflectiveDiffuse.html)

Reflective Diffuse

[](shader-ReflectiveBumpedDiffuse.html)

Reflective Bumped Diffuse

# Reflective Specular

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-ReflSpec.jpg)

One consideration for this shader is that the Base texture’s alpha channel
will double as both the Reflection Map and the Specular Map.

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

## Specular Properties

Specular computes the same simple (Lambertian) lighting as Diffuse, plus a
viewer dependent specular highlight. This is called the Blinn-Phong lighting
model. It has a specular highlight that is dependent on surface angle, light
angle, and viewing angle. The highlight is actually just a realtime-suitable
way to simulate blurred reflection of the light source. The level of blur for
the highlight is controlled with the **Shininess** slider in the **Inspector**
A Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

Additionally, the alpha channel of the main texture acts as a Specular Map
(sometimes called “gloss map”), defining which areas of the object are more
reflective than others. Black areas of the alpha will be zero specular
reflection, while white areas will be full specular reflection. This is very
useful when you want different areas of your object to reflect different
levels of specularity. For example, something like rusty metal would use low
specularity, while polished metal would use high specularity. Lipstick has
higher specularity than skin, and skin has higher specularity than cotton
clothes. A well-made Specular Map can make a huge difference in impressing the
player.

## Performance

Generally, this shader is moderately expensive to render. For more details,
please view the [Shader Peformance page](shader-Performance.html).

ReflectiveSpecular

[](shader-ReflectiveDiffuse.html)

Reflective Diffuse

[](shader-ReflectiveBumpedDiffuse.html)

Reflective Bumped Diffuse

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

