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

# Animator

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

[Switch to Manual](../Manual/class-Animator.html "Go to Animator Component in
the Manual")

### Description

Interface to control the Mecanim animation system.

### Properties

[angularVelocity](Animator-angularVelocity.html)| Gets the avatar angular
velocity for the last evaluated frame.  
---|---  
[animatePhysics](Animator-animatePhysics.html)| When enabled, the physics
system uses animated transforms from GameObjects with kinematic Rigidbody
components to influence other GameObjects.  
[applyRootMotion](Animator-applyRootMotion.html)| Should root motion be
applied?  
[avatar](Animator-avatar.html)| Gets/Sets the current Avatar.  
[avatarRoot](Animator-avatarRoot.html)| Returns the Avatar root Transform.  
[bodyPosition](Animator-bodyPosition.html)| The position of the body center of
mass.  
[bodyRotation](Animator-bodyRotation.html)| The rotation of the body center of
mass.  
[cullingMode](Animator-cullingMode.html)| Controls culling of this Animator
component.  
[deltaPosition](Animator-deltaPosition.html)| Gets the avatar delta position
for the last evaluated frame.  
[deltaRotation](Animator-deltaRotation.html)| Gets the avatar delta rotation
for the last evaluated frame.  
[feetPivotActive](Animator-feetPivotActive.html)| Blends pivot point between
body center of mass and feet pivot.  
[fireEvents](Animator-fireEvents.html)| Sets whether the Animator sends events
of type AnimationEvent.  
[gravityWeight](Animator-gravityWeight.html)| The current gravity weight based
on current animations that are played.  
[hasBoundPlayables](Animator-hasBoundPlayables.html)| Returns true if Animator
has any playables assigned to it.  
[hasRootMotion](Animator-hasRootMotion.html)| Returns true if the current rig
has root motion.  
[hasTransformHierarchy](Animator-hasTransformHierarchy.html)| Returns true if
the object has a transform hierarchy.  
[humanScale](Animator-humanScale.html)| Returns the scale of the current
Avatar for a humanoid rig, (1 by default if the rig is generic).  
[isHuman](Animator-isHuman.html)| Returns true if the current rig is humanoid,
false if it is generic.  
[isInitialized](Animator-isInitialized.html)| Returns whether the animator is
initialized successfully.  
[isMatchingTarget](Animator-isMatchingTarget.html)| If automatic matching is
active.  
[isOptimizable](Animator-isOptimizable.html)| Returns true if the current rig
is optimizable with AnimatorUtility.OptimizeTransformHierarchy.  
[keepAnimatorStateOnDisable](Animator-keepAnimatorStateOnDisable.html)|
Controls the behaviour of the Animator component when a GameObject is
inactive.  
[layerCount](Animator-layerCount.html)| Returns the number of layers in the
controller.  
[layersAffectMassCenter](Animator-layersAffectMassCenter.html)| Additional
layers affects the center of mass.  
[leftFeetBottomHeight](Animator-leftFeetBottomHeight.html)| Get left foot
bottom height.  
[parameterCount](Animator-parameterCount.html)| Returns the number of
parameters in the controller.  
[parameters](Animator-parameters.html)| The AnimatorControllerParameter list
used by the animator. (Read Only)  
[pivotPosition](Animator-pivotPosition.html)| Get the current position of the
pivot.  
[pivotWeight](Animator-pivotWeight.html)| Gets the pivot weight.  
[playableGraph](Animator-playableGraph.html)| The PlayableGraph created by the
Animator.  
[playbackTime](Animator-playbackTime.html)| Sets the playback position in the
recording buffer.  
[recorderMode](Animator-recorderMode.html)| Gets the mode of the Animator
recorder.  
[recorderStartTime](Animator-recorderStartTime.html)| Start time of the first
frame of the buffer relative to the frame at which StartRecording was called.  
[recorderStopTime](Animator-recorderStopTime.html)| End time of the recorded
clip relative to when StartRecording was called.  
[rightFeetBottomHeight](Animator-rightFeetBottomHeight.html)| Get right foot
bottom height.  
[rootPosition](Animator-rootPosition.html)| The root position, the position of
the game object.  
[rootRotation](Animator-rootRotation.html)| The root rotation, the rotation of
the game object.  
[runtimeAnimatorController](Animator-runtimeAnimatorController.html)| The
runtime representation of AnimatorController that controls the Animator.  
[speed](Animator-speed.html)| The playback speed of the Animator. 1 is normal
playback speed.  
[stabilizeFeet](Animator-stabilizeFeet.html)| Automatic stabilization of feet
during transition and blending.  
[targetPosition](Animator-targetPosition.html)| Returns the position of the
target specified by SetTarget.  
[targetRotation](Animator-targetRotation.html)| Returns the rotation of the
target specified by SetTarget.  
[updateMode](Animator-updateMode.html)| Specifies the update mode of the
Animator.  
[velocity](Animator-velocity.html)| Gets the avatar velocity for the last
evaluated frame.  
[writeDefaultValuesOnDisable](Animator-writeDefaultValuesOnDisable.html)|
Specifies whether playable graph values are reset or preserved when the
Animator is disabled.  
  
### Public Methods

[ApplyBuiltinRootMotion](Animator.ApplyBuiltinRootMotion.html)| Apply the
default Root Motion.  
---|---  
[CrossFade](Animator.CrossFade.html)| Creates a crossfade from the current
state to any other state using normalized times.  
[CrossFadeInFixedTime](Animator.CrossFadeInFixedTime.html)| Creates a
crossfade from the current state to any other state using times in seconds.  
[GetAnimatorTransitionInfo](Animator.GetAnimatorTransitionInfo.html)| Returns
an AnimatorTransitionInfo with the informations on the current transition.  
[GetBehaviour](Animator.GetBehaviour.html)| Returns the first
StateMachineBehaviour that matches type T or is derived from T. Returns null
if none are found.  
[GetBehaviours](Animator.GetBehaviours.html)| Returns all
StateMachineBehaviour that match type T or are derived from T. Returns null if
none are found.  
[GetBoneTransform](Animator.GetBoneTransform.html)| Retrieves the Transform
mapped to a human bone based on its id.  
[GetBool](Animator.GetBool.html)| Returns the value of the given boolean
parameter.  
[GetCurrentAnimatorClipInfo](Animator.GetCurrentAnimatorClipInfo.html)|
Returns an array of all the AnimatorClipInfo in the current state of the given
layer.  
[GetCurrentAnimatorClipInfoCount](Animator.GetCurrentAnimatorClipInfoCount.html)|
Returns the number of AnimatorClipInfo in the current state.  
[GetCurrentAnimatorStateInfo](Animator.GetCurrentAnimatorStateInfo.html)|
Returns an AnimatorStateInfo with the information on the current state.  
[GetFloat](Animator.GetFloat.html)| Returns the value of the given float
parameter.  
[GetIKHintPosition](Animator.GetIKHintPosition.html)| Gets the position of an
IK hint.  
[GetIKHintPositionWeight](Animator.GetIKHintPositionWeight.html)| Gets the
translative weight of an IK Hint (0 = at the original animation before IK, 1 =
at the hint).  
[GetIKPosition](Animator.GetIKPosition.html)| Gets the position of an IK goal.  
[GetIKPositionWeight](Animator.GetIKPositionWeight.html)| Gets the translative
weight of an IK goal (0 = at the original animation before IK, 1 = at the
goal).  
[GetIKRotation](Animator.GetIKRotation.html)| Gets the rotation of an IK goal.  
[GetIKRotationWeight](Animator.GetIKRotationWeight.html)| Gets the rotational
weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).  
[GetInteger](Animator.GetInteger.html)| Returns the value of the given integer
parameter.  
[GetLayerIndex](Animator.GetLayerIndex.html)| Returns the index of the layer
with the given name.  
[GetLayerName](Animator.GetLayerName.html)| Returns the layer name.  
[GetLayerWeight](Animator.GetLayerWeight.html)| Returns the weight of the
layer at the specified index.  
[GetNextAnimatorClipInfo](Animator.GetNextAnimatorClipInfo.html)| Returns an
array of all the AnimatorClipInfo in the next state of the given layer.  
[GetNextAnimatorClipInfoCount](Animator.GetNextAnimatorClipInfoCount.html)|
Returns the number of AnimatorClipInfo in the next state.  
[GetNextAnimatorStateInfo](Animator.GetNextAnimatorStateInfo.html)| Returns an
AnimatorStateInfo with the information on the next state.  
[GetParameter](Animator.GetParameter.html)| See AnimatorController.parameters.  
[HasState](Animator.HasState.html)| Returns true if the state exists in this
layer, false otherwise.  
[InterruptMatchTarget](Animator.InterruptMatchTarget.html)| Interrupts the
automatic target matching.  
[IsInTransition](Animator.IsInTransition.html)| Returns true if there is a
transition on the given layer, false otherwise.  
[IsParameterControlledByCurve](Animator.IsParameterControlledByCurve.html)|
Returns true if the parameter is controlled by a curve, false otherwise.  
[MatchTarget](Animator.MatchTarget.html)| Automatically adjust the GameObject
position and rotation.  
[Play](Animator.Play.html)| Plays a state.  
[PlayInFixedTime](Animator.PlayInFixedTime.html)| Plays a state.  
[Rebind](Animator.Rebind.html)| Rebind all the animated properties and mesh
data with the Animator.  
[ResetTrigger](Animator.ResetTrigger.html)| Resets the value of the given
trigger parameter.  
[SetBoneLocalRotation](Animator.SetBoneLocalRotation.html)| Sets local
rotation of a human bone during a IK pass.  
[SetBool](Animator.SetBool.html)| Sets the value of the given boolean
parameter.  
[SetFloat](Animator.SetFloat.html)| Send float values to the Animator to
affect transitions.  
[SetIKHintPosition](Animator.SetIKHintPosition.html)| Sets the position of an
IK hint.  
[SetIKHintPositionWeight](Animator.SetIKHintPositionWeight.html)| Sets the
translative weight of an IK hint (0 = at the original animation before IK, 1 =
at the hint).  
[SetIKPosition](Animator.SetIKPosition.html)| Sets the position of an IK goal.  
[SetIKPositionWeight](Animator.SetIKPositionWeight.html)| Sets the translative
weight of an IK goal (0 = at the original animation before IK, 1 = at the
goal).  
[SetIKRotation](Animator.SetIKRotation.html)| Sets the rotation of an IK goal.  
[SetIKRotationWeight](Animator.SetIKRotationWeight.html)| Sets the rotational
weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).  
[SetInteger](Animator.SetInteger.html)| Sets the value of the given integer
parameter.  
[SetLayerWeight](Animator.SetLayerWeight.html)| Sets the weight of the layer
at the given index.  
[SetLookAtPosition](Animator.SetLookAtPosition.html)| Sets the look at
position.  
[SetLookAtWeight](Animator.SetLookAtWeight.html)| Set look at weights.  
[SetTarget](Animator.SetTarget.html)| Sets an AvatarTarget and a
targetNormalizedTime for the current state.  
[SetTrigger](Animator.SetTrigger.html)| Sets the value of the given trigger
parameter.  
[StartPlayback](Animator.StartPlayback.html)| Sets the animator in playback
mode.  
[StartRecording](Animator.StartRecording.html)| Sets the animator in recording
mode, and allocates a circular buffer of size frameCount.  
[StopPlayback](Animator.StopPlayback.html)| Stops the animator playback mode.
When playback stops, the avatar resumes getting control from game logic.  
[StopRecording](Animator.StopRecording.html)| Stops animator record mode.  
[Update](Animator.Update.html)| Evaluates the animator based on deltaTime.  
[WriteDefaultValues](Animator.WriteDefaultValues.html)| Forces a write of the
default values stored in the animator.  
  
### Static Methods

[StringToHash](Animator.StringToHash.html)| Generates a parameter id from a
string.  
---|---  
  
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

