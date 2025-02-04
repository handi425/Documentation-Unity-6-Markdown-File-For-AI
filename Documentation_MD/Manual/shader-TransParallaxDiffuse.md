[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransParallaxDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransParallaxDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransParallaxDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransParallaxDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransParallaxDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransParallaxDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransParallaxDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransParallaxDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Shader Family](shader-TransparentFamily.html)
  * Transparent Parallax Diffuse

[](shader-TransBumpedSpecular.html)

Transparent Bumped Specular

[](shader-TransParallaxSpecular.html)

Transparent Parallax Specular

# Transparent Parallax Diffuse

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransParallaxBump.jpg)

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

TransParallaxDiffuse

[](shader-TransBumpedSpecular.html)

Transparent Bumped Specular

[](shader-TransParallaxSpecular.html)

Transparent Parallax Specular

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

