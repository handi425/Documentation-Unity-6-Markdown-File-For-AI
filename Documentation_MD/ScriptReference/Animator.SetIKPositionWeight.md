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

#  [Animator](Animator.html).SetIKPositionWeight

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

public void SetIKPositionWeight([AvatarIKGoal](AvatarIKGoal.html) goal, float
value);

### Parameters

goal | The AvatarIKGoal that is set.  
---|---  
value | The translative weight.  
  
### Description

Sets the translative weight of an IK goal (0 = at the original animation
before IK, 1 = at the goal).

An IK goal is a target position and rotation for a specific body part. Unity
can calculate how to move the part toward the target from the starting point
(ie, the current position and rotation obtained from the animation).  
  
This function sets a weight value in the range 0..1 to determine how far
between the start and goal positions the IK will aim. The position itself is
set separately using [SetIKPosition](Animator.SetIKPosition.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) objToPickUp;
        [Animator](Animator.html) animator;  
      
        void Start()
        {
            animator = GetComponent<[Animator](Animator.html)>();
        }  
      
        void OnAnimatorIK(int layerIndex)
        {
            // Retrieves the value of the parameter "RightHandReach" that must be created in the [AnimatorController](Animations.AnimatorController.html).
            float reach = animator.GetFloat("RightHandReach");  
      
            // Sets IK [Position](UIElements.Position.html) and IK [Position](UIElements.Position.html) Weight.
            animator.SetIKPositionWeight([AvatarIKGoal.RightHand](AvatarIKGoal.RightHand.html), reach);
            animator.SetIKPosition([AvatarIKGoal.RightHand](AvatarIKGoal.RightHand.html), objToPickUp.position);
        }
    }
    

Additional resources: [SetIKPosition](Animator.SetIKPosition.html),
[SetIKRotationWeight](Animator.SetIKRotationWeight.html).

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

