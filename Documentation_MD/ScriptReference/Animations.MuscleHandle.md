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

# MuscleHandle

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

Handle for a muscle in the
[AnimationHumanStream](Animations.AnimationHumanStream.html).

MuscleHandle can only be used on
[AnimationHumanStream](Animations.AnimationHumanStream.html), otherwise an
`InvalidOperationException` is thrown.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    public struct MuscleHandleExampleJob : [IAnimationJob](Animations.IAnimationJob.html)
    {
        public [MuscleHandle](Animations.MuscleHandle.html) muscleHandle;  
      
        public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream) {}
        public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream)
        {
            [AnimationHumanStream](Animations.AnimationHumanStream.html) humanStream = stream.AsHuman();  
      
            // Get a muscle value.
            float muscleValue = humanStream.GetMuscle(muscleHandle);  
      
            // Set a muscle value.
            humanStream.SetMuscle(muscleHandle, muscleValue);
        }
    }  
      
    [[RequireComponent](RequireComponent.html)(typeof([Animator](Animator.html)))]
    public class MuscleHandleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            var output = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(graph, "output", GetComponent<[Animator](Animator.html)>());  
      
            var job = new MuscleHandleExampleJob();
            job.muscleHandle = new [MuscleHandle](Animations.MuscleHandle.html)([HumanPartDof.LeftArm](HumanPartDof.LeftArm.html), [ArmDof.HandDownUp](ArmDof.HandDownUp.html));  
      
            var scriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(graph, job);
            output.SetSourcePlayable(scriptPlayable);  
      
            graph.Evaluate(1.0f);  
      
            graph.Destroy();
        }
    }
    

### Static Properties

[muscleHandleCount](Animations.MuscleHandle-muscleHandleCount.html)| The total
number of DoF parts in a humanoid. (Read Only)  
---|---  
  
### Properties

[dof](Animations.MuscleHandle-dof.html)| The muscle human sub-part. (Read
Only)  
---|---  
[humanPartDof](Animations.MuscleHandle-humanPartDof.html)| The muscle human
part. (Read Only)  
[name](Animations.MuscleHandle-name.html)| The name of the muscle. (Read Only)  
  
### Constructors

[MuscleHandle](Animations.MuscleHandle-ctor.html)| The different constructors
that creates the muscle handle.  
---|---  
  
### Static Methods

[GetMuscleHandles](Animations.MuscleHandle.GetMuscleHandles.html)| Fills the
array with all the possible muscle handles on a humanoid.  
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

