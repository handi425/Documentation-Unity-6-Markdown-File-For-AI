[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shader-stripping.html)
  * [中文](/cn/current/Manual/urp/shader-stripping.html)
  * [日本語](/ja/current/Manual/urp/shader-stripping.html)
  * [한국어](/kr/current/Manual/urp/shader-stripping.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shader-stripping.html)
  * [中文](/cn/current/Manual/urp/shader-stripping.html)
  * [日本語](/ja/current/Manual/urp/shader-stripping.html)
  * [한국어](/kr/current/Manual/urp/shader-stripping.html)

  * [Materials and shaders](../materials-and-shaders.html)
  * [Shaders](../Shaders.html)
  * [Shaders in URP](../urp/shaders-in-universalrp.html)
  * Reduce shader variants in URP

[](../urp/shaders-in-universalrp-select.html)

Assign a shader to a material in URP

[](../urp/writing-custom-shaders-urp.html)

Writing custom shaders in URP

# Reduce shader variants in URP

The **shaders** A program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) in the Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) use [shader
keywords](https://docs.unity3d.com/Manual/shader-keywords) to support many
different features, which can mean Unity compiles a lot of [shader
variants](https://docs.unity3d.com/Manual/shader-variants)A verion of a shader
program that Unity generates according to a specific combination of shader
keywords and their status. A Shader object can contain multiple shader
variants. [More info](../shader-variants.html)  
See in [Glossary](../Glossary.html#Shadervariant).

If you disable features in the [URP Asset](universalrp-asset.html), URP
automatically excludes (‘strips’) the related shader variants. This speeds up
builds, and reduces memory usage and file sizes.

For example, if your project doesn’t use shadows for directional lights, by
default Unity still includes variants that support directional light shadows
in your build. If you disable **Cast Shadows** in the URP Asset, URP strips
these variants.

If you want to examine the code that strips shaders in URP, check the
`Editor/ShaderPreprocessor.cs` file. The file uses the
[IPreprocessShaders](https://docs.unity3d.com/ScriptReference/Build.IPreprocessShaders.html)
API.

For more information on stripping shader variants, refer to the following
pages:

  * [Check how many shader variants you have](../shader-how-many-variants.html).
  * [General guidance on shader stripping](../shader-variant-stripping.html), which applies to all render pipelines.

## Check how many shader variants your build has

To log how many variants Unity compiles and strips in total, follow these
steps:

  1. Open the [Graphics settings window](urp-global-settings.html).
  2. In the **Shader Stripping** section, select a logging level other than **Disabled**.
  3. Build your project.
  4. To see the logged information, open the `Editor.log` log file and search for `ShaderStrippingReport`. For the location of `Editor.log`, refer to [log files](../log-files.html).

To log more detailed shader variant information, follow these steps:

  1. Open the [Graphics settings window](urp-global-settings.html).
  2. In the **Additional Shader Stripping Settings** section, select **Export Shader Variants**.
  3. Build your project.
  4. In the folder with your project files, open `Temp/graphics-settings-stripping.json` and `Temp/shader-stripping.json`.

For more information, refer to the following in the Unity User Manual:

  * [Check how many shader variants you have](../shader-how-many-variants.html)
  * [Shader variant stripping](../shader-variant-stripping.html)

## Strip feature shader variants

By default, URP compiles variants where a feature is enabled, and variants
where a feature is disabled.

To reduce the number of variants, you can enable **Strip Unused Variants** in
[URP Graphics settings](urp-global-settings.html) and do the following:

  * Disable a feature in all URP Assets in your build, so URP keeps only variants where the feature is disabled.
  * Enable a feature in all URP Assets in your build, so URP keeps only variants where the feature is enabled.

If you disable the **Strip Unused Variants setting** , URP can’t strip
variants where the feature is disabled. This might increase the number of
variants.

### Disable a feature

To let Unity strip variants related to a feature, make sure you disable it in
all the URP Assets in your build.

Unity includes the following URP Assets in your build:

  * The URP Asset you set as the default render pipeline asset in [Graphics settings](https://docs.unity3d.com/Manual/class-GraphicsSettings.html).
  * Any URP Asset you set as a **Render Pipeline Asset** in a [Quality settings level](https://docs.unity3d.com/Manual/class-QualitySettings.html) you enable for the current build target.

Avoid including URP Assets in your build that use different [rendering
paths](rendering-paths-introduction.html#rendering-path-comparison)The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](../RenderingPaths.html)  
See in [Glossary](../Glossary.html#RenderingPath) because this causes Unity to
create two sets of variants for each keyword.

**Feature** | **How to disable the feature** | **Shader keywords this turns off** | **Rendering Path**  
---|---|---|---  
Accurate G-buffer normals | Disable **Accurate G-buffer normals** in the URP Asset. This has no effect on platforms that use the Vulkan graphics API. | `_GBUFFER_NORMALS_OCT` | Deferred  
Additional lights | In the **URP Asset** , in the **Lighting section** , disable **Additional Lights**. |  `_ADDITIONAL_LIGHTS`, `_ADDITIONAL_LIGHTS_VERTEX` | Forward  
Ambient occlusion | Remove the [Ambient Occlusion](post-processing-ssao.html)A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](../Glossary.html#Ambientocclusion) Renderer Feature in all Renderers that URP Assets use. | `_SCREEN_SPACE_OCCLUSION` | Forward and Deferred  
Decals | Remove the [Decals](renderer-feature-decal.html) Renderer Feature in all Renderers that URP Assets use. |  `_DBUFFER_MRT1`, `_DBUFFER_MRT2`, `_DBUFFER_MRT3`, `_DECAL_NORMAL_BLEND_LOW`, `_DECAL_NORMAL_BLEND_MEDIUM`, `_DECAL_NORMAL_BLEND_HIGH`, `_DECAL_LAYERS` | Forward and Deferred  
Fast sRGB to linear conversion | In the **URP Asset** , in the ****Post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](../PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](../Glossary.html#post-processing)** section, disable **Fast sRGB/Linear conversions**. | `_USE_FAST_SRGB_LINEAR_CONVERSION` | Forward and Deferred  
Holes in **terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](../terrain-UsingTerrains.html)  
See in [Glossary](../Glossary.html#Terrain) | In the **URP Asset** , in the **Rendering** section, disable **Terrain Holes**. | `_ALPHATEST_ON` | Forward  
Light cookies | Remove [Cookie textures](https://docs.unity3d.com/Manual/Cookies.html) from all the lights in your project. | `_LIGHT_COOKIES` | Forward and Deferred  
Rendering Layers for lights | Disable [Rendering Layers for Lights](features/rendering-layers.html). | `_LIGHT_LAYERS` | Forward and Deferred  
**Reflection Probe** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](../class-ReflectionProbe.html)  
See in [Glossary](../Glossary.html#ReflectionProbe) blending | Disable [Probe Blending](../class-ReflectionProbe.html). | `_REFLECTION_PROBE_BLENDING` | Forward and Deferred  
Reflection Probe box projection | Disable [Box Projection](../class-ReflectionProbe.html). | `_REFLECTION_PROBE_BOX_PROJECTION` | Forward and Deferred  
Render Pass | Disable **Native Render** in all Renderers that URP Assets use. | `_RENDER_PASS_ENABLED` | Forward and Deferred  
Shadows from additional lights | In the URP Asset, in the **Additional Lights** section, disable **Cast Shadows**. | `_ADDITIONAL_LIGHT_SHADOWS` | Forward and Deferred  
Shadows from the main light | In the URP Asset, in the **Main Light** section, disable **Cast Shadows**. The keywords Unity removes might depend on your settings. |  `_MAIN_LIGHT_SHADOWS`, `_MAIN_LIGHT_SHADOWS_CASCADE`, `_MAIN_LIGHT_SHADOWS_SCREEN` | Forward and Deferred  
Soft shadows | In the URP Asset, in the **Shadows** section, disable **Soft shadows**. | `_SHADOWS_SOFT` | Forward and Deferred  
  
## Strip post-processing shader variants

Enable **Strip Unused Post Processing Variants** in [URP Graphics
settings](urp-global-settings.html) to strip shader variants for [Volume
Overrides](VolumeOverrides.html) you don’t use.

For example if your project uses only the Bloom effect, URP keeps Bloom
variants but strips all other post-processing variants.

Unity checks for Volume Overrides in all scenes, so you can’t strip variants
by removing a **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) from your build but keeping it in
your project.

**Volume Override removed** | **Shader keywords this turns off**  
---|---  
Bloom |  `_BLOOM_HQ`, `BLOOM_HQ_DIRT`, `_BLOOM_LQ`, `BLOOM_LQ_DIRT`  
Chromatic Aberration | `_CHROMATIC_ABERRATION`  
Film Grain | `_FILM_GRAIN`  
**HDR** high dynamic range  
See in [Glossary](../Glossary.html#HDR) Grading | `_HDR_GRADING`  
Lens Distortion | `_DISTORTION`  
**Tonemapping** The process of remapping HDR values of an image into a range
suitable to be displayed on screen. [More
info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#Tonemapping) |  `_TONEMAP_ACES`, `_TONEMAP_NEUTRAL`, `_TONEMAP_GRADING`  
  
You should also enable **Strip Screen Coord Override Variants** in URP
Graphics settings, unless you override screen coordinates to support post
processing on large numbers of multiple displays (‘cluster’ displays).

## Strip XR and VR shader variants

If you don’t use [XR](https://docs.unity3d.com/Manual/XR.html)An umbrella term
encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality
(MR) applications. Devices supporting these forms of interactive applications
can be referred to as XR devices. [More info](../XR.html)  
See in [Glossary](../Glossary.html#XR) or
[VR](https://docs.unity3d.com/Manual/VROverview.html)Virtual Reality [More
info](../VROverview.html)  
See in [Glossary](../Glossary.html#VR), you can [disable the XR and VR
modules](https://docs.unity3d.com/Documentation/Manual/upm-ui.html). This
allows URP to strip XR and VR related shader variants from its standard
shaders.

## Remove variants if you use a custom Renderer Feature

If you create a [custom Renderer
Feature](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.ScriptableRendererFeature.html),
you can use the
[FilterAttribute](https://docs.unity3d.com/2023.1/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.html)
API to remove shader variants when you enable or disable settings in the [URP
Asset](universalrp-asset.html).

For example, you can do the following:

  1. Use [[SerializeField]](https://docs.unity3d.com/ScriptReference/SerializeField.html) to add a Boolean variable to the custom Renderer Feature and add it as a checkbox in the URP Asset **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector).

  2. Use [ShaderKeywordFilter.RemoveIf](https://docs.unity3d.com/2023.1/Documentation/ScriptReference/ShaderKeywordFilter.RemoveIfAttribute.html) to remove shader variants when you enable the checkbox.

## Additional resources

  * [Troubleshooting shaders](../shader-troubleshooting.html)

[](../urp/shaders-in-universalrp-select.html)

Assign a shader to a material in URP

[](../urp/writing-custom-shaders-urp.html)

Writing custom shaders in URP

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

