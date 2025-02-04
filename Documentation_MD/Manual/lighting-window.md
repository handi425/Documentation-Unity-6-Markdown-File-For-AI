[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/lighting-window.html)
  * [中文](/cn/current/Manual/lighting-window.html)
  * [日本語](/ja/current/Manual/lighting-window.html)
  * [한국어](/kr/current/Manual/lighting-window.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/lighting-window.html)
  * [中文](/cn/current/Manual/lighting-window.html)
  * [日本語](/ja/current/Manual/lighting-window.html)
  * [한국어](/kr/current/Manual/lighting-window.html)

  * [Lighting](LightingOverview.html)
  * [Lighting reference](lighting-reference.html)
  * Lighting window reference

[](lighting-reference.html)

Lighting reference

[](class-LightingSettings.html)

Lighting Settings Asset Inspector window reference

# Lighting window reference

The Lighting window (menu: **Window** > **Rendering** > **Lighting**) is the
main control point for Unity’s lighting features. You can use the Lighting
window to adjust settings related to the lighting in your Scene, and to
optimise your precomputed lighting data for quality, bake time, and storage
space.

## Related APIs

You can perform many of the functions available in the Lighting window in
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), using the
[LightingSettings](../ScriptReference/LightingSettings.html) and
[Lightmapping](../ScriptReference/Lightmapping.html) APIs.

## Lighting window layout

The Lighting window contains the following elements:

  * The Scene tab
  * The Adaptive Probe Volumes tab \- Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) and High-Definition
Render Pipeline (HDRP) only

  * The Environment tab
  * The Realtime Lightmaps tab
  * The Baked Lightmaps tab
  * The control area, at the bottom of the window

## The Scene tab

The **Scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) tab displays information about the
[Lighting Settings Asset](class-LightingSettings.html) that is assigned to the
active Scene. If no Lighting Settings Asset is assigned to the active Scene,
it displays information about the [default LightingSettings object](class-
LightingSettings.html).

The Scene tab is divided into the following sections:

  * Lighting Settings Asset controls
  * Lighting settings \- Realtime Lighting, Mixed Lighting and Lightmapping settings

### Lighting Settings Asset controls

Use the controls in this section to assign a Lighting Settings Asset to the
active Scene, or to create a new Lighting Settings Asset.

**Property:** | **Function:**  
---|---  
**Lighting Settings** | The Lighting Settings Asset assigned to the active Scene.  
**New Lighting Settings** | Click this button to generate a new Lighting Settings Asset in your Project, and automatically assign the new Lighting Settings Asset to the active Scene.  
  
### Lighting Settings

Use this section to view and edit the properties of the Lighting Settings
Asset or `LightingSettings` object assigned to the current Scene. See
[Lighting Settings Asset](class-LightingSettings.html).

## The Adaptive Probe Volumes tab - URP and HDRP only

The Adaptive Probe Volumes tab contains settings related to Adaptive Probe
Volumes (APV). This tab only appears if you use URP or HDRP in your project.
Refer to the following for more information:

  * [Adaptive Probe Volumes in URP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/manual/probevolumes.html)
  * [Adaptive Probe Volumes in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/probevolumes.html)

## The Environment tab

The Environment tab contains settings related to environmental lighting
effects for the current Scene. The contents depend on the render pipeline that
your Project uses.

The Environment tab is divided into two sections:

  * Environment
  * Other settings

#### Environment

The Environment section contains lighting-related settings and controls that
apply to the environmental lighting in the current scene, such as the Skybox,
diffuse lighting and reflections.

**Property:** | **Function:**  
---|---  
**Skybox Material** | A [Skybox](sky-landing.html) is a Material that appears behind everything else in the Scene to simulate the sky or other distant background. Use this property to choose the Skybox you want to use for the Scene. The default value is the built-in Default Skybox.  
**Sun Source** | Select a Light to use as the sun in your Scene. Unity uses this Light to simulate the effect of sun position and intensity on the Skybox and your Scene. If you set this to **None** , Unity considers the brightest directional light in the Scene the sun. Lights whose **Render Mode** property is set to **Not Important** do not affect the Skybox.   
  
