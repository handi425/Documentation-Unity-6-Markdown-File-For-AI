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

# AnimationHumanStream

struct in UnityEngine.Animations

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

[ ]()

### Description

The humanoid stream of animation data passed from one
[Playable](Playables.Playable.html) to another.

The AnimationHumanStream structure is passed through the animation
[Playable](Playables.Playable.html) structures, like
[AnimationClipPlayable](Animations.AnimationClipPlayable.html) and
[AnimationMixerPlayable](Animations.AnimationMixerPlayable.html). They can be
modified when used with an
[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html), like the
[AnimationScriptPlayable](Animations.AnimationScriptPlayable.html).  
  
The Playables implementing
[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html) take a custom
C# job, which must implement [IAnimationJob](Animations.IAnimationJob.html),
and the AnimationHumanStream is then passed to its callbacks during the
animation processing pass.  
  
Additional resources: [AnimationStream](Animations.AnimationStream.html),
[AnimationStream.isHumanStream](Animations.AnimationStream-
isHumanStream.html), and AnimationStream.AsHuman().

### Properties

[bodyLocalPosition](Animations.AnimationHumanStream-bodyLocalPosition.html)|
The position of the body center of mass relative to the root.  
---|---  
[bodyLocalRotation](Animations.AnimationHumanStream-bodyLocalRotation.html)|
The rotation of the body center of mass relative to the root.  
[bodyPosition](Animations.AnimationHumanStream-bodyPosition.html)| The
position of the body center of mass in world space.  
[bodyRotation](Animations.AnimationHumanStream-bodyRotation.html)| The
rotation of the body center of mass in world space.  
[humanScale](Animations.AnimationHumanStream-humanScale.html)| The scale of
the Avatar. (Read Only)  
[isValid](Animations.AnimationHumanStream-isValid.html)| Returns true if the
stream is valid; false otherwise. (Read Only)  
[leftFootHeight](Animations.AnimationHumanStream-leftFootHeight.html)| The
left foot height from the floor. (Read Only)  
[leftFootVelocity](Animations.AnimationHumanStream-leftFootVelocity.html)| The
left foot velocity from the last evaluated frame. (Read Only)  
[rightFootHeight](Animations.AnimationHumanStream-rightFootHeight.html)| The
right foot height from the floor. (Read Only)  
[rightFootVelocity](Animations.AnimationHumanStream-rightFootVelocity.html)|
The right foot velocity from the last evaluated frame. (Read Only)  
  
### Public Methods

[GetGoalLocalPosition](Animations.AnimationHumanStream.GetGoalLocalPosition.html)|
Returns the position of this IK goal relative to the root.  
---|---  
[GetGoalLocalRotation](Animations.AnimationHumanStream.GetGoalLocalRotation.html)|
Returns the rotation of this IK goal relative to the root.  
[GetGoalPosition](Animations.AnimationHumanStream.GetGoalPosition.html)|
Returns the position of this IK goal in world space.  
[GetGoalPositionFromPose](Animations.AnimationHumanStream.GetGoalPositionFromPose.html)|
Returns the position of this IK goal in world space computed from the stream
current pose.  
[GetGoalRotation](Animations.AnimationHumanStream.GetGoalRotation.html)|
Returns the rotation of this IK goal in world space.  
[GetGoalRotationFromPose](Animations.AnimationHumanStream.GetGoalRotationFromPose.html)|
Returns the rotation of this IK goal in world space computed from the stream
current pose.  
[GetGoalWeightPosition](Animations.AnimationHumanStream.GetGoalWeightPosition.html)|
Returns the position weight of the IK goal.  
[GetGoalWeightRotation](Animations.AnimationHumanStream.GetGoalWeightRotation.html)|
Returns the rotation weight of the IK goal.  
[GetHintPosition](Animations.AnimationHumanStream.GetHintPosition.html)|
Returns the position of this IK Hint in world space.  
[GetHintWeightPosition](Animations.AnimationHumanStream.GetHintWeightPosition.html)|
Returns the position weight of the IK Hint.  
[GetMuscle](Animations.AnimationHumanStream.GetMuscle.html)| Returns the
muscle value.  
[ResetToStancePose](Animations.AnimationHumanStream.ResetToStancePose.html)|
Reset the current pose to the stance pose (T Pose).  
[SetGoalLocalPosition](Animations.AnimationHumanStream.SetGoalLocalPosition.html)|
Sets the position of this IK goal relative to the root.  
[SetGoalLocalRotation](Animations.AnimationHumanStream.SetGoalLocalRotation.html)|
Sets the rotation of this IK goal relative to the root.  
[SetGoalPosition](Animations.AnimationHumanStream.SetGoalPosition.html)| Sets
the position of this IK goal in world space.  
[SetGoalRotation](Animations.AnimationHumanStream.SetGoalRotation.html)| Sets
the rotation of this IK goal in world space.  
[SetGoalWeightPosition](Animations.AnimationHumanStream.SetGoalWeightPosition.html)|
Sets the position weight of the IK goal.  
[SetGoalWeightRotation](Animations.AnimationHumanStream.SetGoalWeightRotation.html)|
Sets the rotation weight of the IK goal.  
[SetHintPosition](Animations.AnimationHumanStream.SetHintPosition.html)| Sets
the position of this IK hint in world space.  
[SetHintWeightPosition](Animations.AnimationHumanStream.SetHintWeightPosition.html)|
Sets the position weight of the IK Hint.  
[SetLookAtBodyWeight](Animations.AnimationHumanStream.SetLookAtBodyWeight.html)|
Sets the LookAt body weight.  
[SetLookAtClampWeight](Animations.AnimationHumanStream.SetLookAtClampWeight.html)|
Sets the LookAt clamp weight.  
[SetLookAtEyesWeight](Animations.AnimationHumanStream.SetLookAtEyesWeight.html)|
Sets the LookAt eyes weight.  
[SetLookAtHeadWeight](Animations.AnimationHumanStream.SetLookAtHeadWeight.html)|
Sets the LookAt head weight.  
[SetLookAtPosition](Animations.AnimationHumanStream.SetLookAtPosition.html)|
Sets the look at position in world space.  
[SetMuscle](Animations.AnimationHumanStream.SetMuscle.html)| Sets the muscle
value.  
[SolveIK](Animations.AnimationHumanStream.SolveIK.html)| Execute the IK
solver.  
  
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

