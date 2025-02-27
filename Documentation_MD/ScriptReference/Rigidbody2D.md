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

# Rigidbody2D

class in UnityEngine

/

Inherits from:[Component](Component.html)

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

Provides physics movement and other dynamics, and the ability to attach
[Collider2D](Collider2D.html) to it.

The [Rigidbody2D](Rigidbody2D.html) is a fundamental physics component that
provides multiple simulation dynamics, such as
[Rigidbody2D.position](Rigidbody2D-position.html) and
[Rigidbody2D.rotation](Rigidbody2D-rotation.html) for pose control, and
[Rigidbody2D.linearVelocity](Rigidbody2D-linearVelocity.html) and
[Rigidbody2D.angularVelocity](Rigidbody2D-angularVelocity.html) for velocity
control.  
  
You can attach multiple [Collider2D](Collider2D.html) to a
[Rigidbody2D](Rigidbody2D.html) to detect collisions and provide a collision
response when you set [Rigidbody2D.bodyType](Rigidbody2D-bodyType.html) to
[RigidbodyType2D.Dynamic](RigidbodyType2D.Dynamic.html).

### Properties

[angularDamping](Rigidbody2D-angularDamping.html)| The angular damping of the
Rigidbody2D angular velocity.  
---|---  
[angularVelocity](Rigidbody2D-angularVelocity.html)| Angular velocity in
degrees per second.  
[attachedColliderCount](Rigidbody2D-attachedColliderCount.html)| Returns the
number of Collider2D attached to this Rigidbody2D.  
[bodyType](Rigidbody2D-bodyType.html)| The physical behaviour type of the
Rigidbody2D.  
[centerOfMass](Rigidbody2D-centerOfMass.html)| The center of mass of the
rigidBody in local space.  
[collisionDetectionMode](Rigidbody2D-collisionDetectionMode.html)| The method
used by the physics engine to check if two objects have collided.  
[constraints](Rigidbody2D-constraints.html)| Controls which degrees of freedom
are allowed for the simulation of this Rigidbody2D.  
[excludeLayers](Rigidbody2D-excludeLayers.html)| The additional Layers that
all Collider2D attached to this Rigidbody2D should exclude when deciding if a
contact with another Collider2D should happen or not.  
[freezeRotation](Rigidbody2D-freezeRotation.html)| Controls whether physics
will change the rotation of the object.  
[gravityScale](Rigidbody2D-gravityScale.html)| The degree to which this object
is affected by gravity.  
[includeLayers](Rigidbody2D-includeLayers.html)| The additional Layers that
all Collider2D attached to this Rigidbody2D should include when deciding if a
contact with another Collider2D should happen or not.  
[inertia](Rigidbody2D-inertia.html)| The Rigidbody's resistance to changes in
angular velocity (rotation).  
[interpolation](Rigidbody2D-interpolation.html)| Physics interpolation used
between updates.  
[linearDamping](Rigidbody2D-linearDamping.html)| The linear damping of the
Rigidbody2D linear velocity.  
[linearVelocity](Rigidbody2D-linearVelocity.html)| The linear velocity of the
Rigidbody2D represents the rate of change over time of the Rigidbody2D
position in world-units.  
[linearVelocityX](Rigidbody2D-linearVelocityX.html)| The X component of the
linear velocity of the Rigidbody2D in world-units per second.  
[linearVelocityY](Rigidbody2D-linearVelocityY.html)| The Y component of the
linear velocity of the Rigidbody2D in world-units per second.  
[localToWorldMatrix](Rigidbody2D-localToWorldMatrix.html)| The transformation
matrix used to transform the Rigidbody2D to world space.  
[mass](Rigidbody2D-mass.html)| Mass of the Rigidbody.  
[position](Rigidbody2D-position.html)| The position of the rigidbody.  
[rotation](Rigidbody2D-rotation.html)| The rotation of the rigidbody.  
[sharedMaterial](Rigidbody2D-sharedMaterial.html)| The PhysicsMaterial2D that
is applied to all Collider2D attached to this Rigidbody2D.  
[simulated](Rigidbody2D-simulated.html)| Indicates whether the rigid body
should be simulated or not by the physics system.  
[sleepMode](Rigidbody2D-sleepMode.html)| The sleep state that the rigidbody
will initially be in.  
[totalForce](Rigidbody2D-totalForce.html)| The total amount of force that has
been explicitly applied to this Rigidbody2D since the last physics simulation
step.  
[totalTorque](Rigidbody2D-totalTorque.html)| The total amount of torque that
has been explicitly applied to this Rigidbody2D since the last physics
simulation step.  
[useAutoMass](Rigidbody2D-useAutoMass.html)| Should the total rigid-body mass
be automatically calculated from the [[Collider2D.density]] of attached
colliders?  
[useFullKinematicContacts](Rigidbody2D-useFullKinematicContacts.html)| Should
kinematic/kinematic and kinematic/static collisions be allowed?  
[worldCenterOfMass](Rigidbody2D-worldCenterOfMass.html)| Gets the center of
mass of the rigidBody in global space.  
  
### Public Methods