For more information about the **Render Mode** setting, see the Additional
settings section of [Lights](https://docs.unity3d.com/Manual/class-
Light.html).  
**Realtime Shadow Color** | Define the color that Unity uses to render real-time shadows in Subtractive Lighting Mode.  
**Environment Lighting** | This section contains settings that affect [ambient light](lighting-ambient-light.html) in the current Scene.  
**Source** | Use this to define a source color for ambient light in the Scene. The default value is **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox).  
| **Skybox** | Use the colors of the Skybox set in **Skybox Material** to determine the ambient light coming from different angles. This allows for more precise effects than **Gradient**.  
| **Gradient** | Choose separate colors for ambient light from the sky, horizon and ground, and blend smoothly between them.  
| **Color** | Use a flat color for all ambient light.  
**Intensity Multiplier** | Use this to set the brightness of the ambient light in the Scene, defined as a value between 0 and 8. The default value is 1.  
**Environment Reflections** | This section contains global settings for [Reflection Probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) baking, and settings that
affect global reflections.  
**Source** | Use this setting to specify whether you want to use the Skybox for reflection effects, or a Cubemap of your choice. The default value is **Skybox**.  
| **Skybox** | Select this to use the Skybox as the reflection source.  
| **Custom** | Select this to use either a Cubemap asset or a [RenderTexture of type cube](class-RenderTexture.html) for reflections.  
**Resolution** | Use this to set the resolution of the Skybox for reflection purposes. This property is visible only when **Source** is set to **Skybox**.  
**Cubemap** A collection of six square textures that can represent the
reflections in an environment or the skybox drawn behind your geometry. The
six squares form the faces of an imaginary cube that surrounds an object; each
face represents the view along the directions of the world axes (up, down,
left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) | Use this to specify the Cubemap to use for reflection purposes. This property is visible only when **Source** is set to **Cubemap**.  
**Compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) | Use this to define whether or not reflection textures are compressed. The default setting is **Auto**.  
| **Auto** | The reflection texture is compressed if the compression format is suitable.  
| **Uncompressed** | The reflection texture is stored in memory uncompressed.  
| **Compressed** | The texture is compressed.  
**Intensity Multiplier** | The degree to which the reflection source is visible in reflective objects.  
**Bounces** | A reflection bounce occurs when a reflection from one object is then reflected by another object. Use this property to set how many times the Reflection Probes evaluate bounces back and forth between objects. If this is set to 1, then Unity only takes the initial reflection (from the skybox or cube map specified in the **Reflection Source** property) into account.  
  
#### Other Settings

The Other Settings section contains settings for fog, [Halos](class-
Halo.html)The glowing light areas around light sources, used to give the
impression of small dust particles in the air. [More info](class-Halo.html)  
See in [Glossary](Glossary.html#Halo), [Flares](class-Flare.html) and
[Cookies](Cookies.html).

| Property: | Function:  
---|---|---  
**Fog** A post-processing effect that overlays a color onto objects depending
on the distance from the camera. Use this to simulate fog or mist in outdoor
environments, or to hide clipping of objects near the camera’s far clip plane.
[More info](PostProcessingOverview.html)  
See in [Glossary](Glossary.html#Fog) | Enables or disables fog in the Scene. Note that fog is not available with the [Deferred rendering path](RenderingPaths.html).  
| Color | Use the color picker to set the color Unity uses to draw fog in the Scene.  
| Mode | Define the way in which the fogging accumulates with distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).  
| **Linear** | Fog density increases linearly with distance.  
| Start | Set the distance from the Camera at which the fog starts.  
| End | Set the distance from the Camera at which the fog completely obscures Scene **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).  
| **Exponential** | Fog density increases exponentially with distance.  
| Density | Use this to control the density of the fog. The fog appears more dense as the **Density** increases.  
| **Exponential Squared** | Fog density increases faster with distance (exponentially and squared).  
| Density | Use this to control the density of the fog. The fog appears more dense as the **Density** increases.  
**Halo Texture** | Set the Texture you want to use for drawing a [Halo](class-Halo.html) around lights.  
**Halo Strength** | Define the visibility of Halos around Lights, from a value between 0 and 1.  
**Flare Fade Speed** | Define the time (in seconds) over which [lens flares](class-LensFlare.html)A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](class-LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare) fade from view after initially
appearing. This is set to 3 by default.  
**Flare Strength** | Define the visibility of lens flares from lights, from a value between 0 and 1.  
**Spot Cookie** | Set the [Cookie](Cookies.html) texture you want to use for [Spot Lights](Lighting.html). The default is ‘Soft’. To revert to ‘Soft’, select **None**.  
  
