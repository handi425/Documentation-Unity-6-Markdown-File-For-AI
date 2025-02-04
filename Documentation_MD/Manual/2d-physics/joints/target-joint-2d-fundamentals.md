[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/target-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Target Joint 2D](../../2d-physics/joints/target-joint-2d-landing.html)
  * Target Joint 2D fundamentals

[](../../2d-physics/joints/target-joint-2d-landing.html)

Target Joint 2D

[](../../2d-physics/joints/target-joint-2d-reference.html)

Target Joint 2D

# Target Joint 2D fundamentals

Use this **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) to connect a **Rigidbody** A
component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) to a point in space. The aim
of this joint is to keep zero linear distance between two points: An anchor
point on a Rigidbody object and a world space position, called the “**Target**
”. The joint applies linear force to the Rigidbody object, it does not apply
torque (angular force).

The joint uses a simulated spring. You can set the spring’s stiffness and
movement by adjusting its settings. For example, to set a stiff and barely
moving spring:

  * Set a high (1,000,000 is the highest) **Frequency** == a stiff spring.

  * Set a high (1 is the highest) ****Damping Ratio** A joint setting to control spring oscillation. A higher damping ratio means the spring will come to rest faster. [More info](../../2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#DampingRatio)** == a barely moving
spring.

To simulate a looser and more freely moving spring, you would use the
following settings:

  * Set a low **Frequency** == a loose spring.

  * Set a low **Damping Ratio** == a moving spring.

When the spring applies its force between the Rigidbody object and target, it
tends to overshoot the distance you have set between them, and then rebound
repeatedly, giving in a continuous oscillation. The **Damping Ratio** sets how
quickly the Rigidbody object stops moving. The **Frequency** sets how quickly
the Rigidbody object oscillates either side of the distance you have
specified.

This joint has one constraint:

  * Maintain a zero linear distance between the anchor point on a Rigidbody object and a world space position (**Target**).

You can use this joint to construct physical objects that need to move to
designated target positions and stay there until another **target position** A
joint property to set the target position that the joint’s drive force should
move it to. [More info](../../class-ConfigurableJoint.html)  
See in [Glossary](../../Glossary.html#TargetPosition) is selected or the
target is cleared. For example:

  * A game where players pick up cakes, using a mouse-click, and drag them into to a plate. You can use this joint to move each cake to the plate.

You could also use the joint to allow objects to hang: If the anchor point is
not the **center of mass** Represents the average position of all mass in a
Rigidbody for the purposes of physics calculations. By default it is computed
from all colliders belonging to the Rigidbody, but can be modified via script.
[More info](../../../../../ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](../../Glossary.html#CenterofMass), then the object will
rotate. Such as:

  * A game where players pick up boxes. If they use a mouse-click to pick a box up by its corner and drag it, it will hang from the cursor.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Target Joint 2D component reference](target-joint-2d-reference.html)

TargetJoint2D

[](../../2d-physics/joints/target-joint-2d-landing.html)

Target Joint 2D

[](../../2d-physics/joints/target-joint-2d-reference.html)

Target Joint 2D

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

