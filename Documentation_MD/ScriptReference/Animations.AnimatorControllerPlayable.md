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

# AnimatorControllerPlayable

struct in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

Leave feedback

  

Implements interfaces:[IPlayable](Playables.IPlayable.html)

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

An implementation of [IPlayable](Playables.IPlayable.html) that controls an
animation [RuntimeAnimatorController](RuntimeAnimatorController.html).

NOTE: You can use [PlayableExtensions](Playables.PlayableExtensions.html)
methods with AnimatorControllerPlayable objects.

### Static Properties

[Null](Animations.AnimatorControllerPlayable.Null.html)| Returns an invalid
AnimatorControllerPlayable.  
---|---  
  
### Public Methods

[CrossFade](Animations.AnimatorControllerPlayable.CrossFade.html)| Creates a
crossfade from the current state to any other state using normalized times.  
---|---  
[CrossFadeInFixedTime](Animations.AnimatorControllerPlayable.CrossFadeInFixedTime.html)|
Creates a crossfade from the current state to any other state using times in
seconds.  
[GetAnimatorTransitionInfo](Animations.AnimatorControllerPlayable.GetAnimatorTransitionInfo.html)|
Returns an AnimatorTransitionInfo with the informations on the current
transition.  
[GetBool](Animations.AnimatorControllerPlayable.GetBool.html)| Returns the
value of the given boolean parameter.  
[GetCurrentAnimatorClipInfo](Animations.AnimatorControllerPlayable.GetCurrentAnimatorClipInfo.html)|
Returns an array of all the AnimatorClipInfo in the current state of the given
layer.  
[GetCurrentAnimatorClipInfoCount](Animations.AnimatorControllerPlayable.GetCurrentAnimatorClipInfoCount.html)|
Returns the number of AnimatorClipInfo in the current state.  
[GetCurrentAnimatorStateInfo](Animations.AnimatorControllerPlayable.GetCurrentAnimatorStateInfo.html)|
Returns an AnimatorStateInfo with the information on the current state.  
[GetFloat](Animations.AnimatorControllerPlayable.GetFloat.html)| Returns the
value of the given float parameter.  
[GetInteger](Animations.AnimatorControllerPlayable.GetInteger.html)| Returns
the value of the given integer parameter.  
[GetLayerIndex](Animations.AnimatorControllerPlayable.GetLayerIndex.html)|
Returns the index of the layer with the given name.  
[GetLayerName](Animations.AnimatorControllerPlayable.GetLayerName.html)|
Returns the layer name.  
[GetLayerWeight](Animations.AnimatorControllerPlayable.GetLayerWeight.html)|
Returns the weight of the layer at the specified index.  
[GetNextAnimatorClipInfo](Animations.AnimatorControllerPlayable.GetNextAnimatorClipInfo.html)|
Returns an array of all the AnimatorClipInfo in the next state of the given
layer.  
[GetNextAnimatorClipInfoCount](Animations.AnimatorControllerPlayable.GetNextAnimatorClipInfoCount.html)|
Returns the number of AnimatorClipInfo in the next state.  
[GetNextAnimatorStateInfo](Animations.AnimatorControllerPlayable.GetNextAnimatorStateInfo.html)|
Returns an AnimatorStateInfo with the information on the next state.  
[GetParameter](Animations.AnimatorControllerPlayable.GetParameter.html)| See
AnimatorController.parameters.  
[HasState](Animations.AnimatorControllerPlayable.HasState.html)| Returns true
if the state exists in this layer, false otherwise.  
[IsInTransition](Animations.AnimatorControllerPlayable.IsInTransition.html)|
Returns true if there is a transition on the given layer, false otherwise.  
[IsParameterControlledByCurve](Animations.AnimatorControllerPlayable.IsParameterControlledByCurve.html)|
Returns true if the parameter is controlled by a curve, false otherwise.  
[Play](Animations.AnimatorControllerPlayable.Play.html)| Plays a state.  
[PlayInFixedTime](Animations.AnimatorControllerPlayable.PlayInFixedTime.html)|
Plays a state.  
[ResetTrigger](Animations.AnimatorControllerPlayable.ResetTrigger.html)|
Resets the value of the given trigger parameter.  
[SetBool](Animations.AnimatorControllerPlayable.SetBool.html)| Sets the value
of the given boolean parameter.  
[SetFloat](Animations.AnimatorControllerPlayable.SetFloat.html)| Send float
values to the AnimatorController to affect transitions.  
[SetInteger](Animations.AnimatorControllerPlayable.SetInteger.html)| Sets the
value of the given integer parameter.  
[SetLayerWeight](Animations.AnimatorControllerPlayable.SetLayerWeight.html)|
Sets the weight of the layer at the given index.  
[SetTrigger](Animations.AnimatorControllerPlayable.SetTrigger.html)| Sets the
value of the given trigger parameter.  
  
### Static Methods

[Create](Animations.AnimatorControllerPlayable.Create.html)| Creates an
AnimatorControllerPlayable in the PlayableGraph.  
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

