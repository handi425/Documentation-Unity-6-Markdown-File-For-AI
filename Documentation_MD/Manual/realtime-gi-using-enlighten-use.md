[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/realtime-gi-using-enlighten-use.html)
  * [中文](/cn/current/Manual/realtime-gi-using-enlighten-use.html)
  * [日本語](/ja/current/Manual/realtime-gi-using-enlighten-use.html)
  * [한국어](/kr/current/Manual/realtime-gi-using-enlighten-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/realtime-gi-using-enlighten-use.html)
  * [中文](/cn/current/Manual/realtime-gi-using-enlighten-use.html)
  * [日本語](/ja/current/Manual/realtime-gi-using-enlighten-use.html)
  * [한국어](/kr/current/Manual/realtime-gi-using-enlighten-use.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html)
  * Enable Enlighten Realtime Global Illumination

[](realtime-gi-using-enlighten.html)

Introduction to Realtime Global Illumination using Enlighten

[](realtime-gi-using-enlighten-optimize.html)

Optimize Enlighten Realtime Global Illumination

# Enable Enlighten Realtime Global Illumination

To enable Enlighten Realtime Global Illumination in your Scene, open the
[Lighting window](lighting-window.html) (menu: **Window** > **Rendering** >
**Lighting**) and enable **Realtime Global Illumination**.

To disable the effect of **Realtime GI** on a specific Light, select the Light
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and, in the Light component, set
the **Indirect Multiplier** to 0. This means that the Light doesn’t contribute
any indirect light to the **Scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

To disable **Realtime GI** altogether, open the Lighting window (menu:
**Window** > **Rendering** > **Lighting**) and uncheck **Realtime Global
Illumination**.

For detailed step-by-step advice on using **Enlighten** A lighting system by
Geomerics used in Unity for Enlighten Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination), see the Unity tutorial on
[Precomputed Realtime GI](https://learn.unity.com/project/lighting-
optimization-with-precomputed-realtime-gi).

## Light Probes and Enlighten Realtime Global Illumination

Note that [Light Probes](LightProbes.html)Light probes store information about
how light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) behave differently when you enable
Enlighten Realtime Global Illumination.

In order to react to runtime changes in Scene lighting, they sample lighting
iteratively at runtime.

When you disable Enlighten Realtime Global Illumination in a Scene, Light
Probes only use baked lighting data. This means that they don’t react to
runtime changes in Scene lighting.

## Shadows and Enlighten Realtime Global Illumination

If a Light also casts shadows, Unity renders both dynamic and static
GameObjects in the Scene into the Light’s [shadow map](Shadows.html). The
[Material Shaders](Shaders.html) of both static and dynamic GameObjects sample
this shadow map so that these GameObjects cast real-time shadows onto each
other. The **Shadow Distance** setting determines the maximum distance at
which shadows begin to fade out and disappear entirely, which in turn affects
performance and image quality.

Enlighten Realtime Global Illumination results also include soft shadows,
unless the Scene is very small. These shadows are typically more coarse-
grained than what lightmapping can achieve.

To modify **Shadow Distance** settings, navigate to **Edit** > **Project
Settings** > **Quality** > **Shadows**.

[](realtime-gi-using-enlighten.html)

Introduction to Realtime Global Illumination using Enlighten

[](realtime-gi-using-enlighten-optimize.html)

Optimize Enlighten Realtime Global Illumination

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

