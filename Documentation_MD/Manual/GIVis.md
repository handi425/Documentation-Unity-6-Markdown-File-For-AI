[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/GIVis.html)
  * [中文](/cn/current/Manual/GIVis.html)
  * [日本語](/ja/current/Manual/GIVis.html)
  * [한국어](/kr/current/Manual/GIVis.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/GIVis.html)
  * [中文](/cn/current/Manual/GIVis.html)
  * [日本語](/ja/current/Manual/GIVis.html)
  * [한국어](/kr/current/Manual/GIVis.html)

  * [Lighting](LightingOverview.html)
  * [Lighting reference](lighting-reference.html)
  * Debug Draw Modes for lighting reference

[](class-LightmapParameters.html)

Lightmap Parameters Asset Inspector window reference

[](materials-and-shaders.html)

Materials and shaders

# Debug Draw Modes for lighting reference

The **Scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view has several Debug Draw Modes to
help you understand and debug the lighting in your scene.

Use the [Scene view View Options toolbar](ViewModes.html) to select a Debug
Draw Mode.

If you use the Universal Rendering Pipeline or the High Definition **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), not all the modes appear. You
can use the **Rendering Debugger** window to debug lighting in these
pipelines.

## Lighting

### Contributors / Receivers

![](../uploads/Main/ContributorsReceiversDebugDrawMode.jpg)

The **Contributors / Receivers** mode displays the following colors depending
on whether objects contribute to and receive **global illumination** A group
of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination):

  * Orange means the object doesn’t contribute to global illumination. To change this, use the **Contribute GI** flag in the object’s [Static Editor Flags property](StaticObjects.html).
  * Green means the object receives global illumination from **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). To change this, use the **Receive
Global Illumination** setting in the object’s [Mesh Renderer component](class-
MeshRenderer.html).

  * Blue means the object receives global illumination from **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe). To change this, use the **Receive
Global Illumination** setting in the object’s [Mesh Renderer component](class-
MeshRenderer.html).

Use the [Preferences window](Preferences.html#colors) to customize the colors.

### Shadow Cascades

![](../uploads/Main/ShadCascade4Visualization.png)

The **Shadow Cascades** mode displays a different color for each [shadow
cascade](shadow-cascades.html). The colors match the shadow cascade colors in
the **Shadows** section of the [Quality Settings window](class-
QualitySettings.html#Shadows).

You can use this mode to help you adjust the shadow distance, cascade count
and cascade shadow splits.

This mode uses the **Scene view** An interactive view into the world you are
creating. You use the Scene View to select and position scenery, characters,
cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) far plane instead of the shadow
distance. You might need to reduce the shadow distance if you want to match
the in-game behavior of a **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) with a small far plane distance.

## Global Illumination

The following modes are enabled when you use [Enlighten Realtime Global
Illumination](realtime-gi-using-enlighten.html) or [Baked Global
Illumination](Lightmapping.html).

### Indirect (Realtime Global Illumination only)

![](../uploads/Main/GIVis7.png)

The **Indirect** mode displays the realtime lightmaps generated by
**Enlighten** A lighting system by Geomerics used in Unity for Enlighten
Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination.

### Directionality

![](../uploads/Main/GIVis8.png)

The **Directionality** mode displays the dominant light direction as a color.
Refer to [Directional Mode](LightmappingDirectional.html) for more
information.

### Albedo

![](../uploads/Main/GIVis5.png)

The **Albedo** mode displays the albedo color of materials.

### Emissive

![](../uploads/Main/GIVis6.png)

The **Emissive** mode displays the emissive color of [emissive
materials](lighting-emissive-materials.html).

### UV Charts

![](../uploads/Main/GIVis3.png)

The **UV Charts** mode displays a different color for each UV chart (also
known as a UV island).

You can use this mode to check how lightmaps scale onto geometry. Change the
scale using settings such as **Resolution** in the [Lightmap Parameters
Asset](class-LightmapParameters.html), or the **Scale in Lightmap** property
of individual renderers.

### Systems (Realtime Global Illumination only)

![](../uploads/Main/GIVis4.png)

The **Systems** mode displays a different color for each group of clusters
(systems) that Enlighten Realtime Global Illumination creates to generate
realtime lightmaps.

