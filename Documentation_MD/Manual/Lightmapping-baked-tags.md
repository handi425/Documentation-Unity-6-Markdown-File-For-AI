[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Lightmapping-baked-tags.html)
  * [中文](/cn/current/Manual/Lightmapping-baked-tags.html)
  * [日本語](/ja/current/Manual/Lightmapping-baked-tags.html)
  * [한국어](/kr/current/Manual/Lightmapping-baked-tags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Lightmapping-baked-tags.html)
  * [中文](/cn/current/Manual/Lightmapping-baked-tags.html)
  * [日本語](/ja/current/Manual/Lightmapping-baked-tags.html)
  * [한국어](/kr/current/Manual/Lightmapping-baked-tags.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Baking lightmaps before runtime](Lightmapping-baking-before-runtime.html)
  * [Configuring lightmaps and baking](Lightmapping-configure.html)
  * Group GameObjects together in a lightmap with Baked Tags

[](progressive-lightmapper.html)

Select the CPU or GPU for baking

[](Lightmapping-troubleshooting.html)

Troubleshooting baked lightmaps

# Group GameObjects together in a lightmap with Baked Tags

![](../uploads/Main/BakedLightmaps-Merged.png)
![](../uploads/Main/BakedLightmaps-Merged2.png)

The two images above shows two views of the same **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene):

  1. **Top:** Everything is in one atlas because all the **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) have the same **Baked Tag**.

  2. **Bottom:** One GameObject is assigned a different **Baked Tag** , and forced into a second **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap).

[](progressive-lightmapper.html)

Select the CPU or GPU for baking

[](Lightmapping-troubleshooting.html)

Troubleshooting baked lightmaps

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

