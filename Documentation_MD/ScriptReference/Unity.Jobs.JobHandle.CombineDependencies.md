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

#  [JobHandle](Unity.Jobs.JobHandle.html).CombineDependencies

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

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
CombineDependencies([Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) job0,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) job1);

## Declaration

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
CombineDependencies([Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) job0,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) job1,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) job2);

## Declaration

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
CombineDependencies(NativeArray<JobHandle> jobs);

## Declaration

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
CombineDependencies(NativeSlice<JobHandle> jobs);

### Description

Combines multiple dependencies into a single dependency.

All job schedule methods for [IJob](Unity.Jobs.IJob.html) or
[IJobParallelFor](Unity.Jobs.IJobParallelFor.html) job types take a single
dependency. Sometimes you might need to express dependencies against multiple
running jobs at the same time. Use this method to combine a set of
dependencies into a single dependency that can be passed to a job.

    
    
    // Schedule 3 jobs, jobs a and b can run in parallel to each other,
    // job c will only run once both jobA and jobB has completed  
      
    // Schedule job a
    var jobA = new MyJob(...);
    var jobAHandle = jobA.Schedule();  
      
    // Schedule job b
    var jobB = new MyJob(...);
    var jobBHandle = jobB.Schedule();  
      
    // For job c, combine dependencies of job a and b
    // Then use that for scheduling the next job
    var jobC = new DependentJob(...);
    var dependency = [JobHandle.CombineDependencies](Unity.Jobs.JobHandle.CombineDependencies.html)(jobAHandle, jobBHandle);
    jobC.Schedule(dependency);
    

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

