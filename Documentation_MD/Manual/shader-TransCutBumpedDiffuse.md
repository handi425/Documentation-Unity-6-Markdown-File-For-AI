[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-TransCutBumpedDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransCutBumpedDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransCutBumpedDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransCutBumpedDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-TransCutBumpedDiffuse.html)
  * [中文](/cn/current/Manual/shader-TransCutBumpedDiffuse.html)
  * [日本語](/ja/current/Manual/shader-TransCutBumpedDiffuse.html)
  * [한국어](/kr/current/Manual/shader-TransCutBumpedDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](shader-TransparentCutoutFamily.html)
  * Transparent Cutout Bumped Diffuse

[](shader-TransCutSpecular.html)

Transparent Cutout Specular

[](shader-TransCutBumpedSpecular.html)

Transparent Cutout Bumped Specular

# Transparent Cutout Bumped Diffuse

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-TransCutoutBump.jpg)

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

## Normal Mapped Properties

Like a **Diffuse** shader, this computes a simple (Lambertian) lighting model.
The lighting on the surface decreases as the angle between it and the light
decreases. The lighting depends only on the angle, and does not change as the
**camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) moves or rotates around.

**Normal mapping** simulates small surface details using a texture, instead of
spending more polygons to actually carve out details. It does not actually
change the shape of the object, but uses a special texture called a **Normal
Map** A type of Bump Map texture that allows you to add surface detail such as
bumps, grooves, and scratches to a model which catch the light as if they are
represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) to achieve this effect. In the
normal map, each **pixel** The smallest unit in a computer image. Pixel size
depends on your screen resolution. Pixel lighting is calculated at every
screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel)’s color value represents the angle of
the surface normal. Then by using this value instead of the one from geometry,
lighting is computed. The normal map effectively overrides the **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)’s geometry when calculating lighting of
the object.

### Creating Normal maps

You can import normal maps created outside of Unity, or you can import a
regular grayscale image and convert it to a Normal Map from within Unity.
(This page refers to a legacy shader which has been superseded by the
[Standard Shader](shader-StandardShader.html), but you can learn more about
how to use [Normal Maps in the Standard
Shader](StandardShaderMaterialParameterNormalMap.html))

### Technical Details

The Normal Map is a tangent space type of normal map. Tangent space is the
space that “follows the surface” of the model geometry. In this space, Z
always points away from the surface. Tangent space Normal Maps are a bit more
expensive than the other “object space” type Normal Maps, but have some
advantages:

  1. It’s possible to use them on deforming models - the bumps will remain on the deforming surface and will just work.
  2. It’s possible to reuse parts of the normal map on different areas of a model; or use them on different models.

## Diffuse Properties

Diffuse computes a simple (Lambertian) lighting model. The lighting on the
surface decreases as the angle between it and the light decreases. The
lighting depends only on this angle, and does not change as the camera moves
or rotates around.

## Performance

Generally, this shader is cheap to render. For more details, please view the
[Shader Peformance page](shader-Performance.html).

TransCutBumpedDiffuse

[](shader-TransCutSpecular.html)

Transparent Cutout Specular

[](shader-TransCutBumpedSpecular.html)

Transparent Cutout Bumped Specular

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

