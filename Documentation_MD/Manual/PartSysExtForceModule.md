[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysExtForceModule.html)
  * [中文](/cn/current/Manual/PartSysExtForceModule.html)
  * [日本語](/ja/current/Manual/PartSysExtForceModule.html)
  * [한국어](/kr/current/Manual/PartSysExtForceModule.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysExtForceModule.html)
  * [中文](/cn/current/Manual/PartSysExtForceModule.html)
  * [日本語](/ja/current/Manual/PartSysExtForceModule.html)
  * [한국어](/kr/current/Manual/PartSysExtForceModule.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * External Forces module reference

[](PartSysRotBySpeedModule.html)

Rotation by Speed module reference

[](PartSysCollisionModule.html)

Collision module reference

# External Forces module reference

This property modifies the effect of **wind zones** A GameObject that adds the
effect of wind to your terrain. For instance, Trees within a wind zone will
bend in a realistic animated fashion and the wind itself will move in pulses
to create natural patterns of movement among the tree. [More info](class-
WindZone.html)  
See in [Glossary](Glossary.html#windzone) and [Particle System Force
Fields](class-ParticleSystemForceField.html) on particles emitted by the
system.

![](../uploads/Main/PartSysExtForcesInsp.png)
![](../uploads/Main/PartSysExtForcesInspList.png)

## Properties

For some properties in this section, you can use different modes to set their
value. For information on the modes you can use, see [Varying properties over
time](PartSysUsage.html#VaryOverTime).

**_Property_** | **_Function_**  
---|---  
**Multiplier** | Scale value applied to wind zone forces.  
**Influence Filter** | Choose whether to include Force Fields based on a **Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#LayerMask), or via an explicit **List**.  
**List** | Define an explicit list of Force Fields that can affect this **Particle System** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem). This appears when the
**Influence Filter** is set to **List**.  
**Influence Mask** | Use a Layer Mask to determine which Force Fields affect this Particle System. This appears when the **Influence Filter** is set to **Layer Mask**.   
This is set to **Everything** by default, but you can enable or disable the
following options individually:  
\- **Nothing** (automatically unticks all other options, turning them off)  
\- **Everything** (automatically ticks all other options, turning them on)  
\- **Default**  
\- **TransparentFX**  
\- **Ignore[Raycast](Raycasters)**  
\- **Water**  
\- **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI)  
\- **[PostProcessing](PostProcessingOverview.html)**  
  
## Additional resources

  * [Particle physics forces](particle-physics-forces.html)

[](PartSysRotBySpeedModule.html)

Rotation by Speed module reference

[](PartSysCollisionModule.html)

Collision module reference

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

