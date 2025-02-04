[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/differences-linear-gamma-color-space.html)
  * [中文](/cn/current/Manual/differences-linear-gamma-color-space.html)
  * [日本語](/ja/current/Manual/differences-linear-gamma-color-space.html)
  * [한국어](/kr/current/Manual/differences-linear-gamma-color-space.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/differences-linear-gamma-color-space.html)
  * [中文](/cn/current/Manual/differences-linear-gamma-color-space.html)
  * [日本語](/ja/current/Manual/differences-linear-gamma-color-space.html)
  * [한국어](/kr/current/Manual/differences-linear-gamma-color-space.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Color](graphics-color.html)
  * [Color spaces](color-spaces-landing.html)
  * Differences between linear and gamma color space

[](color-spaces.html)

Color spaces in Unity

[](gamma-color-space.html)

Gamma color space

# Differences between linear and gamma color space

When using linear rendering, input values to the lighting equations are
different to those in gamma space. This means differing results depending on
the color space. For example, light striking surfaces has differing response
curves, and Image Effects behave differently.

## Light fall-off

The fall-off from distance and normal-based lighting differs in two ways:

  * When rendering in linear mode, the additional gamma correction that is performed makes a light’s radius appear larger.

  * Lighting edges also appear more clearly. This more correctly models lighting intensity fall-off on surfaces.

![Left: Lighting a sphere in linear space. Right: Lighting a sphere in gamma
space](../uploads/Main/LinearRendering-LightingSphereLinearGamma.png) Left:
Lighting a sphere in linear space. Right: Lighting a sphere in gamma space

## Linear intensity response

When you are using gamma rendering, the colors and Textures that are supplied
to a **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) already have gamma correction applied
to them. When they are used in a Shader, the colors of high luminance are
actually brighter than they should be compared to linear lighting. This means
that as light intensity increases, the surface gets brighter in a nonlinear
way. This leads to lighting that can be too bright in many places. It can also
give models and **scenes** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) a washed-out feel. When you are using
linear rendering, the response from the surface remains linear as the light
intensity increases. This leads to much more realistic surface shading and a
much nicer color response from the surface.

The Infinite 3D Head Scan image below demonstrates different light intensities
on a human head model under linear lighting and gamma lighting.

![Infinite 3D Head Scan by Lee Perry-Smith, licensed under a Creative Commons
Attribution 3.0 Unported License \(available from www.ir-
ltd.net\)](../uploads/Main/LinearRendering-Infinite3DHeadScan.jpg) Infinite 3D
Head Scan by Lee Perry-Smith, licensed under a Creative Commons Attribution
3.0 Unported License (available from www.ir-ltd.net)

## Linear and gamma blending

When blending into a framebuffer, the blending occurs in the color space of
the framebuffer.

When you use gamma space rendering, nonlinear colors get blended together.
This is not the mathematically correct way to blend colors, and can give
unexpected results, but it is the only way to do a blend on some graphics
hardware.

When you use linear space rendering, blending occurs in linear color space:
This is mathematically correct and gives precise results.

The image below demonstrates the different types of blending:

![Top: Blending in linear color space produces expected blending
results<br/>Bottom: Blending in gamma color space results in over-saturated
and overly-bright blends](../uploads/Main/LinearRendering-
BlendingLinearGamma.jpg) Top: Blending in linear color space produces expected
blending results  
Bottom: Blending in gamma color space results in over-saturated and overly-
bright blends

[](color-spaces.html)

Color spaces in Unity

[](gamma-color-space.html)

Gamma color space

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

