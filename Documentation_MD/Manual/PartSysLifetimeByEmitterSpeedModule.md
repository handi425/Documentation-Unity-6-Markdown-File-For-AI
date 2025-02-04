[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [中文](/cn/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [日本語](/ja/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [한국어](/kr/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [中文](/cn/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [日本語](/ja/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)
  * [한국어](/kr/current/Manual/PartSysLifetimeByEmitterSpeedModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Lifetime by Emitter Speed module reference

[](PartSysInheritVelocity.html)

Inherit Velocity module reference

[](PartSysForceOverLifeModule.html)

Force over Lifetime module reference

# Lifetime by Emitter Speed module reference

This module controls the initial lifetime of each particle based on the speed
of the emitter when the particle spawns.

![](../uploads/Main/part-sys-lifetime-by-emitter-speed-ui.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**Property** | **Function**  
---|---  
**Multiplier** | The multiplier to apply to the particle’s initial lifetime. The module uses this value differently depending on the curve mode you set. The curve modes are:  
• **Constant** : Uses the constant multiplier value you set for this property.
Using this curve mode ignores the **Speed Range** property.  
• **Curve** : Takes the emitter’s speed, maps it to a value between 0 and 1
based on the **Speed Range** , then uses the normalized value to sample the
curve.  
• **Random Between Two Constants** : Sets a random multiplier for each
particle between the two values you set for this property. Using this curve
mode ignores the **Speed Range** property.  
• **Random Between Two Curves** : Takes the emitter’s speed, maps it to a
value between 0 and 1 based on the **Speed Range** , then uses the normalized
value to sample each curve. For each particle, the module sets the multiplier
to a random value between the two samples.  
**Speed Range** | The minimum and maximum emitter speeds the Particle System maps to a value along the **Multiplier** curve. If the emitter’s speed is equal to the first value, the multiplier is the value at the start of the curve. If the emitter’s speed is equal to the second value, the multiplier is the value at the end of the curve.  
This property is only relevant if the curve mode for **Multiplier** is set to
**Curve** or **Random Between Two Curves**.  
  
## Additional resources

  * [Particle emissions and emitters](particle-emissions-emitters.html)

[](PartSysInheritVelocity.html)

Inherit Velocity module reference

[](PartSysForceOverLifeModule.html)

Force over Lifetime module reference

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

