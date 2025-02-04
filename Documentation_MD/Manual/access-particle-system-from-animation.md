[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/access-particle-system-from-animation.html)
  * [中文](/cn/current/Manual/access-particle-system-from-animation.html)
  * [日本語](/ja/current/Manual/access-particle-system-from-animation.html)
  * [한국어](/kr/current/Manual/access-particle-system-from-animation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/access-particle-system-from-animation.html)
  * [中文](/cn/current/Manual/access-particle-system-from-animation.html)
  * [日本語](/ja/current/Manual/access-particle-system-from-animation.html)
  * [한국어](/kr/current/Manual/access-particle-system-from-animation.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * Access the Particle System from the Animation system

[](class-ParticleSystemForceField.html)

Particle System Force Field component reference

[](custom-data-streams-particle-systems.html)

Custom data streams in Particle Systems

# Access the Particle System from the Animation system

All particle properties are accessible by the Animation system, meaning you
can **keyframe** A frame that marks the start or end point of a transition in
an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) them in and control them from your
animations.

To access the **Particle System** A component that simulates fluid entities
such as liquids, clouds and flames by generating and animating large numbers
of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)’s properties, there must be an
**Animator component** A component on a model that animates that model using
the Animation system. The component has a reference to an Animator Controller
asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent) attached to the Particle
System’s **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). An Animation Controller and an
Animation are also required.

![To animate a Particle System, add an Animator Component, and assign an
Animation Controller with an
Animation.](../uploads/Main/ParticleSystemAnimatorComponent.png) To animate a
Particle System, add an Animator Component, and assign an Animation Controller
with an Animation.

To animate a Particle System property, open the **Animation Window** with the
GameObject containing the Animator and Particle System selected. Click **Add
Property** to add properties.

![Add properties to the animation in the Animation
Window.](../uploads/Main/ParticleSystemAnimationWindow.png) Add properties to
the animation in the Animation Window.

Scroll to the right to reveal the **add controls**.

![](../uploads/Main/ParticleSystemAnimationScrollRight.png)

Note that for curves, you can only keyframe the overall **curve multiplier** ,
which can be found next to the curve editor in the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

[](class-ParticleSystemForceField.html)

Particle System Force Field component reference

[](custom-data-streams-particle-systems.html)

Custom data streams in Particle Systems

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

