[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-create-material.html)
  * [中文](/cn/current/Manual/shader-create-material.html)
  * [日本語](/ja/current/Manual/shader-create-material.html)
  * [한국어](/kr/current/Manual/shader-create-material.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-create-material.html)
  * [中文](/cn/current/Manual/shader-create-material.html)
  * [日本語](/ja/current/Manual/shader-create-material.html)
  * [한국어](/kr/current/Manual/shader-create-material.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](shader-built-in-configure-properties.html)
  * Creating a material from a prebuilt shader

[](shader-built-in-configure-properties.html)

Configuring material properties in prebuilt shaders

[](StandardShaderTextureMaps.html)

Texture maps

# Creating a material from a prebuilt shader

The Standard **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) allows for many configurations in
order to represent a great variety of material types. Values can be set with
texture maps or colour pickers and sliders. Generally UV mapping is required
in conjunction with textures to describe which part of your **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) refers to which part of the texture map.
The Standard Shader material allows you therefore to have different material
properties across the same mesh when used in conjunction with specular and
smoothness map or a metallic map. In other words you can create rubber, metal
and wood on one mesh where the resolution of the texture can exceed the
polygon topology allowing for smooth borders and transition between material
types, of course this has implications for a greater complexity in the
workflow, but this will depend on your texture creation method.

Textures for your materials tend to be generated in one of two ways - painting
and compositing in a 2D image editor like Photoshop, or rendering / baking
from your 3D package, where you can also make use of higher resolution models
to generate your **normal maps** A type of Bump Map texture that allows you to
add surface detail such as bumps, grooves, and scratches to a model which
catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) and occlusion maps in addition to
the albedo, specular and other maps. This workflow varies dependent on the
external packages used.

Generally no texture map should contain inherent lighting (shadows,
highlights, etc). One of the advantages of PBS is that objects react to light
as you would expect, which is not possible if maps already contain lighting
information.

[](shader-built-in-configure-properties.html)

Configuring material properties in prebuilt shaders

[](StandardShaderTextureMaps.html)

Texture maps

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

