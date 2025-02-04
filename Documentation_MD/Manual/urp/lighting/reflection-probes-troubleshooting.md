[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [中文](/cn/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [日本語](/ja/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [한국어](/kr/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [中文](/cn/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [日本語](/ja/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)
  * [한국어](/kr/current/Manual/urp/lighting/reflection-probes-troubleshooting.html)

  * [Lighting](../../LightingOverview.html)
  * [Lighting in URP](../../urp/lighting-landing.html)
  * [Reflections in URP](../../urp/lighting/reflection-probes.html)
  * Troubleshooting reflections

[](../../urp/lighting/reflection-probes-introduction.html)

Reflection Probes in URP

[](../../urp/probevolumes.html)

Adaptive Probe Volumes (APV) in URP

# Troubleshooting reflections

## Troubleshoot reflections suddenly appearing

Reflection probe blending lets you avoid a situation where a reflection
suddenly appears on an object when it enters the probe box volume. When
**reflection probe** A rendering component that captures a spherical view of
its surroundings in all directions, rather like a camera. The captured image
is then stored as a Cubemap that can be used by objects with reflective
materials. [More info](../../class-ReflectionProbe.html)  
See in [Glossary](../../Glossary.html#ReflectionProbe) blending is enabled,
Unity gradually fades probe **cubemaps** A collection of six square textures
that can represent the reflections in an environment or the skybox drawn
behind your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](../../class-
Cubemap-landing.html)  
See in [Glossary](../../Glossary.html#Cubemap) in and out as the reflective
object passes from one volume to the other.

URP supports reflection probe blending in all **Rendering Paths** The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](../../RenderingPaths.html)  
See in [Glossary](../../Glossary.html#RenderingPath).

[](../../urp/lighting/reflection-probes-introduction.html)

Reflection Probes in URP

[](../../urp/probevolumes.html)

Adaptive Probe Volumes (APV) in URP

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

