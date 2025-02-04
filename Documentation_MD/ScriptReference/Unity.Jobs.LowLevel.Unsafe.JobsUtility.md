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

# JobsUtility

class in Unity.Jobs.LowLevel.Unsafe

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

Provides methods for creating, running, and debugging jobs.

### Static Properties

[CacheLineSize](Unity.Jobs.LowLevel.Unsafe.JobsUtility.CacheLineSize.html)|
The size of a cache line.  
---|---  
[IsExecutingJob](Unity.Jobs.LowLevel.Unsafe.JobsUtility.IsExecutingJob.html)|
Checks if this is in a job.  
[JobCompilerEnabled](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobCompilerEnabled.html)|
Set whether to run jobs in Mono or Burst.  
[JobDebuggerEnabled](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobDebuggerEnabled.html)|
Set whether to use the jobs debugger at runtime.  
[JobWorkerCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerCount.html)|
Current number of worker threads available to the Unity JobQueue.  
[JobWorkerMaximumCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.JobWorkerMaximumCount.html)|
Maximum number of worker threads available to the Unity JobQueue (Read Only).  
[MaxJobThreadCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.MaxJobThreadCount.html)|
The maximum number of job threads that the job system can create.  
[ThreadIndex](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndex.html)| Gets
the index for the current thread when executing a job, otherwise 0.  
[ThreadIndexCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ThreadIndexCount.html)|
Gets the maximum number of job workers that can work on a job at the same
time.  
  
### Static Methods

[CreateJobReflectionData](Unity.Jobs.LowLevel.Unsafe.JobsUtility.CreateJobReflectionData.html)|
Creates job reflection data.  
---|---  
[GetJobRange](Unity.Jobs.LowLevel.Unsafe.JobsUtility.GetJobRange.html)| Gets
the begin index and end index of a range.  
[GetWorkStealingRange](Unity.Jobs.LowLevel.Unsafe.JobsUtility.GetWorkStealingRange.html)|
Gets a work stealing range.  
[PatchBufferMinMaxRanges](Unity.Jobs.LowLevel.Unsafe.JobsUtility.PatchBufferMinMaxRanges.html)|
Injects debug checks for min and max ranges of a native array.  
[ResetJobWorkerCount](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ResetJobWorkerCount.html)|
Reset JobWorkerCount to the Unity adjusted value.  
[Schedule](Unity.Jobs.LowLevel.Unsafe.JobsUtility.Schedule.html)| Schedules a
single IJob.  
[ScheduleParallelFor](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ScheduleParallelFor.html)|
Schedules a IJobParallelFor job.  
[ScheduleParallelForDeferArraySize](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ScheduleParallelForDeferArraySize.html)|
Schedules a IJobParallelFor job.  
[ScheduleParallelForTransform](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ScheduleParallelForTransform.html)|
Schedules an IJobParallelForTransform job.  
[ScheduleParallelForTransformReadOnly](Unity.Jobs.LowLevel.Unsafe.JobsUtility.ScheduleParallelForTransformReadOnly.html)|
Schedules an IJobParallelForTransform job with read-only access to the
transform data.  
  
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