Refer to [How Enlighten Realtime Global Illumination works](realtime-gi-using-
enlighten.html#how-enlighten-realtime-global-illumination-works) for more
information.

### Clustering (Realtime Global Illumination only)

![](../uploads/Main/GIVis10.png)

The **Clustering** mode displays a different color for each cluster Enlighten
Realtime Global Illumination creates to generate realtime lightmaps.

Large scenes might generate more clusters than Unity can store in memory. To
reduce the number of clusters, use the **Cluster Resolution** setting in the
[Lightmap Parameters Asset](class-LightmapParameters.html) to adjust the ratio
of clusters to geometry.

Refer to [How Enlighten Realtime Global Illumination works](realtime-gi-using-
enlighten.html#how-enlighten-realtime-global-illumination-works) for more
information.

### Lit Clustering (Realtime Global Illumination only)

![](../uploads/Main/GIVis11.png)

The **Lit Clustering** mode displays a different color for each cluster
Enlighten Realtime Global Illumination creates to generate realtime lightmaps,
and applies color from the realtime lightmaps.

### Texel Validity (Baked Global Illumination only)

![](../uploads/Main/GIVis14.png)

The **Texel Validity** mode displays red on a surface if the baked lightmap
texel is invalid. Unity marks a texel as invalid when the lightmapping process
emits rays from the surface and hits mostly backfaces. Unity tries to
interpolate a color for an invalid texel by looking at neighboring valid
texels.

To adjust the threshold for marking texels as invalid, use the **Backface
Tolerance** setting in the [Lightmap Parameters Asset](class-
LightmapParameters.html).

### UV Overlap (Baked Global Illumination only)

![](../uploads/Main/GIVis15.png)

The **UV Overlap** mode displays red if a baked lightmap texel is too close to
a texel in another lightmap chart, which might cause aliasing, pixelation and
other issues. Refer to [Fixing lightmap UV overlap](ProgressiveLightmapper-
UVOverlap.html) for more information.

### Lightmap indices (Baked Global Illumination only)

![](../uploads/Main/LightmapIndicesDebugDrawMode.jpg)

The **Lightmap indices** mode displays a different color for each baked
lightmap.

### Light Overlap (Baked Global Illumination only)

![](../uploads/Main/GIVis13.png)

If you use the [Shadowmask Lighting Mode](lighting-mode.html#shadowmask), the
**Light Overlap** mode displays a light volume as red if the light doesn’t
contribute to the baked shadow mask textures. This means there are more than 4
light volumes that overlap, so the highlighted light has to fall back to fully
baked. Refer to [Light Mode: Shadowmask](lighting-mode.html#shadowmask) for
more information.

### Baked Lightmap (Baked Global Illumination only)

![](../uploads/Main/GIVis9.png)

The **Baked Lightmap** mode displays the lightmaps generated by Baked Global
Illumination.

### Shadowmask (Baked Global Illumination only)

![](../uploads/Main/GIVis12.png)

If you use the [Shadowmask Lighting Mode](lighting-mode.html#shadowmask), the
****Shadowmask** A Texture that shares the same UV layout and resolution with
its corresponding lightmap. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask)** mode displays the baked shadow
mask textures. Refer to [Light Mode: Shadowmask](lighting-
mode.html#shadowmask) for more information.

## Lighting Visualization overlay reference

The properties in the Lighting Visualization overlay depend on the Debug Draw
Mode you select.

Property | Value | Description  
---|---|---  
**Lighting Data** | Select whether Unity uses the current baked lightmaps in the Debug Draw Mode, or temporary lightmaps that Unity rebakes when you update the scene. Refer to [Preview lightmapping](Lightmapping-preview.html) for more information.  
| **Baked** | Use the current baked lightmaps.  
| **Preview** | Use temporary lightmaps that Unity rebakes when you update the scene.  
**Show Lightmap Resolution** | Use a checkerboard pattern to display the resolution of lightmaps. Each check is one **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) in a lightmap.  
**Highlight Back-Facing Geometry** | Display back-facing geometry as purple. Use the [Preferences window](Preferences.html#colors) to change the color.  
**Adjust Lightmap Exposure** | Raise or lower the brightness of the lightmap colors, to help make the range of colors more visible. The default value is 0.  
  
## Additional resources

  * [Lightmapping troubleshooting guide](https://forum.unity.com/threads/lightmapping-troubleshooting-guide.1340936/) on the Unity Forums.

[](class-LightmapParameters.html)

Lightmap Parameters Asset Inspector window reference

[](materials-and-shaders.html)

Materials and shaders

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

