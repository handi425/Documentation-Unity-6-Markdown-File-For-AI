[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [中文](/cn/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [中文](/cn/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-troubleshoot-artefacts.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * [Troubleshooting Adaptive Probe Volumes](../urp/probevolumes-fixissues.html)
  * Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-light-probe-validity.html)

Light Probe validity in Adaptive Probe Volumes in URP

[](../urp/probevolumes-troubleshoot-light-leaks.html)

Troubleshooting light leaks in Adaptive Probe Volumes in URP

# Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

Adjust settings or use Volume overrides to fix artefacts from Adaptive Probe
Volumes.

### Adjust Virtual Offset

You can configure **Virtual Offset Settings** in the [Adaptive Probe Volumes
panel](probevolumes-lighting-panel-reference.html) in the Lighting window.
This changes how URP calculates the validity of **Light Probes** Light probes
store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe).

You can adjust the following:

  * The length of the sampling ray Unity uses to find a valid capture point.
  * How far Unity moves a Light Probe’s capture position to avoid geometry.
  * How far Unity moves the start point of rays.
  * How many times a probe’s sampling ray hits **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](../CollidersOverview.html)  
See in [Glossary](../Glossary.html#Collider) before Unity considers the probe
invalid.

You can also disable Virtual Offset for a Baking Set. Virtual Offset only
affects baking time, so disabling Virtual Offset doesn’t affect runtime
performance.

### Adjust Dilation

You can configure **Probe Dilation Settings** in the [Adaptive Probe Volumes
panel](probevolumes-lighting-panel-reference.html) in the Lighting window).
This changes how URP calculates the validity of Light Probes, and how invalid
Light Probes use lighting data from nearby valid Light Probes.

You can adjust the following:

  * The percentage of backfaces a Light Probe can sample before URP considers that probe invalid.
  * How far away from the invalid probe Unity searches for valid probes to contribute lighting data.
  * How many iterations of Dilation URP does during the bake.
  * How to weight the data from valid probes based on their spatial relationship with the invalid probe.

[How you adjust Light Probe density](probevolumes-changedensity.html) affects
the final results, because URP uses the settings as a multiplier to calculate
the distance between probes.

You can also disable Dilation for a Baking Set. Dilation only affects baking
time, so disabling Dilation doesn’t affect runtime performance.

[](../urp/probevolumes-light-probe-validity.html)

Light Probe validity in Adaptive Probe Volumes in URP

[](../urp/probevolumes-troubleshoot-light-leaks.html)

Troubleshooting light leaks in Adaptive Probe Volumes in URP

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

