[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/wheel-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Wheel Joint 2D](../../2d-physics/joints/wheel-joint-2d-landing.html)
  * Wheel Joint 2D fundamentals

[](../../2d-physics/joints/wheel-joint-2d-landing.html)

Wheel Joint 2D

[](../../2d-physics/joints/wheel-joint-2d-reference.html)

Wheel Joint 2D

# Wheel Joint 2D fundamentals

Use this **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) to simulate wheels and
suspension. The aim of the joint is to keep the position of two points on a
line that extends to infinity, whilst at the same time making them overlap.
Those two points can be two **Rigidbody2D** components or a **Rigidbody2D**
component and a fixed position in the world. (Connect to a fixed position in
the world by setting **Connected Rigidbody** to None).

Wheel Joint 2D acts like a combination of a [Slider Joint 2D](./slider-
joint-2d-reference.html) (without its motor or limit constraints) and a [Hinge
Joint 2D](./hinge-joint-2d-reference.html) (without its limit constraint).

The joint applies a linear force to both connected rigid body objects to keep
them on the line, an angular motor to rotate the objects on the line, and a
spring to simulate wheel suspension.

Set the **Maximum Motor Speed** and **Maximum Motor Force** (torque, in this
joint) to control the angular motor speed, and make the two rigid body objects
rotate.

You can set the wheel suspension stiffness and movement in order to simulate
different degrees of suspension. For example, to simulate a stiff, barely
moving suspension:

  * Set a high (1,000,000 is the highest) **Frequency** == stiff suspension.

  * Set a high (1 is the highest) ****Damping Ratio** A joint setting to control spring oscillation. A higher damping ratio means the spring will come to rest faster. [More info](../../2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#DampingRatio)** == barely moving
suspension.

To simulate a looser and more freely moving suspension, you would use the
following settings:

  * Set a low **Frequency** == loose suspension.

  * Set a low **Damping Ratio** == moving suspension.

It has two simultaneous constraints:

  * Maintain a zero relative linear distance away from a specified line between two anchor points on two rigid body objects.
  * Maintain an angular speed between two anchor points on two rigid body objects. (Set the speed via the **Maximum Motor Speed** option and maximum torque via **Maximum Motor Force**.)

You can use this joint to construct physical objects that need to react as if
they are connected with a rotational pivot but cannot move away from a
specified line. Such as:

  * Simulating wheels with a motor to drive the wheels and a line defining the movement allowed for the suspension.

## Behavior difference to the Wheel Collider

Unlike the [Wheel Collider](../../class-WheelCollider.html)A special collider
for grounded vehicles. It has built-in collision detection, wheel physics, and
a slip-based tire friction model. It can be used for objects other than
wheels, but it is specifically designed for vehicles with wheels. [More
info](../../class-WheelCollider.html)  
See in [Glossary](../../Glossary.html#WheelCollider) used with 3D physics, the
Wheel Joint 2D uses a separate ****Rigidbody** A component that allows a
GameObject to be affected by simulated gravity and other forces. [More
info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody)** object for the wheel, which
rotates when the force is applied. (The Wheel Collider, by contrast, simulates
the suspension using a raycast and the wheel’s rotation is purely a graphical
effect). The wheel object will typically be a [Circle Collider
2D](../collider/circle-collider-2d-reference.html) with a [Physics Material
2D](../physics-material-2d-reference.html)Use to adjust the friction and
bounce that occurs between 2D physics objects when they collide [More
info](../../2d-physics/physics-material-2d-reference.html)  
See in [Glossary](../../Glossary.html#PhysicsMaterial2D) that gives the right
amount of traction for your gameplay.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Wheel Joint 2D component reference](wheel-joint-2d-reference.html)

WheelJoint2D

[](../../2d-physics/joints/wheel-joint-2d-landing.html)

Wheel Joint 2D

[](../../2d-physics/joints/wheel-joint-2d-reference.html)

Wheel Joint 2D

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

