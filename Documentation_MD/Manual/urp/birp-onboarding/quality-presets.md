[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/birp-onboarding/quality-presets.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/quality-presets.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/quality-presets.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/quality-presets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/birp-onboarding/quality-presets.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/quality-presets.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/quality-presets.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/quality-presets.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Installing and upgrading URP](../../urp/InstallingAndConfiguringURP.html)
  * [Upgrading from the Built-In Render Pipeline to URP](../../urp/upgrading-from-birp.html)
  * Convert quality settings from the Built-In Render Pipeline to URP

[](../../urp/birp-onboarding/birp-light-falloff-in-urp.html)

Change how lights fade to match the Built-In Render Pipeline

[](../../urp/birp-onboarding/quality-settings-location.html)

Find Built-In Render Pipeline quality settings in URP

# Convert quality settings from the Built-In Render Pipeline to URP

This page provides recommended URP graphics [Quality Level](../../class-
QualitySettings.html) settings for **Low** and **High** quality level values.
These settings approximately match the performance of the equivalent **Low**
and **High** default presets in the Built-In **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline).

URP changes the implementation of many features and settings, and as a result
they often have a different performance impact to the Built-In Render Pipeline
equivalent. When you upgrade a project from the Built-In Render Pipeline to
URP, your existing quality levels might provide a different level of
performance, and you might need to update or create new quality levels for
your project. You can use the values on this page as a starting point.

This page is split into the following sections:

  * Project SettingsA broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](../../comp-ManagerGroup.html)  
See in [Glossary](../../Glossary.html#ProjectSettings)

  * URP Asset

> **Note** : In URP, many quality level settings have moved from the Project
> Settings window to the URP Asset. For more information on where to find
> these settings in URP projects, refer to [Built-In Render Pipeline Quality
> Settings Reference](quality-settings-location.html).

## Project Settings

You can change the following settings in [Project Settings](../../class-
QualitySettings.html) under **Project Settings** > **Quality**.

**Setting** | **“Low” preset value** | **“High” preset value**  
---|---|---  
**Rendering** |  |   
Real-time **Reflection Probes** A rendering component that captures a
spherical view of its surroundings in all directions, rather like a camera.
The captured image is then stored as a Cubemap that can be used by objects
with reflective materials. [More info](../../class-ReflectionProbe.html)  
See in [Glossary](../../Glossary.html#ReflectionProbe) | No | Yes  
Resolution Scaling Fixed DPI Factor | 1 | 1  
**VSync** Vertical synchronization (VSync) is a display setting that caps a
game’s frame rate to match the refresh rate of a monitor, to prevent image
tearing.  
See in [Glossary](../../Glossary.html#VSync) Count | Don’t Sync | Every V Blank  
**Textures** |  |   
Global Mipmap Limit | Half Resolution | Full Resolution  
Anisotropic Textures | Disabled | Disabled  
Texture Streaming | No | No  
**Particles** |  |   
Particle Raycast Budget | 16 | 256  
****Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](../../terrain-UsingTerrains.html)  
See in [Glossary](../../Glossary.html#Terrain)** |  |   
**Billboards** A textured 2D object that rotates so that it always faces the
Camera. [More info](../../class-BillboardRenderer.html)  
See in [Glossary](../../Glossary.html#Billboard) Face **Camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) Position | No | Yes  
**Shadows** |  |   
**Shadowmask** A Texture that shares the same UV layout and resolution with
its corresponding lightmap. [More info](../../lighting-mode.html#shadowmask)  
See in [Glossary](../../Glossary.html#Shadowmask) Mode | Shadowmask | **Distance Shadowmask** A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](../../lighting-mode.html#shadowmask)  
See in [Glossary](../../Glossary.html#DistanceShadowmask)  
**Async Asset Upload** |  |   
Time Slice | 2 | 2  
Buffer Size | 16 | 16  
Persistent Buffer | Yes | Yes  
****Level of Detail** The _Level Of Detail_ (LOD) technique is an optimization
that reduces the number of triangles that Unity has to render for a GameObject
when its distance from the Camera increases. [More
info](../../LevelOfDetail.html)  
See in [Glossary](../../Glossary.html#levelofdetail)** |  |   
LOD Bias | 0.4 | 1  
Maximum LOD level | 0 | 0  
**Meshes** |  |   
Skin Weights | 4 Bones | Unlimited  
  
## URP Asset

You can change the following settings inside any [URP Asset](./../universalrp-
asset.html).

**Setting** | **“Low” preset value** | **“High” preset value**  
---|---|---  
**Rendering** |  |   
Depth Texture | No | No  
Opaque Texture | No | No  
Terrain Holes | Yes | Yes  
**Quality** |  |   
**HDR** high dynamic range  
See in [Glossary](../../Glossary.html#HDR) | Yes | Yes  
Anti Aliasing (MSAA) | Disabled | 2x  
Render Scale | 1 | 1  
**Lighting** |  |   
Main Light | Per **Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel) | Per Pixel  
Cast Shadows | No | Yes  
Shadows Resolution | N/A | 2048  
Additional Lights | Disabled | Per Pixel  
Per Object Limit | N/A | 4  
Cast Shadows | N/A | Yes  
Shadow Atlas Resolution | N/A | 2048  
Shadow Resolution Tiers | N/A |   
Low | N/A | 512  
Medium | N/A | 1024  
High | N/A | 2048  
Cookie Atlas Resolution | N/A | 2048  
Cookie Atlas Format | N/A | Color High  
Reflection Probes |  |   
Probe Blending | No | Yes  
Box Projection | No | No  
**Shadows** |  |   
Max Distance | N/A | 50  
Cascade Count | N/A | 3  
Split 1 | N/A | 12.5  
Split 2 | N/A | 33.8  
Last Border | N/A | 3.8  
Working Unit | N/A | Metric  
Depth Bias | N/A | 1  
Normal Bias | N/A | 1  
Soft Shadows | N/A | Yes  
****Post-processing** A process that improves product visuals by applying
filters and effects before the image appears on screen. You can use post-
processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More
info](../../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../../Glossary.html#post-processing)** |  |   
Grading Mode | Low Dynamic Range | Low Dynamic Range  
LUT Size | 16 | 32  
Fast sRGB/Linear Conversion | No | No  
  
## Additional resources

  * [Find Quality Settings in URP](./quality-settings-location.html)
  * [URP Asset](./../universalrp-asset.html)

[](../../urp/birp-onboarding/birp-light-falloff-in-urp.html)

Change how lights fade to match the Built-In Render Pipeline

[](../../urp/birp-onboarding/quality-settings-location.html)

Find Built-In Render Pipeline quality settings in URP

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

