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

#  [Animator](Animator.html).GetBehaviour

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

public T GetBehaviour();

### Description

Returns the first [StateMachineBehaviour](StateMachineBehaviour.html) that
matches type `T` or is derived from `T`. Returns null if none are found.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class RunBehaviour : [StateMachineBehaviour](StateMachineBehaviour.html)
    {
        // OnStateUpdate is called at each [Update](PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
        override public void OnStateUpdate([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            [Transform](Transform.html) transform = animator.GetComponent<[Transform](Transform.html)>();  
      
            [RaycastHit](RaycastHit.html) hitInfo;
            [Vector3](Vector3.html) dir = transform.TransformDirection([Vector3.forward](Vector3-forward.html));
            if ([Physics.Raycast](Physics.Raycast.html)(transform.position + new [Vector3](Vector3.html)(0, 1.5f, 0), dir, out hitInfo, 10))
            {
                if (hitInfo.collider.tag == "Obstacle")
                {
                    animator.GetBehaviour<SlideBehaviour>().target = transform.position + 1.25f * hitInfo.distance * dir;
                    if (hitInfo.distance < 6)
                        animator.SetTrigger("Slide");
                }
            }
        }
    }  
      
    public class SlideBehaviour : [StateMachineBehaviour](StateMachineBehaviour.html)
    {
        public [Vector3](Vector3.html) target;  
      
        public float slideMatchTargetStart = 0.11f;
        public float slideMatchTargetStop = 0.40f;  
      
        // OnStateUpdate is called at each [Update](PlayerLoop.Update.html) frame between OnStateEnter and OnStateExit callback
        override public void OnStateUpdate([Animator](Animator.html) animator, [AnimatorStateInfo](AnimatorStateInfo.html) stateInfo, int layerIndex)
        {
            animator.MatchTarget(target, new [Quaternion](Quaternion.html)(), [AvatarTarget.Root](AvatarTarget.Root.html), new [MatchTargetWeightMask](MatchTargetWeightMask.html)(new [Vector3](Vector3.html)(1, 0, 1), 0), slideMatchTargetStart, slideMatchTargetStop);
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

