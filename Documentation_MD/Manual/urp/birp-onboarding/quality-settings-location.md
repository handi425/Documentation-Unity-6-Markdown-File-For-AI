[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/quality-settings-location.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [中文](/cn/current/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [日本語](/ja/current/Manual/urp/birp-onboarding/quality-settings-location.html)
  * [한국어](/kr/current/Manual/urp/birp-onboarding/quality-settings-location.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Render pipelines](../../render-pipelines.html)
  * [Using the Universal Render Pipeline](../../universal-render-pipeline.html)
  * [Get started with URP](../../urp/introduction-landing.html)
  * [Installing and upgrading URP](../../urp/InstallingAndConfiguringURP.html)
  * [Upgrading from the Built-In Render Pipeline to URP](../../urp/upgrading-from-birp.html)
  * Find Built-In Render Pipeline quality settings in URP

[](../../urp/birp-onboarding/quality-presets.html)

Convert quality settings from the Built-In Render Pipeline to URP

[](../../urp/upgrade-guides.html)

Upgrade URP

# Find Built-In Render Pipeline quality settings in URP

URP splits its quality settings between **Project Settings** A broad
collection of settings which allow you to configure how Physics, Audio,
Networking, Graphics, Input and many other areas of your project behave. [More
info](../../comp-ManagerGroup.html)  
See in [Glossary](../../Glossary.html#ProjectSettings) and the URP Asset to
allow for more versatility in the quality levels your project has. As a
result, some settings that Built-In **Render Pipeline** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](../../render-pipelines.html)  
See in [Glossary](../../Glossary.html#Renderpipeline) (BiRP) listed in the
Project Settings **Quality** section have moved or changed, or no longer
exist.

The following table describes all the settings that the Built-in Renderer
lists in the Project Settings **Quality** section, and where that setting is
now located within URP.

**BiRP Setting** | **URP Setting**  
---|---  
**Rendering** |   
Render Pipeline Asset |  **Project Settings** > **Quality** > **Rendering** > **Render Pipeline Asset**  
Pixel Light Count | In URP, the maximum number of real-time lights per object depends on the render path in use. For more information, refer to [Rendering Path comparison](../rendering-paths-introduction-urp.html).  
  
To set the light count per object, use the following property: **URP Asset** >
**Lighting** > **Additional Lights** > **Per Pixel** > **Per Object Limit**  
Anti-aliasing | There are two types of anti-aliasing in URP: you control Multisample Anti-aliasing (MSAA) in the URP Asset, and other anti-aliasing types on a per camera basis. For more information refer to [Anti-aliasing in the Universal Render Pipeline](./../anti-aliasing.html).  
  
To control MSAA, use the following property:  
  
**URP Asset** > **Quality** > **Anti-aliasing (MSAA)**  
  
To control any other type of anti-aliasing, use the following property on a
per camera basis:  
  
**Camera** > **Rendering** > **Anti-aliasing**  
Real-time Reflection Probes |  **Project Settings** > **Quality** > **Rendering** > **Real-time Reflection Probes**  
Resolution Scaling Fixed DPI Factor | This property remains in the same place in URP. However, URP also supports the use of Upscalers to handle resolution scaling in the URP Asset. For more information on the use of upscalers, refer to [Quality in the URP Asset](../universalrp-asset.html#quality).  
  
To set Resolution Scaling Fixed DPI Factor, use the following property:  
  
**Project Settings** > **Quality** > **Rendering** > **Resolution Scaling
Fixed DPI Factor**  
  
To set resolution scaling in the URP Asset, use the following property:  
  
**URP Asset** > **Quality** > **Render Scale** and **Upscaling Filter**  
VSync Count |  **Project Settings** > **Quality** > **Rendering** > **VSync Count**  
**Textures** |   
Global Mipmap Limit |  **Project Settings** > **Quality** > **Textures** > **Global Mipmap Limit**  
Anisotropic Textures |  **Project Settings** > **Quality** > **Textures** > **Anisotropic Textures**  
Texture Streaming |  **Project Settings** > **Quality** > **Textures** > **Texture Streaming**  
**Particles** |   
**Soft Particles** Particles that create semi-transparent effects like smoke,
fog or fire. Soft particles fade out as they approach an opaque object, to
prevent intersections with the geometry. [More info](../../shader-
StandardParticleShaders.html)  
See in [Glossary](../../Glossary.html#SoftParticles) | To enable soft particles use the **shader** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) keyword `_SOFTPARTICLES_ON`
inside the relevant particle shaders.  
Particle Raycast Budget |  **Project Settings** > **Quality** > **Particles** > **Particle Raycast Budget**  
****Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](../../terrain-UsingTerrains.html)  
See in [Glossary](../../Glossary.html#Terrain)** |   
Billboards Face Camera Position |  **Project Settings** > **Quality** > **Terrain** > **Billboards Face Camera Position**  
Use Legacy Details Distribution |  **Project Settings** > **Quality** > **Terrain** > **Use Legacy Details Distribution**  
**Shadows** |   
Shadowmask Mode |  **Project Settings** > **Quality** > **Shadows** > **Shadowmask Mode**  
Shadows | In URP you can enable shadows from two types of light separately. One is the Main Light of a scene, and the other is all other Additional Lights. To do this, set following properties as necessary:  
  
To enable shadows cast by the Main Light, use the following property:  
  
**URP Asset** > **Lighting** > **Main Light** > **Cast Shadows**  
  
To enable shadows cast by Additional Lights, use the following property:  
  
**URP Asset** > **Lighting** > **Additional Lights** > **Cast Shadows**  
  
**Note** : You no longer select the type of Shadows when you enable shadows.
Instead to use Soft Shadows, enable **URP Asset** > **Shadows** > **Soft
Shadows** and select an appropriate quality level.  
Shadow Resolution | You can set Shadow Resolution separately for the Main Light and Additional Lights. Additional Lights use a Shadow Atlas with three tiers: Low, Medium, and High.  
  
To set the shadow resolution for the Main Light, use the following property:  
  
**URP Asset** > **Lighting** > **Main Light** > **Shadow Resolution**  
  
To set the shadow resolution for Additional Lights, use the following
properties:  
  
**URP Asset** > **Lighting** > **Additional Lights** > **Shadow Atlas
Resolution** and **Shadow Resolution Tiers**  
Shadow Projection | URP only supports Stable Fit Shadow Projection.  
Shadow Distance |  **URP Asset** > **Shadows** > **Max Distance**  
Shadow Near Plane Offset | No equivalent setting, because URP’s shadow system doesn’t use this property.  
Shadow Cascades |  **URP Asset** > **Shadows** > **Cascade Count**  
Cascade Splits | Shadow Cascade Splits are now controlled by a dynamic set of properties based on the Cascade Count. The URP Asset displays a visual representation of the Cascade Splits below the Split values as a bar with multiple segments, with each segment representing the size of a given split.  
  
You can control the size of each Shadow Cascade Split with the following
properties:  
  
**URP Asset** > **Shadows** > **Cascade Count** > **Split 1** , **Split 2** ,
**Split 3** , and **Last Border**  
**Async Asset Upload** |   
Time Slice |  **Project Settings** > **Quality** > **Async Asset Upload** > **Time Slice**  
Buffer Size |  **Project Settings** > **Quality** > **Async Asset Upload** > **Buffer Size**  
Persistent Buffer |  **Project Settings** > **Quality** > **Async Asset Upload** > **Persistent Buffer**  
****Level of Detail** The _Level Of Detail_ (LOD) technique is an optimization
that reduces the number of triangles that Unity has to render for a GameObject
when its distance from the Camera increases. [More
info](../../LevelOfDetail.html)  
See in [Glossary](../../Glossary.html#levelofdetail)** |   
LOD Bias |  **Project Settings** > **Quality** > **Level of Detail** > **LOD Bias**  
Maximum LOD level |  **Project Settings** > **Quality** > **Level of Detail** > **Maximum LOD Level**  
LOD Cross Fade |  **URP Asset** > **Quality** > **LOD Cross Fade**  
  
**Note** : URP offers two options for LOD Cross Fade: Bayer and Blue Noise.
These are both different to Built-In’s use of Dither.  
**Meshes** |   
Skin Weights |  **Project Settings** > **Quality** > **Meshes** > **Skin Weights**  
  
## Additional resources

  * [URP Quality Presets](./quality-presets.html)
  * [URP Asset](./../universalrp-asset.html)
  * [Shadows in URP](./../Shadows-in-URP.html)

[](../../urp/birp-onboarding/quality-presets.html)

Convert quality settings from the Built-In Render Pipeline to URP

[](../../urp/upgrade-guides.html)

Upgrade URP

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

