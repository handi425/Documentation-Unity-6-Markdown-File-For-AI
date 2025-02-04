[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-inspector-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-inspector-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-inspector-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-inspector-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-inspector-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-inspector-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-inspector-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-inspector-reference.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Adaptive Probe Volume Inspector reference

[](../urp/probevolumes-troubleshoot-light-leaks.html)

Troubleshooting light leaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-lighting-panel-reference.html)

Adaptive Probe Volumes panel reference

# Adaptive Probe Volume Inspector reference

Select an Adaptive Probe Volume and open the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) to view its properties.

**Property** | **Description**  
---|---  
**Mode**  
**Global** | URP sizes this Adaptive Probe Volume to include all renderers in the scene or Baking Set that have **Contribute Global Illumination** enabled in their [Mesh Renderer component](https://docs.unity3d.com/Manual/class-MeshRenderer.html). URP recalculates the volume size every time you save or generate lighting.  
**Scene** | URP sizes this Adaptive Probe Volume to include all renderers in the same scene as this Adaptive Probe Volume. URP recalculates the volume size every time you save or generate lighting.  
**Local** | Set the size of this Adaptive Probe Volume manually.  
**Size** | Set the size of this Adaptive Probe Volume. This setting only appears when you set **Mode** to **Local**.  
**Subdivision Override**  
**Override Probe Spacing** | Override the Probe Spacing set in the **Baking Set** for this Adaptive Probe Volume. This cannot exceed the **Min Probe Spacing** and **Max Probe Spacing** values in the [Adaptive Probe Volumes panel in the Lighting window](probevolumes-lighting-panel-reference).  
**Geometry Settings**  
**Override Renderer Filters** | Enable filtering by Layer which GameObjects URP considers when it generates probe positions. Use this to exclude certain GameObjects from contributing to Adaptive Probe Volume lighting.  
**Layer Mask** | Filter by Layer which GameObjects URP considers when it generates probe positions.  
**Min Renderer Size** | The smallest [Renderer](https://docs.unity3d.com/ScriptReference/Renderer.html) size URP considers when it generates probe positions.  
**Fill Empty Spaces** | Enable URP filling the empty space between and around Renderers with bricks. Bricks in empty spaces always use the **Max Probe Spacing** value.  
  
[](../urp/probevolumes-troubleshoot-light-leaks.html)

Troubleshooting light leaks in Adaptive Probe Volumes in URP

[](../urp/probevolumes-lighting-panel-reference.html)

Adaptive Probe Volumes panel reference

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

