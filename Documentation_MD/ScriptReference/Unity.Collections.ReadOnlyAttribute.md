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

# ReadOnlyAttribute

class in Unity.Collections

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Marks a member of a struct used in a job as read-only.

Native containers are read-write by default when used in a job. This means
that you can't schedule two jobs that reference the same containers
simultaneously. Add the ReadOnly attribute to a native container field in a
job struct to mark the container as read-only. This allows two jobs to run in
parallel and read data from the same native container.  
  
Additional resources: [IJob](Unity.Jobs.IJob.html),
[IJobParallelFor](Unity.Jobs.IJobParallelFor.html).

    
    
    using Unity.Jobs;
    using Unity.Collections;
    using UnityEngine;  
      
    public struct MyJob : [IJob](Unity.Jobs.IJob.html)
    {
        [[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html)]
        public NativeArray<int> input;  
      
        public NativeArray<int> output;  
      
        public void Execute()
        {
            for (var i = 0; i < output.Length; ++i)
                output[i] = input[i];
        }
    }  
      
    public class ParallelReplicator : [MonoBehaviour](MonoBehaviour.html)
    {
        public void OnUpdate()
        {
            const int n = 10000;
            var original = new NativeArray<int>(n, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            var clone1 = new NativeArray<int>(n, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            var clone2 = new NativeArray<int>(n, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));  
      
            var job1 = new MyJob
            {
                input = original,
                output = clone1
            };
            var job2 = new MyJob
            {
                input = original,
                output = clone2
            };  
      
            var jobX = new MyJob
            {
                input = original,
                output = clone2
            };  
      
            // Run the jobs in parallel.
            var jobs = [JobHandle.CombineDependencies](Unity.Jobs.JobHandle.CombineDependencies.html)(job1.Schedule(), job2.Schedule());  
      
            // jobX.Schedule(); // Not allowed, throws exception because job2 is writing into clone2.  
      
            jobs.Complete();  
      
            jobX.Schedule().Complete(); // Allowed, because job2 has been completed by now.  
      
            original.Dispose();
            clone1.Dispose();
            clone2.Dispose();
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

