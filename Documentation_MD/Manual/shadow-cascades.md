[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shadow-cascades.html)
  * [中文](/cn/current/Manual/shadow-cascades.html)
  * [日本語](/ja/current/Manual/shadow-cascades.html)
  * [한국어](/kr/current/Manual/shadow-cascades.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shadow-cascades.html)
  * [中文](/cn/current/Manual/shadow-cascades.html)
  * [日本語](/ja/current/Manual/shadow-cascades.html)
  * [한국어](/kr/current/Manual/shadow-cascades.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * [Real-time shadows](shadow-realtime.html)
  * [Shadow cascades](shadow-cascades-landing.html)
  * Introduction to shadow cascades

[](shadow-cascades-landing.html)

Shadow cascades

[](shadow-cascades-use.html)

Configure shadow cascades

# Introduction to shadow cascades

Shadow cascades let you improve the visual fidelity of shadows without
increasing the shadow map resolution.

For example, the following illustration shows shadow rendering with different
numbers of shadow cascades. The shadow resolution is 2048 in all cases.

![Shadow rendering with different cascade numbers. A: 1 cascade, B: 2
cascades, C: 3 cascades, D: 4 cascades](../uploads/urp/shadows/shadow-
cascades-comparison.png)  
Shadow rendering with different cascade numbers. A: 1 (no cascades), B: 2
cascades, C: 3 cascades, D: 4 cascades.

Shadow cascades only work with directional lights.

From a technical perspective, shadow cascades mitigate a problem called
[perspective aliasing](shadow-cascades-implementation-
details.html#perspective-aliasing), where real-time shadows from [directional
lights](Lighting.html) appear pixelated when they are near the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

## Additional resources

  * [Configure shadow cascades](shadow-cascades-use.html)

  * [Performance impact of shadow cascades]()

  * [Technical implementation details](shadow-cascades-implementation-details.html)

[](shadow-cascades-landing.html)

Shadow cascades

[](shadow-cascades-use.html)

Configure shadow cascades

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

