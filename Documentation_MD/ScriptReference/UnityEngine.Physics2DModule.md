[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# UnityEngine.Physics2DModule

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

The Physics2d module implements 2D physics in Unity.

### Classes

[AnchoredJoint2D](AnchoredJoint2D.html)| Parent class for all joints that have
anchor points.  
---|---  
[AreaEffector2D](AreaEffector2D.html)| Applies forces within an area.  
[BoxCollider2D](BoxCollider2D.html)| Collider for 2D physics representing an
axis-aligned rectangle.  
[BuoyancyEffector2D](BuoyancyEffector2D.html)| Applies forces to simulate
buoyancy, fluid-flow and fluid drag.  
[CapsuleCollider2D](CapsuleCollider2D.html)| A capsule-shaped primitive
collider.  
[CircleCollider2D](CircleCollider2D.html)| Collider for 2D physics
representing an circle.  
[Collider2D](Collider2D.html)| Parent class for collider types used with 2D
gameplay.  
[Collision2D](Collision2D.html)| Collision details returned by 2D physics
callback functions.  
[CompositeCollider2D](CompositeCollider2D.html)| A Collider that can merge
other Colliders together.  
[ConstantForce2D](ConstantForce2D.html)| Applies both linear and angular
(torque) forces continuously to the rigidbody each physics update.  
[CustomCollider2D](CustomCollider2D.html)| Represents a Collider2D that is
configured by assigning PhysicsShape2D geometry to it via a
PhysicsShapeGroup2D.  
[DistanceJoint2D](DistanceJoint2D.html)| Joint that keeps two Rigidbody2D
objects a fixed distance apart.  
[EdgeCollider2D](EdgeCollider2D.html)| Collider for 2D physics representing an
arbitrary set of connected edges (lines) defined by its vertices.  
[Effector2D](Effector2D.html)| A base class for all 2D effectors.  
[FixedJoint2D](FixedJoint2D.html)| Connects two Rigidbody2D together at their
anchor points using a configurable spring.  
[FrictionJoint2D](FrictionJoint2D.html)| Applies both force and torque to
reduce both the linear and angular velocities to zero.  
[HingeJoint2D](HingeJoint2D.html)| Joint that allows a Rigidbody2D object to
rotate around a point in space or a point on another object.  
[Joint2D](Joint2D.html)| Parent class for joints to connect Rigidbody2D
objects.  
[Physics2D](Physics2D.html)| Global settings and helpers for 2D physics.  
[PhysicsMaterial2D](PhysicsMaterial2D.html)| Asset type that defines the
surface properties of a Collider2D.  
[PhysicsSceneExtensions2D](PhysicsSceneExtensions2D.html)| Scene extensions to
access the underlying physics scene.  
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)| Represents a group of
PhysicsShape2D and their geometry.  
[PhysicsUpdateBehaviour2D](PhysicsUpdateBehaviour2D.html)| A base type for 2D
physics components that required a callback during FixedUpdate.  
[PlatformEffector2D](PlatformEffector2D.html)| Applies "platform" behaviour
such as one-way collisions etc.  
[PointEffector2D](PointEffector2D.html)| Applies forces to attract/repulse
against a point.  
[PolygonCollider2D](PolygonCollider2D.html)| Collider for 2D physics
representing an arbitrary polygon defined by its vertices.  
[RelativeJoint2D](RelativeJoint2D.html)| Keeps two Rigidbody2D at their
relative orientations.  
[Rigidbody2D](Rigidbody2D.html)| Provides physics movement and other dynamics,
and the ability to attach Collider2D to it.  
[SliderJoint2D](SliderJoint2D.html)| Joint that restricts the motion of a
Rigidbody2D object to a single line.  
[SpringJoint2D](SpringJoint2D.html)| Joint that attempts to keep two
Rigidbody2D objects a set distance apart by applying a force between them.  
[SurfaceEffector2D](SurfaceEffector2D.html)| Applies tangent forces along the
surfaces of colliders.  
[TargetJoint2D](TargetJoint2D.html)| The joint attempts to move a Rigidbody2D
to a specific target position.  
[WheelJoint2D](WheelJoint2D.html)| The wheel joint allows the simulation of
wheels by providing a constraining suspension motion with an optional motor.  
  
