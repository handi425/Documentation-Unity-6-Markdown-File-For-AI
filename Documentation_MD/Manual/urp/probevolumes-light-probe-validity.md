[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-light-probe-validity.html)
  * [中文](/cn/current/Manual/urp/probevolumes-light-probe-validity.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-light-probe-validity.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-light-probe-validity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-light-probe-validity.html)
  * [中文](/cn/current/Manual/urp/probevolumes-light-probe-validity.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-light-probe-validity.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-light-probe-validity.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * [Troubleshooting Adaptive Probe Volumes](../urp/probevolumes-fixissues.html)
  * Light Probe validity in Adaptive Probe Volumes in URP

[](../urp/probevolumes-fixissues.html)

Troubleshooting Adaptive Probe Volumes

[](../urp/probevolumes-troubleshoot-artefacts.html)

Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

# Light Probe validity in Adaptive Probe Volumes in URP

Light Probes inside geometry are called invalid probes. The Universal **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) marks a **Light
Probe** Light probes store information about how light passes through space in
your scene. A collection of light probes arranged within a given space can
improve lighting on moving objects and static LOD scenery within that space.
[More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) as invalid when the probe fires
sampling rays to capture surrounding light data, but the rays hit the unlit
backfaces inside geometry.

URP uses the following techniques to minimise incorrect lighting data from
Light Probes:

  * [Virtual Offset](probevolumes-troubleshoot-artefacts.html#virtualoffset) tries to make invalid Light Probes valid, by moving their capture points so they’re outside any [colliders](https://docs.unity3d.com/Documentation/Manual/CollidersOverview.html)An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](../CollidersOverview.html)  
See in [Glossary](../Glossary.html#Collider).

  * [Dilation](probevolumes-troubleshoot-artefacts.html#dilation) detects Light Probes that remain invalid after Virtual Offset, and gives them data from valid Light Probes nearby.
  * [Rendering Layers](probevolumes-troubleshoot-light-leaks.html#layers) prevent objects from sampling probes that are on another **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](../Layers.html)  
See in [Glossary](../Glossary.html#LayerMask), reducing light leaking in
certain scenarios.

You can check which Light Probes are invalid using the [Rendering
Debugger](features/rendering-debugger.html)

![In the Scene on the left, Virtual Offset isnt active and dark bands are
visible. In the Scene on the right, Virtual Offset is
active.](../../uploads/urp/probe-volumes/probevolumes-virtualoffsetvsnot.png)  

![In the Scene on the left, Dilation isnt active and some areas are too dark.
In the Scene on the right, Dilation is active.](../../uploads/urp/probe-
volumes/probevolumes-dilationvsnot.png)  

[](../urp/probevolumes-fixissues.html)

Troubleshooting Adaptive Probe Volumes

[](../urp/probevolumes-troubleshoot-artefacts.html)

Troubleshooting dark blotches or streaks in Adaptive Probe Volumes in URP

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

