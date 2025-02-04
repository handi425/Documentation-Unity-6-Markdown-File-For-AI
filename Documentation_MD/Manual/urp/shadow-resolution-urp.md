[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shadow-resolution-urp.html)
  * [中文](/cn/current/Manual/urp/shadow-resolution-urp.html)
  * [日本語](/ja/current/Manual/urp/shadow-resolution-urp.html)
  * [한국어](/kr/current/Manual/urp/shadow-resolution-urp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shadow-resolution-urp.html)
  * [中文](/cn/current/Manual/urp/shadow-resolution-urp.html)
  * [日本語](/ja/current/Manual/urp/shadow-resolution-urp.html)
  * [한국어](/kr/current/Manual/urp/shadow-resolution-urp.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Shadows in URP](../urp/Shadows-in-URP.html)
  * Configure shadow resolution in the Universal Render Pipeline

[](../urp/Shadows-in-URP.html)

Shadows in URP

[](../urp/renderer-feature-screen-space-shadows.html)

Add screen space shadows in URP

# Configure shadow resolution in the Universal Render Pipeline

This page describes how to configure the shadow resolution of the directional
light and the additional lights.

## Set the shadow resolution of the main light

To set the resolution of shadows from the main light, select **URP Asset** >
**Lighting** > **Main Light** > **Shadow Resolution**.

###  Set the maximum distance of the main light shadow

Unity spreads the shadow map over the area defined by the **Max Distance**
property. The higher the value, the lower the pixel density of the shadow map.
Set the **Max Distance** property in **URP Asset** > **Shadows** > **Max
Distance**.

For example, the following illustration shows that reducing the **Max
Distance** value from 40 to 10 lets you use a lower resolution shadow map
(1024 pixels instead of 2048 pixels) and achieve higher shadow quality in the
area close to the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera). Cascade count value is 1.

![A: Max Distance 40, Shadow Resolution 2048. B: Max Distance 10, Shadow
Resolution 1024.](../../uploads/urp/shadows/shadow-max-distance-affects-
resolution.png)  
A: **Max Distance** 40, **Shadow Resolution** 2048\. B: **Max Distance** 10,
**Shadow Resolution** 1024.

##  Set the shadow resolution of additional lights

In URP, point lights and spot lights are called additional lights.

###  Set the size of shadow atlases in URP

Set the size of these atlases in your Unity project’s [URP Asset](universalrp-
asset.html). The atlas size determines the maximum resolution of additional
light shadows in your **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

URP renders all real-time shadows for a frame using one common shadow map
atlas for all spot lights and point lights in your scene, and another shadow
map atlas for directional lights.

For example, an atlas of size 1024 × 1024 can fit:

  * Four shadow maps of 512 × 512 **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel).

  * Sixteen shadow maps of 256 × 256 pixels.

### Control the amount of video memory shadows use

To make sure that the resolution URP uses for a specific additional light
shadow does not get lower than a specific value, consider the number of shadow
maps required in the scene, and select a big enough shadow atlas resolution.

Consider the following example:

  * A scene has four spot lights and one point light.

  * Each shadow map resolution must be at least 256 x 256 pixels.

In this example Unity needs to render ten shadow maps (one for each spot
light, and six for the point light), each with a resolution of 256 x 256
pixels.

A shadow atlas of 512 x 512 pixels would not be enough, because it can contain
only four maps of 256 x 256 pixels. The application requires a shadow atlas of
1024 x 1024 pixels, which can contain up to sixteen maps of 256 x 256 pixels.

## Additional resources

  * [Shadow mapping and performance](../shadow-mapping.html#shadow-mapping-performance)

[](../urp/Shadows-in-URP.html)

Shadows in URP

[](../urp/renderer-feature-screen-space-shadows.html)

Add screen space shadows in URP

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

