[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterDetail.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterDetail.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterDetail.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterDetail.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterDetail.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterDetail.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterDetail.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterDetail.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](shader-built-in-configure-properties.html)
  * [Texture maps](StandardShaderTextureMaps.html)
  * Secondary Maps (Detail Maps) and Detail Mask

[](StandardShaderMaterialParameterEmission.html)

Add light emission to a material

[](Built-inShaderGuide.html)

Legacy prebuilt shaders

# Secondary Maps (Detail Maps) and Detail Mask

Secondary Maps (or Detail maps) allow you to overlay a second set of textures
on top of the main textures listed above. You can apply a second Albedo colour
map, and a second **Normal map** A type of Bump Map texture that allows you to
add surface detail such as bumps, grooves, and scratches to a model which
catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap). Typically, these would be mapped
on a much smaller scale repeated many times across the object’s surface,
compared with the main Albedo and Detail maps.

The reason for this is to allow the material to have sharp detail when viewed
up close, while also having a normal **level of detail** The _Level Of Detail_
(LOD) technique is an optimization that reduces the number of triangles that
Unity has to render for a GameObject when its distance from the Camera
increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail) when viewed from further away,
without having to use a single extremely high texture map to achieve both
goals.

Typical uses for detail textures would be:

  * Adding skin detail, such as pores and hairs, to a character’s skin
  * Adding tiny cracks and lichen growth to a brick wall
  * adding small scratches and scuffs to a large metal container

![This character has a skin texture map, but no detail texture yet. We will
add skin pores as a detail
texture.](../uploads/Main/StandardShaderDetailNotAppliedYet.jpg) This
character has a skin texture map, but no detail texture yet. We will add skin
pores as a detail texture. ![The Albedo skin pore detail
texture](../uploads/Main/StandardShaderDetailSkin.jpg) The Albedo skin pore
detail texture ![The normal map for the skin pore
detail](../uploads/Main/StandardShaderDetailSkinNormal.jpg) The normal map for
the skin pore detail ![The end result, the character now has subtle skin pore
detail across her skin, at a much higher resolution than the base Albedo or
Normal map layer would have
allowed.](../uploads/Main/StandardShaderDetailApplied.jpg) The end result, the
character now has subtle skin pore detail across her skin, at a much higher
resolution than the base Albedo or Normal map layer would have allowed.
![Detail textures can have a subtle but striking effect on the way light hits
a surface. This is the same character in a different lighting
context.](../uploads/Main/StandardShaderDetailDifferentContext.jpg) Detail
textures can have a subtle but striking effect on the way light hits a
surface. This is the same character in a different lighting context.

If you use a single normal map do ALWAYS plug it into the primary channel. The
Secondary normal map channel is more expensive than the primary one but has
the exact same effect.

### Detail Mask

The detail mask texture allows you to mask off certain areas of your model to
have the detail texture applied. This means you can show the detail texture in
certain areas, and hide it in others. In the example of the skin pores above,
you might want to create a mask so the pores are not shown on the lips or
eyebrows.

[](StandardShaderMaterialParameterEmission.html)

Add light emission to a material

[](Built-inShaderGuide.html)

Legacy prebuilt shaders

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

