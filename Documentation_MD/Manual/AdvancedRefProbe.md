[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AdvancedRefProbe.html)
  * [中文](/cn/current/Manual/AdvancedRefProbe.html)
  * [日本語](/ja/current/Manual/AdvancedRefProbe.html)
  * [한국어](/kr/current/Manual/AdvancedRefProbe.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AdvancedRefProbe.html)
  * [中文](/cn/current/Manual/AdvancedRefProbe.html)
  * [日本語](/ja/current/Manual/AdvancedRefProbe.html)
  * [한국어](/kr/current/Manual/AdvancedRefProbe.html)

  * [Lighting](LightingOverview.html)
  * [Reflections](reflections-landing.html)
  * Troubleshooting reflections

[](RefProbePerformance.html)

Optimize reflections

[](class-ReflectionProbe.html)

Reflection Probe Inspector window reference

# Troubleshooting reflections

## Box projection

Normally, the reflection **cubemap** A collection of six square textures that
can represent the reflections in an environment or the skybox drawn behind
your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](class-
Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) is assumed to be at an infinite
distance from any given object. Different angles of the cubemap will be
visible as the object turns but it is not possible for the object to move
closer or farther away from the reflected surroundings. This often works very
well for outdoor scenes but its limitations show in an indoor **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene); the interior walls of a room are
clearly not an infinite distance away and the reflection of a wall should get
larger the closer the object gets to it.

The **Box Projection** option allows you to create a reflection cubemap at a
finite distance from the probe, thus allowing objects to show different-sized
reflections according to their distance from the cubemap’s walls. The size of
the surrounding cubemap is determined by the probes zone of effect, as
determined by its **Box Size** property. For example, with a probe that
reflects the interior of a room, you should set the size to match the
dimensions of the room.

In the Built in Render Pipeline, you can enable global **Box Projection** for
a given [Graphics tier](graphics-tiers.html) in [**Project Settings** A broad
collection of settings which allow you to configure how Physics, Audio,
Networking, Graphics, Input and many other areas of your project behave. [More
info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) > **Graphics** > **Tier
Settings**](class-GraphicsSettings.html#Tier). You can disable this setting
for individual Reflection Probes in the Reflection Probe inspector if you want
to create infinite projection.

![The parallax issue is fixed by using Box Projection
option](../uploads/Main/GraphicsSettings_BoxProjection.jpg) The parallax issue
is fixed by using Box Projection option

## Additional resources

  * [Troubleshooting reflections in URP](urp/lighting/reflection-probes-troubleshooting.html)

[](RefProbePerformance.html)

Optimize reflections

[](class-ReflectionProbe.html)

Reflection Probe Inspector window reference

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

