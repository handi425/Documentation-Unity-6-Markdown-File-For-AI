[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-emissions-emitters.html)
  * [中文](/cn/current/Manual/particle-emissions-emitters.html)
  * [日本語](/ja/current/Manual/particle-emissions-emitters.html)
  * [한국어](/kr/current/Manual/particle-emissions-emitters.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-emissions-emitters.html)
  * [中文](/cn/current/Manual/particle-emissions-emitters.html)
  * [日本語](/ja/current/Manual/particle-emissions-emitters.html)
  * [한국어](/kr/current/Manual/particle-emissions-emitters.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * Particle emissions and emitters

[](configuring-particles.html)

Configuring particles

[](configuring-global-particle-properties.html)

Configuring global particle properties

# Particle emissions and emitters

Understand particle emissions, and how Unity manages them via **Particle
System** A component that simulates fluid entities such as liquids, clouds and
flames by generating and animating large numbers of small 2D images in the
scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) modules.

## Rate of emission

The rate of emission can be constant or can vary over the lifetime of the
system according to a curve. If the [Emission
module](PartSysEmissionModule.html) **Rate over Distance** mode is active, a
certain number of particles are released per unit of distance moved by the
parent object. This is very useful for simulating particles that are actually
created by the motion of the object (for example, dust from a car’s wheels on
a dirt track).

If **Rate over Time** is active, then the desired number of particles are
emitted each second regardless of how the parent object moves. Additionally,
you can add bursts of extra particles that appear at specific times (for
example, a steam train chimney that produces puffs of smoke).

## Emitter shape

The [Shape](PartSysShapeModule.html) module defines the volume or surface from
which [particles](class-ParticleSystem.html)A small, simple image or mesh that
is emitted by a particle system. A particle system can display and move
particles in great numbers to represent a fluid or amorphous entity. The
effect of all the particles together creates the impression of the complete
entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) can be emitted, and the direction of
the start velocity. The **Shape** property defines the shape of the emission
volume, and the rest of the module properties vary depending on the Shape you
choose.

All shapes (except [Mesh](class-Mesh.html)) have properties that define their
dimensions, such as the **Radius** property. To edit these, drag the handles
on the wireframe emitter shape in the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. The choice of shape affects the
region from which particles can be launched, but also the initial direction of
the particles. For example, a **Sphere** emits particles outward in all
directions, a **Cone** emits a diverging stream of particles, and a **Mesh**
The main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) emits particles in directions that are
normal to the surface.

### Configuring mesh-based emitter shapes

You can choose to only emit particles from a particular material (sub-Mesh) by
checking the **Single Material** property and you can offset the emission
position along the Mesh’s normals by checking the **Normal Offset** property.

To ignore the color of the Mesh, check the **Use Mesh Colors** property. To
read the texture colors from a mesh, assign the Texture you wish to read to
the **Texture** An image used when rendering a GameObject, Sprite, or UI
element. Textures are often applied to the surface of a mesh to give it visual
detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) property.

Meshes must be read/write enabled to work on the Particle System. If you
assign them in the Editor, Unity handles this for you. But if you want to
assign different meshes at run time, you need to check the **Read/Write
Enabled** setting in the [Import Settings](FBXImporter-Model.html).

The **Mode** property allows the Particle System to emit particles in a
predictable order on the surface of a Mesh. When emitting from Vertices, this
property allows you to emit each new particle from the next vertex in the
array of vertices in the Mesh. When emitting from Edges, the Particle System
can emit particles smoothly along the edges of the Mesh’s triangles/lines.

## Particle lifetime based on emitter speed

The [Lifetime by Emitter Speed](PartSysLifetimeByEmitterSpeedModule.html)
controls the initial lifetime of each particle based on the speed of the
emitter when the particle spawns. It multiplies the start lifetime of
particles by a value that depends on the speed of the object that spawned
them. For most Particle Systems, this is the **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) velocity, but for sub-emitters,
the velocity comes from the parent particle that the sub-emitter particle
originated from.

## Particle emissions from other particles

Many types of particles produce effects at different stages of their lifetimes
that can also be implemented using Particle System [Sub
Emitters](PartSysSubEmitModule.html). For example, a bullet might be
accompanied by a puff of smoke powder as it leaves the gun barrel, and a
fireball might explode on impact. You can use sub-emitters to create effects
like these.

Sub-emitters are ordinary Particle System objects created in the scene. This
means that sub-emitters can have sub-emitters of their own (this type of
arrangement can be useful for complex effects like fireworks). However, it is
very easy to generate an enormous number of particles using sub-emitters,
which can be resource-intensive.

To trigger a sub-emitter, you can use these are the conditions:

  * **Birth** : When the particles are created.
  * **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision): When the particles collide with an
object.

  * **Death** : When the particles are destroyed.
  * **Trigger** : When the particles interact with a Trigger **collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).

  * **Manual** : Only triggered when requested via script. See [ParticleSystem.TriggerSubEmitter](../ScriptReference/ParticleSystem.TriggerSubEmitter.html).

Note that the **Collision** , **Trigger** , **Death** and **Manual** events
can only use burst emission in the [Emission](PartSysEmissionModule.html)
module.

Additionally, you can transfer properties from the parent particle to each
newly created particle using the **Inherit** options. The transferrable
properties are size, rotation, color and lifetime. To control how velocity is
inherited, configure the [Inherit Velocity](PartSysInheritVelocity.html)
module on the sub-emitter system.

It is also possible to configure a probability that a sub-emitter event will
trigger, by setting the **Emit Probability** property. A value of 1 guarantees
that the event will trigger, whereas lower values reduce the probability.

## Additional resources

  * [Shape Module reference](PartSysShapeModule.html)
  * [Emission Module reference](PartSysEmissionModule.html)
  * [Sub Emitters Module reference](PartSysSubEmitModule.html)
  * [Lifetime By Emitter Speed Module reference](PartSysLifetimeByEmitterSpeedModule.html)

[](configuring-particles.html)

Configuring particles

[](configuring-global-particle-properties.html)

Configuring global particle properties

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

