[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shadow-cascades-performance.html)
  * [中文](/cn/current/Manual/shadow-cascades-performance.html)
  * [日本語](/ja/current/Manual/shadow-cascades-performance.html)
  * [한국어](/kr/current/Manual/shadow-cascades-performance.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shadow-cascades-performance.html)
  * [中文](/cn/current/Manual/shadow-cascades-performance.html)
  * [日本語](/ja/current/Manual/shadow-cascades-performance.html)
  * [한국어](/kr/current/Manual/shadow-cascades-performance.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * [Real-time shadows](shadow-realtime.html)
  * [Shadow cascades](shadow-cascades-landing.html)
  * Performance impact of shadow cascades

[](shadow-cascades-use.html)

Configure shadow cascades

[](shadow-cascades-implementation-details.html)

Implementation details of shadow cascades

# Performance impact of shadow cascades

Increasing the number of shadow cascades increases the number of draw calls in
the shadow rendering pass, which has a negative impact on rendering
performance.

Reducing the number of shadow cascades lets you significantly reduce the
number of shadow rendering draw calls.

A lower number of shadow cascades might reduce the visual quality of shadows
in the **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Choose the number of cascades based on
the performance and visual quality requirements of your project on a scene-by-
scene basis.

You can configure different shadow cascade settings and shadow resolution
settings for different quality levels using multiple URP Assets.

[](shadow-cascades-use.html)

Configure shadow cascades

[](shadow-cascades-implementation-details.html)

Implementation details of shadow cascades

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

