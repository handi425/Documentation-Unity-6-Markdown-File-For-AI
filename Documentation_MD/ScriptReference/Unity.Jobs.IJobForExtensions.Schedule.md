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

#  [IJobForExtensions](Unity.Jobs.IJobForExtensions.html).Schedule

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

public static [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) Schedule(T
jobData, int arrayLength, [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
dependency);

### Parameters

jobData | The job and data to schedule.  
---|---  
arrayLength | The number of iterations to execute the for loop over.  
dependency | The [JobHandle](Unity.Jobs.JobHandle.html) of the job's dependency. You can use dependencies to make sure that a job executes on worker threads after the dependency has completed execution and two jobs that read or write to same data don't run in parallel.  
  
### Returns

**JobHandle** The [JobHandle](Unity.Jobs.JobHandle.html) of the scheduled job.
You can use the `JobHandle` as a dependency for a later job or to make sure
that the job completes on the main thread.

### Description

Schedules the job to execute on a single worker thread.

Additional resources: [IJobFor](Unity.Jobs.IJobFor.html).

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

