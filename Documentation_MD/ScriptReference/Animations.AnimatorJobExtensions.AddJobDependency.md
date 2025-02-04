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

#
[AnimatorJobExtensions](Animations.AnimatorJobExtensions.html).AddJobDependency

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

public static void AddJobDependency([Animator](Animator.html) animator,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) jobHandle);

### Parameters

animator | The [Animator](Animator.html) instance that calls this method.  
---|---  
jobHandle | The [JobHandle](Unity.Jobs.JobHandle.html) of the job that needs to run before animator jobs.  
  
### Description

Creates a dependency between animator jobs and the job represented by the
supplied job handle. To add multiple job dependencies, call this method for
each job that need to run before the Animator's jobs.

After each update the [Animator](Animator.html) dependencies are flushed.

    
    
    using UnityEngine;
    using UnityEngine.Animations;
    using UnityEngine.Playables;  
      
    using Unity.Collections;
    using Unity.Jobs;  
      
    public class MyMonoBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        NativeArray<int> input0;
        NativeArray<int> input1;
        NativeArray<int> output;  
      
        [PlayableGraph](Playables.PlayableGraph.html) graph;
        [Animator](Animator.html) animator;  
      
        public struct SumDataForJob : [IJob](Unity.Jobs.IJob.html)
        {
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<int> input0;  
      
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<int> input1;  
      
            public NativeArray<int> output;  
      
            public void Execute()
            {
                for (var i = 0; i < output.Length; ++i)
                    output[i] = input0[i] + input1[i];
            }
        }  
      
        public struct MyAnimationJob : [IAnimationJob](Animations.IAnimationJob.html)
        {
            [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
            public NativeArray<int> input;  
      
            public float            sum;  
      
            public void ProcessRootMotion([AnimationStream](Animations.AnimationStream.html) stream)
            {
                sum = 0;
                for (var i = 0; i < input.Length; ++i)
                    sum += input[i];
            }  
      
            public void ProcessAnimation([AnimationStream](Animations.AnimationStream.html) stream) {}
        }  
      
        public void Start()
        {
            input0 = new NativeArray<int>(10, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            input1 = new NativeArray<int>(10, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            output = new NativeArray<int>(10, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            for (var i = 0; i < output.Length; i++)
            {
                input0[i] = i;
                input1[i] = 10 * i;
                output[i] = 0;
            }  
      
            animator = gameObject.AddComponent<[Animator](Animator.html)>();  
      
            graph = [PlayableGraph.Create](Playables.PlayableGraph.Create.html)();
            var myAnimationJob = new MyAnimationJob();
            myAnimationJob.input = output;  
      
            var scriptPlayable = [AnimationScriptPlayable.Create](Animations.AnimationScriptPlayable.Create.html)(graph, myAnimationJob);
            var playableOutput = [AnimationPlayableOutput.Create](Animations.AnimationPlayableOutput.Create.html)(graph, "output", animator);  
      
            playableOutput.SetSourcePlayable(scriptPlayable);
            graph.Play();
        }  
      
        public void [Update](PlayerLoop.Update.html)()
        {
            SumDataForJob sumJob;
            sumJob.input0 = input0;
            sumJob.input1 = input1;
            sumJob.output = output;  
      
            var jobHandle = sumJob.Schedule();
            animator.AddJobDependency(jobHandle);
        }  
      
        public void OnDestroy()
        {
            graph.Destroy();
            input0.Dispose();
            input1.Dispose();
            output.Dispose();
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

