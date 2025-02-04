[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ArticulationBody.html)
  * [中文](/cn/current/Manual/class-ArticulationBody.html)
  * [日本語](/ja/current/Manual/class-ArticulationBody.html)
  * [한국어](/kr/current/Manual/class-ArticulationBody.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ArticulationBody.html)
  * [中文](/cn/current/Manual/class-ArticulationBody.html)
  * [日本語](/ja/current/Manual/class-ArticulationBody.html)
  * [한국어](/kr/current/Manual/class-ArticulationBody.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Articulations](articulations-section.html)
  * Articulation Body component reference

[](physics-articulations.html)

Introduction to physics articulations

[](ragdoll-physics-section.html)

Ragdoll physics

# Articulation Body component reference

[Switch to Scripting](../ScriptReference/ArticulationBody.html "Go to
ArticulationBody page in the Scripting Reference")

Articulation Bodies enable you to build [physics articulations](physics-
articulations.html) such as robotic arms or kinematic chains with
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that are hierarchically organized.
They help you get realistic physics behaviors in the context of simulation for
industrial applications.

## Properties

An Articulation Body allows you to define in one single component the
properties that you would similarly define through a
[RigidBody](RigidbodiesOverview.html)A component that allows a GameObject to
be affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) and a [regular Joint](Joints.html)
in a classic configuration. That said, these properties depend on the
GameObject position in the hierarchy:

  * For the root GameObject of the articulation, you can only set up physical body properties:

![](../uploads/Main/articulation-body-properties-root.png)

  * For any child GameObject within the articulation, you can set up physical body properties as well as the type and properties of the **joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) that links this GameObject to its
parent GameObject:

![](../uploads/Main/articulation-body-properties-child.png)

The Articulation Body properties fall into the following main categories:

  * Physical body properties

  * Joint anchor properties

  * Joint type selection and properties

  * Joint drive properties

### Physical body properties

Define the way the Articulation Body responds to the physics environment.

![](../uploads/Main/articulation-body-properties-physical-body.png) Property | Function  
---|---  
**Mass** | The mass of the Articulation Body (in kilograms by default).  
**Immovable** | Use this property to define whether this articulation body is movable or not. You can set this property only for the root Articulation Body. This property is useful to make the base body of robotic hands immovable, for example. The **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) solves it separately from all
the other constraints and guarantees that it is not violated.  
**Use Gravity** | Use this property to make the gravity affect this Articulation Body or not.  
  
### Joint anchor properties

Define the coordinates of the joint anchors for the Articulation Body and its
parent Articulation Body.

