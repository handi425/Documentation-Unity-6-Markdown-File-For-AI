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

#  [Animator](Animator.html).MatchTarget

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

## Declaration

public void MatchTarget([Vector3](Vector3.html) matchPosition,
[Quaternion](Quaternion.html) matchRotation, [AvatarTarget](AvatarTarget.html)
targetBodyPart, [MatchTargetWeightMask](MatchTargetWeightMask.html)
weightMask, float startNormalizedTime, float targetNormalizedTime = 1);

### Parameters

matchPosition | The position we want the body part to reach.  
---|---  
matchRotation | The rotation in which we want the body part to be.  
targetBodyPart | The body part that is involved in the match.  
weightMask | Structure that contains weights for matching position and rotation.  
startNormalizedTime | Start time within the animation clip (0 - beginning of clip, 1 - end of clip).  
targetNormalizedTime | End time within the animation clip (0 - beginning of clip, 1 - end of clip), values greater than 1 can be set to trigger a match after a certain number of loops. Ex: 2.3 means at 30% of 2nd loop.  
completeMatch | Allows you to specify what should happen if the MatchTarget function is interrupted. A value of true causes the GameObject to immediately move to the matchPosition if interrupted. A value of false causes the GameObject to stay at its current position if interrupted.  
  
### Description

Automatically adjust the `GameObject` position and rotation.

Adjust the `GameObject` position and rotation so that the AvatarTarget reaches
the matchPosition when the current state is at the specified progress. Target
matching only works on the base layer (index 0). You can only queue one match
target at a time and you must wait for the first one to finish, otherwise your
target matching will be discarded. If you call a
[MatchTarget](Animator.MatchTarget.html) with a start time lower than the
clip's normalized time and the clip can loop,
[MatchTarget](Animator.MatchTarget.html) will adjust the time to match the
next clip loop. For example, start time= 0.2 normalized time = 0.3, start time
will be 1.2. [Animator.applyRootMotion](Animator-applyRootMotion.html) must be
enabled for MatchTarget to take effect.

    
    
    using UnityEngine;  
      
    public class TargetMatchingManager : [MonoBehaviour](MonoBehaviour.html)
    {
        public void MatchTarget([Vector3](Vector3.html) matchPosition, [Quaternion](Quaternion.html) matchRotation, [AvatarTarget](AvatarTarget.html) target, [MatchTargetWeightMask](MatchTargetWeightMask.html) weightMask, float normalisedStartTime, float normalisedEndTime)
        {
            var animator = GetComponent<[Animator](Animator.html)>();  
      
            if (animator.isMatchingTarget)
                return;  
      
            float normalizeTime = [Mathf.Repeat](Mathf.Repeat.html)(animator.GetCurrentAnimatorStateInfo(0).normalizedTime, 1f);  
      
            if (normalizeTime > normalisedEndTime)
                return;  
      
            animator.MatchTarget(matchPosition, matchRotation, target, weightMask, normalisedStartTime, normalisedEndTime);
        }
    }
    

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

