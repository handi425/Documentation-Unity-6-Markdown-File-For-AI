[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/HDREmulationScale.html)
  * [中文](/cn/current/Manual/urp/HDREmulationScale.html)
  * [日本語](/ja/current/Manual/urp/HDREmulationScale.html)
  * [한국어](/kr/current/Manual/urp/HDREmulationScale.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/HDREmulationScale.html)
  * [中文](/cn/current/Manual/urp/HDREmulationScale.html)
  * [日本語](/ja/current/Manual/urp/HDREmulationScale.html)
  * [한국어](/kr/current/Manual/urp/HDREmulationScale.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Blend Modes in 2D lighting](../urp/2d-light-blending.html)
  * HDR emulation scale

[](../urp/SecondaryTextures.html)

Add normal map and mask textures to a sprite in URP

[](../urp/2DShadows.html)

Create shadows with Shadow Caster 2D in URP

# HDR emulation scale

All Lights in the 2D lighting system support **HDR** high dynamic range  
See in [Glossary](../Glossary.html#HDR). While a typical RGBA32 color channel
has the range of zero to one, a HDR channel can go beyond one.

![Light RGB\(1,1,1\)](../../uploads/urp/2D/image_32.png) | ![HDR Light RGB\(1,1,1\) + Light RGB\(2,2,2\)](../../uploads/urp/2D/image_33.png)  
---|---  
Light RGB(1,1,1) | HDR Light RGB(1,1,1) + Light RGB(2,2,2)  
  
However, not all platforms natively support HDR textures. HDR Emulation Scale
allows those platforms to use HDR lighting by compressing the number of
expressible colors in exchange for extra intensity range. Scale describes this
extra intensity range. Increasing this value too high may cause undesirable
banding to occur.

Light Intensity scale examples:

![HDR Reference](../../uploads/urp/2D/image_34.png) | ![Light Intensity Scale 1 \(No HDR\)](../../uploads/urp/2D/image_35.png)  
---|---  
HDR Reference | Light Intensity Scale 1 (No HDR)  
![Light Intensity Scale 4](../../uploads/urp/2D/image_36.png) | ![Light Intensity Scale 12](../../uploads/urp/2D/image_37.png)  
Light Intensity Scale 4 | Light Intensity Scale 12  
  
When choosing a value for HDR Emulation Scale, the developer should choose the
combined maximum brightness for the lights in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) as the value.

[](../urp/SecondaryTextures.html)

Add normal map and mask textures to a sprite in URP

[](../urp/2DShadows.html)

Create shadows with Shadow Caster 2D in URP

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

