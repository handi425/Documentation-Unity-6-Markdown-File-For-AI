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

# Rigidbody

class in UnityEngine

/

Inherits from:[Component](Component.html)

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

### Description

Control of an object's position through physics simulation.

Adding a Rigidbody component to an object will put its motion under the
control of Unity's physics engine. Even without adding any code, a Rigidbody
object will be pulled downward by gravity and will react to collisions with
incoming objects if the right [Collider](Collider.html) component is also
present.  
  
The Rigidbody also has a scripting API that lets you apply forces to the
object and control it in a physically realistic way. For example, a car's
behaviour can be specified in terms of the forces applied by the wheels. Given
this information, the physics engine can handle most other aspects of the
car's motion, so it will accelerate realistically and respond correctly to
collisions.  
  
In a script, the [FixedUpdate](MonoBehaviour.FixedUpdate.html) function is
recommended as the place to apply forces and change Rigidbody settings (as
opposed to [Update](MonoBehaviour.Update.html), which is used for most other
frame update tasks). The reason for this is that physics updates are carried
out in measured time steps that don't coincide with the frame update.
FixedUpdate is called immediately before each physics update and so any
changes made there will be processed directly.  
  
A common problem when starting out with Rigidbodies is that the game physics
appears to run in "slow motion". This is actually due to the scale used for
your models. The default gravity settings assume that one world unit
corresponds to one metre of distance. With non-physical games, it doesn't make
much difference if your models are all 100 units long but when using physics,
they will be treated as very large objects. If a large scale is used for
objects that are supposed to be small, they will appear to fall very slowly -
the physics engine thinks they are very large objects falling over very large
distances. With this in mind, be sure to keep your objects more or less at
their scale in real life (so a car should be about 4 units = 4 metres, for
example).

### Properties

[angularDamping](Rigidbody-angularDamping.html)| The angular damping of the
object.  
---|---  
[angularVelocity](Rigidbody-angularVelocity.html)| The angular velocity vector
of the rigidbody measured in radians per second.  
[automaticCenterOfMass](Rigidbody-automaticCenterOfMass.html)| Whether or not
to calculate the center of mass automatically.  
[automaticInertiaTensor](Rigidbody-automaticInertiaTensor.html)| Whether or
not to calculate the inertia tensor automatically.  
[centerOfMass](Rigidbody-centerOfMass.html)| The center of mass relative to
the transform's origin.  
[collisionDetectionMode](Rigidbody-collisionDetectionMode.html)| The
Rigidbody's collision detection mode.  
[constraints](Rigidbody-constraints.html)| Controls which degrees of freedom
are allowed for the simulation of this Rigidbody.  
[detectCollisions](Rigidbody-detectCollisions.html)| Should collision
detection be enabled? (By default always enabled).  
[excludeLayers](Rigidbody-excludeLayers.html)| The additional layers that all
Colliders attached to this Rigidbody should exclude when deciding if the
Collider can come into contact with another Collider.  
[freezeRotation](Rigidbody-freezeRotation.html)| Controls whether physics will
change the rotation of the object.  
[includeLayers](Rigidbody-includeLayers.html)| The additional layers that all
Colliders attached to this Rigidbody should include when deciding if the
Collider can come into contact with another Collider.  
[inertiaTensor](Rigidbody-inertiaTensor.html)| The inertia tensor of this
body, defined as a diagonal matrix in a reference frame positioned at this
body's center of mass and rotated by Rigidbody.inertiaTensorRotation.  
[inertiaTensorRotation](Rigidbody-inertiaTensorRotation.html)| The rotation of
the inertia tensor.  
[interpolation](Rigidbody-interpolation.html)| Interpolation provides a way to
manage the appearance of jitter in the movement of your Rigidbody GameObjects
at run time.  
[isKinematic](Rigidbody-isKinematic.html)| Controls whether physics affects
the rigidbody.  
[linearDamping](Rigidbody-linearDamping.html)| The linear damping of the
object.  
[linearVelocity](Rigidbody-linearVelocity.html)| The linear velocity vector of
the rigidbody. It represents the rate of change of Rigidbody position.  
[mass](Rigidbody-mass.html)| The mass of the rigidbody.  
[maxAngularVelocity](Rigidbody-maxAngularVelocity.html)| The maximum angular
velocity of the rigidbody measured in radians per second. (Default 7) range {
0, infinity }.  
[maxDepenetrationVelocity](Rigidbody-maxDepenetrationVelocity.html)| Maximum
velocity of a rigidbody when moving out of penetrating state.  
[maxLinearVelocity](Rigidbody-maxLinearVelocity.html)| The maximum linear
velocity of the rigidbody measured in meters per second.  
[position](Rigidbody-position.html)| The position of the rigidbody.  
[rotation](Rigidbody-rotation.html)| The rotation of the Rigidbody.  
[sleepThreshold](Rigidbody-sleepThreshold.html)| The mass-normalized energy
threshold, below which objects start going to sleep.  
[solverIterations](Rigidbody-solverIterations.html)| The solverIterations
determines how accurately Rigidbody joints and collision contacts are
resolved. Overrides Physics.defaultSolverIterations. Must be positive.  
[solverVelocityIterations](Rigidbody-solverVelocityIterations.html)| The
solverVelocityIterations affects how how accurately Rigidbody joints and
collision contacts are resolved. Overrides
Physics.defaultSolverVelocityIterations. Must be positive.  
[useGravity](Rigidbody-useGravity.html)| Controls whether gravity affects this
rigidbody.  
[worldCenterOfMass](Rigidbody-worldCenterOfMass.html)| The center of mass of
the rigidbody in world space (Read Only).  
  
