[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-concept.html)
  * [中文](/cn/current/Manual/urp/probevolumes-concept.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-concept.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-concept.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-concept.html)
  * [中文](/cn/current/Manual/urp/probevolumes-concept.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-concept.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-concept.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Introduction to Adaptive Probe Volumes

[](../urp/probevolumes.html)

Adaptive Probe Volumes (APV) in URP

[](../urp/probevolumes-use.html)

Use Adaptive Probe Volumes

# Introduction to Adaptive Probe Volumes

An Adaptive Probe Volume is a group of [Light
Probes](https://docs.unity3d.com/Manual/LightProbes.html)Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) that Unity places automatically
based on the geometry density in your **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene), to create baked indirect lighting.
You can use Adaptive Probe Volumes instead of manually placing and configuring
Light Probes.

## Advantages and limitations

**Feature** | **Light Probe Groups** | **Adaptive Probe Volumes**  
---|---|---  
Selection of surrounding probes | Per **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) | Per **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel)  
Optimize memory use with streaming | No | Yes  
Place probes automatically | No | Yes  
Blend between different bakes | No | Yes  
Place probes manually | Yes | No  
  
Adaptive Probe Volumes have the following advantages:

  * Unity samples surrounding probes per-pixel rather than per GameObject. This sampling approach results in better lighting consistency, and fewer seams between adjacent GameObjects.
  * You can adjust Light Probe layouts across a scene, for example using a denser set of Light Probes in an interior area with more detailed lighting or geometry. Refer to [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity.html) for more information.
  * Adaptive Probe Volumes work well if you [work with multiple scenes](https://docs.unity3d.com/Manual/MultiSceneEditing.html). Refer to [Baking Sets](probevolumes-concept.html#baking-sets) for more information.
  * Adaptive Probe Volumes include [streaming](probevolumes-streaming.html) functionality to support large open worlds.
  * You can use Adaptive Probe Volumes to [update light from the sky at runtime with sky occlusion](probevolumes-skyocclusion.html).

![The car model is made up of separate GameObjects. The left scene uses Light
Probe Groups, which use per-object lighting, so each part of the car samples a
single blended probe value. The right scene uses Adaptive Probe Volumes, which
use per-pixel lighting, so each part of the car samples its nearest probes.
This image uses the ArchVizPRO Photostudio URP asset from the Unity Asset
Store.](../../uploads/urp/probe-volumes/probevolumes-per-pixel.jpg)  

Adaptive Probe Volumes have the following limitations:

  * You can’t adjust the locations of Light Probes inside an Adaptive Probe Volume. You can use settings and overrides to try to fix visible artifacts, but it might not be possible to make sure Light Probes follow walls or are at the exact boundary between different lighting areas. Refer to [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues.html) for more information.
  * You can’t convert [Light Probe Groups](https://docs.unity3d.com/Manual/LightProbes.html)A component that enables you to add Light Probes to GameObjects in your scene. [More info](../class-LightProbeGroup.html)  
See in [Glossary](../Glossary.html#LightProbeGroup) into an Adaptive Probe
Volume.

## How Adaptive Probe Volumes work

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) automatically fills
an Adaptive Probe Volume with a 3D structure of ‘bricks’. Each brick contains
64 Light Probes, arranged in a 4 × 4 × 4 grid.

URP uses bricks with different sizes to match the amount of geometry in
different areas of your scene. For example, in areas with more geometry, URP
uses small bricks with a short distance between Light Probes. The Light Probes
capture lighting at a higher resolution, so lighting is more accurate.

The default Light Probe spacing is 1, 3, 9, or 27 m.

![In this screenshot from the Rendering Debugger, the small purple bricks
contain Light Probes spaced 1 meter apart, to capture data from high-geometry
areas. The large blue bricks contain Light Probes spaced 3 meters apart, to
capture data from areas with less geometry.](../../uploads/urp/probe-
volumes/probevolumes-debug-displayprobebricks1.PNG)  

Each pixel of a GameObject samples lighting data from the eight closest Light
Probes around it.

You can do the following:

  * Use the Rendering Debugger to visualize the layout of bricks and Light Probes. Refer to [Display Adaptive Probe Volumes](probevolumes-showandadjust.html).
  * [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity.html).
  * [Add a Volume to your scene](probevolumes-troubleshoot-light-leaks.html#volume) to adjust which Light Probes GameObjects sample.

## Baking Sets

To store lighting from a scene in an Adaptive Probe Volume, the scene must be
part of a Baking Set.

A Baking Set contains the following:

  * One or more scenes, which optionally include Adaptive Probe Volumes.
  * A single collection of settings.

By default, URP uses **Single Scene** mode, and places each scene in its own
Baking Set automatically. However, only one Baking Set can be active at any
time, so if you [work with multiple
scenes](https://docs.unity3d.com/Manual/MultiSceneEditing.html), you must add
these scenes to a single Baking Set if you want to bake them together. Refer
to [Bake multiple scenes together with Baking Sets](probevolumes-
usebakingsets.html) for more information.

### Lighting Scenarios

A Lighting Scenario asset contains the baked lighting data for a scene or
Baking Set. You can bake different lighting setups into different Lighting
Scenario assets, and change which one URP uses at runtime, or blend between
them.

Refer to [Bake different lighting setups with Lighting
Scenarios](probevolumes-bakedifferentlightingsetups.html) for more
information.

#### How Lighting Scenarios store data

Adaptive Probe Volumes splits Lighting Scenario data into two parts, to avoid
duplicating data:

  * The shared data, which contains mainly the scene subdivision information and probe placement.
  * The per scenario data, which contains the probe lighting information.

URP can’t share the data or blend between Lighting Scenarios if you move
geometry between bakes, because the Light Probe positions might change. Refer
to [Keep Light Probes the same in different Lighting Scenarios](probevolumes-
bakedifferentlightingsetups.html#keep-light-probes-the-same-in-different-
lighting-scenarios) for more information.

## Additional resources

  * [Light Probes](https://docs.unity3d.com/Manual/LightProbes.html)
  * [Work with multiple scenes in Unity](https://docs.unity3d.com/Documentation/Manual/MultiSceneEditing.html)

[](../urp/probevolumes.html)

Adaptive Probe Volumes (APV) in URP

[](../urp/probevolumes-use.html)

Use Adaptive Probe Volumes

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

