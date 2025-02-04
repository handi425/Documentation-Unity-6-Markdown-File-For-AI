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

#  [AnimationHumanStream](Animations.AnimationHumanStream.html).SolveIK

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

## Declaration

public void SolveIK();

### Description

Execute the IK solver.

The humanoid IK solver is executed using the IK goal position, rotation, and
weight currently set in the
[AnimationHumanStream](Animations.AnimationHumanStream.html).

    
    
    using UnityEngine;
    using UnityEngine.Playables;
    using UnityEngine.Animations;  
      
    public struct IKJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [TransformSceneHandle](Animations.TransformSceneHandle.html) effector;
        public [PropertySceneHandle](Animations.PropertySceneHandle.html) positionWeight;
        public [PropertySceneHandle](Animations.PropertySceneHandle.html) rotationWeight;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream) {}  
      
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
            [AnimationHumanStream](Animations.AnimationHumanStream.html) humanStream = stream.AsHuman();
            if (effector.IsValid(stream) && positionWeight.IsValid(stream) && rotationWeight.IsValid(stream))
            {
                humanStream.SetGoalPosition([AvatarIKGoal.LeftFoot](AvatarIKGoal.LeftFoot.html), effector.GetPosition(stream));
                humanStream.SetGoalRotation([AvatarIKGoal.LeftFoot](AvatarIKGoal.LeftFoot.html), effector.GetRotation(stream));
                humanStream.SetGoalWeightPosition([AvatarIKGoal.LeftFoot](AvatarIKGoal.LeftFoot.html), positionWeight.GetFloat(stream));
                humanStream.SetGoalWeightRotation([AvatarIKGoal.LeftFoot](AvatarIKGoal.LeftFoot.html), rotationWeight.GetFloat(stream));
            }  
      
            humanStream.SolveIK();
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

