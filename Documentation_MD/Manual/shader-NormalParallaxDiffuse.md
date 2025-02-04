[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalParallaxDiffuse.html)
  * [中文](/cn/current/Manual/shader-NormalParallaxDiffuse.html)
  * [日本語](/ja/current/Manual/shader-NormalParallaxDiffuse.html)
  * [한국어](/kr/current/Manual/shader-NormalParallaxDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalParallaxDiffuse.html)
  * [中文](/cn/current/Manual/shader-NormalParallaxDiffuse.html)
  * [日本語](/ja/current/Manual/shader-NormalParallaxDiffuse.html)
  * [한국어](/kr/current/Manual/shader-NormalParallaxDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Normal Shader Family](shader-NormalFamily.html)
  * Parallax Diffuse

[](shader-NormalBumpedSpecular.html)

Bumped Specular

[](shader-NormalParallaxSpecular.html)

Parallax Bumped Specular

# Parallax Diffuse

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-NormalParallaxBump.jpg)

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

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the
surface decreases as the angle between it and the light decreases. The
lighting depends only on this angle, and does not change as the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) moves or rotates around.

## Performance

Generally, this shader is on the more expensive rendering side. For more
details, please view the [Shader Peformance page](shader-Performance.html).

NormalParallaxDiffuse

[](shader-NormalBumpedSpecular.html)

Bumped Specular

[](shader-NormalParallaxSpecular.html)

Parallax Bumped Specular

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

