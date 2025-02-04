[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransSpecular.html)
  * [中文](/cn/current/Manual/shader-TransSpecular.html)
  * [日本語](/ja/current/Manual/shader-TransSpecular.html)
  * [한국어](/kr/current/Manual/shader-TransSpecular.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransSpecular.html)
  * [中文](/cn/current/Manual/shader-TransSpecular.html)
  * [日本語](/ja/current/Manual/shader-TransSpecular.html)
  * [한국어](/kr/current/Manual/shader-TransSpecular.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Shader Family](shader-TransparentFamily.html)
  * Transparent Specular

[](shader-TransDiffuse.html)

Transparent Diffuse

[](shader-TransBumpedDiffuse.html)

Transparent Bumped Diffuse

# Transparent Specular

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransSpec.jpg)

One consideration for this shader is that the Base texture’s alpha channel
defines both the Transparent areas as well as the Specular Map.

## Transparent Properties

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this shader.

This shader can make **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) geometry partially or fully transparent
by reading the alpha channel of the main texture. In the alpha, 0 (black) is
completely transparent while 255 (white) is completely opaque. If your main
texture does not have an alpha channel, the object will appear completely
opaque.

Using transparent objects in your game can be tricky, as there are traditional
graphical programming problems that can present sorting issues in your game.
For example, if you see odd results when looking through two windows at once,
you’re experiencing the classical problem with using transparency. The general
rule is to be aware that there are some cases in which one transparent object
may be drawn in front of another in an unusual way, especially if the objects
are intersecting, enclose each other or are of very different sizes. For this
reason, you should use transparent objects if you need them, and try not to
let them become excessive. You should also make your designer(s) aware that
such sorting problems can occur, and have them prepare to change some design
to work around these issues.

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

TransSpecular

[](shader-TransDiffuse.html)

Transparent Diffuse

[](shader-TransBumpedDiffuse.html)

Transparent Bumped Diffuse

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

