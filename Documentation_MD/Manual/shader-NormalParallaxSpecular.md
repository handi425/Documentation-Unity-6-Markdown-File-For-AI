[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalParallaxSpecular.html)
  * [中文](/cn/current/Manual/shader-NormalParallaxSpecular.html)
  * [日本語](/ja/current/Manual/shader-NormalParallaxSpecular.html)
  * [한국어](/kr/current/Manual/shader-NormalParallaxSpecular.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalParallaxSpecular.html)
  * [中文](/cn/current/Manual/shader-NormalParallaxSpecular.html)
  * [日本語](/ja/current/Manual/shader-NormalParallaxSpecular.html)
  * [한국어](/kr/current/Manual/shader-NormalParallaxSpecular.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Normal Shader Family](shader-NormalFamily.html)
  * Parallax Bumped Specular

[](shader-NormalParallaxDiffuse.html)

Parallax Diffuse

[](shader-NormalDecal.html)

Decal

# Parallax Bumped Specular

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-NormalParallaxBumpSpec.jpg)

## Parallax Normal mapped Properties

**Parallax Normal mapped** is the same as regular **Normal mapped** , but with
a better simulation of “depth”. The extra depth effect is achieved through the
use of a **Height Map**. The Height Map is contained in the alpha channel of
the **Normal map** A type of Bump Map texture that allows you to add surface
detail such as bumps, grooves, and scratches to a model which catch the light
as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap). In the alpha, black is zero depth
and white is full depth. This is most often used in bricks/stones to better
display the cracks between them.

The Parallax mapping technique is pretty simple, so it can have artifacts and
unusual effects. Specifically, very steep height transitions in the Height Map
should be avoided. Adjusting the **Height** value in the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) can also cause the object to become
distorted in an odd, unrealistic way. For this reason, it is recommended that
you use gradual Height Map transitions or keep the **Height** slider toward
the shallow end.

## Specular Properties

Specular computes the same simple (Lambertian) lighting as Diffuse, plus a
viewer dependent specular highlight. This is called the Blinn-Phong lighting
model. It has a specular highlight that is dependent on surface angle, light
angle, and viewing angle. The highlight is actually just a realtime-suitable
way to simulate blurred reflection of the light source. The level of blur for
the highlight is controlled with the **Shininess** slider in the
**Inspector**.

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

Generally, this shader is on the more expensive rendering side. For more
details, please view the [Shader Peformance page](shader-Performance.html).

NormalParallaxSpecular

[](shader-NormalParallaxDiffuse.html)

Parallax Diffuse

[](shader-NormalDecal.html)

Decal

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

