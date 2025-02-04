[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RigidbodiesOverview.html)
  * [中文](/cn/current/Manual/RigidbodiesOverview.html)
  * [日本語](/ja/current/Manual/RigidbodiesOverview.html)
  * [한국어](/kr/current/Manual/RigidbodiesOverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RigidbodiesOverview.html)
  * [中文](/cn/current/Manual/RigidbodiesOverview.html)
  * [日本語](/ja/current/Manual/RigidbodiesOverview.html)
  * [한국어](/kr/current/Manual/RigidbodiesOverview.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Rigidbody physics](rigidbody-physics-section.html)
  * Introduction to rigid body physics 

[](rigidbody-physics-section.html)

Rigidbody physics

[](rigidbody-configure-colliders.html)

Configure Rigidbody Colliders

# Introduction to rigid body physics

In real-world physics, a rigid body is any physical body that does not deform
or change shape under physics forces. The distance between any two given
points of a rigid body remains constant in time, regardless of external forces
exerted on it.

To simulate physics-based behavior such as movement, gravity, **collision** A
collision occurs when the physics engine detects that the colliders of two
GameObjects make contact or overlap, when at least one has a Rigidbody
component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision), and joints, you need to configure
items in your **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as rigid bodies. To configure
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as rigid bodies in Unity’s PhysX
system, you can assign them the [Rigidbody](class-Rigidbody.html)A component
that allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component. The Rigidbody component
is represented in the API by the
[`Rigidbody`](../ScriptReference/Rigidbody.html) class.

## Rigid body GameObjects with physics-based movement

In Unity, a [Rigidbody](class-Rigidbody.html) component provides a physics-
based way to control the movement and position of a GameObject. Instead of the
[Transform](class-Transform.html) properties, you can use simulated physics
forces and torque to move the GameObject, and let the **physics engine** A
system that simulates aspects of physical systems so that objects can
accelerate correctly and be affected by collisions, gravity and other forces.
[More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) calculate the results.

In most cases, if a GameObject has a Rigidbody, you should use the Rigidbody
properties to move the GameObject, instead of the Transform properties. The
Rigidbody properties apply forces and torque from the physics system, which
change the GameObject’s Transform; if you then change the Transform directly,
Unity cannot correctly calculate the physics simulation, and you might see
unwanted behavior. This is particularly true of rigid bodies with
[Joints](joints-section.html)A physics component allowing a dynamic connection
between Rigidbody components, usually allowing some degree of movement such as
a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint).

Unity handles physics-based movement globally, not locally. When a GameObject
with a Rigidbody moves via physics-based movement, it moves independently of
any parent or child GameObject. A child GameObject that has a Rigidbody still
uses its parent GameObject to define its local position for initialization,
but Unity calculates its physics-based movement in global space.

To control a Rigidbody via script, the primary classes are
[`AddForce`](../ScriptReference/Rigidbody.AddForce.html) (to add forces to a
GameObject) and [`AddTorque`](../ScriptReference/Rigidbody.AddTorque.html) (to
apply torque to a GameObject).

## Rigid body GameObjects without physics-based movement

There are some cases where you might want the physics system to detect a
GameObject, but not to control it. For example, you might want
[Colliders](collision-section.html)An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) to detect a GameObject, but you
intend to control that GameObject’s movement and position via its
[Transform](class-Transform.html).

Movement in Unity that is not physics-based is called **kinematic motion**.
The Rigidbody component has the property **Is Kinematic** which, when enabled,
defines the attached GameObject as non-physics-based, and removes it from the
control of the physics engine. This allows you to move it kinematically via
the Transform without Unity’s physics simulation calculations overriding the
changes.

A kinematic Rigidbody can apply physics-based force to physics-based Rigidbody
GameObjects, but does not receive physics-based force. For example, a
kinematic Rigidbody can collide with and “push” a Rigidbody that has physics-
based movement, but a Rigidbody with physics-based movement cannot “push” a
kinematic Rigidbody.

If you use a [Joint](joints-section.html) to attach a kinematic Rigidbody to a
non-kinematic Rigidbody, the Joint cannot exert forces to move the kinematic
Rigidbody. It can only ever move the non-kinematic Rigidbody. However, you can
still move the kinematic Rigidbody via the Transform, and the Joint can adjust
the pose of the non-kinematic body to satisfy the joint limits.

## Rigidbody optimization

When a Rigidbody moves at a slower speed than the **Sleep Threshold** (see the
[Physics](class-PhysicsManager.html) Project Settings), Unity sets the
Rigidbody to “sleep”, which means that the physics system does not include it
in physics calculations. When a sleeping Rigidbody receives a collision or
force, Unity “wakes up” the Rigidbody and continues to include it in physics
calculations.

By default, the sleeping and waking of a Rigidbody component happens
automatically. However, you can also control this behavior yourself via
script, via the methods
[`Rigidbody.Sleep`](../ScriptReference/Rigidbody.Sleep.html) and
[`Rigidbody.WakeUp`](../ScriptReference/Rigidbody.WakeUp.html).

A Rigidbody might fail to wake up in response to movement and collisions from
static colliders (that is, colliders without a Rigidbody) that are moving via
the **Transform** position instead of the physics system. This is particularly
likely if the physics system can no longer detect the static collider. If this
happens, you can use
[`Rigidbody.WakeUp`](../ScriptReference/Rigidbody.WakeUp.html) to wake up the
sleeping Rigidbody.

For more information on how the PhysX physics system handles sleeping, see the
NVIDIA PhysX SDK Rigidbody Dynamics documentation on
[Sleeping](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/Manual/RigidBodyDynamics.html#sleeping).

[](rigidbody-physics-section.html)

Rigidbody physics

[](rigidbody-configure-colliders.html)

Configure Rigidbody Colliders

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

