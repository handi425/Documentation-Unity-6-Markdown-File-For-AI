[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [中文](/cn/current/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/2d-joint-constraints.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [中文](/cn/current/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/2d-joint-constraints.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/2d-joint-constraints.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * 2D joint constraints

[](../../2d-physics/joints/introduction-to-2d-joints.html)

Introduction to 2D joints

[](../../2d-physics/joints/distance-joint-2d-landing.html)

Distance Joint 2D

# 2D joint constraints

A constraint is a rule which a **joint** A physics component allowing a
dynamic connection between Rigidbody components, usually allowing some degree
of movement such as a hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) will try to ensure isn’t
permanently broken. There are different types of constraints, and all joints
provide at least one constraint that apply to and govern the **Rigidbody** A
component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2D behavior. Some constraints
limit behavior such as ensuring a Rigidbody stays on a line, or in a certain
position. Some are ‘driving’ constraints which actively compel a Rigidbody
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) to behave in a certain way,
such as trying to make a GameObject maintain a certain speed.

## Temporarily breaking constraints

Unity’s physics system expects that constraints can be temporarily broken,
such as when the objects move further apart than their set distance constraint
or move faster than their set speed constraint. When a constraint isn’t
broken, the joint doesn’t apply any forces. When a constraint is broken, the
joint applies forces to fix the constraint.

For example, with ‘driving’ constraints, the joint applies forces to maintain
the distance or ensure the speed set by the constraint. While this application
of force is typically performed quickly, it doesn’t always instantly fix the
constraint and instead it fixes the constraint gradually over time. This can
lead to joints appearing to stretch or appear less rigid. The lag happens
because the physics system is trying to apply joint forces to fix constraints,
while other physics forces are simultaneously still acting to break those same
constraints. In addition to the conflicting forces acting on GameObjects, some
joints are more stable and react faster than others.

Whatever constraints the joint provides, the joint only uses forces to fix the
constraint. These are either a linear (straight line) force or angular
(torque) force.

**Note** : It’s recommended to be cautious when applying large forces to
Rigidbody objects that have joints attached, especially those with large
masses, due to the conflicting forces acting on joints.

## Permanently breaking joints

All joints are able to monitor the force or torque that they’re applying to
stay within its own constraints. Some joints monitor both force and torque
while others monitor only force. This informs you of when a joint exceeds a
specific force or torque in trying to maintain its constraints, and you can
specify these thresholds as
[`Joint2D.breakForce`](../../../ScriptReference/Joint2D-breakForce.html) and
[`Joint2D.breakTorque`](../../../ScriptReference/Joint2D-breakTorque.html).
When a joint exceeds these thresholds, it’s known as joint breaking.

You can specify the action to be taken when a joint breaks with
[`Joint2D.breakAction`](../../../ScriptReference/Joint2D-breakAction.html).
The default break action is to destroy the Joint2D component, and you can
refer to
[`JointBreakAction2D`](../../../ScriptReference/JointBreakAction2D.html) for
other available fixed actions.

## Additional resources

  * [API documentation on Joint2D](../../../ScriptReference/Joint2D.html)

[](../../2d-physics/joints/introduction-to-2d-joints.html)

Introduction to 2D joints

[](../../2d-physics/joints/distance-joint-2d-landing.html)

Distance Joint 2D

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

