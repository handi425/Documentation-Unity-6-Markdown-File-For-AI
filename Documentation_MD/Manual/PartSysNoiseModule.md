[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysNoiseModule.html)
  * [中文](/cn/current/Manual/PartSysNoiseModule.html)
  * [日本語](/ja/current/Manual/PartSysNoiseModule.html)
  * [한국어](/kr/current/Manual/PartSysNoiseModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysNoiseModule.html)
  * [中文](/cn/current/Manual/PartSysNoiseModule.html)
  * [日本語](/ja/current/Manual/PartSysNoiseModule.html)
  * [한국어](/kr/current/Manual/PartSysNoiseModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Noise module reference

[](PartSysVelOverLifeModule.html)

Velocity over Lifetime module reference

[](PartSysLimitVelOverLifeModule.html)

Limit Velocity over Lifetime module reference

# Noise module reference

Add turbulence to particle movement using this module.

![](../uploads/Main/PartSysNoiseModule.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

Property | Function  
---|---  
**Separate Axes** | Control the strength and remapping independently on each axis.  
**Strength** | A curve that defines how strong the noise effect is on a particle over its lifetime. Higher values will make particles move faster and further.  
**Frequency** | Low values create soft, smooth noise, and high values create rapidly changing noise. This controls how often the particles change their direction of travel, and how abrupt those changes of direction are.  
**Scroll Speed** | Move the noise field over time to cause more unpredictable and erratic particle movement.  
**Damping** | When enabled, strength is proportional to frequency. Tying these values together means the noise field can be scaled while maintaining the same behaviour, but at a different size.  
**Octaves** | Specify how many layers of overlapping noise are combined to produce the final noise values. Using more layers gives richer, more interesting noise, but significantly adds to the performance cost.  
**Octave Multiplier** | For each additional noise layer, reduce the strength by this proportion.  
**Octave Scale** | For each additional noise layer, adjust the frequency by this multiplier.  
**Quality** | Lower quality settings reduce the performance cost significantly, but also affect how interesting the noise looks. Use the lowest quality that gives you the desired behavior for maximum performance.  
**Remap** | Remap the final noise values into a different range.  
**Remap Curve** | The curve that describes how the final noise values are transformed. For example, you could use this to pick out the lower ranges of the noise field and ignore the higher ranges by creating a curve that starts high and ends at zero.  
**Position Amount** | A multiplier to control how much the noise affects particle positions.  
**Rotation Amount** | A multiplier to control how much the noise affects particle rotations, in degrees per second.  
**Size Amount** | A multiplier to control how much the noise affects particle sizes.  
  
## Additional resources

  * [Particle movement patterns](particle-movement-patterns.html)

[](PartSysVelOverLifeModule.html)

Velocity over Lifetime module reference

[](PartSysLimitVelOverLifeModule.html)

Limit Velocity over Lifetime module reference

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

