[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ParticleSystem.html)
  * [中文](/cn/current/Manual/class-ParticleSystem.html)
  * [日本語](/ja/current/Manual/class-ParticleSystem.html)
  * [한국어](/kr/current/Manual/class-ParticleSystem.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ParticleSystem.html)
  * [中文](/cn/current/Manual/class-ParticleSystem.html)
  * [日本語](/ja/current/Manual/class-ParticleSystem.html)
  * [한국어](/kr/current/Manual/class-ParticleSystem.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * Particle System component reference

[](particle-system-job-system-integration.html)

Integrate the C# Job System into the Particle System workflow

[](ParticleSystemModules.html)

Particle System module component reference

# Particle System component reference

[Switch to Scripting](../ScriptReference/ParticleSystem.html "Go to
ParticleSystem page in the Scripting Reference")

A **Particle System** component simulates fluid entities such as liquids,
clouds and flames by generating and animating large numbers of small 2D images
in the **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For a full introduction to particle
systems and their uses, see further documentation on [Particle
Systems](ParticleSystems.html).

![](../uploads/Main/PartSysMainInspPartEffect.png) **Property** | **Function**  
---|---  
**Simulate Layers** | Allows you to preview Particle Systems that are not selected. By default, only selected Particle Systems play in the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView). However, when you set Simulate
Layers to anything other than **Nothing** , effects that match the **Layer
Mask** A value defining which layers to include or exclude from an operation,
such as rendering, collision or your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#LayerMask) play automatically, without you
needing to select them. This is particularly useful for previewing
environmental effects.  
**Resimulate** | When this property is enabled, the Particle System immediately applies property changes to particles it has already generated. When disabled, the Particle System leaves existing particles as they are, and only applies property changes to new particles.  
**Show Bounds** | When this property is enabled, Unity displays the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](Glossary.html#Boundingvolume) around the selected Particle
Systems. These bounds determine whether a Particle System is currently on
screen or not.  
**Show Only Selected** | When this property is enabled, Unity hides all non-selected Particle Systems, allowing you to focus on producing a single effect.  
  
ParticleSystem

[](particle-system-job-system-integration.html)

Integrate the C# Job System into the Particle System workflow

[](ParticleSystemModules.html)

Particle System module component reference

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

