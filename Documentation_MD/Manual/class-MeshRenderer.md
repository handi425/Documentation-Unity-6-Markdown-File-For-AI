[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-MeshRenderer.html)
  * [中文](/cn/current/Manual/class-MeshRenderer.html)
  * [日本語](/ja/current/Manual/class-MeshRenderer.html)
  * [한국어](/kr/current/Manual/class-MeshRenderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-MeshRenderer.html)
  * [中文](/cn/current/Manual/class-MeshRenderer.html)
  * [日本語](/ja/current/Manual/class-MeshRenderer.html)
  * [한국어](/kr/current/Manual/class-MeshRenderer.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Mesh components reference](mesh-components-reference.html)
  * Mesh Renderer component reference

[](mesh-components-reference.html)

Mesh components reference

[](class-SkinnedMeshRenderer.html)

Skinned Mesh Renderer component reference

# Mesh Renderer component reference

[Switch to Scripting](../ScriptReference/MeshRenderer.html "Go to MeshRenderer
page in the Scripting Reference")

A **Mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer component renders a mesh. It
works with a [Mesh Filter](class-MeshFilter.html)A mesh component that takes a
mesh from your assets and passes it to the Mesh Renderer for rendering on the
screen. [More info](class-MeshFilter.html)  
See in [Glossary](Glossary.html#MeshFilter) component on the same
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject); the **Mesh Renderer** renders the
mesh that the Mesh Filter references.

To render a deformable mesh, use a [Skinned Mesh
Renderer](https://docs.unity3d.com/Manual/class-SkinnedMeshRenderer.html)
instead.

In C# code, the [MeshRenderer](../ScriptReference/MeshRenderer.html) class
represents a Mesh Renderer component. The `MeshRenderer` class inherits much
of its functionality from the [Renderer](../ScriptReference/Renderer.html)
class. As such, this component has a lot in common with other components that
inherit from `Renderer`, such as [Line Renderer](class-LineRenderer.html)A
component that takes an array of two or more points in 3D space and draws a
straight line between each one. You can use a single Line Renderer component
to draw anything from a simple straight line to a complex spiral. [More
info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer), and [Trail Renderer](class-
TrailRenderer.html)A visual effect that lets you to make trails behind
GameObjects in the Scene as they move. [More info](class-TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer).

## Mesh Renderer Inspector reference

  * MaterialsAn asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material)  

  * Lighting  

  * Lightmapping  

  * Probes  

  * Ray TracingThe process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](Glossary.html#Raytracing)  

  * Additional Settings

### Materials

![The Materials section](../uploads/Main/mesh-renderer-inspector-
materials.png) The Materials section

The **Materials** section lists all the [materials](class-Material.html) that
this component uses.

**Property** | **Description**  
---|---  
**Size** | The number of elements in the material list.  
  
If you decrease the number of elements, Unity deletes the elements at the end
of the list. If you increase the number of elements, Unity adds new elements
to the end of the list. Unity populates new elements with the same material
that the element at the end of the list uses.  
**Element** | The materials in the list. You can assign a material asset to each element.  
  
By default, Unity orders the list alphabetically based on the name of the
materials. This list is reorderable, and Unity updates the number of the
elements automatically as you change their order.  
  
**Note:** If there are more materials than there are sub-meshes, Unity renders
the last sub-mesh with each of the remaining materials, one on top of the
next. If the materials are not fully opaque, you can layer different materials
and create interesting visual effects. However, fully opaque materials
overwrite previous layers, so any additional opaque materials that Unity
applies to the last sub-mesh negatively affect performance and produce no
benefit.

## Lighting

The **Lighting** section contains properties that relate to lighting.

**Property** | **Description**  
---|---  
**Cast Shadows** | Specify if and how this Renderer casts shadows when a suitable [Light](class-Light.html) shines on it.  
  
This property corresponds to the
[Renderer.shadowCastingMode](../ScriptReference/Renderer-
shadowCastingMode.html) API.  
| **On** | This Renderer casts a shadow when a shadow-casting Light shines on it.  
| **Off** | This Renderer does not cast shadows.  
| **Two-sided** | This Renderer casts two-sided shadows. This means that single-sided objects like a plane or a quad can cast shadows, even if the light source is behind the mesh.  
  
For [Baked Global Illumination](class-LightingSettings.html#MixedLighting) or
Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) to support two-sided shadows, the
material must support [Double Sided Global
Illumination](https://docs.unity3d.com/Manual/class-Material.html).  
| **Shadows Only** | This Renderer casts shadows, but the Renderer itself isn’t visible.  
**Receive Shadows** | Specify if Unity displays shadows cast onto this Renderer.  
  
This property only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
This property corresponds to the
[Renderer.receiveShadows](../ScriptReference/Renderer-receiveShadows.html)
API.  
**Contribute Global Illumination** | Include this Renderer in global illumination calculations, which take place at bake time.  
  
This property only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
Enabling this property enables the Contribute GI flag in the GameObject’s
[Static Editor Flags](StaticObjects.html). It corresponds to the
[StaticEditorFlags.ContributeGI](../ScriptReference/StaticEditorFlags.ContributeGI.html)
API.  
**Receive Global Illumination** | Whether Unity provides global illumination data to this Renderer from baked lightmaps, or from runtime Light Probes.  
  
This property is only editable if you enable **Contribute Global
Illumination**. It only has an effect if you enable [Baked Global
Illumination](class-LightingSettings.html#MixedLighting) or Enlighten
[Realtime Global Illumination](class-LightingSettings.html#RealtimeLighting)
for this scene.  
  
This property corresponds to the
[MeshRenderer.receiveGI](../ScriptReference/MeshRenderer-receiveGI.html) API.  
| **Lightmaps** | Unity provides global illumination data to this Renderer from lightmaps.  
| **Light Probes** | Unity provides global illumination data to this Renderer from [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) in the scene.  
**Prioritize Illumination** | Enable this property to always include this Renderer in Enlighten Realtime Global Illumination calculations. This ensures that the Renderer is affected by distant emissives, even those which are normally excluded from Global Illumination calculations for performance reasons.  
  
This property is visible only if **Contribute GI** is enabled in the
GameObject’s [Static Editor Flags](StaticObjects.html), your project uses the
Built-in Render Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
  
## Lightmapping

The **Lightmapping** section contains properties relating to baked and real-
time **lightmaps** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap).

This section is visible only if only if **Receive**Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination)** is set to **Lightmaps**.

![](../uploads/Main/class-MeshRenderer-1.png) **Property:** | **Function:**  
---|---  
**Scale in Lightmap** | Specify the relative size of the Renderer’s UVs within a lightmap.  
  
A value of 0 results in the Renderer not being lightmapped, but it still
contributes to lighting other Renderers in the Scene. A value greater than 1.0
increases the number of pixels (the lightmap resolution) used for this
Renderer, while a value less than 1.0 decreases it.  
  
You can use this property to optimize lightmaps so that important and detailed
areas are more accurately lit. For example, an isolated building with flat,
dark walls uses a low lightmap scale (less than 1.0) while a collection of
colourful motorcycles displayed close together requires a high scale value.  
  
This property corresponds to the
[MeshRenderer.scaleInLightmap](../ScriptReference/MeshRenderer-
scaleInLightmap.html) API.  
**Stitch Seams** | Enable [Lightmap seam stitching](Lightmapping-SeamStitching.html) for this Renderer.  
  
This property corresponds to the
[MeshRenderer.stitchLightmapSeams](../ScriptReference/MeshRenderer-
stitchLightmapSeams.html) API.  
**Lightmap Parameters** | Choose or create a [Lightmap Parameters](class-LightmapParameters.html) asset for this Renderer.  
**Optimize Realtime UVs** | Determine whether Unity [merges the real-time lightmap UVs](LightingGiUvs.html) for this Renderer.  
  
This property is visible only if your Project uses the Built-in Render
Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
**Max Distance** | Specify the maximum worldspace distance for UV chart simplification in real-time lightmaps. If charts are within this distance, Unity simplifies them.  
  
This property is visible only if your Project uses the Built-in Render
Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
**Max Angle** | Specify the maximum angle in degrees between faces sharing a UV edge in real-time lightmaps. If the angle between the faces is below this value, Unity simplifies the UV charts.  
  
This property is visible only if your Project uses the Built-in Render
Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
**Ignore Normals** | Enable this option to prevent Unity from splitting the UV charts in real-time lightmaps.  
  
This property is visible only if your Project uses the Built-in Render
Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
**Min Chart Size** | Specify the minimum texel size used for a UV chart in real-time lightmaps. If stitching is required, a value of 4 creates a chart of 4x4 texels to store lighting and directionality. If stitching is not required, a value of 2 reduces the texel density and provides better lighting build times and game performance.  
  
This property is visible only if your Project uses the Built-in Render
Pipeline, and Enlighten [Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) is enabled in your scene.  
  
When you’ve baked your lighting data (menu: **Window** > **Rendering** >
**Lighting** > **Generate Lighting** ), this section also shows the baked
lightmaps and real-time lightmaps in the current scene that this Renderer
uses.

![Example of lightmaps that appear in your Scene after
baking.](../uploads/Main/class-MeshRenderer-2.png) Example of lightmaps that
appear in your Scene after baking.

### Probes

The **Probes** section contains properties relating to [Light
Probe](LightProbes.html) and [Reflection Probes](class-ReflectionProbe.html)A
rendering component that captures a spherical view of its surroundings in all
directions, rather like a camera. The captured image is then stored as a
Cubemap that can be used by objects with reflective materials. [More
info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe).

**Property** | **Description**  
---|---  
**Light Probes** | Set how this Renderer receives light from the [Light Probes](LightProbes.html) system.  
  
This property corresponds to the
[Renderer.lightProbeUsage](../ScriptReference/Renderer-lightProbeUsage.html)
API.  
| **Off** | The Renderer doesn’t use any interpolated Light Probes.  
| **Blend Probes** | The Renderer uses one interpolated Light Probe. This is the default value.  
| **Use Proxy Volume** | The Renderer uses a 3D grid of interpolated Light Probes.  
| **Custom Provided** | The Renderer extracts Light Probe shader uniform values from the [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html).  
**Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  
  
This property is only visible when **Light Probes** is set to **Use Proxy
Volume**.  
**Reflection Probes** | Set how the Renderer receives reflections from the [Reflection Probe](class-ReflectionProbe.html) system.  
  
This property corresponds to the
[Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API.  
| **Off** | Disables Reflection Probes. Unity uses a skybox for reflection.  
| **Blend Probes** | Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings.  
| **Blend Probes and Skybox** | Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments.  
| **Simple** | Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes.  
**Anchor Override** | Set the Transform that Unity uses to determine the interpolation position when using the [Light Probe](LightProbes.html) or [Reflection Probe](class-ReflectionProbe.html) systems. By default, this is the centre of the bounding box of the Renderer’s geometry.  
  
This property corresponds to the
[Renderer.probeAnchor](../ScriptReference/Renderer-probeAnchor.html) API.  
  
### Ray Tracing

The Ray Tracing section contains properties that relate to ray tracing
effects.

This section only appears if your graphics card supports ray tracing and you
[upgrade your project to use DirectX 12 in the Player settings
window](GraphicsAPIs.html).

These properties have no effect unless you configure your project in one of
the following ways:

  * You use the High Definition **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (HDRP) and [enable ray
tracing](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-
definition@14.0/manual/Ray-Tracing-Getting-Started.html).

  * You write your own C# script to implement ray tracing effects with [RayTracingShader](../ScriptReference/Rendering.RayTracingShader.html) and [RayTracingAccelerationStructure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html).

**Property:** | **Function:**  
---|---  
**Ray Tracing Mode** | Specify if and how often Unity updates this Renderer during ray tracing. More frequent updates increase rendering time.  
| **Off** | Unity excludes this Renderer from ray tracing calculations. This option causes the Renderer to not appear in ray-traced reflections, for example.  
| **Static** | Unity doesn’t update the [ray tracing acceleration structure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html) if the GameObject’s **Transform** or mesh geometry changes. This means ray tracing effects don’t change at runtime.  
| **Dynamic Transform** | Unity updates the ray tracing acceleration structure if the GameObject’s **Transform** changes, but not if the mesh geometry changes. This is the default value for a Mesh Renderer. If your project uses HDRP, this setting is the same as **Dynamic Geometry** because HDRP rebuilds the acceleration structure every frame.  
| **Dynamic Geometry** | Unity updates the ray tracing acceleration structure every frame with the GameObject’s **Transform** and mesh geometry. This is the default value for a Skinned Mesh Renderer.  
**Procedural Geometry** | Causes Unity to render this Renderer procedurally with an intersection **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) rather than with the mesh in the
**Mesh Filter** component.  
**Acceleration Structure Build Flags** | Specifies whether this Renderer overrides the default build flags you specify when you create a [ray tracing acceleration structure](../ScriptReference/Rendering.RayTracingAccelerationStructure.html).  
  
### Additional Settings

The **Additional Settings** section contains additional properties.

**Property** | **Description**  
---|---  
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
**Note:** not all platforms support motion vectors. See
[SystemInfo.supportsMotionVectors](../ScriptReference/SystemInfo-
supportsMotionVectors.html) for more information.  
  
This property corresponds to the
[Renderer.motionVectorGenerationMode](../ScriptReference/Renderer-
motionVectorGenerationMode.html) API.  
| **Camera Motion Only** | Use only Camera movement to track motion.  
| **Per Object Motion** | Use a specific pass to track motion for this Renderer.  
| **Force No Motion** | Do not track motion.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity’s [occlusion culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) system culls this Renderer
when it is blocked from a Camera’s view by a Static Occluder. Otherwise, the
system does not cull this Renderer when it is blocked from a Camera’s view by
a Static Occluder.  
  
Dynamic Occlusion is enabled by default. Disable it for effects such as
drawing the outline of a character behind a wall.  
  
MeshRenderer

[](mesh-components-reference.html)

Mesh components reference

[](class-SkinnedMeshRenderer.html)

Skinned Mesh Renderer component reference

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

