[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-rotation.html)
  * [中文](/cn/current/Manual/particle-rotation.html)
  * [日本語](/ja/current/Manual/particle-rotation.html)
  * [한국어](/kr/current/Manual/particle-rotation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-rotation.html)
  * [中文](/cn/current/Manual/particle-rotation.html)
  * [日本語](/ja/current/Manual/particle-rotation.html)
  * [한국어](/kr/current/Manual/particle-rotation.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle movement](particle-movement.html)
  * Particle rotation

[](create-particles-that-change-velocity-over-time.html)

Create particles that change velocity over time

[](particle-appearance.html)

Particle appearance

# Particle rotation

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can change a particle’s
rotation based on its speed or lifetime.

## Rotation by speed

The [Rotation by Speed](PartSysRotBySpeedModule.html) module can change a
particle’s rotation based on its speed in distance units per second.

This module can be used when the particles represent solid objects moving over
the ground such as rocks from a landslide. The rotation of the particles can
be set in proportion to the speed so that they roll over the surface
convincingly.

The Speed Range is only applied when the velocity is in one of the curve
modes. Fast particles will rotate using the values at the right end of the
curve, while slower particles will use values from the left side of the curve.

## Rotation over lifetime

The [Rotation Over Lifetime](PartSysRotOverLifeModule.html) module can change
a particle’s rotation based on how long it has existed.

This module is useful when particles represent small solid objects, such as
pieces of debris from an explosion. Assigning random values of rotation will
make the effect more realistic than having the particles remain upright as
they fly. The random rotations will also help to break up the regularity of
similarly shaped particles (the same texture repeated many times can be very
noticeable).

[](create-particles-that-change-velocity-over-time.html)

Create particles that change velocity over time

[](particle-appearance.html)

Particle appearance

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

