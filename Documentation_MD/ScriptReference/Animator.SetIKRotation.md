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

#  [Animator](Animator.html).SetIKRotation

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

public void SetIKRotation([AvatarIKGoal](AvatarIKGoal.html) goal,
[Quaternion](Quaternion.html) goalRotation);

### Parameters

goal | The AvatarIKGoal that is set.  
---|---  
goalRotation | The rotation of the goal in world space which should follow Unity's world coordinates convention (see below).  
  
### Description

Sets the rotation of an IK goal.

An IK goal is a specified target position and rotation for a specific body
part. Unity calculates how to move the body part towards this target from a
starting point. This starting point could be, for example, the current
position and rotation obtained from an animation.  
  
This function sets the IK goal rotation in world space. When specifying the IK
goal rotation, it should follow Unity's world coordinates convention: • The
`X-Axis` is parallel to the palm of the hand (or sole of the foot), pointing
sideways to the right of the hand (or foot).  
• The `Y-Axis` is perpendicular to the top of the hand (or foot), pointing
upwards.  
• The `Z-Axis` is parallel to the palm of the hand (or sole of the foot),
pointing forwards toward the fingers (or toes).  
  
  
It is recommended that the bone orientation of the avatar skeleton pose should
also follow Unity's world coordinates convention. If your avatar skeleton pose
follows a different convention, the bone rotation applied to the corresponding
`GameObject` might differ from the IK goal rotation.  
  
In addition, you can set a weight value to set the amount of influence that
the IK goal rotation has over the starting rotation. Use the
`SetIKRotationWeight` method to set a weight value between 0..1 where a weight
of 0 means no influence and a weight of 1 means full influence.  
  
The following code example demonstrates how to use the `SetIKRotation` method
and `SetIKRotationWeight` method.

    
    
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
    

Additional resources:
[SetIKRotationWeight](Animator.SetIKRotationWeight.html),
[SetIKPosition](Animator.SetIKPosition.html).

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

