[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ReflectionProbe.html)
  * [中文](/cn/current/Manual/class-ReflectionProbe.html)
  * [日本語](/ja/current/Manual/class-ReflectionProbe.html)
  * [한국어](/kr/current/Manual/class-ReflectionProbe.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ReflectionProbe.html)
  * [中文](/cn/current/Manual/class-ReflectionProbe.html)
  * [日本語](/ja/current/Manual/class-ReflectionProbe.html)
  * [한국어](/kr/current/Manual/class-ReflectionProbe.html)

  * [Lighting](LightingOverview.html)
  * [Reflections](reflections-landing.html)
  * Reflection Probe Inspector window reference

[](AdvancedRefProbe.html)

Troubleshooting reflections

[](urp/lighting-landing.html)

Lighting in URP

# Reflection Probe Inspector window reference

[Switch to Scripting](../ScriptReference/ReflectionProbe.html "Go to
ReflectionProbe page in the Scripting Reference")

**_Property:_** | **_Function:_**  
---|---  
**Type** | Choose whether the probe is for a **Baked** , **Custom** , or **Realtime** setup. If you select **Baked** , the **Reflection Probe** does not capture **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) at runtime that have their
Reflection Probe Static flag disabled. If you want to capture dynamic
GameObjects in a baked Reflection Probe, select **Custom** and enable
**Dynamic Objects**.  
**Dynamic Objects** | (**Custom** type only) Forces objects not marked as **Static** to be baked in to the reflection.  
**Cubemap** A collection of six square textures that can represent the
reflections in an environment or the skybox drawn behind your geometry. The
six squares form the faces of an imaginary cube that surrounds an object; each
face represents the view along the directions of the world axes (up, down,
left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) | (**Custom** type only) Sets a custom [cubemap](class-Cubemap-landing.html) for the probe.  
**Refresh Mode** | (**Realtime** type only) Selects if and how the probe will refresh at runtime. The _On Awake_ option renders the probe only once when it first becomes active. _Every Frame_ renders the probe every frame update, optionally using **Time Slicing** (see below). The **Via Scripting** option refreshes the probe from a user script command rather than an automatic update.  
**Time Slicing** | (**Realtime** type only) How should the probe distribute its updates over time? The options are **All Faces At Once** (spreads update over nine frames), **Individual Faces** (updates over fourteen frames) and **No Time Slicing** (the update happens entirely within one frame). See below for further details.  
**Runtime settings**  
**Importance** | A value that indicates the relative priority of this Reflection Probe for sorting. Unity renders probes with a higher value on top of those with a lower value where an object is in range of more than one probe. This setting also affects **Blending**. Refer to [Using Reflection Probes](UsingReflectionProbes.html) for more information about reflection probe blending.  
**Intensity** | The intensity modifier that is applied to the texture of this probe in its **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).  
**Box Projection** | Check this box to enable projection for reflection UV mappings. If you use the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP), you must also enable
**Box Projection** in the [URP asset](urp/universalrp-asset.html).  
**Box Size** | The size of the probe’s bounding box in which the probe can contribute to reflections. The size is in world space. Also used by **Box Projection**.  
**Box Offset** | The center of the probe’s bounding box in which the probe can contribute to reflections. The offset is relative to the position of the probe. Also used by **Box Projection**.  
**Cubemap capture settings**  
**Resolution** | The resolution of the captured reflection image.  
**HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) | Should High Dynamic Range rendering be enabled for the cubemap? This also determines whether probe data is saved in [OpenEXR](http://www.openexr.com/) or PNG format.  
**Shadow Distance** | Distance at which shadows are drawn when rendering the probe.  
**Clear Flags** | Option to specify how empty background areas of the cubemap will be filled. The options are **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) and **Solid Color**.  
**Background** | Background colour to which the reflection cubemap is cleared before rendering.  
**Culling Mask** Allows you to include or omit objects to be rendered by a
Camera, by Layer.  
See in [Glossary](Glossary.html#CullingMask) | Allows objects on specified layers to be included or excluded in the reflection. See the section about the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s culling mask on the
[Layers](Layers.html)Layers in Unity can be used to selectively opt groups of
GameObjects in or out of certain processes or calculations. This includes
camera rendering, lighting, physics collisions, or custom calculations in your
own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#Layer) page.  
**Use Occlusion Culling** | Should **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) be used when baking the
probe?  
**Clipping Planes** A plane that limits how far or close a camera can see from
its current position. A camera’s viewable range is between the far and near
clipping planes. See far clipping plane and near clipping plane. [More
info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane) | Near and **far clipping planes** The maximum draw distance for a camera. Geometry beyond the plane defined by this value is not rendered. The plane is perpendicular to the camera’s forward (Z) direction.  
See in [Glossary](Glossary.html#Farclippingplane) of the probe’s “camera”.  
  
## Additional resources

  * [Reflections in URP](urp/lighting/reflection-probes.html)
  * [Reflection and refraction in the High-Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Reflection-in-HDRP.html)

ReflectionProbe

[](AdvancedRefProbe.html)

Troubleshooting reflections

[](urp/lighting-landing.html)

Lighting in URP

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

