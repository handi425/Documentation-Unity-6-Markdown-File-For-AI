[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LODRealtimeGI.html)
  * [中文](/cn/current/Manual/LODRealtimeGI.html)
  * [日本語](/ja/current/Manual/LODRealtimeGI.html)
  * [한국어](/kr/current/Manual/LODRealtimeGI.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LODRealtimeGI.html)
  * [中文](/cn/current/Manual/LODRealtimeGI.html)
  * [日本語](/ja/current/Manual/LODRealtimeGI.html)
  * [한국어](/kr/current/Manual/LODRealtimeGI.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html)
  * LOD and Enlighten Realtime Global Illumination

[](realtime-gi-using-enlighten-optimize.html)

Optimize Enlighten Realtime Global Illumination

[](ProfilerGI.html)

Global Illumination Profiler module

# LOD and Enlighten Realtime Global Illumination

Objects with **Receive**Global Illumination** A group of techniques that model
both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination)** set to ****Lightmaps** A
pre-rendered texture that contains the effects of light sources on static
objects in the scene. Lightmaps are overlaid on top of scene geometry to
create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap)** have a lighting solution with
lightmaps for baked direct and [indirect
lighting](LightmappingDirectional.html), and lightmaps for **Enlighten** A
lighting system by Geomerics used in Unity for Enlighten Realtime Global
Illumination. [More info](https://www.siliconstudio.co.jp/en/products-
service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination. For
more information about **Receive Global Illumination** , see the [Mesh
Renderer settings](class-MeshRenderer.html) and the script reference for
[ReceiveGI](../ScriptReference/ReceiveGI.html).

When you use Unity’s **LOD** The _Level Of Detail_ (LOD) technique is an
optimization that reduces the number of triangles that Unity has to render for
a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) system in a **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) where you have enabled Baked Global
Illumination and Enlighten Realtime Global Illumination, the system lights the
most detailed model out of the **LOD Group** A component to manage level of
detail (LOD) for GameObjects. [More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) as if it has the **Contribute Global
Illumination** setting enabled and isn’t part of the LOD group."

Enlighten can only compute direct lighting for lower LODs and the LOD system
must rely on [Light Probes](LightProbes.html)Light probes store information
about how light passes through space in your scene. A collection of light
probes arranged within a given space can improve lighting on moving objects
and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) to sample indirect lighting.

To enable the Editor to produce lightmaps with Enlighten Realtime Global
Illumination, select the **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) you want to affect, view its
Renderer component in the **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, and ensure that
**Contribute Global Illumination** is enabled.

For lower LODs in a LOD Group, you can only combine baked lightmaps with
Enlighten Realtime Global Illumination from [Light Probes](LightProbes.html)
or [Light Probe Proxy Volumes](class-LightProbeProxyVolume.html)A component
that allows you to use more lighting information for large dynamic GameObjects
that cannot use baked lightmaps (for example, large Particle Systems or
skinned Meshes). [More info](class-LightProbeProxyVolume.html)  
See in [Glossary](Glossary.html#LightProbeProxyVolume), which you must place
around the LOD Group.

![An animation showing how real-time ambient color affects the Enlighten
Realtime Global Illumination used by lower
LODs](../uploads/Main/LODRealtimeGI.gif) An animation showing how real-time
ambient color affects the Enlighten Realtime Global Illumination used by lower
LODs

[](realtime-gi-using-enlighten-optimize.html)

Optimize Enlighten Realtime Global Illumination

[](ProfilerGI.html)

Global Illumination Profiler module

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

