[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Post-Processing-Color-Curves.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Color-Curves.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Color-Curves.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Color-Curves.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Post-Processing-Color-Curves.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Color-Curves.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Color-Curves.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Color-Curves.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * Color Curves Volume Override reference for URP

[](../urp/Post-Processing-Color-Adjustments.html)

Color Adjustments Volume Override reference for URP

[](../urp/depth-of-field-urp.html)

Depth of Field in URP

# Color Curves Volume Override reference for URP

Grading curves are an advanced way to adjust specific ranges in hue,
saturation, or luminosity. You can adjust the curves in eight available graphs
to achieve effects such as specific hue replacement or desaturating certain
luminosities.

## Properties

**Curve** | **Description**  
---|---  
**Master** | This curve affects the luminance across the whole image. The x-axis of the graph represents input luminance and the y-axis represents output luminance. You can use this to further adjust the appearance of basic attributes such as contrast and brightness across all color channels at the same time.  
**Red** | This curve affects the red channel intensity across the whole image. The x-axis of the graph represents input intensity and the y-axis represents output intensity for the red channel.  
**Green** | This curve affects the green channel intensity across the whole image. The x-axis of the graph represents input intensity and the y-axis represents output intensity for the green channel.  
**Blue** | This curve affects the blue channel intensity across the whole image. The x-axis of the graph represents input intensity and the y-axis represents output intensity for the blue channel.  
**Hue Vs Hue** | This curve shifts the input hue (x-axis) according to the output hue (y-axis). You can use this to fine tune hues of specific ranges or perform color replacement.  
**Hue Vs Sat** | This curve adjusts saturation (y-axis) according to the input hue (x-axis). You can use this to tone down particularly bright areas or create artistic effects such as monochromatic except a single dominant color.  
**Sat Vs Sat** | This curve adjusts saturation (y-axis) according to the input saturation (x-axis). You can use this to fine tune saturation adjustments made with [Color Adjustments](Post-Processing-Color-Adjustments.html).  
**Lum Vs Sat** | This curve adjusts saturation (y-axis) according to the input luminance (x-axis). You can use this to desaturate areas of darkness to provide an interesting visual contrast.  
  
[](../urp/Post-Processing-Color-Adjustments.html)

Color Adjustments Volume Override reference for URP

[](../urp/depth-of-field-urp.html)

Depth of Field in URP

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

