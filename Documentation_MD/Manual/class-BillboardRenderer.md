[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-BillboardRenderer.html)
  * [中文](/cn/current/Manual/class-BillboardRenderer.html)
  * [日本語](/ja/current/Manual/class-BillboardRenderer.html)
  * [한국어](/kr/current/Manual/class-BillboardRenderer.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-BillboardRenderer.html)
  * [中文](/cn/current/Manual/class-BillboardRenderer.html)
  * [日本語](/ja/current/Manual/class-BillboardRenderer.html)
  * [한국어](/kr/current/Manual/class-BillboardRenderer.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](simplifying-distant-meshes-with-level-of-detail-lod.html)
  * [2D images for low level of detail (LOD)](2d-images-lod.html)
  * Billboard Renderer component reference

[](applying-2d-billboards-low-lod-meshes.html)

Applying 2D billboards for low LOD meshes

[](class-BillboardAsset.html)

Billboard asset reference

# Billboard Renderer component reference

[Switch to Scripting](../ScriptReference/BillboardRenderer.html "Go to
BillboardRenderer page in the Scripting Reference")

Explore the properties and settings in the **Billboard** Renderer component to
customize how Unity renders billboards and their interaction with lighting.

## Properties

Properties on this component are split into the following sections:

  * General
  * Lighting
  * Probes
  * Additional Settings

![](../uploads/Main/BillboardRenderer.png)

### General

This section contains general properties in the root of the component.

**Property:** | **Function:**  
---|---  
**Billboard** | Specifies the [Billboard Asset](class-BillboardAsset.html) this component renders.  
  
### Lighting

The **Lighting** section contains properties that specify how this Billboard
Renderer interacts with lighting in Unity.

**Property:** | **Function:**  
---|---  
**Cast Shadows** | Specify if and how the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) casts shadows when a suitable
[Light](class-Light.html) shines on it.  
| **On** | The Mesh casts a shadow when a shadow-casting Light shines on it.  
| **Off** | The Mesh does not cast shadows.  
| **Two Sided** | The Mesh casts two-sided shadows from either side. **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) and the Progressive
**Lightmapper** A tool in Unity that bakes lightmaps according to the
arrangement of lights and geometry in your scene. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) do not support two-sided shadows.  
| **Shadows Only** | Shadows from the Mesh are visible, but not the Mesh itself.  
**Receive Shadows** | Enable this option to make the Mesh display any shadows that are cast upon it. This is only supported when using the [Progressive Lightmapper](progressive-lightmapper.html).  
  
### Probes

The **Probes** section contains properties relating to Light Probes and
Reflection Probes.

**Property** | **Function**  
---|---  
**Light Probes** | Set how this Renderer receives light from the [Light Probe](LightProbes.html) system.  
  
For more information, see [Light Probes](LightProbes.html)Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).  
| **Off** | The Renderer doesn’t use any interpolated Light Probes.  
| **Blend Probes** | The Renderer uses one interpolated Light Probe. This is the default value.  
| **Use Proxy Volume** | The Renderer uses a 3D grid of interpolated Light Probes.  
| **Custom Provided** | The Renderer extracts Light Probe **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) uniform values from the
[MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html).  
**Proxy Volume Override** | Set a reference to another GameObject that has a Light Probe Proxy Volume component.  
  
This property is only visible when **Light Probes** is set to **Use Proxy
Volume**.  
**Reflection Probes** | Set how the Renderer receives reflections from the [Reflection Probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) system.  
| **Off** | Disables Reflection Probes. Unity uses a **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) for reflection.  
| **Blend Probes** | Enables Reflection Probes. Blending occurs only between Reflection Probes. This is useful in indoor environments where the character may transition between areas with different lighting settings.  
| **Blend Probes and Skybox** | Enables Reflection Probes. Blending occurs between Reflection Probes, or between Reflection Probes and the default reflection. This is useful for outdoor environments.  
| **Simple** | Enables Reflection Probes, but no blending occurs between Reflection Probes when there are two overlapping volumes.  
  
### Additional Settings

This section contains additional rendering properties.

**Property** | **Function**  
---|---  
**Motion Vectors** | Set whether to use motion vectors to track this Renderer’s per-pixel, screen-space motion from one frame to the next. You can use this information to apply post-processing effects such as motion blur.  
  
Note that not all platforms support motion vectors. See
[SystemInfo.supportsMotionVectors](../ScriptReference/SystemInfo-
supportsMotionVectors.html) for more information.  
| ****Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) Motion Only** | Use only Camera movement to track motion.  
| **Per Object Motion** | Use a specific pass to track motion for this Renderer.  
| **Force No Motion** | Do not track motion.  
**Dynamic Occlusion** | When **Dynamic Occlusion** is enabled, Unity culls this Renderer when it is blocked from a Camera’s view by a Static Occluder. Dynamic Occlusion is enabled by default.  
  
When **Dynamic Occlusion** is disabled, Unity does not cull this Renderer when
it is blocked from a Camera’s view by a Static Occluder. Disable Dynamic
Occlusion to achieve effects such as drawing the outline of a character behind
a wall.  
  
See documentation on [occlusion culling](OcclusionCulling.html)A process that
disables rendering GameObjects that are hidden (occluded) from the view of the
camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) for more information.  
  
BillboardRenderer

[](applying-2d-billboards-low-lod-meshes.html)

Applying 2D billboards for low LOD meshes

[](class-BillboardAsset.html)

Billboard asset reference

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

