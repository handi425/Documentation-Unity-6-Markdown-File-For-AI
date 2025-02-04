[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-velocity.html)
  * [中文](/cn/current/Manual/particle-velocity.html)
  * [日本語](/ja/current/Manual/particle-velocity.html)
  * [한국어](/kr/current/Manual/particle-velocity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-velocity.html)
  * [中文](/cn/current/Manual/particle-velocity.html)
  * [日本語](/ja/current/Manual/particle-velocity.html)
  * [한국어](/kr/current/Manual/particle-velocity.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle movement](particle-movement.html)
  * Particle velocity

[](particle-movement-patterns.html)

Particle movement patterns

[](create-particles-that-change-velocity-over-time.html)

Create particles that change velocity over time

# Particle velocity

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can change a particle’s
velocity.

## Limiting velocity over lifetime

The [Limit Velocity over Lifetime](PartSysLimitVelOverLifeModule.html) module
is very useful for simulating air resistance that slows the particles,
especially when a decreasing curve is used to lower the speed limit over time.
For example, an explosion or firework initially bursts at great speed but the
particles emitted from it rapidly slow down as they pass through the air.

The **Drag** option offers a more physically accurate simulation of air
resistance by offering options to apply varying amounts of resistance based on
the size and speed of the particles.

## Inheriting velocity

Use the [Inherit Velocity](PartSysInheritVelocity.html) module on subemitters.
Each particle in the parent system can spawn particles in the subemitter. This
module reads the velocity from the parent particle and controls how the speed
of the subemitter particles reacts to that velocity over time.

## Details

This effect is very useful for emitting particles from a moving object, such
as dust clouds from a car, smoke from a rocket, steam from a steam train’s
chimney, or any situation where the particles should initially be moving at a
percentage of the speed of the object they appear to come from. This module
only has an effect on the particles when **Simulation Space** is set to
**World** The area in your scene in which all objects reside. Often used to
specify that coordinates are world-relative, as opposed to object-relative.  
See in [Glossary](Glossary.html#World) in the [Main
module](PartSysMainModule.html).

It is also possible to use curves to influence the effect over time. For
example, you could apply a strong attraction to newly created particles, which
reduces over time. This could be useful for steam train smoke, which would
drift off slowly over time and stop following the train it was emitted from.

Unity calculates the emitter’s velocity in one of two ways: * Based on the
velocity of an attached **Rigidbody** A component that allows a GameObject to
be affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component * Based on how far the
Particle System’s **Transform component** A Transform component determines the
Position, Rotation, and Scale of each object in the scene. Every GameObject
has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent) travelled during the
current frame

To specify the method Unity uses, see the Main module’s [Emitter
Velocity](PartSysMainModule.html) property:

[](particle-movement-patterns.html)

Particle movement patterns

[](create-particles-that-change-velocity-over-time.html)

Create particles that change velocity over time

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

