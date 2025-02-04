[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shadow-distance.html)
  * [中文](/cn/current/Manual/shadow-distance.html)
  * [日本語](/ja/current/Manual/shadow-distance.html)
  * [한국어](/kr/current/Manual/shadow-distance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shadow-distance.html)
  * [中文](/cn/current/Manual/shadow-distance.html)
  * [日本語](/ja/current/Manual/shadow-distance.html)
  * [한국어](/kr/current/Manual/shadow-distance.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * [Real-time shadows](shadow-realtime.html)
  * Set shadow distance in a scene

[](shadow-mapping.html)

Shadow mapping

[](shadow-cascades-landing.html)

Shadow cascades

# Set shadow distance in a scene

Use the **Shadow Distance** property to determine the distance from the
**Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) up to which Unity renders real-time
shadows.

Shadows from **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) become less noticeable the farther
the GameObjects are from the Camera. This is both because the shadows appear
smaller on the screen, and because distant GameObjects are usually not the
focus of attention. You can take advantage of this effect by disabling real-
time shadow rendering for distant GameObjects. This saves on wasted rendering
operations, and can improve runtime performance. Additionally, the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) often looks better without distant
shadows.

If the current Camera Far Plane is closer than the Shadow Distance, Unity uses
the Camera Far Plane instead of the Shadow Distance.

To disguise missing shadows beyond the Shadow Distance, you can use visual
effects such as fog.

## Setting the Shadow Distance

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), set the Shadow Distance
property in your Project’s [Quality Settings](class-QualitySettings.html).

In the Universal Render Pipeline (URP), set the Shadow Distance property in
the [Universal Render Pipeline
Asset](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.universal@latest/index.html?subfolder=/manual/universalrp-
asset.html).

In the High Definition Render Pipeline (HDRP), set the Shadow Distance
property for each [Volume](https://docs.unity3d.com/Packages/com.unity.render-
pipelines.high-definition@latest/index.html?subfolder=/manual/Volumes.html).

## Shadow Distance and Shadowmask Lighting Mode

If your Scene uses the [Shadowmask Lighting Mode](lighting-mode.html#baked-
indirect), Unity renders shadows from [Mixed Lights](lighting-mode-
landing.html)Light components whose Mode property is set to Mixed. Some
calculations for Mixed Lights are performed in advance, and some calculations
for Mixed Lights are performed at runtime. The behavior of all Mixed Lights in
a Scene is determined by the Scene’s Lighting Mode. [More info](LightModes-
landing.html)  
See in [Glossary](Glossary.html#MixedLights) beyond the Shadow Distance, using
either [Light Probes](LightProbes.html)Light probes store information about
how light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) or a shadow mask Texture. You can
configure how Unity renders shadows beyond the Shadow Distance.

[](shadow-mapping.html)

Shadow mapping

[](shadow-cascades-landing.html)

Shadow cascades

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

