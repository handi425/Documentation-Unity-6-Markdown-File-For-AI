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

# UnityEngine.PhysicsModule

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

The Physics module implements 3D physics in Unity.

### Classes

[ArticulationBody](ArticulationBody.html)| A body that forms part of a Physics
articulation.  
---|---  
[BoxCollider](BoxCollider.html)| A box-shaped primitive collider.  
[CapsuleCollider](CapsuleCollider.html)| A capsule-shaped primitive collider.  
[CharacterController](CharacterController.html)| A CharacterController allows
you to easily do movement constrained by collisions without having to deal
with a rigidbody.  
[CharacterJoint](CharacterJoint.html)| Character Joints are mainly used for
Ragdoll effects.  
[Collider](Collider.html)| A base class of all colliders.  
[Collision](Collision.html)| Describes a collision.  
[ConfigurableJoint](ConfigurableJoint.html)| The configurable joint is an
extremely flexible joint giving you complete control over rotation and linear
motion.  
[ConstantForce](ConstantForce.html)| A force applied constantly.  
[ControllerColliderHit](ControllerColliderHit.html)| ControllerColliderHit is
used by CharacterController.OnControllerColliderHit to give detailed
information about the collision and how to deal with it.  
[FixedJoint](FixedJoint.html)| The Fixed joint groups together 2 rigidbodies,
making them stick together in their bound position.  
[HingeJoint](HingeJoint.html)| The HingeJoint groups together 2 rigid bodies,
constraining them to move like connected by a hinge.  
[ImmediatePhysics](LowLevelPhysics.ImmediatePhysics.html)| This class contains
methods to run the immediate simulation steps.  
[Joint](Joint.html)| Joint is the base class for all joints.  
[MeshCollider](MeshCollider.html)| A mesh collider allows you to do collision
detection between meshes and primitives.  
[Physics](Physics.html)| Global physics properties and helper methods.  
[PhysicsMaterial](PhysicsMaterial.html)| Physics material describes how to
handle colliding objects (friction, bounciness).  
[PhysicsSceneExtensions](PhysicsSceneExtensions.html)| Scene extensions to
access the underlying physics scene.  
[Rigidbody](Rigidbody.html)| Control of an object's position through physics
simulation.  
[SphereCollider](SphereCollider.html)| A sphere-shaped primitive collider.  
[SpringJoint](SpringJoint.html)| The spring joint ties together 2 rigid
bodies, spring forces will be automatically applied to keep the object at the
given distance.  
  
### Structs

[ArticulationDrive](ArticulationDrive.html)| Drive applies forces and torques
to the connected bodies.  
---|---  
[ArticulationJacobian](ArticulationJacobian.html)| The floating point dense
Jacobian matrix of the articulation body hierarchy.  
[ArticulationReducedSpace](ArticulationReducedSpace.html)| Coordinates in
reduced space.  
[BoxcastCommand](BoxcastCommand.html)| Use this struct to set up a box cast
command to be performed asynchronously during a job.  
[BoxGeometry](LowLevelPhysics.BoxGeometry.html)| Contains the basic geometric
shape of a box.  
[CapsulecastCommand](CapsulecastCommand.html)| Use this struct to set up a
capsule cast command that is performed asynchronously during a job.  
[CapsuleGeometry](LowLevelPhysics.CapsuleGeometry.html)| Contains the basic
geometric shape of a capsule.  
[ClosestPointCommand](ClosestPointCommand.html)| Struct used to set up a
closest point command to be performed asynchronously during a job.When you use
this struct to schedule a batch of closest commands, they are performed
asynchronously and in parallel to each other. The results of the closest
points are written to the results buffer. Because the results are written
asynchronously, the results buffer cannot be accessed until the job has been
completed.The result for a command at index N in the command buffer is stored
at index N in the results buffer.  
[ColliderHit](ColliderHit.html)| Struct used to retrieve information from an
Overlap batch query.  
[ContactPair](ContactPair.html)| A pair of Colliders that belong to the bodies
in the parent ContactPairHeader struct.  
[ContactPairHeader](ContactPairHeader.html)| A header struct which contains
colliding bodies.  
[ContactPairPoint](ContactPairPoint.html)| A readonly struct describing a
contact point between two Colliders.  
[ContactPoint](ContactPoint.html)| Describes a contact point where the
collision occurs.  
[ConvexMeshGeometry](LowLevelPhysics.ConvexMeshGeometry.html)| Contains the
basic geometric shape of a convex mesh.  
[GeometryHolder](LowLevelPhysics.GeometryHolder.html)| Holds the basic
information of a geometric shape and its type.  
[ImmediateContact](LowLevelPhysics.ImmediateContact.html)| Describes a contact
where two shapes collide.  
[ImmediateTransform](LowLevelPhysics.ImmediateTransform.html)| A transform,
containing a position and rotation.  
[JointDrive](JointDrive.html)| How the joint's movement will behave along its
local X axis.  
[JointLimits](JointLimits.html)| JointLimits is used by the HingeJoint to
limit the joints angle.  
[JointMotor](JointMotor.html)| The JointMotor is used to motorize a joint.  
[JointSpring](JointSpring.html)| JointSpring is used add a spring force to
HingeJoint and PhysicsMaterial.  
[ModifiableContactPair](ModifiableContactPair.html)| A light-weight proxy that
allows to access the contact buffers directly.  
[ModifiableMassProperties](ModifiableMassProperties.html)| Mass-related
modifiable properties of a contact pair.  
[OverlapBoxCommand](OverlapBoxCommand.html)| Struct used to set up an overlap
box command to be performed asynchronously during a job.  
[OverlapCapsuleCommand](OverlapCapsuleCommand.html)| Struct used to set up an
overlap capsule command to be performed asynchronously during a job.  
[OverlapSphereCommand](OverlapSphereCommand.html)| Struct used to setup an
overlap sphere command to be performed asynchronously during a job.  
[PhysicsScene](PhysicsScene.html)| Represents a single instance of a 3D
physics Scene.  
[QueryParameters](QueryParameters.html)| Creates a struct to set up parameters
for batch queries: RaycastCommand, BoxcastCommand, CapsulecastCommand,
SpherecastCommand.  
[RaycastCommand](RaycastCommand.html)| Struct used to set up a raycast command
to be performed asynchronously during a job.  
[RaycastHit](RaycastHit.html)| Structure used to get information back from a
raycast.  
[SoftJointLimit](SoftJointLimit.html)| The limits defined by the
CharacterJoint.  
[SoftJointLimitSpring](SoftJointLimitSpring.html)| The configuration of the
spring attached to the joint's limits: linear and angular. Used by
CharacterJoint and ConfigurableJoint.  
[SpherecastCommand](SpherecastCommand.html)| Use this struct to set up a
sphere cast command that is performed asynchronously during a job.  
[SphereGeometry](LowLevelPhysics.SphereGeometry.html)| Contains the basic
geometric shape of a sphere.  
[TerrainGeometry](LowLevelPhysics.TerrainGeometry.html)| Contains the
geometric shape of a Terrain collider.  
[TriangleMeshGeometry](LowLevelPhysics.TriangleMeshGeometry.html)| Contains
the basic geometric shape of a non-convex mesh (sometimes known as a triangle
mesh).  
[WheelFrictionCurve](WheelFrictionCurve.html)| WheelFrictionCurve is used by
the WheelCollider to describe friction properties of the wheel tire.  
  
