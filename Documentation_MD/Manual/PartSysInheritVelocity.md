[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysInheritVelocity.html)
  * [中文](/cn/current/Manual/PartSysInheritVelocity.html)
  * [日本語](/ja/current/Manual/PartSysInheritVelocity.html)
  * [한국어](/kr/current/Manual/PartSysInheritVelocity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysInheritVelocity.html)
  * [中文](/cn/current/Manual/PartSysInheritVelocity.html)
  * [日本語](/ja/current/Manual/PartSysInheritVelocity.html)
  * [한국어](/kr/current/Manual/PartSysInheritVelocity.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Inherit Velocity module reference

[](PartSysLimitVelOverLifeModule.html)

Limit Velocity over Lifetime module reference

[](PartSysLifetimeByEmitterSpeedModule.html)

Lifetime by Emitter Speed module reference

# Inherit Velocity module reference

Use this module on subemitters. Each particle in the parent system can spawn
particles in the subemitter. This module reads the velocity from the parent
particle and controls how the speed of the subemitter particles reacts to that
velocity over time.

![](../uploads/Main/PartSysInheritVelocity55.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Mode** | Specifies how the emitter velocity is applied to particles  
Current | The emitter’s current velocity will be applied to all particles on every frame. For example, if the emitter slows down, all particles will also slow down.  
Initial | The emitter’s velocity will be applied once, when each particle is born. Any changes to the emitter’s velocity made after a particle is born will not affect that particle.  
**Multiplier** | The proportion of the emitter’s velocity that the particle should inherit.  
  
## Additional resources

  * [Particle velocity](particle-velocity.html)
  * [Create particles that change velocity over time](create-particles-that-change-velocity-over-time.html)

[](PartSysLimitVelOverLifeModule.html)

Limit Velocity over Lifetime module reference

[](PartSysLifetimeByEmitterSpeedModule.html)

Lifetime by Emitter Speed module reference

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

