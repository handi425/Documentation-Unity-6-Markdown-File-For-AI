[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-collisions.html)
  * [中文](/cn/current/Manual/particle-collisions.html)
  * [日本語](/ja/current/Manual/particle-collisions.html)
  * [한국어](/kr/current/Manual/particle-collisions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-collisions.html)
  * [中文](/cn/current/Manual/particle-collisions.html)
  * [日本語](/ja/current/Manual/particle-collisions.html)
  * [한국어](/kr/current/Manual/particle-collisions.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle physics](particle-physics.html)
  * Particle collisions

[](apply-forces-particles.html)

Apply forces to particles

[](particle-triggers.html)

Particle triggers

# Particle collisions

The [Collisions](PartSysCollisionModule.html) module controls how particles
collide with **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

When other objects surround a **Particle System** A component that simulates
fluid entities such as liquids, clouds and flames by generating and animating
large numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem), the effect is often more
convincing when the particles interact with those objects. For example, water
or debris should be obstructed by a solid wall rather than simply passing
through it. With the **Collision** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) module enabled, particles can
collide with objects in the Scene.

A Particle System can be set so its particles collide with any **Collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) in the scene by selecting **World**
The area in your scene in which all objects reside. Often used to specify that
coordinates are world-relative, as opposed to object-relative.  
See in [Glossary](Glossary.html#World) mode from the pop-up. Colliders can
also be disabled according to the layer they are on by using the **Collides
With** property. The pop-up also has a **Planes** mode option which allows you
to add a set of planes to the Scene that don’t need to have Colliders. This
option is useful for simple floors, walls and similar objects, and has a lower
processor overhead than **World** mode.

When **Planes** mode is enabled, a list of transforms (typically empty
GameObjects) can be added via the **Planes** property. The planes extend
infinitely in the objects’ local XZ planes, with the positive Y axis
indicating the planes’ normal vectors. To assist with development, the planes
will be shown as **Gizmos** A graphic overlay associated with a GameObject in
a Scene, and displayed in the Scene View. Built-in scene tools such as the
move tool are Gizmos, and you can create custom Gizmos using textures or
scripting. Some Gizmos are only drawn when the GameObject is selected, while
other Gizmos are drawn by the Editor regardless of which GameObjects are
selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) in the Scene, regardless of whether or
not the objects have any visible **Mesh** The main graphics primitive of
Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) themselves. The Gizmos can be shown as a
wireframe grid or a solid plane, and can also be scaled. However, the scaling
only applies to the visualization - the collision planes themselves extend
infinitely through the Scene.

When collisions are enabled, the size of a particle is sometimes a problem
because its graphic can be clipped as it makes contact with a surface. This
can result in a particle appearing to “sink” partway into a surface before
stopping or bouncing. The **Radius Scale** property addresses this issue by
defining an approximate circular radius for the particles, as a percentage of
its actual size. This size information is used to prevent clipping and avoid
the sinking-in effect.

The **Dampen** and **Bounce** properties are useful for when the particles
represent solid objects. For example, gravel will tend to bounce off a hard
surface when thrown but a snowball’s particles might lose speed during a
collision. **Lifetime Loss** and **Min Kill Speed** can help to reduce the
effects of residual particles following a collision. For example, a fireball
might last for a few seconds while flying through the air but after colliding,
the separate fire particles should dissipate quickly.

You can also detect particle collisions from a script if **Send Collision
Messages** is enabled. The script can be attached to the object with the
particle system, or the one with the Collider, or both. By detecting
collisions, you can use particles as active objects in gameplay, for example
as projectiles, magic spells and power-ups. See the script reference page for
[MonoBehaviour.OnParticleCollision](../ScriptReference/MonoBehaviour.OnParticleCollision.html)
for further details and examples.

### World Collision Quality

The World Collision module has a **Collision Quality** property, which you can
set to **High** , **Medium** or **Low**. When **Collision Quality** is set to
**Medium (Static Colliders)** or **Low (Static Colliders)** , collisions use a
grid of voxels (values on a 3D grid) to cache previous collisions, for fast
re-use in later frames.

This cache consists of a plane in each voxel, where the plane represents the
collision surface at that location. On each frame, Unity checks the cache for
a plane at the position of the particle, and if there is one, Unity uses it
for **collision detection** An automatic process performed by Unity which
determines whether a moving GameObject with a Rigidbody and collider component
has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection). Otherwise, it asks the
physics system. If a collision is returned, it is added to the cache for fast
querying on subsequent frames.

This is an approximation, so some missed collisions might occur. You can
reduce the Voxel Size value to help with this; however, doing so uses extra
memory, and is less efficient.

The only difference between **Medium** and **Low** is how many times per frame
the system is allowed to query the physics system. Low makes fewer queries per
frame than Medium. Once the per-frame budget has been exceeded, only the cache
is used for any remaining particles. This can lead to an increase in missed
collisions, until the cache has been more comprehensively populated.

[](apply-forces-particles.html)

Apply forces to particles

[](particle-triggers.html)

Particle triggers

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

