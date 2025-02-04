[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/activate-access-particle-system-modules.html)
  * [中文](/cn/current/Manual/activate-access-particle-system-modules.html)
  * [日本語](/ja/current/Manual/activate-access-particle-system-modules.html)
  * [한국어](/kr/current/Manual/activate-access-particle-system-modules.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/activate-access-particle-system-modules.html)
  * [中文](/cn/current/Manual/activate-access-particle-system-modules.html)
  * [日本語](/ja/current/Manual/activate-access-particle-system-modules.html)
  * [한국어](/kr/current/Manual/activate-access-particle-system-modules.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System module component reference](ParticleSystemModules.html)
  * Activate and access Particle System modules

[](ParticleSystemModules.html)

Particle System module component reference

[](PartSysMainModule.html)

Main module reference

# Activate and access Particle System modules

The Particle System component has many properties, and for convenience, the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) organises them into collapsible
sections called “modules”. These modules are documented in separate pages. See
documentation on [Particle System Modules](ParticleSystemModules.html) to
learn about each one.

![](../uploads/Main/PartSysMainInsp.png)

To expand and collapse modules, click the bar that shows their name. Use the
checkbox on the left to enable or disable the functionality of the properties
in that module. For example, if you don’t want to vary the sizes of particles
over their lifetime, uncheck the **Size over Lifetime** module.

The **Open Editor** button displays the options in a separate Editor window,
which allows you to edit multiple systems at once.

The [Particle Effect panel](PartSysUsage.html) in the **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View contains some additional options
for previewing Particle Systems.

All Particle System modules are part of the [Particle System](class-
ParticleSystem.html)A component that simulates fluid entities such as liquids,
clouds and flames by generating and animating large numbers of small 2D images
in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) component.

To create a new Particle System and enable a module:

  1. Click **GameObject** > **Effects** > **Particle System**.
  2. In the Inspector, find the Particle System component.
  3. In the Particle System component, find the fold-out for the module you want to apply.
  4. To the left of the fold-out header, enable the checkbox.

# Access modules via the API

Modules are part of the Particle System component, so you can access it via
the [ParticleSystem](../ScriptReference/ParticleSystem.html) class.

[](ParticleSystemModules.html)

Particle System module component reference

[](PartSysMainModule.html)

Main module reference

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

