[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/lighting-mode.html)
  * [中文](/cn/current/Manual/lighting-mode.html)
  * [日本語](/ja/current/Manual/lighting-mode.html)
  * [한국어](/kr/current/Manual/lighting-mode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/lighting-mode.html)
  * [中文](/cn/current/Manual/lighting-mode.html)
  * [日本語](/ja/current/Manual/lighting-mode.html)
  * [한국어](/kr/current/Manual/lighting-mode.html)

  * [Lighting](LightingOverview.html)
  * [Light sources](lighting-light-sources.html)
  * [Light components](lighting-light-components.html)
  * [Configuring Light components](lighting-light-components-configuring.html)
  * [Configuring Mixed lights with Lighting Modes](lighting-mode-landing.html)
  * Lighting Mode

[](lighting-mode-landing.html)

Configuring Mixed lights with Lighting Modes

[](lighting-mode-choose.html)

Choose a Lighting Mode

# Lighting Mode

This section describes the effect of the **Lighting Mode** property of a
[Lighting Settings Asset](class-LightingSettings.html).

The Lighting Mode determines the behavior of all Mixed Lights in all
**Scenes** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that use the Lighting Settings Asset.
The available modes are:

  * Baked Indirect combines real-time direct lighting with baked indirect lighting. This mode provides real-time shadows with real-time shadowmaps. This Lighting Mode offers realistic lighting and reasonable shadow fidelity, and is suitable for mid-range hardware.
  * **Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask) combines real-time direct lighting
with baked indirect lighting. It supports baked shadows for distant
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) (with Shadow masks) and blends
them automatically with real-time shadows (Shadow maps). Shadowmask Lighting
Mode is the most realistic and the most resource-intensive Lighting Mode. You
can use Quality Settings to configure its performance and visual fidelity.
This Lighting Mode is suitable for high-end or mid-range hardware.

  * Subtractive provides baked direct and indirect lighting. It renders direct real-time shadows for one Directional Light only. This Lighting Mode doesn’t provide particularly realistic lighting results, and is suitable for stylized art or low-end hardware.

See [render pipeline feature comparison](render-pipelines-feature-
comparison.html) for more information about support for each Lighting Mode
across **render pipelines** A series of operations that take the contents of a
Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline).

## Baked Indirect