### Enumerations

[ArticulationDofLock](ArticulationDofLock.html)| The lock type applied to a
particular degree of freedom of an articulation body.  
---|---  
[ArticulationDriveAxis](ArticulationDriveAxis.html)| An axis of a drive of an
ArticulationBody.  
[ArticulationDriveType](ArticulationDriveType.html)| The drive type applied to
a particular drive of an ArticulationBody.  
[ArticulationJointType](ArticulationJointType.html)| The type of the joint
that restricts movement of the two connected articulation bodies.  
[CollisionDetectionMode](CollisionDetectionMode.html)| The collision detection
mode constants used for Rigidbody.collisionDetectionMode.  
[CollisionFlags](CollisionFlags.html)| CollisionFlags is a bitmask returned by
CharacterController.Move.  
[ConfigurableJointMotion](ConfigurableJointMotion.html)| Constrains movement
for a ConfigurableJoint along the 6 axes.  
[ForceMode](ForceMode.html)| Use ForceMode to specify how to apply a force
using Rigidbody.AddForce or ArticulationBody.AddForce.  
[GeometryType](LowLevelPhysics.GeometryType.html)| The set of basic geometry
shape types that can exist.  
[JointProjectionMode](JointProjectionMode.html)| Determines how to snap
physics joints back to its constrained position when it drifts off too much.  
[MeshColliderCookingOptions](MeshColliderCookingOptions.html)| Cooking options
that are available with MeshCollider.  
[PhysicsMaterialCombine](PhysicsMaterialCombine.html)| Describes how physics
materials of the colliding objects are combined.The friction force as well as
the residual bounce impulse are applied symmetrically to both of the colliders
in contact, so each pair of overlapping colliders must have a single set of
friction and bouciness settings. However, one can set arbitrary physics
materials to any colliders. For that particular reason, there is a mechanism
that allows the combination of two different sets of properties that
correspond to each of the colliders in contact into one set to be used in the
solver.Specifying Average, Maximum, Minimum or Multiply as the physics
material combine mode, you directly set the function that is used to combine
the settings corresponding to the two overlapping colliders into one set of
settings that can be used to apply the material effect.Note that there is a
special case when the two overlapping colliders have physics materials with
different combine modes set. In this particular case, the function that has
the highest priority is used. The priority order is as follows: Average <
Minimum < Multiply < Maximum. For example, if one material has Average set but
the other one has Maximum, then the combine function to be used is Maximum,
since it has higher priority.  
[QueryTriggerInteraction](QueryTriggerInteraction.html)| Overrides the global
Physics.queriesHitTriggers.  
[RigidbodyConstraints](RigidbodyConstraints.html)| Use these flags to
constrain motion of Rigidbodies.  
[RigidbodyInterpolation](RigidbodyInterpolation.html)|  Rigidbody
interpolation mode.  
[RotationDriveMode](RotationDriveMode.html)| Control ConfigurableJoint's
rotation with either X & YZ or Slerp Drive.  
[SimulationMode](SimulationMode.html)| A selection of modes that control when
Unity executes the physics simulation.  
[SimulationOption](SimulationOption.html)| An enumerator that specifies
physics simulation options.  
[SimulationStage](SimulationStage.html)| A flag enum to determine which
simulation stages to run.  
  
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