![](../uploads/Main/articulation-body-properties-joint-anchor.png) Property | Function  
---|---  
**Compute Parent Anchor** | Enable this property to make the parent-relative anchor match the anchor of the current Articulation Body. If you disable this property, you can separately set values for **Parent Anchor Position** and **Parent Anchor Rotation**.  
**Anchor Position** | The position coordinates of the Anchor, relative to the current Articulation Body.  
**Anchor Rotation** | The rotation coordinates of the Anchor, relative to the current Articulation Body.  
**Parent Anchor Position** | The position coordinates of the Parent Anchor, relative to the parent Articulation Body. This property only appears if you disable **Compute Parent Anchor**.  
**Parent Anchor Rotation** | The rotation coordinates of the Parent Anchor, relative to the parent Articulation Body. This property only appears if you disable **Compute Parent Anchor**.  
**Snap Anchor to closest contact** | Computes the point on the surface of this Articulation Body that is closest to the **center of mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](../ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](Glossary.html#CenterofMass) of the parent Articulation Body,
and sets the anchor to it. If **Compute Parent Anchor** is enabled, Unity also
updates the parent anchor accordingly.  
  
### Joint type selection and joint properties

Select the type of joint that links the current Articulation Body to its
parent Articulation Body, and define its common and specific properties.

![](../uploads/Main/articulation-body-properties-joint-type.png) Property |  | Function  
---|---|---  
**Articulation Joint Type** |  | The type of joint that connects this Articulation Body to its parent Articulation Body. **Note:** All types of joints have in common the properties that this table describes, and some of them have specific additional properties.  
| Fixed | Sets a rigid, unbreakable and unstretchable link between bodies. A Fixed articulation joint has no additional properties than the ones that this table describes.  
| Prismatic | Prevents all motion except sliding along a particular axis. See also the Prismatic joint additional properties.  
| Revolute | Allows rotation around a particular axis (like a hinge). See also the Revolute joint additional properties.  
| Spherical | Anatomical joint, which allows two swings and one twist. See also the Spherical joint additional properties.  
**Linear Damping** |  | Coefficient that controls the linear slow down.  
**Angular Damping** |  | Coefficient that controls the rotational slow down.  
**Joint Friction** |  | Coefficient that controls the energy loss caused by friction in the joint.  
  
#### Prismatic joint additional properties

![](../uploads/Main/articulation-body-properties-joint-prismatic.png) Property |  | Function  
---|---|---  
**Axis** |  | Specifies the axis that the prismatic joint allows motion along, relative to the parent anchor.  
**Motion** |  | Specifies the motion restriction type along that axis.  
| Free | Allows the Articulation Body to freely move along the selected **Axis** of the parent anchor.  
| Limited | Restricts the movement of the Articulation Body along the selected **Axis** of the parent anchor, according to the **Lower Limit** and **Upper Limit** you specify in the **Drive** properties.  
**X Drive** , **Y Drive** , or **Z Drive** |  | The properties of the linear drive that is attached to the joint, according to the selected **Axis** of the parent anchor. **Note:** There is only one Drive section here. Its title automatically adjusts according to the axis selection.  
  
#### Revolute joint additional properties

![](../uploads/Main/articulation-body-properties-joint-revolute.png) Property |  | Function  
---|---|---  
**Motion** |  | Specifies the rotation restriction type around the X axis of the parent anchor.  
| Free | Allows the Articulation Body to freely rotate around the X axis of the parent anchor.  
| Limited | Restricts the rotation of the Articulation Body around the X axis of the parent anchor, according to the **Lower Limit** and **Upper Limit** you specify in the **X Drive** properties.  
**X Drive** |  | The properties of the rotational drive that is attached to the joint, around the X axis of the parent anchor.  
  
#### Spherical joint additional properties

![](../uploads/Main/articulation-body-properties-joint-spherical.png) Property |  | Function  
---|---|---  
**Swing Y** |  | Specifies the rotation restriction type around the Y axis.  
| Free | Allows the Articulation Body to freely rotate around the Y axis of the parent anchor.  
| Limited | Restricts the rotation of the Articulation Body around the Y axis of the parent anchor, according to the **Lower Limit** and **Upper Limit** you specify in the **Y Drive** properties.  
| Locked | Totally locks the rotation of the Articulation Body around the Y axis of the parent anchor. **Note:** You cannot lock more than two degrees of freedom at the same time.  
**Swing Z** |  | Specifies the rotation restriction type around the Z axis. The options are the same for all 3 axes.  
**Twist** |  | Specifies the rotation restriction type around the X axis. The options are the same for all 3 axes.  
**Y Drive** , **Z Drive** , and **X Drive** |  | The properties of the rotational drive that is attached to the joint, respectively around the Y, Z and X axes of the parent anchor. **Note:** There is a separate subsection for each drive. If you lock an axe, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) does not display its Drive
properties.  
  
### Joint drive properties

Set up joint limits about a specific axis, as well as the joint drive effect
parameters for this axis.

![](../uploads/Main/articulation-body-properties-joint-drive.png) Property | Function  
---|---  
**Lower Limit** | The limit below which the joint prevents the body from moving or rotating, depending on the joint type. You can define this property only if you set the related **Motion** , **Swing** or **Twist** property to **Limited**.  
**Upper Limit** | The limit above which the joint prevents the body from moving or rotating, depending on the joint type. You can define this property only if you set the related **Motion** , **Swing** or **Twist** property to **Limited**.  
**Stiffness** | The stiffness of the spring that attracts the joint to the target.  
**Damping** | The damping of the spring that attracts the joint to the target.  
**Force limit** | The maximum amount of force or torque this drive can produce.  
**Target** | The target value this drive aims to reach.  
****Target velocity** A joint property to set the desired velocity with which
the joint should move to the Target Position under the drive force. [More
info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetVelocity)** | The target velocity this drive aims to reach.  
  
## Configuring articulation joints

### Joint drive effect

Any drive is an implicit 1D spring that aims to bring the current drive
parameters to the target by the application of an effect (forces or torques)
computed by this formula:

**Effect = stiffness * (targetPosition - drivePosition) + damping *
(targetVelocity - driveVelocity)**

A drive attached to a linear degree of freedom produces forces. A drive
attached to a rotational degree of freedom produces torques. You can set each
parameter of this formula through the Joint drive properties to fine-tune the
desired effect for any axis involved in a joint.

Notice that the effect formula consists of two independent terms that you can
balance, and even cancel out. For example:

  * If you set the stiffness to zero, you get a drive that only aims at reaching a specific velocity.

  * If you set the damping to zero, you get a drive that aims at reaching a certain position without trying to reach any particular velocity. In that case, the drive does not try to eventually stop once the target is reached.

## Joint anchors

There are two anchors per each joint:

  * The **Anchor** , relative to the current Articulation Body

  * The **Parent Anchor** , relative to the parent Articulation Body

