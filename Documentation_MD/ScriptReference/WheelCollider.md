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

# WheelCollider

class in UnityEngine

/

Inherits from:[Collider](Collider.html)

/

Implemented in:[UnityEngine.VehiclesModule](UnityEngine.VehiclesModule.html)

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

[Switch to Manual](../Manual/class-WheelCollider.html "Go to WheelCollider
Component in the Manual")

### Description

A special collider for vehicle wheels.

Wheel collider is used to model vehicle wheels. It simulates a spring and
damper suspension setup, and uses a slip based tire friction model to
calculate wheel contact forces.  
  
Wheel's collision detection is performed by casting a ray from
[center](WheelCollider-center.html) downwards the local y-axis. The wheel has
a [radius](WheelCollider-radius.html) and can extend downwards by
[suspensionDistance](WheelCollider-suspensionDistance.html) amount.  
  
The wheel is controlled with [motorTorque](WheelCollider-motorTorque.html),
[brakeTorque](WheelCollider-brakeTorque.html) and [steerAngle](WheelCollider-
steerAngle.html) properties.  
  
Wheel collider computes friction separately from the rest of physics engine,
using a slip based friction model. This allows for more realistic behaviour,
but makes wheel colliders ignore standard
[PhysicsMaterial](PhysicsMaterial.html) settings. Simulation of different road
materials is done by changing the [forwardFriction](WheelCollider-
forwardFriction.html) and [sidewaysFriction](WheelCollider-
sidewaysFriction.html) based on what material the wheel is hitting. Additional
resources: [GetGroundHit](WheelCollider.GetGroundHit.html) and
[WheelFrictionCurve](WheelFrictionCurve.html).

### Properties

[brakeTorque](WheelCollider-brakeTorque.html)| Brake torque expressed in
Newton metres.  
---|---  
[center](WheelCollider-center.html)| The center of the wheel, measured in the
object's local space.  
[forceAppPointDistance](WheelCollider-forceAppPointDistance.html)| Application
point of the suspension and tire forces measured from the base of the resting
wheel.  
[forwardFriction](WheelCollider-forwardFriction.html)| Properties of tire
friction in the direction the wheel is pointing in.  
[isGrounded](WheelCollider-isGrounded.html)| Indicates whether the wheel
currently collides with something (Read Only).  
[mass](WheelCollider-mass.html)| The mass of the wheel, expressed in
kilograms. Must be larger than zero. Typical values would be in range (20,80).  
[motorTorque](WheelCollider-motorTorque.html)| Motor torque on the wheel axle
expressed in Newton metres. Positive or negative depending on direction.  
[radius](WheelCollider-radius.html)| The radius of the wheel, measured in
local space.  
[rotationSpeed](WheelCollider-rotationSpeed.html)| Rotation speed of the
wheel, measured in degrees per second.  
[rpm](WheelCollider-rpm.html)| Current wheel axle rotation speed, in rotations
per minute (Read Only).  
[sidewaysFriction](WheelCollider-sidewaysFriction.html)| Properties of tire
friction in the sideways direction.  
[sprungMass](WheelCollider-sprungMass.html)| The mass supported by this
WheelCollider.  
[steerAngle](WheelCollider-steerAngle.html)| Steering angle in degrees, always
around the local y-axis.  
[suspensionDistance](WheelCollider-suspensionDistance.html)| Maximum extension
distance of wheel suspension, measured in local space.  
[suspensionExpansionLimited](WheelCollider-suspensionExpansionLimited.html)|
Limits the expansion velocity of the Wheel Collider's suspension. If you set
this property on a Rigidbody that has several Wheel Colliders, such as a
vehicle, then it affects all other Wheel Colliders on the Rigidbody.  
[suspensionSpring](WheelCollider-suspensionSpring.html)| The parameters of
wheel's suspension. The suspension attempts to reach a target position by
applying a linear force and a damping force.  
[wheelDampingRate](WheelCollider-wheelDampingRate.html)| The damping rate of
the wheel. Must be larger than zero.  
  
### Public Methods

[ConfigureVehicleSubsteps](WheelCollider.ConfigureVehicleSubsteps.html)|
Configure vehicle sub-stepping parameters.  
---|---  
[GetGroundHit](WheelCollider.GetGroundHit.html)| Gets ground collision data
for the wheel.  
[GetWorldPose](WheelCollider.GetWorldPose.html)| Gets the world space pose of
the wheel accounting for ground contact, suspension limits, steer angle, and
rotation angle (angles in degrees).  
[ResetSprungMasses](WheelCollider.ResetSprungMasses.html)| Reset the sprung
masses of the vehicle.  
  
### Inherited Members

### Properties

[attachedArticulationBody](Collider-attachedArticulationBody.html)| The
articulation body the collider is attached to.  
---|---  
[attachedRigidbody](Collider-attachedRigidbody.html)| The rigidbody the
collider is attached to.  
[bounds](Collider-bounds.html)| The world space bounding volume of the
collider (Read Only).  
[contactOffset](Collider-contactOffset.html)| Contact offset value of this
collider.  
[enabled](Collider-enabled.html)| Enabled Colliders will collide with other
Colliders, disabled Colliders won't.  
[excludeLayers](Collider-excludeLayers.html)| The additional layers that this
Collider should exclude when deciding if the Collider can contact another
Collider.  
[GeometryHolder](Collider.GeometryHolder.html)| The structure holding the
geometric shape of the collider and its type. (Read Only)  
[hasModifiableContacts](Collider-hasModifiableContacts.html)| Specify whether
this Collider's contacts are modifiable or not.  
[includeLayers](Collider-includeLayers.html)| The additional layers that this
Collider should include when deciding if the Collider can contact another
Collider.  
[isTrigger](Collider-isTrigger.html)| Specify if this collider is configured
as a trigger.  
[layerOverridePriority](Collider-layerOverridePriority.html)| A decision
priority assigned to this Collider used when there is a conflicting decision
on whether a Collider can contact another Collider.  
[material](Collider-material.html)| The material used by the collider.  
[providesContacts](Collider-providesContacts.html)| Whether or not this
Collider generates contacts for Physics.ContactEvent.  
[sharedMaterial](Collider-sharedMaterial.html)| The shared physics material of
this collider.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[ClosestPoint](Collider.ClosestPoint.html)| Returns a point on the collider
that is closest to a given location.  
---|---  
[ClosestPointOnBounds](Collider.ClosestPointOnBounds.html)| The closest point
to the bounding box of the attached collider.  
[GetGeometry](Collider.GetGeometry.html)| Returns the geometric shape of the
collider of the requested type.  
[Raycast](Collider.Raycast.html)| Casts a Ray that ignores all Colliders
except this one.  
[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
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

[OnCollisionEnter](Collider.OnCollisionEnter.html)| OnCollisionEnter is called
when this collider/rigidbody has begun touching another rigidbody/collider.  
---|---  
[OnCollisionExit](Collider.OnCollisionExit.html)| OnCollisionExit is called
when this collider/rigidbody has stopped touching another rigidbody/collider.  
[OnCollisionStay](Collider.OnCollisionStay.html)| OnCollisionStay is called
once per frame for every Collider or Rigidbody that touches another Collider
or Rigidbody.  
[OnTriggerEnter](Collider.OnTriggerEnter.html)| Called when a Collider with
the Collider.isTrigger property overlaps another Collider.  
[OnTriggerExit](Collider.OnTriggerExit.html)| OnTriggerExit is called when the
Collider other has stopped touching the trigger.  
[OnTriggerStay](Collider.OnTriggerStay.html)| OnTriggerStay is called almost
all the frames for every Collider other that is touching the trigger. The
function is on the physics timer so it won't necessarily run every frame.  
  
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

