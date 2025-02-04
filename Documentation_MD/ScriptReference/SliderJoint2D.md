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

# SliderJoint2D

class in UnityEngine

/

Inherits from:[AnchoredJoint2D](AnchoredJoint2D.html)

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

Joint that restricts the motion of a [Rigidbody2D](Rigidbody2D.html) object to
a single line.

Additional resources: [Rigidbody2D](Rigidbody2D.html),
[DistanceJoint2D](DistanceJoint2D.html), [HingeJoint2D](HingeJoint2D.html),
[SpringJoint2D](SpringJoint2D.html),
[JointTranslationLimits2D](JointTranslationLimits2D.html).

### Properties

[angle](SliderJoint2D-angle.html)| The angle of the line in space (in
degrees).  
---|---  
[autoConfigureAngle](SliderJoint2D-autoConfigureAngle.html)| Should the angle
be calculated automatically?  
[jointSpeed](SliderJoint2D-jointSpeed.html)| The current joint speed.  
[jointTranslation](SliderJoint2D-jointTranslation.html)| The current joint
translation.  
[limits](SliderJoint2D-limits.html)| Restrictions on how far the joint can
slide in each direction along the line.  
[limitState](SliderJoint2D-limitState.html)| Gets the state of the joint
limit.  
[motor](SliderJoint2D-motor.html)| Parameters for a motor force that is
applied automatically to the Rigibody2D along the line.  
[referenceAngle](SliderJoint2D-referenceAngle.html)| The angle (in degrees)
referenced between the two bodies used as the constraint for the joint.  
[useLimits](SliderJoint2D-useLimits.html)| Should motion limits be used?  
[useMotor](SliderJoint2D-useMotor.html)| Should a motor force be applied
automatically to the Rigidbody2D?  
  
### Public Methods

[GetMotorForce](SliderJoint2D.GetMotorForce.html)| Gets the motor force of the
joint given the specified timestep.  
---|---  
  
### Inherited Members

### Properties

[anchor](AnchoredJoint2D-anchor.html)| The joint's anchor point on the object
that has the joint component.  
---|---  
[autoConfigureConnectedAnchor](AnchoredJoint2D-autoConfigureConnectedAnchor.html)|
Should the connectedAnchor be calculated automatically?  
[connectedAnchor](AnchoredJoint2D-connectedAnchor.html)| The joint's anchor
point on the second object (ie, the one which doesn't have the joint
component).  
[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[attachedRigidbody](Joint2D-attachedRigidbody.html)| The Rigidbody2D attached
to the Joint2D.  
[breakAction](Joint2D-breakAction.html)| The action to take when the joint
breaks the breakForce or breakTorque.  
[breakForce](Joint2D-breakForce.html)| The force that needs to be applied for
this joint to break.  
[breakTorque](Joint2D-breakTorque.html)| The torque that needs to be applied
for this joint to break.  
[connectedBody](Joint2D-connectedBody.html)| The Rigidbody2D object to which
the other end of the joint is attached (ie, the object without the joint
component).  
[enableCollision](Joint2D-enableCollision.html)| Should the two Rigidbody2D
connected with this joint collide with each other?  
[reactionForce](Joint2D-reactionForce.html)| Gets the reaction force of the
joint.  
[reactionTorque](Joint2D-reactionTorque.html)| Gets the reaction torque of the
joint.  
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
[GetReactionForce](Joint2D.GetReactionForce.html)| Gets the reaction force of
the joint given the specified timeStep.  
[GetReactionTorque](Joint2D.GetReactionTorque.html)| Gets the reaction torque
of the joint given the specified timeStep.  
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

[OnJointBreak2D](Joint2D.OnJointBreak2D.html)| Called when a Joint2D attached
to the same game object breaks.  
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