By default, Unity automatically computes the Parent Anchor to match the pose
of the Anchor. However, you can disable the **Compute Parent Anchor** property
to manually set the Parent Anchor:

![](../uploads/Main/articulation-body-properties-joint-anchors.png)

Currently, the Unity Editor displays the anchors with a scaled transform tool
to differentiate them from the GameObject transform tool:

![](../uploads/Main/articulation-body-joint-anchor-tools.png)

To change the position of the anchors, you can either use the Inspector and
edit the Joint anchor properties or directly move and rotate their transform
tools in the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View.

**Note:** When you create a new Articulation Body, Unity positions the anchors
at the local zero of their respective bodies. However, the local zero is not
an ideal default position for the anchor if the connected bodies have
**colliders** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) attached, because the joint might
then try to push the bodies into each other. The **Snap Anchor to closest
contact** button helps you set a more reasonable default location of the
anchors, which works with many articulations.

### Joint degrees of freedom and limits

**Note:** Currently, the **Scene View** An interactive view into the world you
are creating. You use the Scene View to select and position scenery,
characters, cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) allows you to visualize the joint
limits but not to manipulate them graphically.

#### Fixed joint

A **fixed joint** A joint type that is completely constrained, allowing two
objects to be held together. Implemented as a spring so some motion may still
occur. [More info](class-FixedJoint.html)  
See in [Glossary](Glossary.html#FixedJoint) has no degrees of freedom, so the
Scene View displays no specific markers.

#### Prismatic joint

A prismatic joint is practically a slider along a specified axis relative to
the parent anchor. This axis can only be a basis axis (X, Y, or Z) but you can
still rotate the parent anchor to get a different axis orientation in world
space.

You can set up a prismatic joint to have a free or limited translation. To do
this, use the Inspector and edit the prismatic joint specific properties.

**Note:** You cannot lock a prismatic joint, otherwise this would remove its
only degree of freedom and would make it a degenerate joint.

When you set the prismatic joint **Motion** to **Limited** , the Scene View
displays markers to represent the translation limits:

  * The small red marker represents the lower limit.

  * The small green marker represents the upper limit.

  * The dotted white line materializes allowed translation between the limits.

To manipulate the joint limits, you must use the Inspector and edit their
values in the Joint drive properties.

![](../uploads/Main/articulation-body-joint-prismatic-limited.png)  
_Example of a limited prismatic joint._

**Note:** The Scene View displays no specific markers when you set the
prismatic joint **Motion** to **Free**.

#### Revolute joint

A revolute joint is essentially a hinge with a single rotational degree of
freedom around the parent anchor’s X axis. You can still rotate the parent
anchor to get a different axis orientation in world space.

You can set up a revolute joint to have a free or limited rotation. To do
this, use the Inspector and edit the revolute joint specific properties.

**Note:** You cannot lock a revolute joint, otherwise this would remove its
only degree of freedom and would make it a degenerate joint.

When you set the revolute joint **Motion** to **Free** , the Scene View
displays a red disk to represent the free rotation allowed around the X axis.

![](../uploads/Main/articulation-body-joint-revolute-free.png)  
_Example of a free revolute joint._

When you set the revolute joint **Motion** to **Limited** , the Scene View
displays markers to represent the rotation limits:

  * The small red marker represents the lower limit.

  * The small green marker represents the upper limit.

  * The red circle sector materializes the allowed rotation angle between the limits.

  * The Z axis of the parent anchor serves as the reference (zero) for both limit angles.

To manipulate the joint limits, you must use the Inspector and edit their
values in the Joint drive properties.

![](../uploads/Main/articulation-body-joint-revolute-limited.png)  
_Example of a limited revolute joint._

#### Spherical joint

A spherical joint is an anatomical joint that is best suited for simulating
humanoid limbs.

This joint type can have up to three rotational degrees of freedom. You can
set up each of these rotations to be free, limited, or locked. To do this, use
the Inspector and edit the revolute joint specific properties.

**Note:** You cannot lock all rotations at the same time for a spherical
joint, otherwise this would remove all its degrees of freedom and would make
it a degenerate joint. Also, you should not lock both swing axes to mimic a
revolute joint, because the simulation would happen differently than with the
revolute joint and would be more expensive.

Like with the revolute joint:

  * The Scene View displays free rotations with colored disks and limited rotations with colored circle sectors. Each color (red, green, blue) represents the rotation around the axis of this color (respectively: X, Y, Z).

  * The small red and green markers respectively represent the lower and upper limits.

![](../uploads/Main/articulation-body-joint-spherical-free.png)  
_Example of a free spherical joint._

![](../uploads/Main/articulation-body-joint-spherical-limited.png)  
_Example of a spherical joint with limited swings._

ArticulationBody

[](physics-articulations.html)

Introduction to physics articulations

[](ragdoll-physics-section.html)

Ragdoll physics

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

