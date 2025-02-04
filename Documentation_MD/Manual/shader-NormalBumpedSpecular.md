[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-NormalBumpedSpecular.html)
  * [中文](/cn/current/Manual/shader-NormalBumpedSpecular.html)
  * [日本語](/ja/current/Manual/shader-NormalBumpedSpecular.html)
  * [한국어](/kr/current/Manual/shader-NormalBumpedSpecular.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-NormalBumpedSpecular.html)
  * [中文](/cn/current/Manual/shader-NormalBumpedSpecular.html)
  * [日本語](/ja/current/Manual/shader-NormalBumpedSpecular.html)
  * [한국어](/kr/current/Manual/shader-NormalBumpedSpecular.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Legacy prebuilt shaders](Built-inShaderGuide.html)
  * [Normal Shader Family](shader-NormalFamily.html)
  * Bumped Specular

[](shader-NormalBumpedDiffuse.html)

Bumped Diffuse

[](shader-NormalParallaxDiffuse.html)

Parallax Diffuse

# Bumped Specular

**Note.** Unity 5 introduced the [Standard Shader](shader-StandardShader.html)
which replaces this **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

![](../uploads/Shaders/Shader-NormalBumpSpec.jpg)

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

NormalBumpedSpecular

[](shader-NormalBumpedDiffuse.html)

Bumped Diffuse

[](shader-NormalParallaxDiffuse.html)

Parallax Diffuse

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

