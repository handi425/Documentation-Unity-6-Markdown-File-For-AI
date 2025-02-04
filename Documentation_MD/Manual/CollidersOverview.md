[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CollidersOverview.html)
  * [中文](/cn/current/Manual/CollidersOverview.html)
  * [日本語](/ja/current/Manual/CollidersOverview.html)
  * [한국어](/kr/current/Manual/CollidersOverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CollidersOverview.html)
  * [中文](/cn/current/Manual/CollidersOverview.html)
  * [日本語](/ja/current/Manual/CollidersOverview.html)
  * [한국어](/kr/current/Manual/CollidersOverview.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * Introduction to collision

[](collision-section.html)

Collision

[](collider-types-introduction.html)

Introduction to collider types

# Introduction to collision

In Unity, a **collision** happens when two **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that are configured for collision
occupy the same physical space. Collision is a foundational part of most
games, and many interactive applications and simulators.

To handle collision between GameObjects, Unity uses **colliders**. A
**collider** is a Unity component that defines the shape of a GameObject for
the purposes of physical collisions. Colliders are invisible, and do not need
to be the same shape as the GameObject’s mesh.

For guidance on how to add components to a GameObject, see [Use
Components](UsingComponents.html).

Each 3D collider has a 2D equivalent. In Unity, 2D and 3D physics run on
different physics simulation systems. For guidance on 2D physics colliders,
see [Collider 2D](2d-physics/collider/collider-2d-landing.html).

## Collider types

A collider’s type is based on the configuration of its GameObject’s Collider
and **Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components. This configuration
determines how a collider behaves, and how it interacts with other colliders.

  * Static colliders: The GameObject has a collider but no Rigidbody.
  * Rigidbody colliders: The GameObject has a collider and a Rigidbody. 
    * Dynamic colliders: The Rigidbody is dynamic (that is, it has **Is Kinematic** disabled).
    * Kinematic colliders: The Rigidbody is kinematic (that is, it has **Is Kinematic** enabled).

There is also a sub-type of collider called a **Trigger collider**. Trigger
colliders do not physically collide with other colliders; instead, Unity calls
a function when other colliders pass through them.

### Trigger colliders

Trigger colliders don’t cause collisions. Instead, they detect other Colliders
that pass through them, and call functions that you can use to initiate events
(see [Use collisions to trigger other events](collider-interactions-other-
events.html)).

To turn a collider into a trigger collider, enable the **Is Trigger** property
on the Collider component. A trigger collider does not collide with other
colliders; instead, other colliders pass through it.

For a trigger collider to work, at least one GameObject involved in the
collision must have a Rigidbody. Trigger colliders can be any collider type
(static or Rigidbody), but in most cases it’s good practice to make the
trigger collider a [static collider](collider-types-introduction.html). and
add a Rigidbody to the GameObject that passes through the trigger. If several
GameObjects are passing through one trigger, there must be a Rigidbody on at
least one GameObject in each collision pair.

Triggers can be any collider shape (see [Collider shapes](collider-
shapes.html)), and they can be visible or invisible. To make a trigger
invisible, add the collider to an empty GameObject. Only add a trigger to a
visible GameObject if it is okay for other GameObjects to visibly pass through
it.

For gameplay and simulation, triggers might need some adjustment to make them
feel intuitive for the player. For example, you could experiment with making a
trigger collider slightly larger than its associated visible GameObject, so
that it has a wider radius.

For information on how different collider types interact with each other on
collision, see [Interaction between collider types](collider-types-
interaction.html).

## Collider shapes

Collider components are available in different shape configurations. There are
three main shape types for colliders:

[Primitive colliders](primitive-colliders.html) are built-in simple shapes
that you can attach to your GameObject and scale to approximately the same
size and shape. You can also combine several primitive collider shapes to
create [compound colliders](compound-colliders.html). [Mesh colliders](mesh-
colliders.html)A free-form collider component which accepts a mesh reference
to define its collision surface shape. [More info](class-MeshCollider.html)  
See in [Glossary](Glossary.html#MeshCollider) exactly match the shape of the
GameObject’s [Mesh](mesh.html)The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). They are more accurate than primitive
colliders for complex shapes, but require more computational resources. [Wheel
colliders](wheel-colliders.html)A special collider for grounded vehicles. It
has built-in collision detection, wheel physics, and a slip-based tire
friction model. It can be used for objects other than wheels, but it is
specifically designed for vehicles with wheels. [More info](class-
WheelCollider.html)  
See in [Glossary](Glossary.html#WheelCollider) are raycast-based Colliders
specifically for in-game items that have physics-simulated wheels (for
example, vehicles). They have built-in wheel physics, and controls for
friction.

## Collider surfaces

You can control the friction and bounciness of a collider’s surface. When two
colliders meet, the physics system uses the properties of each surface to
calculate the friction and bounce between them.

For more information, see [Collider surfaces](collider-surfaces.html).

[](collision-section.html)

Collision

[](collider-types-introduction.html)

Introduction to collider types

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

