[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/light-probes-troubleshooting.html)
  * [中文](/cn/current/Manual/light-probes-troubleshooting.html)
  * [日本語](/ja/current/Manual/light-probes-troubleshooting.html)
  * [한국어](/kr/current/Manual/light-probes-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/light-probes-troubleshooting.html)
  * [中文](/cn/current/Manual/light-probes-troubleshooting.html)
  * [日本語](/ja/current/Manual/light-probes-troubleshooting.html)
  * [한국어](/kr/current/Manual/light-probes-troubleshooting.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)
  * Troubleshooting Light Probes

[](LightProbes-Moving.html)

Move Light Probes at runtime

[](LightProbes-Reference.html)

Light Probes reference

# Troubleshooting Light Probes

## Ringing

Under certain circumstances, Light Probes exhibit an unwanted behaviour called
“ringing”. This often happens when there are significant differences in the
light surrounding a **Light Probe** Light probes store information about how
light passes through space in your scene. A collection of light probes
arranged within a given space can improve lighting on moving objects and
static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe). For example, if you have bright
light on one side of a Light Probe, and no light on the other side, the light
intensity can “overshoot” on the back side. This overshoot causes a light spot
on the back side.

![Example of Light Probe ringing](../uploads/Main/class-LightProbeGroup-
Ringing.png) Example of Light Probe ringing

There are several ways to deal with this:

  * In the **Light Probe Group** A component that enables you to add Light Probes to GameObjects in your scene. [More info](class-LightProbeGroup.html)  
See in [Glossary](Glossary.html#LightProbeGroup) component, enable **Remove
Ringing**. Unity automatically removes the unintended light spots. However,
this generally makes the Light Probes less accurate, and reduces light
contrast, so you must check the visual results.

  * Place in-game obstacles in such a way that players can’t get to a position where they can see the light spot.
  * Avoid baking direct light into Light Probes. Direct light tends to have sharp discontinuities (such as shadow edges), which makes it unsuitable for Light Probes. To only bake indirect light, use [Mixed lighting](https://docs.unity3d.com/Manual/LightMode-Mixed.html).

## Troubleshooting Light Probe placement

Your choice of Light Probe positions must take into account that the lighting
is interpolated between sets of Light Probes. Problems can arise if your Light
Probes don’t adequately cover the changes in lighting across your **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

The example below shows a night-time Scene with two bright street lamps on
either side, and a dark area in the middle. If Light Probes are only placed
near the street lamps, and none in the dark area, the lighting from the lamps
“bleeds” across the dark gap, on moving objects. This is because the lighting
is being interpolated from one bright point to another, with no information
about the dark area in-between.

![This image shows poor Light Probe placement. There are no Light Probes in
the dark area between the two lamps, so the dark area is not included in the
interpolation at all.](../uploads/Main/class-LightProbeGroup-12.png) This
image shows poor Light Probe placement. There are no Light Probes in the dark
area between the two lamps, so the dark area is not included in the
interpolation at all.

If you are using Realtime or Mixed lights, this problem may be less
noticeable, because only the _indirect_ light bleeds across the gap. The
problem is more noticable if you are using fully **baked lights** Light
components whose Mode property is set to Baked. Unity pre-calculates the
illumination from Baked Lights before runtime, and does not include them in
any runtime lighting calculations. [More info](LightModes-
introduction.html#baked)  
See in [Glossary](Glossary.html#BakedLights), because in this situation the
direct light on moving objects is also interpolated from the Light Probes. In
this example Scene, the two lamps are baked, so moving objects get their
direct light from Light Probes. Here you can see the result - a moving object
(the ambulance) remains brightly lit while passing through the dark area,
which is not the desired effect. The yellow wireframe tetrahedron shows that
the interpolation is occurring between one brightly lit end of the street to
the other.

![](../uploads/Main/class-LightProbeGroup-13.png)

This is an undesired effect - the ambulance remains brightly lit while passing
through a dark area, because no Light Probes were placed in the dark area.

To solve this, you should place more Light Probes in the dark area, as shown
below:

![](../uploads/Main/class-LightProbeGroup-14.png)

Now the Scene has Light Probes in the dark area too. As a result, the moving
ambulance takes on the darker lighting as it travels from one side of the
Scene to the other.

![The ambulance now takes on the darker lighting in the centre of the Scene,
as desired.](../uploads/Main/class-LightProbeGroup-15.png) The ambulance now
takes on the darker lighting in the centre of the Scene, as desired.

* * *

[](LightProbes-Moving.html)

Move Light Probes at runtime

[](LightProbes-Reference.html)

Light Probes reference

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

