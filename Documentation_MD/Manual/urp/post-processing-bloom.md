[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/post-processing-bloom.html)
  * [中文](/cn/current/Manual/urp/post-processing-bloom.html)
  * [日本語](/ja/current/Manual/urp/post-processing-bloom.html)
  * [한국어](/kr/current/Manual/urp/post-processing-bloom.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/post-processing-bloom.html)
  * [中文](/cn/current/Manual/urp/post-processing-bloom.html)
  * [日本語](/ja/current/Manual/urp/post-processing-bloom.html)
  * [한국어](/kr/current/Manual/urp/post-processing-bloom.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * Bloom Volume Override reference for URP

[](../urp/EffectList.html)

Post-processing Volume Overrides reference for URP

[](../urp/Post-Processing-Channel-Mixer.html)

Channel Mixer Volume Override reference for URP

# Bloom Volume Override reference for URP

![Scene with Bloom effect turned off.](../../uploads/urp/post-proc/Bloom-
off.png) Scene with Bloom effect turned off. ![Scene with Bloom effect turned
on.](../../uploads/urp/post-proc/Bloom.png) Scene with Bloom effect turned on.

The Bloom effect creates fringes of light extending from the borders of bright
areas in an image. This creates the illusion of extremely bright light
overwhelming the **Camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera).

The Bloom effect also has a **Lens Dirt** feature, which you can use to apply
a full-screen layer of smudges or dust to diffract the Bloom effect.

## Properties

### Bloom

**Property** | **Description**  
---|---  
**Threshold** | Set the gamma space brightness value at which URP applies Bloom. URP does not apply Bloom to any **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) that have a brightness lower than
this value. The minimum value is 0, where nothing is filtered. The default
value is 0.9. There is no maximum value.  
**Intensity** | Set the strength of the Bloom filter, in a range from 0 to 1. The default is 0, which means that the Bloom effect is disabled.  
**Scatter** | Set the radius of the bloom effect in a range from 0 to 1. Higher values give a larger radius. The default value is 0.7.  
**Tint** | Use the color picker to select a color for the Bloom effect to tint to.  
**Clamp** | Set the maximum intensity that Unity uses to calculate Bloom. If pixels in your scene are more intense than this, URP renders them at their current intensity, but uses this intensity value for the purposes of Bloom calculations. The default value is 65472.  
**High Quality Filtering** | Enable this to use high quality sampling and bilinear filtering instead of bicubic filtering. This reduces flickering and improves the overall smoothness but is more resource-intensive and can affect performance.  
  
If you experience performance issues with Bloom, disable this property to
greatly improve performance, especially on lower-end hardware and platforms.  
**Downscale** | Set the initial resolution scale for the effect. The lower this value is, the fewer system resources the initial blur effect consumes.  
  
For best performance, set this value to **Quarter** to significantly reducde
the initial resource cost of Bloom.  
**Max Iterations** | The size of the rendered image determines the number of iterations. Use this setting to define the maximum number of iterations. Decreasing this value reduces processing load and increases performance, especially on mobile devices with high DPI screens. The default value is 6.  
  
### Lens Dirt

**Property** | **Description**  
---|---  
**Texture** | Assign a Texture to apply the effect of dirt (such as smudges or dust) to the lens.  
  
If you have performance issues with Bloom, try a lower resolution Texture so
**Lens Dirt** uses less memory.  
**Intensity** | Set the strength of the **Lens Dirt** effect.  
  
[](../urp/EffectList.html)

Post-processing Volume Overrides reference for URP

[](../urp/Post-Processing-Channel-Mixer.html)

Channel Mixer Volume Override reference for URP

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

