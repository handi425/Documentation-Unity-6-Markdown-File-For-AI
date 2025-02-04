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

# CircleCollider2D

class in UnityEngine

/

Inherits from:[Collider2D](Collider2D.html)

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

Collider for 2D physics representing an circle.

Additional resources: [BoxCollider](BoxCollider.html) class,
[PolygonCollider2D](PolygonCollider2D.html) class.

### Properties

[radius](CircleCollider2D-radius.html)| Radius of the circle.  
---|---  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[attachedRigidbody](Collider2D-attachedRigidbody.html)| The Rigidbody2D
attached to the Collider2D.  
[bounceCombine](Collider2D-bounceCombine.html)| The bounciness combine mode
used by the Collider2D.  
[bounciness](Collider2D-bounciness.html)| The bounciness used by the
Collider2D.  
[bounds](Collider2D-bounds.html)| The world space bounding area of the
collider.  
[callbackLayers](Collider2D-callbackLayers.html)| The Layers that this
Collider2D will report collision or trigger callbacks for during a contact
with another Collider2D.  
[composite](Collider2D-composite.html)| Get the CompositeCollider2D that is
available to be attached to the collider.  
[compositeCapable](Collider2D-compositeCapable.html)| Indicates if this
Collider2D is capable of being composited by the CompositeCollider2D.  
[compositeOperation](Collider2D-compositeOperation.html)| The composite
operation to be used by a CompositeCollider2D.  
[compositeOrder](Collider2D-compositeOrder.html)| The composite operation
order to be used when a CompositeCollider2D is used.  
[contactCaptureLayers](Collider2D-contactCaptureLayers.html)| The layers of
other Collider2D involved in contacts with this Collider2D that will be
captured.  
[density](Collider2D-density.html)| The density of the collider used to
calculate its mass (when auto mass is enabled).  
[errorState](Collider2D-errorState.html)| The error state that indicates the
state of the physics shapes the 2D Collider tried to create. (Read Only)  
[excludeLayers](Collider2D-excludeLayers.html)| The additional Layers that
this Collider2D should exclude when deciding if a contact with another
Collider2D should happen or not.  
[forceReceiveLayers](Collider2D-forceReceiveLayers.html)| The Layers that this
Collider2D can receive forces from during a Collision contact with another
Collider2D.  
[forceSendLayers](Collider2D-forceSendLayers.html)| The Layers that this
Collider2D is allowed to send forces to during a Collision contact with
another Collider2D.  
[friction](Collider2D-friction.html)| The friction used by the Collider2D.  
[frictionCombine](Collider2D-frictionCombine.html)| The friction combine mode
used by the Collider2D.  
[includeLayers](Collider2D-includeLayers.html)| The additional Layers that
this Collider2D should include when deciding if a contact with another
Collider2D should happen or not.  
[isTrigger](Collider2D-isTrigger.html)| Is this collider configured as a
trigger?  
[layerOverridePriority](Collider2D-layerOverridePriority.html)| A decision
priority assigned to this Collider2D used when there is a conflicting decision
on whether a contact between itself and another Collision2D should happen or
not.  
[localToWorldMatrix](Collider2D-localToWorldMatrix.html)| The transformation
matrix used to transform the Collider physics shapes to world space.  
[offset](Collider2D-offset.html)| The local offset of the collider geometry.  
[shapeCount](Collider2D-shapeCount.html)| The number of active PhysicsShape2D
the Collider2D is currently using.  
[sharedMaterial](Collider2D-sharedMaterial.html)| The PhysicsMaterial2D that
is applied to this collider.  
[usedByEffector](Collider2D-usedByEffector.html)| Whether the collider is used
by an attached effector or not.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[Cast](Collider2D.Cast.html)| Casts the Collider shape into the Scene starting
at the Collider position ignoring the Collider itself.  
---|---  
[ClosestPoint](Collider2D.ClosestPoint.html)| Returns a point on the perimeter
of this Collider that is closest to the specified position.  
[CreateMesh](Collider2D.CreateMesh.html)| Creates a planar Mesh that is
identical to the area defined by the Collider2D geometry.  
[Distance](Collider2D.Distance.html)| Calculates the minimum separation of
this collider against another collider.  
[GetContacts](Collider2D.GetContacts.html)| Retrieves all contact points for
this Collider.  
[GetShapeBounds](Collider2D.GetShapeBounds.html)| Retrieves a list of Bounds
for all PhysicsShape2D created by this Collider2D, and returns the combined
Bounds of the retrieved list.  
[GetShapeHash](Collider2D.GetShapeHash.html)| Generates a simple hash value
based upon the geometry of the Collider2D.  
[GetShapes](Collider2D.GetShapes.html)| Gets all the PhysicsShape2D used by
the Collider2D.  
[IsTouching](Collider2D.IsTouching.html)| Check whether this collider is
touching the collider or not.  
[IsTouchingLayers](Collider2D.IsTouchingLayers.html)| Checks whether this
collider is touching any colliders on the specified layerMask or not.  
[Overlap](Collider2D.Overlap.html)| Get a list of all Colliders that overlap
this Collider.  
[OverlapPoint](Collider2D.OverlapPoint.html)| Check if a collider overlaps a
point in space.  
[Raycast](Collider2D.Raycast.html)| Casts a ray into the Scene that starts at
the Collider position and ignores the Collider itself.  
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

[OnCollisionEnter2D](Collider2D.OnCollisionEnter2D.html)| Sent when an
incoming collider makes contact with this object's collider (2D physics only).  
---|---  
[OnCollisionExit2D](Collider2D.OnCollisionExit2D.html)| Sent when a collider
on another object stops touching this object's collider (2D physics only).  
[OnCollisionStay2D](Collider2D.OnCollisionStay2D.html)| Sent each frame where
a collider on another object is touching this object's collider (2D physics
only).  
[OnTriggerEnter2D](Collider2D.OnTriggerEnter2D.html)| Sent when another object
enters a trigger collider attached to this object (2D physics only).  
[OnTriggerExit2D](Collider2D.OnTriggerExit2D.html)| Sent when another object
leaves a trigger collider attached to this object (2D physics only).  
[OnTriggerStay2D](Collider2D.OnTriggerStay2D.html)| Sent each frame where
another object is within a trigger collider attached to this object (2D
physics only).  
  
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

