[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [中文](/cn/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [中文](/cn/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * [Changing lighting at runtime](../urp/probe-volumes-change-lighting-at-runtime.html)
  * Choose how to change lighting at runtime

[](../urp/probe-volumes-change-lighting-at-runtime.html)

Changing lighting at runtime

[](../urp/probevolumes-bakedifferentlightingsetups.html)

Bake different lighting setups with Lighting Scenarios

# Choose how to change lighting at runtime

You can change how objects use the baked data in Adaptive Probe Volumes, to
create lighting that changes at runtime. For example, you can turn the lights
on and off in a **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene), or change the time of day.

You can use one of the following processes:

  * [Bake different lighting setups with Lighting Scenarios](probevolumes-bakedifferentlightingsetups.html), for example you can bake a Lighting Scenario for each stage in a day-night cycle.
  * [Update light from the sky at runtime with sky occlusion](probevolumes-skyocclusion.html).

Lighting Scenarios have the following advantages:

  * Lighting Scenarios are more accurate. Lighting Scenarios don’t approximate the light from the sky, or the color of objects that light bounces off.
  * Lighting Scenarios store all the lighting in a scene, so you can update light from both the sky and scene lights.

Sky occlusion has the following advantages:

  * Easier to set up. For example, you only need to bake once to set up the data you need for a day-night cycle.
  * Better performance.
  * Faster and smoother transitions, because sky occlusion doesn’t have to blend between different sets of data.

You can use sky occlusion and Lighting Scenarios together. For example, you
can use sky occlusion to update the light from the sky, and Lighting Scenarios
to update the position of the sun or the state of an interior lamp.

[](../urp/probe-volumes-change-lighting-at-runtime.html)

Changing lighting at runtime

[](../urp/probevolumes-bakedifferentlightingsetups.html)

Bake different lighting setups with Lighting Scenarios

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

