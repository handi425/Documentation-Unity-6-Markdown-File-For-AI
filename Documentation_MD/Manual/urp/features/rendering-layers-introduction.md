[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/rendering-layers-introduction.html)
  * [中文](/cn/current/Manual/urp/features/rendering-layers-introduction.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-layers-introduction.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-layers-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/rendering-layers-introduction.html)
  * [中文](/cn/current/Manual/urp/features/rendering-layers-introduction.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-layers-introduction.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-layers-introduction.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * [Rendering Layers in URP](../../urp/features/rendering-layers.html)
  * Introduction to Rendering Layers in URP

[](../../urp/features/rendering-layers.html)

Rendering Layers in URP

[](../../urp/features/rendering-layers-lights.html)

Enable Rendering Layers for Lights in URP

# Introduction to Rendering Layers in URP

The Rendering Layers feature lets you configure certain Lights to affect only
specific **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject).

For example, in the following illustration, Light `A` affects Sphere `D`, but
not Sphere `C`. Light `B` affects Sphere `C`, but not Sphere `D`.

![Light A affects Sphere D, but not Sphere C. Light B affects Sphere C, but
not Sphere D.](../../../uploads/urp/lighting/rendering-layers/rendering-
layers-example.png) Light A affects Sphere D, but not Sphere C. Light B
affects Sphere C, but not Sphere D.

## Limitations

This feature has the following limitations:

  * Rendering Layers are not supported on OpenGL and OpenGL ES API.

##  Performance

This section contains information related to the impact of Rendering Layers on
performance.

  * Keep the Rendering Layer count as small as possible. Avoid creating Rendering Layers that you don’t use in the project.

  * When using Rendering Layers for decals, increasing the layer count increases the required memory bandwidth and decreases the performance.

  * When using Rendering Layers only for Lights in the Forward **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath), the performance impact
is insignificant.

  * Performance impact grows more significantly when the Rendering Layer count exceeds a multiple of 8. For example: increasing the layer count from 8 to 9 layers has a bigger relative impact than increasing the layer count from 9 to 10 layers.

## Additional resources

  * [How to use Rendering Layers](rendering-layers.html)

[](../../urp/features/rendering-layers.html)

Rendering Layers in URP

[](../../urp/features/rendering-layers-lights.html)

Enable Rendering Layers for Lights in URP

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

