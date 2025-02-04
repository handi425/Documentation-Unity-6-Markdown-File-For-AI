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

# UnityEngine.AnimationModule

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

The Animation module implements Unity's animation system.

### Classes

[AimConstraint](Animations.AimConstraint.html)| Constrains the orientation of
an object relative to the position of one or more source objects, such that
the object is facing the average position of the sources.  
---|---  
[Animation](Animation.html)| The animation component is used to play back
animations.  
[AnimationClip](AnimationClip.html)| Stores keyframe based animations.  
[AnimationEvent](AnimationEvent.html)| AnimationEvent lets you call a script
function similar to SendMessage as part of playing back an animation.  
[AnimationPlayableBinding](Animations.AnimationPlayableBinding.html)| A
PlayableBinding that contains information representing an
AnimationPlayableOutput.  
[AnimationPlayableOutputExtensions](Experimental.Animations.AnimationPlayableOutputExtensions.html)|
Static class providing experimental extension methods for
AnimationPlayableOutput .  
[AnimationPlayableUtilities](Playables.AnimationPlayableUtilities.html)|
Implements high-level utility methods to simplify use of the Playable API with
Animations.  
[AnimationSceneHandleUtility](Animations.AnimationSceneHandleUtility.html)|
Static class providing utility functions for animation scene handles.  
[AnimationState](AnimationState.html)| The AnimationState gives full control
over animation blending.  
[AnimationStreamHandleUtility](Animations.AnimationStreamHandleUtility.html)|
Static class providing utility functions for animation stream handles.  
[Animator](Animator.html)| Interface to control the Mecanim animation system.  
[AnimatorControllerParameter](AnimatorControllerParameter.html)| Used to
communicate between scripting and the controller. Some parameters can be set
in scripting and used by the controller, while other parameters are based on
Custom Curves in Animation Clips and can be sampled using the scripting API.  
[AnimatorJobExtensions](Animations.AnimatorJobExtensions.html)| Static class
providing extension methods for Animator and the animation C# jobs.  
[AnimatorOverrideController](AnimatorOverrideController.html)| Interface to
control Animator Override Controller.  
[AnimatorUtility](AnimatorUtility.html)| Various utilities for animator
manipulation.  
[Avatar](Avatar.html)| Avatar definition.  
[AvatarBuilder](AvatarBuilder.html)| Class to build avatars from user scripts.  
[AvatarMask](AvatarMask.html)| AvatarMask is used to mask out humanoid body
parts and transforms.  
[DiscreteEvaluationAttribute](Animations.DiscreteEvaluationAttribute.html)|
Use this attribute to indicate that a property will be evaluated as a discrete
value during animation playback.  
[GenericBindingUtility](Animations.GenericBindingUtility.html)| Animation
utility functions for reading and writing values from Unity components.  
[HumanPoseHandler](HumanPoseHandler.html)| Use this class to create, read, and
write the HumanPose for a humanoid avatar skeleton hierarchy or an avatar
pose.  
[HumanTrait](HumanTrait.html)| Details of all the human bone and muscle types
defined by Mecanim.  
[LookAtConstraint](Animations.LookAtConstraint.html)|  Constrains the
orientation of an object relative to the position of one or more source
objects, such that the object is facing the average position of the sources.
The LookAtConstraint is a simplified AimConstraint typically used with a
Camera.  
[Motion](Motion.html)| Base class for AnimationClips and BlendTrees.  
[NotKeyableAttribute](Animations.NotKeyableAttribute.html)| Use this attribute
in a script to mark a property as non-animatable.  
[ParentConstraint](Animations.ParentConstraint.html)| Constrains the
orientation and translation of an object to one or more source objects. The
constrained object behaves as if it is in the hierarchy of the sources.  
[PositionConstraint](Animations.PositionConstraint.html)| Constrains the
position of an object relative to the position of one or more source objects.  
[RotationConstraint](Animations.RotationConstraint.html)| Constrains the
rotation of an object relative to the rotation of one or more source objects.  
[RuntimeAnimatorController](RuntimeAnimatorController.html)| The runtime
representation of the AnimatorController. Use this representation to change
the Animator Controller during runtime.  
[ScaleConstraint](Animations.ScaleConstraint.html)| Constrains the scale of an
object relative to the scale of one or more source objects.  
[SharedBetweenAnimatorsAttribute](SharedBetweenAnimatorsAttribute.html)| The
SharedBetweenAnimatorsAttribute specifies that this StateMachineBehaviour is
instantiated only once and shared by all Animator instances. This attribute
reduces the memory footprint for each controller instance.  
[StateMachineBehaviour](StateMachineBehaviour.html)| StateMachineBehaviour is
a component that can be added to a state machine state. It's the base class
any script on a state must derive from.  
  
### Structs

