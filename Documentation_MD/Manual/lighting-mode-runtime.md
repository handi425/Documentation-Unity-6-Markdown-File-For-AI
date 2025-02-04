[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/lighting-mode-runtime.html)
  * [中文](/cn/current/Manual/lighting-mode-runtime.html)
  * [日本語](/ja/current/Manual/lighting-mode-runtime.html)
  * [한국어](/kr/current/Manual/lighting-mode-runtime.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/lighting-mode-runtime.html)
  * [中文](/cn/current/Manual/lighting-mode-runtime.html)
  * [日本語](/ja/current/Manual/lighting-mode-runtime.html)
  * [한국어](/kr/current/Manual/lighting-mode-runtime.html)

  * [Lighting](LightingOverview.html)
  * [Light sources](lighting-light-sources.html)
  * [Light components](lighting-light-components.html)
  * [Configuring Light components](lighting-light-components-configuring.html)
  * [Configuring Mixed lights with Lighting Modes](lighting-mode-landing.html)
  * Adjust Mixed lights at runtime

[](LightMode-Scene.html)

Set the Lighting Mode of a scene

[](LightingExplorer-landing.html)

Configuring lights with the Light Explorer

# Adjust Mixed lights at runtime

In the Baked Indirect Lighting Mode, you can subtly change the properties of a
Mixed Light at runtime. Changes affect the real-time direct lighting that the
Mixed Light contributes to the **Scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), without affecting the baked indirect
lighting that the Mixed Light contributes to the Scene. This allows you to
combine the benefits of baked indirect lighting with some of the dynamic
capabilities of a Realtime Light. This works especially well in Baked Indirect
Lighting Mode, due to the lack of precomputed shadows.

You must be careful with runtime changes to Light properties, and only make
small changes that don’t cause unrealistic combinations of real-time direct
and baked indirect lighting. For example, if you bake a red Mixed Light into a
**lightmap** A pre-rendered texture that contains the effects of light sources
on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) and then change its color to green
at runtime, the direct lighting is green but the indirect lighting baked into
the lightmap remains red. The same applies to moving a Mixed Light at runtime:
direct lighting follows the Light’s new position, but indirect lighting
remains at the position at which the Light was baked.

This video shows an example of how to slightly modify a Mixed Light without
causing noticeable inconsistencies in the indirect lighting:
<https://youtu.be/XN6ya31gm1I>

[](LightMode-Scene.html)

Set the Lighting Mode of a scene

[](LightingExplorer-landing.html)

Configuring lights with the Light Explorer

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

