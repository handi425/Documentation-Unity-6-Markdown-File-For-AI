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

# ConfigurableJoint

class in UnityEngine

/

Inherits from:[Joint](Joint.html)

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

[Switch to Manual](../Manual/class-ConfigurableJoint.html "Go to
ConfigurableJoint Component in the Manual")

### Description

The configurable joint is an extremely flexible joint giving you complete
control over rotation and linear motion.

You can build all other joints with it and much more but it is also more
complicated to setup. It gives you control over motors, drives and joint
limits for each rotation axis and and linear degree of freedom.

### Properties

[angularXDrive](ConfigurableJoint-angularXDrive.html)| Definition of how the
joint's rotation will behave around its local X axis. Only used if Rotation
Drive Mode is Swing & Twist.  
---|---  
[angularXLimitSpring](ConfigurableJoint-angularXLimitSpring.html)| The
configuration of the spring attached to the angular X limit of the joint.  
[angularXMotion](ConfigurableJoint-angularXMotion.html)| Allow rotation around
the X axis to be Free, completely Locked, or Limited according to Low and High
Angular XLimit.  
[angularYLimit](ConfigurableJoint-angularYLimit.html)| Boundary defining
rotation restriction, based on delta from original rotation.  
[angularYMotion](ConfigurableJoint-angularYMotion.html)| Allow rotation around
the Y axis to be Free, completely Locked, or Limited according to Angular
YLimit.  
[angularYZDrive](ConfigurableJoint-angularYZDrive.html)| Definition of how the
joint's rotation will behave around its local Y and Z axes. Only used if
Rotation Drive Mode is Swing & Twist.  
[angularYZLimitSpring](ConfigurableJoint-angularYZLimitSpring.html)| The
configuration of the spring attached to the angular Y and angular Z limits of
the joint.  
[angularZLimit](ConfigurableJoint-angularZLimit.html)| Boundary defining
rotation restriction, based on delta from original rotation.  
[angularZMotion](ConfigurableJoint-angularZMotion.html)| Allow rotation around
the Z axis to be Free, completely Locked, or Limited according to Angular
ZLimit.  
[configuredInWorldSpace](ConfigurableJoint-configuredInWorldSpace.html)| If
enabled, all Target values will be calculated in world space instead of the
object's local space.  
[highAngularXLimit](ConfigurableJoint-highAngularXLimit.html)| Boundary
defining upper rotation restriction, based on delta from original rotation.  
[linearLimit](ConfigurableJoint-linearLimit.html)| Boundary defining movement
restriction, based on distance from the joint's origin.  
[linearLimitSpring](ConfigurableJoint-linearLimitSpring.html)| The
configuration of the spring attached to the linear limit of the joint.  
[lowAngularXLimit](ConfigurableJoint-lowAngularXLimit.html)| Boundary defining
lower rotation restriction, based on delta from original rotation.  
[projectionAngle](ConfigurableJoint-projectionAngle.html)| Set the angular
tolerance threshold (in degrees) for projection.If the joint deviates by more
than this angle around its locked angular degrees of freedom, the solver will
move the bodies to close the angle.Setting a very small tolerance may result
in simulation jitter or other artifacts.Sometimes it is not possible to
project (for example when the joints form a cycle).  
[projectionDistance](ConfigurableJoint-projectionDistance.html)| Set the
linear tolerance threshold for projection.If the joint separates by more than
this distance along its locked degrees of freedom, the solver will move the
bodies to close the distance.Setting a very small tolerance may result in
simulation jitter or other artifacts.Sometimes it is not possible to project
(for example when the joints form a cycle).  
[projectionMode](ConfigurableJoint-projectionMode.html)| Brings violated
constraints back into alignment even when the solver fails. Projection is not
a physical process and does not preserve momentum or respect collision
geometry. It is best avoided if practical, but can be useful in improving
simulation quality where joint separation results in unacceptable artifacts.  
[rotationDriveMode](ConfigurableJoint-rotationDriveMode.html)| Control the
object's rotation with either X & YZ or Slerp Drive by itself.  
[secondaryAxis](ConfigurableJoint-secondaryAxis.html)| The joint's secondary
axis.  
[slerpDrive](ConfigurableJoint-slerpDrive.html)| Definition of how the joint's
rotation will behave around all local axes. Only used if Rotation Drive Mode
is Slerp Only.  
[swapBodies](ConfigurableJoint-swapBodies.html)| Enable this property to swap
the order in which the physics engine processes the Rigidbodies involved in
the joint. This results in different joint motion but has no impact on
Rigidbodies and anchors.  
[targetAngularVelocity](ConfigurableJoint-targetAngularVelocity.html)| This is
a Vector3. It defines the desired angular velocity that the joint should
rotate into.  
[targetPosition](ConfigurableJoint-targetPosition.html)| The desired position
that the joint should move into.  
[targetRotation](ConfigurableJoint-targetRotation.html)| This is a Quaternion.
It defines the desired rotation that the joint should rotate into.  
[targetVelocity](ConfigurableJoint-targetVelocity.html)| The desired velocity
that the joint should move along.  
[xDrive](ConfigurableJoint-xDrive.html)| Definition of how the joint's
movement will behave along its local X axis.  
[xMotion](ConfigurableJoint-xMotion.html)| Allow movement along the X axis to
be Free, completely Locked, or Limited according to Linear Limit.  
[yDrive](ConfigurableJoint-yDrive.html)| Definition of how the joint's
movement will behave along its local Y axis.  
[yMotion](ConfigurableJoint-yMotion.html)| Allow movement along the Y axis to
be Free, completely Locked, or Limited according to Linear Limit.  
[zDrive](ConfigurableJoint-zDrive.html)| Definition of how the joint's
movement will behave along its local Z axis.  
[zMotion](ConfigurableJoint-zMotion.html)| Allow movement along the Z axis to
be Free, completely Locked, or Limited according to Linear Limit.  
  
### Inherited Members

### Properties

[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
---|---  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[anchor](Joint-anchor.html)| The Position of the anchor around which the
joints motion is constrained.  
[autoConfigureConnectedAnchor](Joint-autoConfigureConnectedAnchor.html)|
Should the connectedAnchor be calculated automatically?  
[axis](Joint-axis.html)| The Direction of the axis around which the body is
constrained.  
[breakForce](Joint-breakForce.html)| The force that needs to be applied for
this joint to break.  
[breakTorque](Joint-breakTorque.html)| The torque that needs to be applied for
this joint to break. To be able to break, a joint must be _Locked_ or
_Limited_ on the axis of rotation where the torque is being applied. This
means that some joints cannot break, such as an unconstrained Configurable
Joint.  
[connectedAnchor](Joint-connectedAnchor.html)| Position of the anchor relative
to the connected Rigidbody.  
[connectedArticulationBody](Joint-connectedArticulationBody.html)| A reference
to an articulation body this joint connects to.  
[connectedBody](Joint-connectedBody.html)| A reference to another rigidbody
this joint connects to.  
[connectedMassScale](Joint-connectedMassScale.html)| The scale to apply to the
inverse mass and inertia tensor of the connected body prior to solving the
constraints.  
[currentForce](Joint-currentForce.html)| The force applied by the solver to
satisfy all constraints.  
[currentTorque](Joint-currentTorque.html)| The torque applied by the solver to
satisfy all constraints.  
[enableCollision](Joint-enableCollision.html)| Enable collision between bodies
connected with the joint.  
[enablePreprocessing](Joint-enablePreprocessing.html)| Toggle preprocessing
for this joint.  
[massScale](Joint-massScale.html)| The scale to apply to the inverse mass and
inertia tensor of the body prior to solving the constraints.  
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
  
### Messages

[OnJointBreak](Joint.OnJointBreak.html)| Called when a joint attached to the
same game object broke.  
---|---  
  
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

