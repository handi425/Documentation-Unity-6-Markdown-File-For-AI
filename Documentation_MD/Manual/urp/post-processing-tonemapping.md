[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing-tonemapping.html)
  * [中文](/cn/current/Manual/urp/post-processing-tonemapping.html)
  * [日本語](/ja/current/Manual/urp/post-processing-tonemapping.html)
  * [한국어](/kr/current/Manual/urp/post-processing-tonemapping.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing-tonemapping.html)
  * [中文](/cn/current/Manual/urp/post-processing-tonemapping.html)
  * [日本語](/ja/current/Manual/urp/post-processing-tonemapping.html)
  * [한국어](/kr/current/Manual/urp/post-processing-tonemapping.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * Tonemapping Volume Override reference for URP

[](../urp/Post-Processing-Split-Toning.html)

Split Toning Volume Override reference for URP

[](../urp/post-processing-vignette.html)

Vignette Volume Override reference for URP

# Tonemapping Volume Override reference for URP

Tonemapping is the process of remapping the **HDR** high dynamic range  
See in [Glossary](../Glossary.html#HDR) values of an image to a new range of
values. Its most common purpose is to make an image with a low dynamic range
appear to have a higher range. For more information, refer to the [Wikipedia
article on Tone mapping](https://en.wikipedia.org/wiki/Tone_mapping).

## Properties

**Property** | **Description**  
---|---  
**Mode** | Select a tonemapping algorithm to use for color grading. The options are:

  * **None** : Use this option if you do not want to apply tonemapping.
  * **Neutral** : Use this option if you only want range-remapping with minimal impact on color hue & saturation. It is generally a good starting point for extensive color grading.
  * **ACES** : Use this option to apply a close approximation of the reference ACES tonemapper, for a more cinematic look. It is more contrasted than Neutral, and has an effect on actual color hue & saturation. If you use this tonemapper, Unity does all the grading operations in the ACES color spaces, for optimal precision and results.  
**Note** : ACES HDR tonemapping is not supported on Android devices with
Adreno 300 series GPU.

  
  
## HDR Output

When [HDR Output](post-processing/hdr-in-urp.html) is enabled, additional
properties become available for the **Tonemapping** The process of remapping
HDR values of an image into a range suitable to be displayed on screen. [More
info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#Tonemapping) Volume Override. The available
properties vary depending on the **Mode** property.

### Neutral

Property | Description  
---|---  
**Neutral HDR Range Reduction Mode** | The curve that the Player uses for tone mapping. The options are:

  * **BT2390** : The default. Defined by the [BT.2390](https://www.itu.int/pub/R-REP-BT.2390) broadcasting recommendations.
  * **Reinhard** : A simple Tone Mapping operator.

This option is only available when you enable **Advanced Properties**.  
**Hue Shift Amount** | The value determines the extent to which your content retains its original hue after you apply HDR settings. When this value is 0, the tonemapper attempts to preserve the hue of your content as much as possible by only tonemapping luminance.  
**Detect Paper White** | Enable this property if you want URP to use the Paper White value that the display communicates to the Unity Engine. In some cases, the value the display communicates may not be accurate. Implement a calibration menu for your application so that users can display your content correctly on displays that communicate inaccurate values.  
**Paper White** | The Paper White value of the display. If you do not enable **Detect Paper White** , you must specify a value here.  
**Detect Brightness Limits** | Enable this property if you want URP to use the minimum and maximum nit values that the display communicates. In some cases, the value the display communicates may not be accurate. It is best practice to implement a calibration menu for your application to allow for these situations.  
**Min Nits** | The minimum brightness value of the display. If you do not enable **Detect Brightness Limits** , you must specify a value here and in **Max Nits**.  
**Max Nits** | The maximum brightness value of the display. If you do not enable **Detect Brightness Limits** , you must specify a value here and in **Min Nits**.  
  
#### Misuse of Hue Shift Amount

Creators might author some content with the intention to use **Hue Shift
Amount** to produce special effects. In the illustration below, the **Hue
Shift Amount** is 0 for Image A and 1 for Image B. The flames image B appear
more intense because of the hue shift effect. It is preferable not to author
content in this way, because settings optimized for special effects can have
undesirable effects on other content in the **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

![Image A: Output when Hue Shift Amount is 0. Image B: Output when Hue Shift
Amount is 1.](../../uploads/urp/post-proc/hdr/HDR-Output-HueShift.png) Image
A: Output when Hue Shift Amount is 0. Image B: Output when Hue Shift Amount is
1.

### ACES

This mode has fixed presets to target 1000, 2000, and 4000 nit displays. It is
best practice to implement a calibration menu for your application to ensure
that the user can select the right preset.

Property | Description  
---|---  
**ACES Preset** | The tone mapper preset to use. The options are:

  * **ACES 1000 Nits** : The default. This curve targets 1000 nits displays.
  * **ACES 2000 Nits** : Curve that targets 2000 nits displays.
  * **ACES 4000 Nits** : Curve that targets 4000 nits displays.

  
**Detect Paper White** | Enable this property if you want URP to use the Paper White value that the display communicates to the Unity Engine. In some cases, the value the display communicates may not be accurate. Implement a calibration menu for your application so that users can display your content correctly on displays that communicate inaccurate values.  
**Paper White** | The Paper White value of the display. If you do not enable **Detect Paper White** , you must specify a value here.  
  
[](../urp/Post-Processing-Split-Toning.html)

Split Toning Volume Override reference for URP

[](../urp/post-processing-vignette.html)

Vignette Volume Override reference for URP

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

