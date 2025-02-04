[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-HingeJoint.html)
  * [中文](/cn/current/Manual/class-HingeJoint.html)
  * [日本語](/ja/current/Manual/class-HingeJoint.html)
  * [한국어](/kr/current/Manual/class-HingeJoint.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-HingeJoint.html)
  * [中文](/cn/current/Manual/class-HingeJoint.html)
  * [日本語](/ja/current/Manual/class-HingeJoint.html)
  * [한국어](/kr/current/Manual/class-HingeJoint.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Joints](joints-section.html)
  * Hinge Joint component reference

[](class-FixedJoint.html)

Fixed Joint component reference

[](class-SpringJoint.html)

Spring Joint component reference

# Hinge Joint component reference

[Switch to Scripting](../ScriptReference/HingeJoint.html "Go to HingeJoint
page in the Scripting Reference")

The **Hinge**Joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint)** groups together two
[Rigidbodies](class-Rigidbody.html)A component that allows a GameObject to be
affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody), constraining them to move like
they are connected by a hinge. It is perfect for doors, but can also be used
to model chains, pendulums, and other objects that have a similar hinge-like
motion.

A single **Hinge Joint** should be applied to a ****GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)**. The hinge rotates at the point
specified by the **Anchor** property, moving around the specified **Axis**
property.

The Hinge Joint has **Spring** , **Motor** , and **Limits** properties, which
allow you to fine-tune the joint’s behaviors.

## Properties

**Property:** | **Function:**  
---|---  
**Edit Angular Limits** | Adds a visual **gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) to the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view that helps you edit joint angular
limits. To use this gizmo, set the **Angular X, Y, Z Motion** to **Limited**
and then handles appear for you to drag and adjust the joint’s rotational
space.  
**Connected Body** | Optional reference to the Rigidbody that the joint is dependent upon. If you do not assign a **Connected Body** or **Connected Articulation Body** , the joint connects to the world.   
  
You can use connected bodies to string multiple Hinge Joints together to
create a chain. Add a joint to each link in the chain, and attach the next
link as the **Connected Body**.  
**Connected Articulation Body** | Optional reference to the ArticulationBody that the joint is dependent upon. If not set, the joint connects to the world.  
**Anchor** | The position of the axis around which the body swings. The position is defined in local space. For example, for a normal door hinge, the **Anchor** is at the intersection between the door and the wall. For a door that is connected to the normal door, like a cat flap or a pet door, the normal door should be assigned as the pet door’s **Connected Body** , so that the pet door’s hinge is connected to the main door’s Rigidbody, rather than to a fixed point in world space.  
**Axis** | The direction of the axis around which the body swings. The direction is defined in local space. For example, for a door that opens at the side, like a normal door hinge, the **Axis** is up, positive along the Y axis. For a door that opens from the bottom or top, like a cat flap or a pet door, the **Axis** is sideways, positive along the relative X axis.  
**Auto Configure Connected Anchor** | If this is enabled, Unity calculates the Connected Anchor position automatically to match the global position of the anchor property. This is the default behavior. If this is disabled, you can configure the position of the connected anchor manually.  
**Connected Anchor** | Manual configuration of the connected anchor position.  
**Use Spring** | Spring makes the Rigidbody reach for a specific angle compared to its connected body.   
  
**Spring** and **Motor** are intended to be mutually exclusive. Using both at
the same time leads to unpredictable results.  
**Spring** | Properties of the Spring that are used if **Use Spring** is enabled.  
| **Spring** | The force the object asserts to move into the position.  
| **Damper** | The higher this value, the more the object slows down.  
| ****Target Position** A joint property to set the target position that the
joint’s drive force should move it to. [More info](class-
ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetPosition)** | Target angle of the spring. The spring pulls towards this angle measured in degrees.  
**Use Motor** | The motor makes the object spin around.   
  
**Spring** and **Motor** are intended to be mutually exclusive. Using both at
the same time leads to unpredictable results.  
**Motor** | Properties of the Motor that are used if **Use Motor** is enabled.  
| ****Target Velocity** A joint property to set the desired velocity with
which the joint should move to the Target Position under the drive force.
[More info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetVelocity)** | The speed the object tries to attain.  
| **Force** | The force applied in order to attain the speed.  
| **Free Spin** | If enabled, the motor never decreases the rate of acceleration.  
**Use Limits** | If enabled, the angle of the hinge is restricted within the **Min** & **Max** values.  
**Extended Limits** | Activate to extend the angle of the hinge to 360 degrees in either direction (that is, a limit of [–360, 360]).  
**Use Acceleration** | Activate to make the Hinge Joint’s spring output acceleration rather than force.  
**Limits** | Properties of the Limits that are used if **Use Limits** is enabled.  
| **Min** | The lowest angle the rotation can go.  
| **Max** | The highest angle the rotation can go.  
| **Bounciness** | How much the object bounces when it hits the minimum or maximum stop limit.  
| ****Contact Distance** A joint limit property that sets the minimum distance
tolerance between the joint position and the limit at which the limit will be
enforced. [More info](class-CharacterJoint.html)  
See in [Glossary](Glossary.html#ContactDistance)** | Within the contact distance from the limit contacts persist in order to avoid jitter.  
**Break Force** | The force that needs to be applied for this joint to break.  
**Break Torque** | The torque that needs to be applied for this joint to break.  
**Enable**Collision** A collision occurs when the physics engine detects that
the colliders of two GameObjects make contact or overlap, when at least one
has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision)** | When checked, this enables collisions between bodies connected with a joint.  
**Enable Preprocessing** | Disabling preprocessing helps to stabilize impossible-to-fulfil configurations.  
**Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the Rigidbody, ranging from 0.00001 to infinity. This is useful when the joint connects two Rigidbodies of largely varying mass. The physics solver produces better results when the connected Rigidbodies have a similar mass. When your connected Rigidbodies vary in mass, use this property with the **Connect Mass Scale** property to apply fake masses to make them roughly equal to each other. This produces a high-quality and stable simulation, but reduces the physical behaviour of the Rigidbodies.  
**Connected Mass Scale** | The scale to apply to the inverted mass and inertia tensor of the connected Rigidbody, ranging from 0.00001 to infinity.  
  
HingeJoint

[](class-FixedJoint.html)

Fixed Joint component reference

[](class-SpringJoint.html)

Spring Joint component reference

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

