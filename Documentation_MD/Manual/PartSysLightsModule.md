[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysLightsModule.html)
  * [中文](/cn/current/Manual/PartSysLightsModule.html)
  * [日本語](/ja/current/Manual/PartSysLightsModule.html)
  * [한국어](/kr/current/Manual/PartSysLightsModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysLightsModule.html)
  * [中文](/cn/current/Manual/PartSysLightsModule.html)
  * [日本語](/ja/current/Manual/PartSysLightsModule.html)
  * [한국어](/kr/current/Manual/PartSysLightsModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Lights module reference

[](PartSysTexSheetAnimModule.html)

Texture Sheet Animation module reference

[](PartSysTrailsModule.html)

Trails module reference

# Lights module reference

Add real-time lights to a percentage of your particles using this module.

![](../uploads/Main/PartSysLightsModule.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

Property | Function  
---|---  
**Light** | Assign a [Light](LightingInUnity.html) **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) describing how your particle lights
should look.  
**Ratio** | A value between 0 and 1 describing the proportion of particles that will receive a light.  
**Random Distribution** | Choose whether lights are assigned randomly or periodically. When set to true, every particle has a random chance of receiving a light based on the Ratio. Higher values increase the probability of a particle having a light. When set to false, the Ratio controls how often a newly created particle receives a light (for example, every Nth particle will receive a light).  
**Use Particle Color** | When set to True, the final color of the Light will be modulated by the color of the particle it is attached to. If set to False, the Light color is used without any modification.  
**Size Affects Range** | When enabled, the **Range** specified in the Light will be multiplied by the size of the particle.  
**Alpha Affects Intensity** | When enabled, the **Intensity** of the light is multiplied by the particle alpha value.  
**Range Multiplier** | Apply a custom multiplier to the Range of the light over the lifetime of the particle using this curve.  
**Intensity Multiplier** | Apply a custom multiplier to the Intensity of the light over the lifetime of the particle using this curve.  
**Maximum Lights** | Use this setting to avoid accidentally creating an enormous number of lights, which could make the Editor unresponsive or make your application run very slowly.  
  
## Additional resources

  * [Particle lights and trails](particle-lights-trails.html)

[](PartSysTexSheetAnimModule.html)

Texture Sheet Animation module reference

[](PartSysTrailsModule.html)

Trails module reference

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

