[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-triggers.html)
  * [中文](/cn/current/Manual/particle-triggers.html)
  * [日本語](/ja/current/Manual/particle-triggers.html)
  * [한국어](/kr/current/Manual/particle-triggers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-triggers.html)
  * [中文](/cn/current/Manual/particle-triggers.html)
  * [日本語](/ja/current/Manual/particle-triggers.html)
  * [한국어](/kr/current/Manual/particle-triggers.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle physics](particle-physics.html)
  * Particle triggers

[](particle-collisions.html)

Particle collisions

[](configure-particle-trigger.html)

Configure a particle trigger

# Particle triggers

The Built-in **Particle System** A component that simulates fluid entities
such as liquids, clouds and flames by generating and animating large numbers
of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)’s
[Triggers](PartSysTriggersModule.html) module allows you to access and modify
particles based on their interaction with one or more **Colliders** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) in the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

When you enable this module, the Particle System calls the
[OnParticleTrigger()](../ScriptReference/MonoBehaviour.OnParticleTrigger.html)
callback on attached **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts), which you can use to access lists of
particles depending on where they are in respect to the Colliders in the
Scene.

[](particle-collisions.html)

Particle collisions

[](configure-particle-trigger.html)

Configure a particle trigger

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

