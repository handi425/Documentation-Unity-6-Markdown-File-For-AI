[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterHeightMap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterHeightMap.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterHeightMap.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](shader-built-in-configure-properties.html)
  * [Texture maps](StandardShaderTextureMaps.html)
  * Height maps

[](StandardShaderMaterialParameterNormalMapImport.html)

Import a normal map

[](StandardShaderMaterialParameterOcclusionMap.html)

Occlusion maps

# Height maps

Height mapping (also known as parallax mapping) is a similar concept to normal
mapping, however this technique is more complex - and therefore also more
performance-expensive. **Heightmaps** A greyscale Texture that stores height
data for an object. Each pixel stores the height difference perpendicular to
the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) are usually used in conjunction
with normalmaps, and often they are used to give extra definition to surfaces
where the texture maps are responsible for rendering large bumps and
protrusions.

While normal mapping modifies the lighting across the surface of the texture,
parallax height mapping goes a step further and actually shifts the areas of
the visible surface texture around, to achieve a kind of surface-level
occlusion effect. This means that apparent bumps will have their near side
(facing the camera) expanded and exaggerated, and their far side (facing away
from the camera) will be reduced and seem to be occluded from view.

This effect, while it can produce a very convincing representation of 3D
geometry, is still limited to the surface of the flat polygons of an object’s
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). This means that while surface bumps
will appear to protrude and occlude each other, the “silhouette” of the model
will never be modified, because ultimately the effect is drawn onto the
surface of the model and does not modify the actual geometry.

A heightmap should be a greyscale image, with white areas representing the
high areas of your texture and black representing the low areas. Here’s a
typical albedo map and a heightmap to match.

![An albedo colour map, and a heightmap to
match.](../uploads/Main/StandardShaderHeightmapTexture.jpg) An albedo colour
map, and a heightmap to match.
![](../uploads/Main/StandardShaderParallaxMap.jpg)

From left to right in the above image: 1\. A rocky wall material with albedo
assigned, but no normalmap or heightmap. 2\. The normal assigned. Lighting is
modified on the surface, but rocks do not occlude each other. 3\. The final
effect with normalmap and heightmap assigned. The rocks appear to protrude out
from the surface, and nearer rocks seem to occlude rocks behind them.

Often (but not always) the greyscale image used for a heightmap is also a good
image to use for the occlusion map. For information on occlusion maps, see the
next section.

* * *

[](StandardShaderMaterialParameterNormalMapImport.html)

Import a normal map

[](StandardShaderMaterialParameterOcclusionMap.html)

Occlusion maps

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