### Structs

[ColliderDistance2D](ColliderDistance2D.html)| Represents the separation or
overlap of two Collider2D.  
---|---  
[ContactFilter2D](ContactFilter2D.html)| A set of parameters for filtering
contact results. Define the angle by referring to their position in world
space, where 0 degrees is parallel to the positive x-axis, 90 degrees is
parallel to the positive y-axis, 180 degrees is parallel to the negative
x-axis, and 270 degrees is parallel to the negative y-axis.  
[ContactPoint2D](ContactPoint2D.html)| Details about a specific point of
contact involved in a 2D physics collision.  
[JointAngleLimits2D](JointAngleLimits2D.html)| Angular limits on the rotation
of a Rigidbody2D object around a HingeJoint2D.  
[JointMotor2D](JointMotor2D.html)| Parameters for the optional motor force
applied to a Joint2D.  
[JointSuspension2D](JointSuspension2D.html)| Joint suspension is used to
define how suspension works on a WheelJoint2D.  
[JointTranslationLimits2D](JointTranslationLimits2D.html)| Motion limits of a
Rigidbody2D object along a SliderJoint2D.  
[PhysicsJobOptions2D](PhysicsJobOptions2D.html)| A set of options that control
how physics operates when using the job system to multithread the physics
simulation.  
[PhysicsScene2D](PhysicsScene2D.html)| Represents a single instance of a 2D
physics Scene.  
[PhysicsShape2D](PhysicsShape2D.html)| Represents an efficient low-level
physics shape used by the physics engine.  
[RaycastHit2D](RaycastHit2D.html)| Returns information about 2D Colliders
detected by a 2D physics query in the scene.  
  
### Enumerations

[CapsuleDirection2D](CapsuleDirection2D.html)| The direction that the capsule
sides can extend.  
---|---  
[ColliderErrorState2D](ColliderErrorState2D.html)| Indicates what (if any)
error was encountered when creating a 2D Collider.  
[CollisionDetectionMode2D](CollisionDetectionMode2D.html)| Controls how
collisions are detected when a Rigidbody2D moves.  
[EffectorForceMode2D](EffectorForceMode2D.html)| The mode used to apply
Effector2D forces.  
[EffectorSelection2D](EffectorSelection2D.html)| Selects the source and/or
target to be used by an Effector2D.  
[ForceMode2D](ForceMode2D.html)| Option for how to apply a force using
Rigidbody2D.AddForce.  
[JointBreakAction2D](JointBreakAction2D.html)| Options for selecting which
action to take when a Joint2D breaks.  
[JointLimitState2D](JointLimitState2D.html)| Represents the state of a joint
limit.  
[PhysicsMaterialCombine2D](PhysicsMaterialCombine2D.html)| Describes how
PhysicsMaterial2D friction and bounciness are combined when two Collider2D
come into contact.  
[PhysicsShapeType2D](PhysicsShapeType2D.html)| Options for indicate which
primitive shape type is used to interpret geometry contained within a
PhysicsShape2D object.  
[RigidbodyConstraints2D](RigidbodyConstraints2D.html)| Use these flags to
constrain motion of the Rigidbody2D.  
[RigidbodyInterpolation2D](RigidbodyInterpolation2D.html)| Interpolation mode
for Rigidbody2D objects.  
[RigidbodySleepMode2D](RigidbodySleepMode2D.html)| Settings for a
Rigidbody2D's initial sleep state.  
[RigidbodyType2D](RigidbodyType2D.html)| The physical behaviour type of the
Rigidbody2D.  
[SimulationMode2D](SimulationMode2D.html)| A selection of modes that control
when Unity executes the 2D physics simulation.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

