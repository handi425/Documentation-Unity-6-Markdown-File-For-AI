[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/hinge-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Hinge Joint 2D](../../2d-physics/joints/hinge-joint-2d-landing.html)
  * Hinge Joint 2D fundamentals

[](../../2d-physics/joints/hinge-joint-2d-landing.html)

Hinge Joint 2D

[](../../2d-physics/joints/hinge-joint-2d-reference.html)

Hinge Joint 2D component reference

# Hinge Joint 2D fundamentals

The Hinge **Joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) 2D’s is used to have a joint that
allows a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) to rotate around a
particular point, for example a door hinge, wheels, or pendulums.

You can use this joint to make two points overlap. Those two points can be two
****Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2D** components, or a
**Rigidbody 2D** component and a fixed position in the world space. Connect
the **Hinge Joint** A joint that groups together two Rigidbody components,
constraining them to move like they are connected by a hinge. It is perfect
for doors, but can also be used to model chains, pendulums and so on. [More
info](../../class-HingeJoint.html)  
See in [Glossary](../../Glossary.html#HingeJoint) 2D to a fixed position in
the world by setting **Connected Rigidbody** to **None**. The joint applies a
linear force to both connected Rigidbody 2D GameObjects.

The Hinge Joint 2D has a simulated rotational motor which you can turn on or
off. Set the **Maximum Motor Speed** and **Maximum Motor Force** to control
the angular speed (**Torque**) and make the two Rigidbody 2D GameObjects
rotate in an arc relative to each other. Set the limits of the arc using
**Lower Angle** and **Upper Angle**.

## Constraints

Hinge Joint 2D has three simultaneous constraints. All are optional:

  * Maintain a relative linear distance between two anchor points on two Rigidbody 2D GameObjects.
  * Maintain an angular speed between two anchor points on two Rigidbody 2D GameObjects (limited with a maximum torque in **Maximum Motor Force**).
  * Maintain an angle within a specified arc.

You can use this joint to construct physical GameObjects that need to behave
as if they are connected with a rotational pivot. For example:

  * A see-saw pivot where the horizontal section is connected to the base. Use the joint’s **Angle Limits** to simulate the highest and lowest point of the see-saw’s movement.
  * A pair of scissors connected together with a hinge pivot. Use the joint’s **Angle Limits** to simulate the closing and maximum opening of the scissors.
  * A simple wheel connected to the body of a car with the pivot connecting the wheel at its center to the car. In this example you can use the Hinge Joint 2D’s motor to rotate the wheel.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Hinge Joint 2D component reference](hinge-joint-2d-reference.html)

[](../../2d-physics/joints/hinge-joint-2d-landing.html)

Hinge Joint 2D

[](../../2d-physics/joints/hinge-joint-2d-reference.html)

Hinge Joint 2D component reference

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

