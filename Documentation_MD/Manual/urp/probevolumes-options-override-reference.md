[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-options-override-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-options-override-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-options-override-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-options-override-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-options-override-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-options-override-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-options-override-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-options-override-reference.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Probe Volumes Options Override reference

[](../urp/probevolumes-lighting-panel-reference.html)

Adaptive Probe Volumes panel reference

[](../urp/probevolumes-adjustment-volume-component-reference.html)

Probe Adjustment Volume component reference

# Probe Volumes Options Override reference

Refer to [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues.html)
for more information about using the Probe Volumes Options Override.

**Property** | **Description**  
---|---  
**Normal Bias** | Enable to move the position used by shaded pixels when sampling **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe). The value is in meters. This
affects how sampling is moved along the **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel)’s surface normal.  
**View Bias** | Enable to move the sampling position towards the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) when sampling Light Probes. The
results of **View Bias** vary depending on the camera position. The value is
in meters.  
**Scale Bias with Min Probe Distance** | Scale the **Normal Bias** or **View Bias** so it’s proportional to the spacing between Light Probes in a [brick](probevolumes-concept.html#how-probe-volumes-work).  
**Sampling Noise** | Enable to increase or decrease the amount of noise URP adds to the position used by shaded pixels when sampling Light Probes. This can help [fix seams](probevolumes-troubleshoot-light-leaks.html#fix-seams) between bricks.  
**Animate Sampling Noise** | Enable to animate sampling noise when Temporal Anti-Aliasing (TAA) is enabled. This can make noise patterns less visible.  
**Leak Reduction Mode** | Enable to choose the method Unity uses to reduce leaks. Refer to [Fix light leaks](probevolumes-troubleshoot-light-leaks.html).  
Options:  
• **None** : No leak reduction.  
• **Performance** : The uvw used to sample APV data are warped to try to have
invalid probe not contributing to lighting. This samples APV a single time so
it’s a cheap option but will only work in the simplest cases.  
• **Quality** : This option samples APV between 1 and 3 times to provide the
smoothest result without introducing artifacts. This is as expensive as
Performance mode in the simplest cases, and is better and more expensive in
the most complex cases.  
**Min Valid Dot Product Value** | Enable to make URP reduce a Light Probe’s influence on a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) if the direction towards the
Light Probe is too different to the GameObject’s surface normal direction. The
value is the minimum [dot
product](https://docs.unity3d.com/ScriptReference/Vector3.Dot.html) between
the two directions where URP will reduce the Light Probe’s influence.  
**Intensity Multiplier** | Set the strength of the light contribution from Adaptive Probe Volumes. A value of 0 means Unity doesn’t use the Adaptive Probe Volume data.  
**Sky Occlusion Intensity Multiplier** | Set the strength of the light contribution from sky occlusion data in Adaptive Probe Volumes, if you enable [sky occlusion](probevolumes-skyocclusion.html).  
  
[](../urp/probevolumes-lighting-panel-reference.html)

Adaptive Probe Volumes panel reference

[](../urp/probevolumes-adjustment-volume-component-reference.html)

Probe Adjustment Volume component reference

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

