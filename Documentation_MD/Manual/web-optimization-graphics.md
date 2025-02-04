[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-optimization-graphics.html)
  * [中文](/cn/current/Manual/web-optimization-graphics.html)
  * [日本語](/ja/current/Manual/web-optimization-graphics.html)
  * [한국어](/kr/current/Manual/web-optimization-graphics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-optimization-graphics.html)
  * [中文](/cn/current/Manual/web-optimization-graphics.html)
  * [日本語](/ja/current/Manual/web-optimization-graphics.html)
  * [한국어](/kr/current/Manual/web-optimization-graphics.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Optimize your Web build](web-optimization.html)
  * Recommended Graphics settings to optimize your Web build

[](web-optimization.html)

Optimize your Web build

[](web-optimization-player.html)

Recommended Player settings to optimize your Web build

# Recommended Graphics settings to optimize your Web build

Use the following recommended **Graphics** settings to optimize your builds
for the Unity Web platform.

Find these settings under **Edit** > **Project Settings** > **Graphics**. For
more information on each setting, refer to the details in [Graphics](class-
GraphicsSettings.html).

**Setting** | **Recommended setting** | **Description**  
---|---|---  
Lightmap modes | Automatic (default) | Automatically strip variants that aren’t used.  
Fog modes | Automatic (default) | Automatically strip variants that aren’t used.  
Instancing Variants | Strip Unused (default) | Only include a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variant if at least one material uses
that variant.  
BatchRendererGroup Variants | Strip all | Removes all BatchRendererGroup shader variants.  
Always Included Shaders |  | Remove any shaders from this list that aren’t used in your project  
  
## Lightmap Modes

Use the ****Lightmap** A pre-rendered texture that contains the effects of
light sources on static objects in the scene. Lightmaps are overlaid on top of
scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) Modes** setting to change the shader
variant stripping behavior for lightmap-related shaders. For examples of
lightmap-related shader variants, refer to [Graphics](class-
GraphicsSettings.html).

The recommended setting for each of these settings is **Automatic (default)**
, which removes any shader variants that aren’t used in your build. This
setting is useful because if you don’t strip unused shaders, it can increase
build times, file size and memory usage.

## Fog Modes

Use the **Fog Modes** setting to change the shader variant stripping behavior
for shaders that relate to built-in Unity fog effect. For examples of fog
shader variants and more information, refer to [Graphics](class-
GraphicsSettings.html).

The recommended setting is **Automatic (Default)** , which removes unused fog
shaders from your build. It’s best to remove unused shaders because they can
increase build times, file size and memory usage.

## Instancing Variants

Use the **Instancing Variants** setting to change how much Unity should strip
shader variants for GPU instancing. For more information, refer to
[Graphics](class-GraphicsSettings.html).

The recommended setting is **Strip Unused** , which removes any instancing
variant shaders that your project doesn’t use. It’s best to remove unused
shaders because they can increase build times, file size and memory usage.

To keep some unused shaders for future use or for other shaders to reference
them, choose **Keep All** instead.

## Batch renderer group variants

Use the **Batch renderer group variants** setting to change the shader variant
stripping behavior for shaders related to batch renderer groups (BRGs). For
more information about BRGs, refer to [BatchRendererGroup](batch-renderer-
group.html).

If your project doesn’t use BRGs, set **Batch renderer group variants** to
**Strip all** , which removes all BRG shader variants. Unused shaders can
increase build times, file size and memory usage. If your project uses BRGs,
ignore this recommendation.

## Always included shaders

**Always included shaders** is a list of shaders for which Unity includes all
possible variants in every build. If your project doesn’t use any of the
shaders in the list, it’s best to remove them from the list because unused
shaders can increase build times, file size and memory usage.

For more information, refer to [Graphics](class-GraphicsSettings.html).

### Edit the Always included shaders list via C

To change the **Always included shaders** list via script instead, create a
list of shaders you want to have in the list and assign it like this:

    
    
    GraphicsSettings.alwaysIncludedShaders = newShadersList.ToArray();
    

## Additional resources

  * [Graphics](class-GraphicsSettings.html)

  * [Recommended Player settings to optimize your Web build](web-optimization-player.html)

  * [Recommended Quality settings to optimize your Web build](web-optimization-quality.html)

  * [Remove unused resources from your Web build](web-optimization-remove-resources.html)

  * [Optimize your Web build](web-optimization.html)

  * [Optimize Web platform for mobile](web-optimization-mobile.html)

[](web-optimization.html)

Optimize your Web build

[](web-optimization-player.html)

Recommended Player settings to optimize your Web build

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

