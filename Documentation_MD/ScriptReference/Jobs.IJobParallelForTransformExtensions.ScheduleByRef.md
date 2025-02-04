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
[IJobParallelForTransformExtensions](Jobs.IJobParallelForTransformExtensions.html).ScheduleByRef

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
ScheduleByRef(ref T jobData,
[Jobs.TransformAccessArray](Jobs.TransformAccessArray.html) transforms,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependsOn);

### Parameters

jobData | The job to schedule.  
---|---  
transforms | The [TransformAccessArray](Jobs.TransformAccessArray.html) to run the job on.  
dependsOn | A JobHandle containing any jobs that must finish executing before this job begins. You can combine multiple jobs with [JobHandle.CombineDependencies](Unity.Jobs.JobHandle.CombineDependencies.html). Use dependencies to ensure that two jobs that read or write to the same data don't run in parallel.  
  
### Returns

**JobHandle** The handle identifying the scheduled job, which you can as a
dependency for a later job or to ensure completion on the main thread.

### Description

Schedules an [IJobParallelForTransform](Jobs.IJobParallelForTransform.html)
job with read-write access to the transform data by reference.

This method parallelizes access to transforms in different hierarchies.
Transforms with a shared root object are always processed on the same thread.
All transforms are guaranteed to be valid when this scheduling mode is used.
Invalid transform references in the input array are ignored.

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

