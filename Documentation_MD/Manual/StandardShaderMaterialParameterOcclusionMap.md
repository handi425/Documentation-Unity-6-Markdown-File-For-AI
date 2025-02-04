[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterOcclusionMap.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](shader-built-in-configure-properties.html)
  * [Texture maps](StandardShaderTextureMaps.html)
  * Occlusion maps

[](StandardShaderMaterialParameterHeightMap.html)

Height maps

[](StandardShaderMaterialParameterEmission.html)

Add light emission to a material

# Occlusion maps

The occlusion map is used to provide information about which areas of the
model should receive high or low indirect lighting. Indirect lighting comes
from ambient lighting and reflections, so steep concave parts of your model
like a crack or a fold would not realistically receive much indirect light.

Occlusion texture maps are normally calculated by 3D applications directly
from the 3D model using the modeller or third party software.

An occlusion map is a greyscale image, with white indicating areas that should
receive full indirect lighting, and black indicating no indirect lighting.
Sometimes this is as simple as a greyscale **heightmap** A greyscale Texture
that stores height data for an object. Each pixel stores the height difference
perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) for simple surfaces.

At other times, generating the correct occlusion texture is slightly more
complex. For example, if a character in your **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is wearing a hood, the inside edges of
the hood should be set to very low indirect lighting, or none at all. In these
situations occlusion maps will often be produced by artists using 3D
applications to automatically generate an occlusion map based on the model.

![This occlusion map identifies areas on a characters sleeve that are exposed
or hidden from ambient lighting. It is used on the model pictured
below.](../uploads/Main/StandardShaderOcclusionMapTexture.jpg) This occlusion
map identifies areas on a character’s sleeve that are exposed or hidden from
ambient lighting. It is used on the model pictured below. ![Before and after
applying an occlusion map. The areas that are partially obscured, particularly
in the folds of fabric around the neck, are lit too brightly on the left.
After the ambient occlusion map is assigned, these areas are no longer lit by
the green ambient light from the surrounding wooded
environment.](../uploads/Main/StandardShaderOcclusionMap.jpg) Before and after
applying an occlusion map. The areas that are partially obscured, particularly
in the folds of fabric around the neck, are lit too brightly on the left.
After the ambient occlusion map is assigned, these areas are no longer lit by
the green ambient light from the surrounding wooded environment.

[](StandardShaderMaterialParameterHeightMap.html)

Height maps

[](StandardShaderMaterialParameterEmission.html)

Add light emission to a material

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

