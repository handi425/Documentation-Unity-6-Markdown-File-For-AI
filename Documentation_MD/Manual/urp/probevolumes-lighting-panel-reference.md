[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-lighting-panel-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-lighting-panel-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-lighting-panel-reference.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Adaptive Probe Volumes panel reference

[](../urp/probevolumes-inspector-reference.html)

Adaptive Probe Volume Inspector reference

[](../urp/probevolumes-options-override-reference.html)

Probe Volumes Options Override reference

# Adaptive Probe Volumes panel reference

This page explains the properties in the **Adaptive Probe Volumes** panel in
Lighting settings. To open the panel, from the main menu select **Window** >
**Rendering** > **Lighting** > **Adaptive Probe Volumes**.

## Baking

To open Baking Set properties, either select the Baking Set asset in the
Project window, or from the main menu select **Window** > **Rendering** >
**Lighting** > **Adaptive Probe Volumes** tab.

### Baking

**Property** | **Description**  
---|---  
**Baking Mode**  
**Single Scene** | Use only the active scene to calculate the lighting data in Adaptive Probe Volumes.  
**Baking Set** | Use the scenes in this Baking Set to calculate the lighting data in Adaptive Probe Volumes.  
**Current Baking Set** | The current Baking Set asset.  
**Scenes in Baking Set** | Lists the scenes in the current Baking Set.  
**Status** : Indicates whether the scene is loaded.  
**Bake** : When enabled, URP generates lighting for this scene.  
Use **+** and **-** to add or remove a scene from the active Baking Set.  
Use the two-line icon to the left of each scene to drag the scene up or down
in the list.  
  
### Probe Placement

**Property** | **Description**  
---|---  
**Probe Positions**  
**Recalculate** | Recalculate probe positions during baking, to accommodate changes in scene geometry. Refer to [Bake different lighting setups with Lighting Scenarios](probevolumes-bakedifferentlightingsetups) for more information.  
**Don’t Recalculate** | Don’t recalculate probe positions during baking. This keeps the probe positions the same as the last successful bake, which means URP can blend probes in different Lighting Scenarios. Refer to [Bake different lighting setups with Lighting Scenarios](probevolumes-bakedifferentlightingsetups) for more information.  
  
**Min Probe Spacing** |  The minimum distance between probes, in meters. Refer to [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity) for more information.  
**Max Probe Spacing** |  The maximum distance between probes, in meters. Refer to [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity) for more information.  
**Renderer Filter Settings**  
**Layer Mask** | Specify the [Layers](https://docs.unity3d.com/Manual/Layers.html) URP considers when it generates probe positions. Select a Layer to enable or disable it.  
**Min Renderer Size** | The smallest [Renderer](https://docs.unity3d.com/ScriptReference/Renderer.html) size URP considers when it places probes.  
  
### Lighting Scenarios

This section appears only if you enable **Lighting Scenarios** under ****Light
Probe** Light probes store information about how light passes through space in
your scene. A collection of light probes arranged within a given space can
improve lighting on moving objects and static LOD scenery within that space.
[More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) Lighting** in the [URP
Asset](universalrp-asset.html).

**Property** | **Description**  
---|---  
**Scenarios** | Lists the Lighting Scenarios in the Baking Set. To rename a Lighting Scenario, double-click its name.  
| **Active** | Set the currently loaded Lighting Scenario, which URP writes to when you select **Generate Lighting**.  
| **Status** | Indicates the status of the active Lighting Scenario.  
| **Invalid Scenario** | A warning icon appears if the active Lighting Scenario is baked but URP can’t load it anymore, for example if another Lighting Scenario has been baked that caused changes in the probe subdivision.  
| **Not Baked** | An information icon appears if you haven’t baked any lighting data for the active Lighting Scenario.  
| **Not Loaded** | An information icon appears if **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) in the Baking Set aren’t currently
loaded in the Hierarchy window, so URP can’t determine the Lighting Scenario
status.  
  
## Sky Occlusion Settings

**Property** | **Description**  
---|---  
**Sky Occlusion** | Enable [sky occlusion](probevolumes-skyocclusion.html).  
**Samples** | Set the number of samples Unity uses to calculate the light each probe receives from the sky. Higher values increase the accuracy of the sky occlusion data, but increasing baking time. The default value is 2048.  
**Bounces** | Set the number of times Unity bounces light from the sky off objects when calculating the sky occlusion data. Higher values increase the accuracy of the sky occlusion data, but increase baking time. Use higher values if objects block the direct view from probes to the sky. The default value is 2.  
**Albedo Override** | Set the brightness of the single color Unity uses to represent objects the sky light bounces off, instead of the actual color of the objects. Higher values brighten the baked sky occlusion lighting. The default value is 0.6.  
**Sky Direction** | Enable Unity storing and using more accurate data about the directions from probes towards the sky. Refer to [Add dynamic color and shadows from the sky](probevolumes-skyocclusion.html#enable-more-accurate-sky-direction-data) for more information.  
  
## Probe Invalidity Settings

**Property** | **Description**  
---|---  
**Probe Dilation Settings**  
**Enable Dilation** | When enabled, URP replaces data in invalid probes with data from nearby valid probes. Enabled by default. Refer to [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues).  
**Search Radius** | Determine how far from an invalid probe URP searches for valid neighbors. Higher values include more distant probes that might be in different lighting conditions than the invalid probe, resulting in unwanted behaviors such as light leaks.  
**Validity Threshold** | Set the ratio of backfaces a probe samples before URP considers it invalid. Higher values mean URP is more likely to mark a probe invalid.  
**Dilation Iterations** | Set the number of times Unity repeats the dilation calculation. This increases the spread of dilation effect, but increases the time URP needs to calculate probe lighting.  
**Squared Distance Weighting** | Enable weighing the contribution of neighbouring probes by squared distance, rather than linear distance. Probes that are closer to invalid probes will contribute more to the lighting data.  
**Virtual Offset Settings**  
**Enable Virtual Offset** | Enable URP moving the capture point of invalid probes into a valid area. Refer to [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues).  
**Search Distance Multiplier** | Set the length of the sampling ray URP uses to search for valid probe positions. High values might cause unwanted results, such as probe capture points pushing through neighboring geometry.  
**Geometry Bias** | Set how far URP pushes a probe’s capture point out of geometry after one of its sampling rays hits geometry.  
**Ray Origin bias** | Set the distance between a probe’s center and the point URP uses as the origin of each sampling ray. High values might cause unwanted results, such as rays missing nearby occluding geometry.  
**Layer Mask** | Specify which layers URP includes in collision calculations for [Virtual Offset](probevolumes-fixissues.html).  
**Refresh Virtual Offset Debug** | Re-run the virtual offset simulation to preview updated results, without affecting baked data.  
  
### Adaptive Probe Volume Disk Usage

**Property** | **Description**  
---|---  
**Scenario Size** | Indicates how much space on disk is used by the baked Light Probe data.  
**Baking Set Size** | Indicates how much space on disk is used by all the baked Light Probe data for the currently selected Baking Set. This includes the data for all Lighting Scenarios, and the data shared by all Lighting Scenarios.  
  
[](../urp/probevolumes-inspector-reference.html)

Adaptive Probe Volume Inspector reference

[](../urp/probevolumes-options-override-reference.html)

Probe Volumes Options Override reference

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

