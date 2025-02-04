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

# ArticulationBody

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.PhysicsModule](UnityEngine.PhysicsModule.html)

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

[Switch to Manual](../Manual/class-ArticulationBody.html "Go to
ArticulationBody Component in the Manual")

### Description

A body that forms part of a Physics articulation.

An articulation is a set of bodies arranged in a logical tree. The parent-
child link in this tree reflects that the bodies have their relative motion
constrained. Articulations are solved by a Featherstone solver that works in
reduced coordinates - that is each body has relative coordinates to its parent
but only along the unlocked degrees of freedom. This guarantees there is no
unwanted stretch.  
Like with regular Joints, there are two anchors for each pair of connected
articulation bodies. One anchor is defined in the parent body's reference
frame, whereas the other one is defined in the child's reference frame.
Changing the constraints, you directly affect the allowed space for relative
positions of the two anchors. For instance,
[ArticulationDofLock.LockedMotion](ArticulationDofLock.LockedMotion.html) will
not allow any relative motion at all.

### Properties

[anchorPosition](ArticulationBody-anchorPosition.html)| Position of the anchor
relative to this body.  
---|---  
[anchorRotation](ArticulationBody-anchorRotation.html)| Rotation of the anchor
relative to this body.  
[angularDamping](ArticulationBody-angularDamping.html)| Damping factor that
affects how this body resists rotations.  
[angularVelocity](ArticulationBody-angularVelocity.html)| The angular velocity
of the body defined in world space.  
[automaticCenterOfMass](ArticulationBody-automaticCenterOfMass.html)| Whether
or not to calculate the center of mass automatically.  
[automaticInertiaTensor](ArticulationBody-automaticInertiaTensor.html)|
Whether or not to calculate the inertia tensor automatically.  
[centerOfMass](ArticulationBody-centerOfMass.html)| The center of mass of the
body defined in local space.  
[collisionDetectionMode](ArticulationBody-collisionDetectionMode.html)| The
ArticulationBody's collision detection mode.  
[dofCount](ArticulationBody-dofCount.html)| The amount of degrees of freedom
of a body.  
[driveForce](ArticulationBody-driveForce.html)| The drive force in reduced
coordinates.  
[excludeLayers](ArticulationBody-excludeLayers.html)| The additional layers
that all Colliders attached to this ArticulationBody should exclude when
deciding if the Collider can come into contact with another Collider.  
[immovable](ArticulationBody-immovable.html)| Allows you to specify that this
body is not movable.  
[includeLayers](ArticulationBody-includeLayers.html)| The additional layers
that all Colliders attached to this ArticulationBody should include when
deciding if a the Collider can come into contact with another Collider.  
[index](ArticulationBody-index.html)| The index of the body in the hierarchy
of articulation bodies.  
[inertiaTensor](ArticulationBody-inertiaTensor.html)| The inertia tensor of
this body.  
[inertiaTensorRotation](ArticulationBody-inertiaTensorRotation.html)| The
rotation of the inertia tensor.  
[isRoot](ArticulationBody-isRoot.html)| Indicates whether this body is the
root body of the articulation (Read Only).  
[jointAcceleration](ArticulationBody-jointAcceleration.html)| The joint
acceleration in reduced coordinates.  
[jointForce](ArticulationBody-jointForce.html)| The joint force in reduced
coordinates.  
[jointFriction](ArticulationBody-jointFriction.html)| Allows you to specify
the amount of friction that is applied as a result of the parent body moving
relative to this body.  
[jointPosition](ArticulationBody-jointPosition.html)| The joint position in
reduced coordinates.  
[jointType](ArticulationBody-jointType.html)| The type of joint connecting
this body to its parent body.  
[jointVelocity](ArticulationBody-jointVelocity.html)| The joint velocity in
reduced coordinates.  
[linearDamping](ArticulationBody-linearDamping.html)| Damping factor that
affects how this body resists linear motion.  
[linearLockX](ArticulationBody-linearLockX.html)| The type of lock along X
axis of movement.  
[linearLockY](ArticulationBody-linearLockY.html)| The type of lock along Y
axis of movement.  
[linearLockZ](ArticulationBody-linearLockZ.html)| The type of lock along Z
axis of movement.  
[linearVelocity](ArticulationBody-linearVelocity.html)| Linear velocity of the
body defined in world space.  
[mass](ArticulationBody-mass.html)| The mass of this articulation body.  
[matchAnchors](ArticulationBody-matchAnchors.html)| Whether the parent anchor
should be computed automatically or not.  
[maxAngularVelocity](ArticulationBody-maxAngularVelocity.html)| The maximum
angular velocity of the articulation body measured in radians per second.  
[maxDepenetrationVelocity](ArticulationBody-maxDepenetrationVelocity.html)|
The maximum velocity of an articulation body when moving out of penetrating
state.  
[maxJointVelocity](ArticulationBody-maxJointVelocity.html)| The maximum joint
velocity of the articulation body joint in reduced coordinates.  
[maxLinearVelocity](ArticulationBody-maxLinearVelocity.html)| The maximum
linear velocity of the articulation body measured in meters per second.  
[parentAnchorPosition](ArticulationBody-parentAnchorPosition.html)| Position
of the anchor relative to this body's parent.  
[parentAnchorRotation](ArticulationBody-parentAnchorRotation.html)| Rotation
of the anchor relative to this body's parent.  
[sleepThreshold](ArticulationBody-sleepThreshold.html)| The mass-normalized
energy threshold, below which objects start going to sleep.  
[solverIterations](ArticulationBody-solverIterations.html)| The
solverIterations determines how accurately articulation body joints and
collision contacts are resolved.  
[solverVelocityIterations](ArticulationBody-solverVelocityIterations.html)|
The solverVelocityIterations affects how accurately articulation body joints
and collision contacts are resolved during bounce.  
[swingYLock](ArticulationBody-swingYLock.html)| The magnitude of the conical
swing angle relative to Y axis.  
[swingZLock](ArticulationBody-swingZLock.html)| The magnitude of the conical
swing angle relative to Z axis.  
[twistLock](ArticulationBody-twistLock.html)| The type of lock for twist
movement.  
[useGravity](ArticulationBody-useGravity.html)| Controls whether gravity
affects this articulation body.  
[worldCenterOfMass](ArticulationBody-worldCenterOfMass.html)| The center of
mass of the body defined in world space (Read Only).  
[xDrive](ArticulationBody-xDrive.html)| The properties of drive along or
around X.  
[yDrive](ArticulationBody-yDrive.html)| The properties of drive along or
around Y.  
[zDrive](ArticulationBody-zDrive.html)| The properties of drive along or
around Z.  
  
### Public Methods

[AddForce](ArticulationBody.AddForce.html)| Applies a force to the
ArticulationBody.  
---|---  
[AddForceAtPosition](ArticulationBody.AddForceAtPosition.html)| Applies a
force at a specific position, resulting in applying a torque and force on the
object.  
[AddRelativeForce](ArticulationBody.AddRelativeForce.html)| Applies a force to
the Articulation Body, relative to its local coordinate system.  
[AddRelativeTorque](ArticulationBody.AddRelativeTorque.html)| Applies a torque
to the articulation body, relative to its local coordinate system.  
[AddTorque](ArticulationBody.AddTorque.html)| Add torque to the articulation
body.  
[GetAccumulatedForce](ArticulationBody.GetAccumulatedForce.html)| Returns the
force that the ArticulationBody has accumulated before the simulation step.  
[GetAccumulatedTorque](ArticulationBody.GetAccumulatedTorque.html)| Returns
the torque that the ArticulationBody has accumulated before the simulation
step.  
[GetClosestPoint](ArticulationBody.GetClosestPoint.html)| Return the point on
the articulation body that is closest to a given one.  
[GetDenseJacobian](ArticulationBody.GetDenseJacobian.html)| Calculates and
writes dense Jacobian matrix of the articulation body hierarchy to the
supplied struct.  
[GetDofStartIndices](ArticulationBody.GetDofStartIndices.html)| Calculates and
reads back reduced coordinate data start indexes in reduced coordinate data
buffer for every articulation body in the hierarchy.  
[GetDriveForces](ArticulationBody.GetDriveForces.html)| Reads the entire
hierarchy of Articulation Bodies and fills the supplied list of floats with
Articulation Drive forces.  
[GetDriveTargets](ArticulationBody.GetDriveTargets.html)| Reads back
articulation body joint drive targets of the entire hierarchy to the supplied
list of floats.  
[GetDriveTargetVelocities](ArticulationBody.GetDriveTargetVelocities.html)|
Reads back articulation body joint drive target velocities of the entire
hierarchy to the supplied list of floats .  
[GetJointAccelerations](ArticulationBody.GetJointAccelerations.html)| Reads
back articulation body joint accelerations of the entire hierarchy to the
supplied list of floats .  
[GetJointCoriolisCentrifugalForces](ArticulationBody.GetJointCoriolisCentrifugalForces.html)|
Fills the supplied list of floats with the forces required to counteract the
Coriolis and centrifugal forces for each Articulation Body in the
articulation.  
[GetJointExternalForces](ArticulationBody.GetJointExternalForces.html)| Fills
the supplied list of floats with forces required to counteract any existing
external forces (applied using ArticulationBody.AddForce or
ArticulationBody.AddTorque) for each Articulation Body in the articulation.  
[GetJointForces](ArticulationBody.GetJointForces.html)| Reads back
articulation body joint forces of the entire hierarchy to the supplied list of
floats .  
[GetJointForcesForAcceleration](ArticulationBody.GetJointForcesForAcceleration.html)|
Returns the forces required for the body to reach the provided acceleration in
reduced space.  
[GetJointGravityForces](ArticulationBody.GetJointGravityForces.html)| Fills
the supplied list of floats with forces required to counteract gravity for
each Articulation Body in the articulation.  
[GetJointPositions](ArticulationBody.GetJointPositions.html)| Reads back
articulation body joint positions of the entire hierarchy to the supplied list
of floats .  
[GetJointVelocities](ArticulationBody.GetJointVelocities.html)| Reads back
articulation body joint velocities of the entire hierarchy to the supplied
list of floats .  
[GetPointVelocity](ArticulationBody.GetPointVelocity.html)| Gets the velocity
of the articulation body at the specified worldPoint in global space.  
[GetRelativePointVelocity](ArticulationBody.GetRelativePointVelocity.html)|
The velocity relative to the articulation body at the point relativePoint.  
[IsSleeping](ArticulationBody.IsSleeping.html)| Indicates whether the
articulation body is sleeping.  
[PublishTransform](ArticulationBody.PublishTransform.html)| Reads the position
and rotation of the Articulation Body from the physics system and applies it
to the corresponding Transform component.  
[ResetCenterOfMass](ArticulationBody.ResetCenterOfMass.html)| Resets the
center of mass of the articulation body.  
[ResetInertiaTensor](ArticulationBody.ResetInertiaTensor.html)| Resets the
inertia tensor value and rotation.  
[SetDriveDamping](ArticulationBody.SetDriveDamping.html)| Sets the damping
value of the specified drive.  
[SetDriveForceLimit](ArticulationBody.SetDriveForceLimit.html)| Sets the force
limit of the specified drive.  
[SetDriveLimits](ArticulationBody.SetDriveLimits.html)| Sets the lower and
upper limits of the drive.  
[SetDriveStiffness](ArticulationBody.SetDriveStiffness.html)| Sets the
stiffness value of the specified drive.  
[SetDriveTarget](ArticulationBody.SetDriveTarget.html)| Sets the target value
of the specified drive.  
[SetDriveTargets](ArticulationBody.SetDriveTargets.html)| Assigns articulation
body joint drive targets for the entire hierarchy of bodies.  
[SetDriveTargetVelocities](ArticulationBody.SetDriveTargetVelocities.html)|
Assigns articulation body joint drive target velocities for the entire
hierarchy of bodies.  
[SetDriveTargetVelocity](ArticulationBody.SetDriveTargetVelocity.html)| Sets
the target velocity value of the specified drive.  
[SetJointForces](ArticulationBody.SetJointForces.html)| Assigns articulation
body joint forces for the entire hierarchy of bodies.  
[SetJointPositions](ArticulationBody.SetJointPositions.html)| Assigns
articulation body joint positions for the entire hierarchy of bodies.  
[SetJointVelocities](ArticulationBody.SetJointVelocities.html)| Assigns
articulation body joint velocities for the entire hierarchy of bodies.  
[Sleep](ArticulationBody.Sleep.html)| Forces an articulation body to sleep.  
[SnapAnchorToClosestContact](ArticulationBody.SnapAnchorToClosestContact.html)|
Snap the anchor to the closest contact between the connected bodies.  
[TeleportRoot](ArticulationBody.TeleportRoot.html)| Teleport the root body of
the articulation to a new pose.  
[WakeUp](ArticulationBody.WakeUp.html)| Forces an articulation body to wake
up.  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

