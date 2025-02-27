[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [中文](/cn/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [日本語](/ja/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)
  * [한국어](/kr/current/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Prebuilt shaders](shader-built-in-landing.html)
  * [Configuring material properties in prebuilt shaders](shader-built-in-configure-properties.html)
  * [Texture maps](StandardShaderTextureMaps.html)
  * [Normal maps](StandardShaderMaterialParameterNormalMapLanding.html)
  * Introduction to surface normals

[](StandardShaderMaterialParameterNormalMap.html)

Introduction to normal maps (bump mapping)

[](StandardShaderMaterialParameterNormalMapImport.html)

Import a normal map

# Introduction to surface normals

To really explain how [normal
mapping](StandardShaderMaterialParameterNormalMapLanding.html) works, we will
first describe what a “**normal** ” is, and how it is used in real-time
lighting. Perhaps the most basic example would be a model where each surface
polygon is lit simply according to the surface angles relative to the light.
The surface angle can be represented as a line protruding in a perpendicular
direction from the surface, and this direction (which is a vector) relative to
the surface is called a “**surface normal** ”, or simply, a **normal**.

![Two 12-sided cylinders, on the left with flat shading, and on the right with
smoothed shading](../uploads/Main/BumpMap2Cylinders.png) Two 12-sided
cylinders, on the left with flat shading, and on the right with smoothed
shading

In the image above, the left cylinder has basic flat shading, and each polygon
is shaded according to its relative angle to the light source. The lighting on
each polygon is constant across the polygon’s area because the surface is
flat. Here are the same two cylinders, with their wireframe **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) visible:

![Two 12-sided cylinders, on the left with flat shading, and on the right with
smoothed shading](../uploads/Main/BumpMap2CylindersWire.png) Two 12-sided
cylinders, on the left with flat shading, and on the right with smoothed
shading

The model on the right has the same number of polygons as the model on the
left, however the shading appears smooth - the lighting across the polygons
gives the appearance of a curved surface. Why is this? The reason is that the
**surface normal** at each point used for reflecting light gradually varies
across the width of the polygon, so that for any given point on the surface,
the light bounces _as if that surface was curved_ and not the flat constant
polygon that it really is.

Viewed as a 2D diagram, three of the surface polygons around the outside of
the flat-shaded cylinder would look like this:

![Flat shading on three polygons, viewed as a 2D
diagram](../uploads/Main/BumpMapFlatShadingDiagram.svg) Flat shading on three
polygons, viewed as a 2D diagram

The surface normals are represented by the orange arrows. These are the values
used to calculate how light reflects off the surface, so you can see that
light will respond the same across the length of each polygon, because the
surface normals point in the same direction. This gives the “flat shading”,
and is the reason the left cylinder’s polygons appear to have hard edges.

For the smooth shaded cylinder however, the surface normals vary across the
flat polygons, as represented here:

![Smooth shading on three polygons, viewed as a 2D
diagram](../uploads/Main/BumpMapSmoothShadingDiagram.svg) Smooth shading on
three polygons, viewed as a 2D diagram

The normal directions gradually change across the flat polygon surface, so
that the shading across the surface gives the impression of a smooth curve (as
represented by the green line). This does not affect the actual polygonal
nature of the mesh, only how the lighting is calculated on the flat surfaces.
This apparent curved surface is not really present, and viewing the faces at
glancing angles will reveal the true nature of the flat polygons, however from
most viewing angles the cylinder appears to have a smooth curved surface.

Using this basic smooth shading, the data determining the normal direction is
actually only stored **per vertex** , so the changing values across the
surface are interpolated from one vertex to the next. In the diagram above,
the red arrows indicate the stored normal direction at each vertex, and the
orange arrows indicate examples of the interpolated normal directions across
the area of the polygon.

[](StandardShaderMaterialParameterNormalMap.html)

Introduction to normal maps (bump mapping)

[](StandardShaderMaterialParameterNormalMapImport.html)

Import a normal map

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

