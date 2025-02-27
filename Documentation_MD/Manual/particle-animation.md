[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-animation.html)
  * [中文](/cn/current/Manual/particle-animation.html)
  * [日本語](/ja/current/Manual/particle-animation.html)
  * [한국어](/kr/current/Manual/particle-animation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-animation.html)
  * [中文](/cn/current/Manual/particle-animation.html)
  * [日本語](/ja/current/Manual/particle-animation.html)
  * [한국어](/kr/current/Manual/particle-animation.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle appearance](particle-appearance.html)
  * Particle animations

[](particle-rendering-shading.html)

Particle rendering and shading

[](particle-physics.html)

Particle physics

# Particle animations

Particle animations are typically simpler and less detailed than character
animations. In systems where the particles are visible individually,
animations can be used to convey actions or movements. For example, flames may
flicker and insects in a swarm might vibrate or shudder as if flapping their
wings. In cases where the particles form a single, continuous entity like a
cloud, animated particles can help add to the impression of energy and
movement.

The [Texture Sheet Animation](PartSysTexSheetAnimModule.html) module treats
the Texture as a grid of separate sub-images that can be played back as frames
of animation.

You can use the **Single Row** mode to create separate animation sequences for
particles and switch between animations from a script. This can be useful for
creating variation or switching to a different animation after a **collision**
A collision occurs when the physics engine detects that the colliders of two
GameObjects make contact or overlap, when at least one has a Rigidbody
component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision). The **Random Row** option is
highly effective as a way to break up conspicuous regularity in a **particle
system** A component that simulates fluid entities such as liquids, clouds and
flames by generating and animating large numbers of small 2D images in the
scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) (for example, a group of flame
objects that are all repeating the exact same flickering animation over and
over again). This option can also be used with a single frame per row as a way
to generate particles with random graphics. This can be used to break up
regularity in a object like a cloud or to produce different types of debris or
other objects from a single system. For example, a blunderbuss might fire out
a cluster of nails, bolts, balls and other projectiles, or a car crash effect
may result in springs, car paint, screws and other bits of metal being
emitted.

Use the **Row Mode** property to break up conspicuous regularity in a Particle
System (for example, a group of GameObjects that all repeat an identical
flickering animation over and over again). To generate particles with random
graphics, use this property with a single frame per row. This is useful for
breaking up regularity in a single system, such as cloud, or to produce
different types of debris. For example, a gun might fire out a cluster of
nails, bolts and other projectiles, or a car crash effect could emit springs,
car paint, screws and other bits of metal.

UV flipping is a great way to add more visual variety to your effects without
needing to author additional textures.

Selecting the **Sprites** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) option from the Mode dropdown allows
you to define a list of sprites to be displayed for each particle, instead of
using a regular grid of frames on a texture. Using this mode allows you to
take advantage of many of the features of sprites, such as the Sprite Packer,
custom pivots and different sizes per Sprite frame. The Sprite Packer can help
you share materials between different Particle Systems, by atlasing your
textures, which in turn can improve performance via **Dynamic Batching** An
automatic Unity process which attempts to render multiple meshes as if they
were a single mesh for optimized graphics performance. The technique
transforms all of the GameObject vertices on the CPU and groups many similar
vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching). There are some limitations
to be aware of with this mode. Most importantly, all sprites attached to a
Particle System must share the same texture. This can be achieved by using a
Multiple Mode Sprite, or by using the Sprite Packer. If using custom pivot
points for each Sprite, please note that you cannot blend between their
frames, because the geometry will be different between each frame. Only simple
sprites are supported, not 9 slice. Also be aware that **Mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) particles do not support custom pivots
or varying Sprite sizes.

[](particle-rendering-shading.html)

Particle rendering and shading

[](particle-physics.html)

Particle physics

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

