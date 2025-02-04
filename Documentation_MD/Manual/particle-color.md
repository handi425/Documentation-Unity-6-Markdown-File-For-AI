[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-color.html)
  * [中文](/cn/current/Manual/particle-color.html)
  * [日本語](/ja/current/Manual/particle-color.html)
  * [한국어](/kr/current/Manual/particle-color.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-color.html)
  * [中文](/cn/current/Manual/particle-color.html)
  * [日本語](/ja/current/Manual/particle-color.html)
  * [한국어](/kr/current/Manual/particle-color.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle appearance](particle-appearance.html)
  * Change particle color

[](particle-size.html)

Particle size

[](particle-lights-trails.html)

Particle lights and trails

# Change particle color

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can change a particle’s
rotation based on its speed or lifetime.

## Color by speed

The [Color by Speed](PartSysColorBySpeedModule.html) module can change a
particle’s color based on its speed in distance units per second.

Burning or glowing particles (such as sparks) tend to burn more brightly when
they move quickly through the air (for example, when sparks are exposed to
more oxygen), but then dim slightly as they slow down. To simulate this, you
might use _Color By Speed_ with a gradient that has white at the upper end of
the speed range, and red at the lower end (in the spark example, faster
particles will appear white while slower particles are red).

## Color over lifetime

The [Color Over Lifetime](PartSysColorOverLifeModule.html) module can change a
particle’s color based on how long it has existed.

Many types of natural and fantastical particles vary in color over time, and
so this property has many uses. For example, white hot sparks will cool as
they pass through the air and a magic spell might burst into a rainbow of
colors. Equally important, though, is the variation of alpha (transparency).
It is very common for particles to burn out, fade or dissipate as they reach
the end of their lifetime (for example, hot sparks, fireworks and smoke
particles) and a simple diminishing gradient produces this effect.

When also using the [Start Color](PartSysMainModule.html) property, this
module multiples the 2 colors together, to get the final particle color.

[](particle-size.html)

Particle size

[](particle-lights-trails.html)

Particle lights and trails

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

