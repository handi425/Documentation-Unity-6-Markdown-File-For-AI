[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/configuring-global-particle-properties.html)
  * [中文](/cn/current/Manual/configuring-global-particle-properties.html)
  * [日本語](/ja/current/Manual/configuring-global-particle-properties.html)
  * [한국어](/kr/current/Manual/configuring-global-particle-properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/configuring-global-particle-properties.html)
  * [中文](/cn/current/Manual/configuring-global-particle-properties.html)
  * [日本語](/ja/current/Manual/configuring-global-particle-properties.html)
  * [한국어](/kr/current/Manual/configuring-global-particle-properties.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * Configuring global particle properties

[](particle-emissions-emitters.html)

Particle emissions and emitters

[](particle-movement.html)

Particle movement

# Configuring global particle properties

The **Particle System** A component that simulates fluid entities such as
liquids, clouds and flames by generating and animating large numbers of small
2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)’s
[Main](PartSysMainModule.html) module contains global properties that affect
the whole system. Most of these properties control the initial state of newly
created particles.

The system emits particles for a specific duration, and can be set to emit
continuously using the **Looped** property. This allows you to set particles
to be emitted intermittently or continuously; for example, an object may emit
smoke in short puffs or in a steady stream.

The **Start** properties (**lifetime** , **speed** , **size** , **rotation**
and **color**) specify the state of a particle on emission. You can specify a
particle’s width, height and depth independently, using the **3D Start Size**
property (see Non-uniform particle scaling, below).

All Particle Systems use the same gravity vector specified in the **Physics**
settings. The Gravity Multiplier value can be used to scale the gravity, or
switch it off if set to zero.

## Non-uniform particle scaling

The 3D Start Size property allows you to specify a particle’s width, height
and depth independently. In the Particle System **Main** module, check the
**3D Start Size** checkbox, and enter the values for the initial x (width), y
(height) and z (depth) of the particle. Note that z (depth) only applies to 3D
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) particles. You can also set randomised
values for these properties, in a range between two constants or curves.

You can set the particle’s initial size in the Particle System **Main**
module, and its size over the particle’s lifetime using the **Separate Axes**
option in the **Size over Lifetime** module. You can also set the particle’s
size in relation to its speed using the **Separate Axes** option in the **Size
by Speed** module.

## Simulation Space

The **Simulation Space** property determines whether the particles move with
the Particle System parent object, a custom object, or independently in the
game world. For example, systems like clouds, hoses and flamethrowers need to
be set independently of their parent **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), as they tend to leave trails that
persist in the world space even if the object producing them moves around. On
the other hand, if particles are used to create a spark between two
electrodes, the particles should move along with the parent object. For more
advanced control over how particles follow their Transform, see documentation
on the [Inherit Velocity module](PartSysInheritVelocity.html).

When set to Custom, particles no longer move relative to their own **Transform
component** A Transform component determines the Position, Rotation, and Scale
of each object in the scene. Every GameObject has a Transform. [More
info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent). Instead, they all move
relative to the movement of the specified Transform component. The Particle
System uses the Custom Transform to calculate emitter velocity, which the
Inherit Velocity module and **Rate over Distance** property of the Emission
module use to control particle velocity and emission.

[](particle-emissions-emitters.html)

Particle emissions and emitters

[](particle-movement.html)

Particle movement

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

