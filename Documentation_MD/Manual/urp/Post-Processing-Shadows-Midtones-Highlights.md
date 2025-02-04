[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Shadows-Midtones-Highlights.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * Shadows Midtones Highlights Volume Override reference for URP

[](../urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)

Add screen space lens flares in URP

[](../urp/Post-Processing-Split-Toning.html)

Split Toning Volume Override reference for URP

# Shadows Midtones Highlights Volume Override reference for URP

The **Shadows Midtones Highlights** effect separately controls the shadows,
midtones, and highlights of the render. Unlike [Lift, Gamma, Gain](Post-
Processing-Lift-Gamma-Gain.html), you can use this effect to precisely define
the tonal range for shadows, midtones, and highlights.

## Properties

**Property** | **Description**  
---|---  
**Shadows** | Use this to control the shadows.Use the trackball to select the color URP should shift the hue of the shadows to.Use the slider to offset the color lightness of the trackball color.  
**Midtones** | Use this to control the midtones.Use the trackball to select the color URP should shift the hue of the midtones to.Use the slider to offset the color lightness of the trackball color.  
**Highlights** | Use this to control the highlights.Use the trackball to select the color URP should shift the hue of the highlights to.Use the slider to offset the color lightness of the trackball color.  
  
### Graph view

This graph shows the overall contribution of the **Shadows** (blue),
**Midtones** (green), and **Highlights** (yellow). This is useful to visualize
the transitions between the tonal regions.

### Shadow Limits

**Property** | **Description**  
---|---  
**Start** | Set the start point of the transition between the shadows and the midtones of the render.  
**End** | Set the end point of the transition between the shadows and the midtones of the render.  
  
### Highlight Limits

**Property** | **Description**  
---|---  
**Start** | Set the start point of the transition between the midtones and the highlights of the render.  
**End** | Set the end point of the transition between the midtones and the highlights of the render.  
  
[](../urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)

Add screen space lens flares in URP

[](../urp/Post-Processing-Split-Toning.html)

Split Toning Volume Override reference for URP

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

