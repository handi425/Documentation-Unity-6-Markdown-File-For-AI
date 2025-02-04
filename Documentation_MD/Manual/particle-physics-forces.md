[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-physics-forces.html)
  * [中文](/cn/current/Manual/particle-physics-forces.html)
  * [日本語](/ja/current/Manual/particle-physics-forces.html)
  * [한국어](/kr/current/Manual/particle-physics-forces.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-physics-forces.html)
  * [中文](/cn/current/Manual/particle-physics-forces.html)
  * [日本語](/ja/current/Manual/particle-physics-forces.html)
  * [한국어](/kr/current/Manual/particle-physics-forces.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle physics](particle-physics.html)
  * Particle physics forces

[](particle-physics.html)

Particle physics

[](apply-forces-particles.html)

Apply forces to particles

# Particle physics forces

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can simulate physics forces
that act on a particle.

## Force over lifetime

The [Force over Lifetime](PartSysForceOverLifeModule.html) module can change
the strength of simulated physics forces on a particle based on how long the
particle has existed.

Fluids are often affected by forces as they move. For example, smoke will
accelerate slightly as it rises from a fire, carried up by the hot air around
it. Subtle effects can be achieved by using curves to control the force over
the particles’ lifetimes. Using the previous example, smoke will initially
accelerate upward but as the rising air gradually cools, the force will
diminish. Thick smoke from a fire might initially accelerate, then slow down
as it spreads and perhaps even start to fall to earth if it persists for a
long time.

## External forces

The [External Forces](PartSysExtForceModule.html) module modifies the effect
of **wind zones** A GameObject that adds the effect of wind to your terrain.
For instance, Trees within a wind zone will bend in a realistic animated
fashion and the wind itself will move in pulses to create natural patterns of
movement among the tree. [More info](class-WindZone.html)  
See in [Glossary](Glossary.html#windzone) and [Particle System Force
Fields](class-ParticleSystemForceField.html) on particles emitted by the
system.

To get the best results out of this feature, create separate **GameObjects**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with
[ParticleSystemForceFields](class-ParticleSystemForceField.html) components.

A **Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) can incorporate _wind zones_ which
affect the movement of trees on the landscape. Enabling this section allows
the wind zones to blow particles from the system. The _Multiplier_ value lets
you scale the effect of the wind on the particles, since they will often be
blown more strongly than tree branches.

[](particle-physics.html)

Particle physics

[](apply-forces-particles.html)

Apply forces to particles

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

