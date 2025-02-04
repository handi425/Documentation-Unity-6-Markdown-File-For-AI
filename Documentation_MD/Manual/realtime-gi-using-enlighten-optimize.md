[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/realtime-gi-using-enlighten-optimize.html)
  * [中文](/cn/current/Manual/realtime-gi-using-enlighten-optimize.html)
  * [日本語](/ja/current/Manual/realtime-gi-using-enlighten-optimize.html)
  * [한국어](/kr/current/Manual/realtime-gi-using-enlighten-optimize.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/realtime-gi-using-enlighten-optimize.html)
  * [中文](/cn/current/Manual/realtime-gi-using-enlighten-optimize.html)
  * [日本語](/ja/current/Manual/realtime-gi-using-enlighten-optimize.html)
  * [한국어](/kr/current/Manual/realtime-gi-using-enlighten-optimize.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html)
  * Optimize Enlighten Realtime Global Illumination

[](realtime-gi-using-enlighten-use.html)

Enable Enlighten Realtime Global Illumination

[](LODRealtimeGI.html)

LOD and Enlighten Realtime Global Illumination

# Optimize Enlighten Realtime Global Illumination

Enlighten Realtime **Global Illumination** A group of techniques that model
both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) uses a set of
**lightmaps** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) to store real-time indirect bounces.
For this reason, enabling it increases memory requirements, even if you are
using it along with Baked Global Illumination.

The number of **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) calculations needed to generate
lighting also increases when you use **Enlighten** A lighting system by
Geomerics used in Unity for Enlighten Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination
because it samples an additional set of lightmaps and **Light Probes** Light
probes store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).

If Enlighten Realtime Global Illumination doesn’t respond quickly enough to
changes in your **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) lighting, there are several ways to
address this problem:

  * Reduce the real-time lightmap resolution to speed up calculation at runtime.
  * Increase the CPU Usage setting for **Realtime GI** in the Quality Settings window. The tradeoff is that other systems receive less CPU time to do their work. Whether this is acceptable depends on your Project. This is a per-Scene setting, so you can dedicate more or less CPU time based on the complexity of each individual Scene in your Project.

[](realtime-gi-using-enlighten-use.html)

Enable Enlighten Realtime Global Illumination

[](LODRealtimeGI.html)

LOD and Enlighten Realtime Global Illumination

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

