[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-SelfIllumDiffuse.html)
  * [中文](/cn/current/Manual/shader-SelfIllumDiffuse.html)
  * [日本語](/ja/current/Manual/shader-SelfIllumDiffuse.html)
  * [한국어](/kr/current/Manual/shader-SelfIllumDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-SelfIllumDiffuse.html)
  * [中文](/cn/current/Manual/shader-SelfIllumDiffuse.html)
  * [日本語](/ja/current/Manual/shader-SelfIllumDiffuse.html)
  * [한국어](/kr/current/Manual/shader-SelfIllumDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Self-Illuminated Shader Family](shader-SelfIllumFamily.html)
  * Self-Illuminated Diffuse

[](shader-SelfIllumVertexLit.html)

Self-Illuminated Vertex-Lit

[](shader-SelfIllumSpecular.html)

Self-Illuminated Specular

# Self-Illuminated Diffuse

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-IllumDiffuse.jpg)

## Self-Illuminated Properties

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this shader.

This shader allows you to define bright and dark parts of the object. The
alpha channel of a secondary texture will define areas of the object that
“emit” light by themselves, even when no light is shining on it. In the alpha
channel, black is zero light, and white is full light emitted by the object.
Any **scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) lights will add illumination on top of
the shader’s illumination. So even if your object does not emit any light by
itself, it will still be lit by lights in your scene.

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

SelfIllumDiffuse

[](shader-SelfIllumVertexLit.html)

Self-Illuminated Vertex-Lit

[](shader-SelfIllumSpecular.html)

Self-Illuminated Specular

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