[AddForce](Rigidbody2D.AddForce.html)| Apply a force to the rigidbody.  
---|---  
[AddForceAtPosition](Rigidbody2D.AddForceAtPosition.html)| Apply a force at a
given position in space.  
[AddForceX](Rigidbody2D.AddForceX.html)| Adds a force to the X component of
the Rigidbody2D.linearVelocity only leaving the Y component of the world space
Rigidbody2D.linearVelocity untouched.  
[AddForceY](Rigidbody2D.AddForceY.html)| Adds a force to the Y component of
the Rigidbody2D.linearVelocity only leaving the X component of the world space
Rigidbody2D.linearVelocity untouched.  
[AddRelativeForce](Rigidbody2D.AddRelativeForce.html)| Adds a force to the
local space Rigidbody2D.linearVelocity. In other words, the force is applied
in the rotated coordinate space of the Rigidbody2D.  
[AddRelativeForceX](Rigidbody2D.AddRelativeForceX.html)| Adds a force to the X
component of the Rigidbody2D.linearVelocity in the local space of the
Rigidbody2D only leaving the Y component of the local space
Rigidbody2D.linearVelocity untouched.  
[AddRelativeForceY](Rigidbody2D.AddRelativeForceY.html)| Adds a force to the Y
component of the Rigidbody2D.linearVelocity in the local space of the
Rigidbody2D only leaving the X component of the local space
Rigidbody2D.linearVelocity untouched.  
[AddTorque](Rigidbody2D.AddTorque.html)| Apply a torque at the rigidbody's
centre of mass.  
[Cast](Rigidbody2D.Cast.html)| All the Collider2D shapes attached to the
Rigidbody2D are cast into the Scene starting at each Collider position
ignoring the Colliders attached to the same Rigidbody2D.  
[ClosestPoint](Rigidbody2D.ClosestPoint.html)| Returns a point on the
perimeter of all enabled Colliders attached to this Rigidbody that is closest
to the specified position.  
[Distance](Rigidbody2D.Distance.html)| Calculates the minimum distance of this
collider against all Collider2D attached to this Rigidbody2D.  
[GetAttachedColliders](Rigidbody2D.GetAttachedColliders.html)| Returns all
Collider2D that are attached to this Rigidbody2D.  
[GetContacts](Rigidbody2D.GetContacts.html)| Retrieves all contact points for
all of the Collider(s) attached to this Rigidbody.  
[GetPoint](Rigidbody2D.GetPoint.html)| Get a local space point given the point
point in rigidBody global space.  
[GetPointVelocity](Rigidbody2D.GetPointVelocity.html)| The velocity of the
rigidbody at the point Point in global space.  
[GetRelativePoint](Rigidbody2D.GetRelativePoint.html)| Get a global space
point given the point relativePoint in rigidBody local space.  
[GetRelativePointVelocity](Rigidbody2D.GetRelativePointVelocity.html)| The
velocity of the rigidbody at the point Point in local space.  
[GetRelativeVector](Rigidbody2D.GetRelativeVector.html)| Get a global space
vector given the vector relativeVector in rigidBody local space.  
[GetShapes](Rigidbody2D.GetShapes.html)| Gets all the PhysicsShape2D used by
all Collider2D attached to the Rigidbody2D.  
[GetVector](Rigidbody2D.GetVector.html)| Get a local space vector given the
vector vector in rigidBody global space.  
[IsAwake](Rigidbody2D.IsAwake.html)| Is the rigidbody "awake"?  
[IsSleeping](Rigidbody2D.IsSleeping.html)| Is the rigidbody "sleeping"?  
[IsTouching](Rigidbody2D.IsTouching.html)| Checks whether the collider is
touching any of the collider(s) attached to this rigidbody or not.  
[IsTouchingLayers](Rigidbody2D.IsTouchingLayers.html)| Checks whether any of
the collider(s) attached to this rigidbody are touching any colliders on the
specified layerMask or not.  
[MovePosition](Rigidbody2D.MovePosition.html)| Moves the rigidbody to
position.  
[MovePositionAndRotation](Rigidbody2D.MovePositionAndRotation.html)| Moves the
rigidbody position to position and the rigidbody angle to angle.  
[MoveRotation](Rigidbody2D.MoveRotation.html)| Rotates the Rigidbody to angle
(given in degrees).  
[Overlap](Rigidbody2D.Overlap.html)| Get a list of all Colliders that overlap
all Colliders attached to this Rigidbody2D.  
[OverlapPoint](Rigidbody2D.OverlapPoint.html)| Check if any of the Rigidbody2D
colliders overlap a point in space.  
[SetRotation](Rigidbody2D.SetRotation.html)| Sets the rotation of the
Rigidbody2D to angle (given in degrees).  
[Sleep](Rigidbody2D.Sleep.html)| Make the rigidbody "sleep".  
[Slide](Rigidbody2D.Slide.html)| Slide the Rigidbody2D using the specified
velocity integrated over deltaTime using the configuration specified by
slideMovement.  
[WakeUp](Rigidbody2D.WakeUp.html)| Disables the "sleeping" state of a
rigidbody.  
  
### Inherited Members

### Properties

[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
---|---  
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

