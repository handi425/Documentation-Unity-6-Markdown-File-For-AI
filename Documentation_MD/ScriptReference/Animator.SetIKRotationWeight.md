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

#  [Animator](Animator.html).SetIKRotationWeight

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

public void SetIKRotationWeight([AvatarIKGoal](AvatarIKGoal.html) goal, float
value);

### Parameters

goal | The AvatarIKGoal that is set.  
---|---  
value | The rotational weight.  
  
### Description

Sets the rotational weight of an IK goal (0 = rotation before IK, 1 = rotation
at the IK goal).

An IK goal is a target position and rotation for a specific body part. Unity
can calculate how to move the part toward the target from the starting point
(ie, the current position and rotation obtained from the animation).  
  
This function sets a weight value in the range 0..1 to determine how far
between the start and goal rotations the IK will aim. The goal itself is set
separately using [SetIKRotation](Animator.SetIKRotation.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Transform](Transform.html) objToAimAt;
        [Animator](Animator.html) animator;  
      
        void Start()
        {
            animator = GetComponent<[Animator](Animator.html)>();
        }  
      
        void OnAnimatorIK(int layerIndex)
        {
            [Quaternion](Quaternion.html) handRotation = [Quaternion.LookRotation](Quaternion.LookRotation.html)(objToAimAt.position - transform.position);
            animator.SetIKRotationWeight([AvatarIKGoal.RightHand](AvatarIKGoal.RightHand.html), 1.0f);
            animator.SetIKRotation([AvatarIKGoal.RightHand](AvatarIKGoal.RightHand.html), handRotation);
        }
    }
    

Additional resources: [SetIKRotation](Animator.SetIKRotation.html),
[SetIKPositionWeight](Animator.SetIKPositionWeight.html).

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

