[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shadow-cascades-implementation-details.html)
  * [中文](/cn/current/Manual/shadow-cascades-implementation-details.html)
  * [日本語](/ja/current/Manual/shadow-cascades-implementation-details.html)
  * [한국어](/kr/current/Manual/shadow-cascades-implementation-details.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shadow-cascades-implementation-details.html)
  * [中文](/cn/current/Manual/shadow-cascades-implementation-details.html)
  * [日本語](/ja/current/Manual/shadow-cascades-implementation-details.html)
  * [한국어](/kr/current/Manual/shadow-cascades-implementation-details.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * [Real-time shadows](shadow-realtime.html)
  * [Shadow cascades](shadow-cascades-landing.html)
  * Implementation details of shadow cascades

[](shadow-cascades-performance.html)

Performance impact of shadow cascades

[](ShadowPerformance.html)

Troubleshooting shadows

# Implementation details of shadow cascades

This page describes the technical implementation details of shadow cascades.

## Perspective aliasing

A directional light typically simulates sunlight, and a single directional
light can illuminate the entire **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). This means that its shadow map covers
a large portion of the Scene, which can lead to a problem called perspective
aliasing. Perspective aliasing means that shadow map **pixels** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) close to the **Camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) look enlarged and chunky compared to
those farther away.

![Shadows in the distance \(A\) have an appropriate resolution, whereas
shadows close to camera \(B\) show perspective
aliasing.](../uploads/Main/DirShadowAliasing.jpg) Shadows in the distance (A)
have an appropriate resolution, whereas shadows close to camera (B) show
perspective aliasing.

Perspective aliasing occurs because different areas of the shadow map are
scaled disproportionately by the camera’s perspective. The shadow map from a
light needs to cover only the part of the Scene visible to the Camera, which
is defined by the Camera’s [view frustum](UnderstandingFrustum.html). If you
imagine a simple case where the directional light comes directly from above,
you can see the relationship between the frustum and the shadow map.

![](../uploads/Main/ShadMapFrustumDiagram.svg)

In this simplified example, the distant end of the frustum is covered by 20
pixels of shadow map, while the near end is covered by only 4 pixels. However,
both ends appear the same size on-screen. The result is that the resolution of
the map is effectively much less for shadow areas that are close to the
camera.

## How shadow cascades work

Perspective aliasing is less noticeable when you use the **Soft Shadows**
option, and when you use a higher resolution for the shadow map. However,
these solutions use more memory and bandwidth while rendering.

When using shadow cascades, Unity splits the frustum area into two zones based
on distance from the camera. The zone at the near end uses a separate shadow
map at a reduced size (but with the same resolution). These staged reductions
in shadow map size are known as cascaded shadow maps (sometimes called
parallel split shadow maps).

![](../uploads/Main/ShadMapCascadeDiagram.svg)

[](shadow-cascades-performance.html)

Performance impact of shadow cascades

[](ShadowPerformance.html)

Troubleshooting shadows

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

