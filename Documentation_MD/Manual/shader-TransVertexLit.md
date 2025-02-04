[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransVertexLit.html)
  * [中文](/cn/current/Manual/shader-TransVertexLit.html)
  * [日本語](/ja/current/Manual/shader-TransVertexLit.html)
  * [한국어](/kr/current/Manual/shader-TransVertexLit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransVertexLit.html)
  * [中文](/cn/current/Manual/shader-TransVertexLit.html)
  * [日本語](/ja/current/Manual/shader-TransVertexLit.html)
  * [한국어](/kr/current/Manual/shader-TransVertexLit.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Shader Family](shader-TransparentFamily.html)
  * Transparent Vertex-Lit

[](shader-TransparentFamily.html)

Transparent Shader Family

[](shader-TransDiffuse.html)

Transparent Diffuse

# Transparent Vertex-Lit

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransVertex.jpg)

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

TransVertexLit

[](shader-TransparentFamily.html)

Transparent Shader Family

[](shader-TransDiffuse.html)

Transparent Diffuse

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

