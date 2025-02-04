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
[IJobParallelForTransformExtensions](Jobs.IJobParallelForTransformExtensions.html).ScheduleReadOnly

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
ScheduleReadOnly(T jobData,
[Jobs.TransformAccessArray](Jobs.TransformAccessArray.html) transforms, int
batchSize, [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependsOn);

### Parameters

jobData | The job to schedule.  
---|---  
transforms | The [TransformAccessArray](Jobs.TransformAccessArray.html) to run the job on.  
batchSize | Granularity in which workstealing is performed. For example, a value of 32 means the job queue will steal 32 iterations and then perform them in an efficient inner loop.  
dependsOn | A JobHandle containing any jobs that must finish executing before this job begins. You can combine multiple jobs with [JobHandle.CombineDependencies](Unity.Jobs.JobHandle.CombineDependencies.html). Use dependencies to ensure that two jobs that read or write to the same data don't run in parallel.  
  
### Returns

**JobHandle** The handle identifying the scheduled job, which you can use as a
dependency for a later job or to ensure completion on the main thread.

### Description

Schedules an [IJobParallelForTransform](Jobs.IJobParallelForTransform.html)
job with read-only access to the transform data.

This method provides better parallelization because it can read all transforms
in parallel instead of just parallelizing over different hierarchies.
Transforms aren't guaranteed to be valid when this scheduling mode is used.
Invalid transform references in the input array are still processed. Use
[TransformAccess.isValid](Jobs.TransformAccess-isValid.html) to check whether
a specific instance is valid.

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