[AnimationClipPlayable](Animations.AnimationClipPlayable.html)| A Playable
that controls an AnimationClip.  
---|---  
[AnimationHumanStream](Animations.AnimationHumanStream.html)| The humanoid
stream of animation data passed from one Playable to another.  
[AnimationLayerMixerPlayable](Animations.AnimationLayerMixerPlayable.html)| An
implementation of IPlayable that controls an animation layer mixer.  
[AnimationMixerPlayable](Animations.AnimationMixerPlayable.html)| An
implementation of IPlayable that controls an animation mixer.  
[AnimationPlayableOutput](Animations.AnimationPlayableOutput.html)| A
IPlayableOutput implementation that connects the PlayableGraph to an Animator
in the Scene.  
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html)| A Playable
that can run a custom, multi-threaded animation job.  
[AnimationStream](Animations.AnimationStream.html)| The stream of animation
data passed from one Playable to another.  
[AnimatorClipInfo](AnimatorClipInfo.html)| Information about clip being played
and blended by the Animator.  
[AnimatorControllerPlayable](Animations.AnimatorControllerPlayable.html)| An
implementation of IPlayable that controls an animation
RuntimeAnimatorController.  
[AnimatorStateInfo](AnimatorStateInfo.html)| Information about the current or
next state.  
[AnimatorTransitionInfo](AnimatorTransitionInfo.html)| Information about the
current transition.  
[BoundProperty](Animations.BoundProperty.html)| A BoundProperty is a safe
handle to read and write value in a generic way from any Unity components.  
[ConstraintSource](Animations.ConstraintSource.html)| Represents a source for
the constraint.  
[GenericBinding](Animations.GenericBinding.html)| Defines an animatable
property on a Unity Component.  
[HumanBone](HumanBone.html)| The mapping between a bone in the model and the
conceptual bone in the Mecanim human anatomy.  
[HumanDescription](HumanDescription.html)| Class that holds humanoid avatar
parameters to pass to the AvatarBuilder.BuildHumanAvatar function.  
[HumanLimit](HumanLimit.html)| This class stores the rotation limits that
define the muscle for a single human bone.  
[HumanPose](HumanPose.html)| Retargetable humanoid pose.  
[MatchTargetWeightMask](MatchTargetWeightMask.html)| Use this struct to
specify the position and rotation weight mask for Animator.MatchTarget.  
[MuscleHandle](Animations.MuscleHandle.html)| Handle for a muscle in the
AnimationHumanStream.  
[PropertySceneHandle](Animations.PropertySceneHandle.html)| Handle to read a
Component property on an object in the Scene.  
[PropertyStreamHandle](Animations.PropertyStreamHandle.html)| Handle for a
Component property on an object in the AnimationStream.  
[SkeletonBone](SkeletonBone.html)| Details of the Transform name mapped to the
skeleton bone of a model and its default position and rotation in the T-pose.  
[TransformSceneHandle](Animations.TransformSceneHandle.html)| Handle to read
position, rotation and scale of an object in the Scene.  
[TransformStreamHandle](Animations.TransformStreamHandle.html)| Position,
rotation and scale of an object in the AnimationStream.  
  
### Enumerations

[AnimationBlendMode](AnimationBlendMode.html)| Used by Animation.Play
function.  
---|---  
[AnimationCullingType](AnimationCullingType.html)| This enum controlls culling
of Animation component.  
[AnimationStreamSource](Experimental.Animations.AnimationStreamSource.html)|
Describes how an AnimationStream is initialized  
[AnimationUpdateMode](AnimationUpdateMode.html)| The update mode of the
Animation component.  
[AnimatorControllerParameterType](AnimatorControllerParameterType.html)| The
type of the parameter.  
[AnimatorCullingMode](AnimatorCullingMode.html)| Culling mode for the
Animator.  
[AnimatorRecorderMode](AnimatorRecorderMode.html)| The mode of the Animator's
recorder.  
[AnimatorUpdateMode](AnimatorUpdateMode.html)| The update mode of the
Animator.  
[ArmDof](ArmDof.html)| Enumeration of all the muscles in an arm.  
[AvatarIKGoal](AvatarIKGoal.html)| IK Goal.  
[AvatarIKHint](AvatarIKHint.html)| IK Hint.  
[AvatarMaskBodyPart](AvatarMaskBodyPart.html)| Avatar body part.  
[AvatarTarget](AvatarTarget.html)| Target.  
[Axis](Animations.Axis.html)| Represents the axes used in 3D space.  
[BodyDof](BodyDof.html)| Enumeration of all the muscles in the body.  
[CustomStreamPropertyType](Animations.CustomStreamPropertyType.html)| The type
of custom stream property to create using BindCustomStreamProperty  
[DurationUnit](DurationUnit.html)| Describe the unit of a duration.  
[FingerDof](FingerDof.html)| Enumeration of all the muscles in a finger.  
[HeadDof](HeadDof.html)| Enumeration of all the muscles in the head.  
[HumanBodyBones](HumanBodyBones.html)| Human Body Bones.  
[HumanPartDof](HumanPartDof.html)| Enumeration of all the parts in a human.  
[LegDof](LegDof.html)| Enumeration of all the muscles in a leg.  
[PlayMode](PlayMode.html)| Used by Animation.Play function.  
[QueueMode](QueueMode.html)| Used by Animation.Play function.  
  
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