## The Realtime Lightmaps tab

The Realtime **Lightmaps** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) tab shows a list of all lightmaps
generated by the **Enlighten** A lighting system by Geomerics used in Unity
for Enlighten Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) system in the current
Scene. If Enlighten Realtime Global Illumination is not enabled in your
Project, this tab will be empty.

## The Baked Lightmaps tab

This tab displays a list of all the lightmaps generated by the
[lightmapper](Lightmappers.html)A tool in Unity that bakes lightmaps according
to the arrangement of lights and geometry in your scene. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) for the current scene, and the
[Lighting Data Asset](LightmapSnapshot.html).

If you [use Scene view Draw Modes to preview lightmapping](Lightmapping-
preview.html), the tab also contains the temporary lightmaps Unity generates
for the preview.

If Baked Global Illumination is not enabled in your Project, the tab is empty.

## Control area

Controls for precomputing lighting data are at the bottom of the Lighting
window.

**Property:** | **Function:**  
---|---  
**GPU Baking Device** | Use this to change the GPU that Unity uses for precomputing lighting data. This property is visible only when you use the [GPU Progressive Lightmapper](progressive-lightmapper.html) backend.  
**GPU Baking Profile** | The profile you select in this property defines how the GPU Lightmapper breaks lightmaps into smaller tiles to reduce GPU memory usage. With the **Automatic** profile selected, Unity chooses the tile size based on the size of the largest lightmap while still aiming for good GPU utilization. **Highest Performance** and **High Performance** profiles force a higher fixed tile size for all lightmaps. **Low Memory Usage** and **Lowest Memory Usage** profiles force a lower fixed tile size for all lightmaps. Small tiles take up less GPU memory at the expense of lower GPU utilization, leading to longer bake times. This property is visible only when you use the [GPU Progressive Lightmapper](progressive-lightmapper.html).  
**Bake on Scene Load** | Set whether Unity automatically generates precomputed lighting data.  
| **Never** | Prevent Unity from automatically generating precomputed lighting data when you open a scene. To generate lighting data manually, select **Generate Lighting**. This is the default mode in a new Unity 6 project.  
| **If Missing Lighting Data** | Enable Unity automatically generating precomputed lighting data when you open a scene, if the data doesn’t exist or is invalid. This is the default mode for a project that was created in Unity 2023.2 or earlier. Refer to [Upgrade to Unity 6](UpgradeGuideUnity6.html) for more information.  
**Generate Lighting** | Select the **Generate Lighting** button to precompute lighting data. This data includes lightmaps for the Baked Global Illumination system, lightmaps for the Enlighten Realtime Global Illumination system, Light Probes, Adaptive Probe Volumes, and Reflection Probes. Edits you make after starting the bake process using the **Generate Lighting** button do not affect baked lighting.  
  
Open the **Generate Lighting** dropdown and select **Bake Probe Volumes** to
bake only the Adaptive Probe Volumes in the scene or Baking Set.  
  
Open the **Generate Lighting** dropdown and select **Bake Reflection Probes**
to bake only the Reflection Probes for all open Scenes.  
  
Open the **Generate Lighting** dropdown and select **Clear Baked Data** to
clear all precomputed lighting data from all open scenes without clearing the
[GI Cache](GICache.html)The cached intermediate files used when Unity
precomputes lighting data. Unity keeps this cache to speed up computation.
[More info](GICache.html)  
See in [Glossary](Glossary.html#GICache).  
  
  
  
* * *

  * [Lighting Settings Asset] added in [2020.1](https://docs.unity3d.com/2020.1/Documentation/Manual/30_search.html?q=newin20201) NewIn20201

[](lighting-reference.html)

Lighting reference

[](class-LightingSettings.html)

Lighting Settings Asset Inspector window reference

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