### Public Methods

[AddExplosionForce](Rigidbody.AddExplosionForce.html)| Applies a force to a
rigidbody that simulates explosion effects.  
---|---  
[AddForce](Rigidbody.AddForce.html)| Adds a force to the Rigidbody.  
[AddForceAtPosition](Rigidbody.AddForceAtPosition.html)| Applies force at
position. As a result this will apply a torque and force on the object.  
[AddRelativeForce](Rigidbody.AddRelativeForce.html)| Adds a force to the
rigidbody relative to its coordinate system.  
[AddRelativeTorque](Rigidbody.AddRelativeTorque.html)| Adds a torque to the
rigidbody relative to its coordinate system.  
[AddTorque](Rigidbody.AddTorque.html)| Adds a torque to the rigidbody.  
[ClosestPointOnBounds](Rigidbody.ClosestPointOnBounds.html)| The closest point
to the bounding box of the attached colliders.  
[GetAccumulatedForce](Rigidbody.GetAccumulatedForce.html)| Returns the force
that the Rigidbody has accumulated before the simulation step.  
[GetAccumulatedTorque](Rigidbody.GetAccumulatedTorque.html)| Returns the
torque that the Rigidbody has accumulated before the simulation step.  
[GetPointVelocity](Rigidbody.GetPointVelocity.html)| The velocity of the
rigidbody at the point worldPoint in global space.  
[GetRelativePointVelocity](Rigidbody.GetRelativePointVelocity.html)| The
velocity relative to the rigidbody at the point relativePoint.  
[IsSleeping](Rigidbody.IsSleeping.html)| Is the rigidbody sleeping?  
[Move](Rigidbody.Move.html)| Moves the Rigidbody to position and rotates the
Rigidbody to rotation.  
[MovePosition](Rigidbody.MovePosition.html)| Moves the kinematic Rigidbody
towards position.  
[MoveRotation](Rigidbody.MoveRotation.html)| Rotates the rigidbody to
rotation.  
[PublishTransform](Rigidbody.PublishTransform.html)| Applies the position and
rotation of the Rigidbody to the corresponding Transform component.  
[ResetCenterOfMass](Rigidbody.ResetCenterOfMass.html)| Reset the center of
mass of the rigidbody.  
[ResetInertiaTensor](Rigidbody.ResetInertiaTensor.html)| Reset the inertia
tensor value and rotation.  
[SetDensity](Rigidbody.SetDensity.html)| Sets the mass based on the attached
colliders assuming a constant density.  
[Sleep](Rigidbody.Sleep.html)| Forces a rigidbody to sleep until woken up.  
[SweepTest](Rigidbody.SweepTest.html)| Tests if a rigidbody would collide with
anything, if it was moved through the Scene.  
[SweepTestAll](Rigidbody.SweepTestAll.html)| Like Rigidbody.SweepTest, but
returns all hits.  
[WakeUp](Rigidbody.WakeUp.html)| Forces a rigidbody to wake up.  
  
### Messages

[OnCollisionEnter](Rigidbody.OnCollisionEnter.html)| OnCollisionEnter is
called when this collider/rigidbody has begun touching another
rigidbody/collider.  
---|---  
[OnCollisionExit](Rigidbody.OnCollisionExit.html)| OnCollisionExit is called
when this collider/rigidbody has stopped touching another rigidbody/collider.  
[OnCollisionStay](Rigidbody.OnCollisionStay.html)| OnCollisionStay is called
once per frame for every Collider or Rigidbody that touches another Collider
or Rigidbody.  
  
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