When you set a Scene’s Lighting Mode to **Baked Indirect** , Mixed Lights
behave like [Realtime Lights](LightModes-introduction.html#realtime)Light
components whose Mode property is set to Realtime. Unity calculates and
updates the lighting of Realtime Lights every frame at runtime. No Realtime
Lights are precomputed. [More info](LightModes-introduction.html#realtime)  
See in [Glossary](Glossary.html#RealtimeLights), with the additional benefit
of baking indirect lighting into **lightmaps** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). GameObjects lit by Mixed Lights
cast real-time shadows up to the [Shadow Distance](shadow-distance.html) you
define in the Project.

Mixed Lights behave as follows:

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using Light Probes.
    * Shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.

### Shadows and runtime performance

Because all shadows from Mixed Lights are real-time in Baked Indirect Lighting
Mode, this can impact performance. You can reduce this impact by using the
[Shadow Distance](shadow-distance.html) property to limit the distance up to
which Unity draws real-time shadows.

## Shadowmask

Similar to Baked Indirect Lighting Mode, Shadowmask Lighting Mode combines
real-time direct lighting with baked indirect lighting. However, Shadowmask
Lighting Mode differs from Baked Indirect Lighting Mode in the way that it
renders shadows. Shadowmask Lighting Mode makes it possible for Unity to
combine baked and real-time shadows at runtime and render shadows in the far
distance. It does this by using an additional lightmap texture known as a
shadow mask, and by storing additional information in [Light
Probes](LightProbes.html)Light probes store information about how light passes
through space in your scene. A collection of light probes arranged within a
given space can improve lighting on moving objects and static LOD scenery
within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe). Unity generates Shadow masks and
Light Probe occlusion data for baked shadows.

Shadowmask Lighting Mode provides the highest fidelity shadows among all the
Lighting Modes, but has the highest performance cost and memory requirements.
It’s suitable for rendering realistic scenes where distant GameObjects are
visible, such as open worlds, on high-end or mid-range hardware.

Use the Quality Settings panel to set the Shadowmask Mode Unity uses at
runtime.

  * ****Distance Shadowmask** A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](lighting-mode.html#shadowmask)  
See in [Glossary](Glossary.html#DistanceShadowmask)** provides greater
fidelity shadows at a higher performance cost.

  * **Shadowmask** provides lower fidelity shadows at a lower performance cost.

### With the Distance Shadowmask quality setting

When you set a Scene’s Lighting Mode to Shadowmask and your Project uses the
Distance Shadowmask quality setting, Mixed Lights behave as follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using Light Probes.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects using Light Probes, beyond the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Real-time shadows from static GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects, using the shadow mask, beyond the Shadow Distance.

### With the Shadowmask quality setting

When you set a Scene’s Lighting Mode to Shadowmask and your Project uses the
Shadowmask quality setting, Mixed Lights behave as follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using Light Probes.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects using Light Probes, up to and beyond the Shadow Distance.
  * Static GameObjects lit by Mixed Lights receive: 
    * Real-time direct lighting.
    * Baked indirect lighting, using lightmaps.
    * Real-time shadows from dynamic GameObjects, using the shadow map, up to the Shadow Distance.
    * Baked shadows from static GameObjects, using the shadow mask, up to and beyond the Shadow Distance.

### Shadowmask implementation details

At runtime, Unity uses the shadow mask to determine whether a **pixel** The
smallest unit in a computer image. Pixel size depends on your screen
resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) is in shadow or not. The shadow mask
Texture contains occlusion information about **baked lights** Light components
whose Mode property is set to Baked. Unity pre-calculates the illumination
from Baked Lights before runtime, and does not include them in any runtime
lighting calculations. [More info](LightModes-introduction.html#baked)  
See in [Glossary](Glossary.html#BakedLights). It shares the same UV layout and
resolution with its corresponding lightmap. It contains occlusion information
for up to four lights per texel, stored in RGBA format.

If more than four lights overlap, any additional lights fall back to Baked
Lighting. The baking system determines which lights fall back to Baked
Lighting, and this stays consistent across bakes, unless you modify one of the
overlapping lights. Light Probes also receive the same information for up to
four lights.

Unity computes light overlapping independently of shadow receiving objects.
So, an object can get the influence of ten different mixed lights all from the
same Shadowmask/Probe channel, as long as those light **bounding volumes** A
closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](Glossary.html#Boundingvolume) don’t overlap at any point in
space. If some lights overlap then Unity uses more channels. And, if a light
does overlap while all four channels are already in use, that light falls back
to fully baked.

### Shadows and runtime performance

You can use the [Shadow Distance](shadow-distance.html) property to limit the
distance up to which Unity draws real-time shadows.

## Subtractive

In Subtractive Lighting Mode, all Mixed Lights in your Scene provide baked
direct and indirect lighting. Unity bakes shadows cast by static GameObjects
into the lightmaps. In addition to the baked shadows, one Directional Light,
known as the Main Directional Light, provides real-time shadows for dynamic
GameObjects.

Because shadows are baked into the lightmaps, Unity doesn’t have the
information it needs to accurately combine baked and real-time shadows at
runtime. Instead, Unity provides a **Realtime Shadow Color** for reducing the
contribution from the lightmap to create the illusion of a correct blend
between baked and real-time shadows. You can also tweak the color to achieve a
certain artistic style.

Subtractive Lighting Mode is useful on low-end hardware where performance is a
concern, and where you need only one real-time shadow casting light. It
doesn’t provide particularly realistic lighting effects, and is more suitable
for stylized aesthetics, such as cel shading.

Unity automatically chooses the Directional Light in your Scene with the
highest intensity value to be the Main Directional Light.

When you set a Scene’s Lighting Mode to Subtractive, Mixed Lights behave as
follows.

  * Dynamic GameObjects lit by Mixed Lights receive: 
    * real-time direct lighting
    * baked indirect lighting, using Light Probes
    * real-time shadows from dynamic GameObjects that are lit by the Main Directional Light, using the shadow map, up to the Shadow Distance
    * shadows from static GameObjects, using Light Probes
  * Static GameObjects lit by Mixed Lights receive: 
    * baked direct lighting, using lightmaps
    * baked indirect lighting, using lightmaps
    * baked shadows from static GameObjects, using lightmaps
    * real-time shadows from dynamic GameObjects that are lit by the Main Directional Light, using the shadow map, up to the Shadow Distance

[](lighting-mode-landing.html)

Configuring Mixed lights with Lighting Modes

[](lighting-mode-choose.html)

Choose a Lighting Mode

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

