[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysEmissionModule.html)
  * [中文](/cn/current/Manual/PartSysEmissionModule.html)
  * [日本語](/ja/current/Manual/PartSysEmissionModule.html)
  * [한국어](/kr/current/Manual/PartSysEmissionModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysEmissionModule.html)
  * [中文](/cn/current/Manual/PartSysEmissionModule.html)
  * [日本語](/ja/current/Manual/PartSysEmissionModule.html)
  * [한국어](/kr/current/Manual/PartSysEmissionModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Emission module reference

[](PartSysMainModule.html)

Main module reference

[](PartSysShapeModule.html)

Shape module reference

# Emission module reference

The properties in this module affect the rate and timing of [Particle
System](class-ParticleSystem.html)A component that simulates fluid entities
such as liquids, clouds and flames by generating and animating large numbers
of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) emissions.

![](../uploads/Main/PartSysEmissionModule-0.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Rate over Time** | The number of particles emitted per unit of time.  
**Rate over Distance** | The number of particles emitted per unit of distance moved.  
**Bursts** | A burst is an event which spawns particles. These settings allow particles to be emitted at specified times.  
 _Time_ | Set the time (in seconds, after the Particle System begins playing) at which to emit the burst.  
 _Count_ | Set a value for the number of particles that may be emitted.  
 _Cycles_ | Set a value for how many times to play the burst.  
 _Interval_ | Set a value for the time (in seconds) between when each cycle of the burst is triggered.  
 _Probability_ | Controls how likely it is that each burst event spawns particles. A higher value makes the system produce more particles, and a value of 1 guarantees that the system produces particles.  
  
## Additional resources

  * [Particle emissions and emitters](particle-emissions-emitters.html)

[](PartSysMainModule.html)

Main module reference

[](PartSysShapeModule.html)

Shape module reference

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

