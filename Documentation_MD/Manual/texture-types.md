[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-types.html)
  * [中文](/cn/current/Manual/texture-types.html)
  * [日本語](/ja/current/Manual/texture-types.html)
  * [한국어](/kr/current/Manual/texture-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-types.html)
  * [中文](/cn/current/Manual/texture-types.html)
  * [日本語](/ja/current/Manual/texture-types.html)
  * [한국어](/kr/current/Manual/texture-types.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Get started with textures](textures-getting-started.html)
  * Texture types

[](Textures.html)

Introduction to textures

[](texture-compression-formats.html)

Texture formats in memory

# Texture types

## Albedo texture maps

Albedo texture maps contain the base colors of a material. Make sure albedo
textures don’t contain any lighting or shadows, because Unity adds lighting
based on the positions of the object and the lights.

![Two examples of albedo texture maps. On the left is a texture map for a
character model, and on the right is a wooden crate. There are no shadows or
lighting in the
textures.](../uploads/Main/StandardShaderAlbedoTextureExamples.jpg) Two
examples of albedo texture maps. On the left is a texture map for a character
model, and on the right is a wooden crate. There are no shadows or lighting in
the textures.

## Normal maps

Normal maps are used by **normal map** A type of Bump Map texture that allows
you to add surface detail such as bumps, grooves, and scratches to a model
which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) **Shaders** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) to make low-polygon models look as if
they contain more detail. Unity uses normal maps encoded as RGB images. You
also have the option to generate a normal map from a grayscale height map
image.

### Alpha maps

An alpha map is a Texture that contains only alpha information. You can use an
alpha map to apply varying levels of transparency to a Material.

You can create an alpha map by creating a Texture with information in the
alpha channel, or by creating a grayscale Texture and converting the grayscale
values to alpha in Unity.

See the documentation on [Texture Import Settings](class-TextureImporter.html)
for more information.

## Detail maps

If you want to make a **Terrain** The landscape in your scene. A Terrain
GameObject adds a large flat plane to your scene and you can use the Terrain’s
Inspector window to create a detailed landscape. [More info](terrain-
UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain), you normally use your main Texture
to show areas of terrain such as grass, rocks and sand. If your terrain is
large, it may end up very blurry. Detail Textures hide this fact by fading in
small details as your main Texture gets closer.

When drawing Detail Textures, a neutral gray is invisible, white makes the
main Texture twice as bright, and black makes the main Texture completely
black.

See documentation on [Secondary Maps (Detail
Maps)](StandardShaderMaterialParameterDetail.html) for more information.

## Terrain Heightmaps

Textures can even be used in cases where the image will never be viewed at
all, at least not directly. In a greyscale image, each **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) value is simply a number corresponding
to the shade of grey at that point in the image (this could be a value in the
range 0..1 where zero is black and one is white, say). Although an image like
this can be viewed, there is no reason why the numeric pixel values can’t be
used for other purposes as well, and this is precisely what is done with
**Terrain Heightmaps**.

A _terrain_ is a **mesh** The main graphics primitive of Unity. Meshes make up
a large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) representing an area of ground where
each point on the ground has a particular height from a baseline. The
_heightmap_ for a terrain stores the numeric height samples at regular
intervals as greyscale values in an image where each pixel corresponds to a
grid coordinate on the ground. The values are not shown in the **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as an image but are converted to
coordinates that are used to generate the terrain mesh.

Interestingly, even though a **heightmap** A greyscale Texture that stores
height data for an object. Each pixel stores the height difference
perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) is not viewed directly as an image,
there are still common image processing techniques that are useful when
applied to the height data. For example, adding noise to a heightmap will
create the impression of rocky terrain while blurring will smooth it out to
produce a softer, rolling landscape.

More information about terrains in Unity can be found in [this
section](script-Terrain.html) of the manual.

## Additional resources

  * [Textures reference](textures-reference.html)
  * [Default texture Import Settings window reference](texture-type-default.html)
  * [Normal Map texture Import Settings window reference](texture-type-normal-map.html)

[](Textures.html)

Introduction to textures

[](texture-compression-formats.html)

Texture formats in memory

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

