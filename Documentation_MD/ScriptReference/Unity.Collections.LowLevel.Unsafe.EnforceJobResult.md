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

# EnforceJobResult

enumeration

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

Enumerates the possible values returned by
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
methods that wait for all jobs accessing the native container associated with
the handle to finish.

The members of this enum describe whether the job system had to wait for any
jobs to finish.  
  
The following methods use this enum as a return type:

  * [AtomicSafetyHandle.EnforceAllBufferJobsHaveCompleted](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompleted.html)
  * [AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndDisableReadWrite](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndDisableReadWrite.html)
  * [AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndRelease](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndRelease.html).

### Properties

[AllJobsAlreadySynced](Unity.Collections.LowLevel.Unsafe.EnforceJobResult.AllJobsAlreadySynced.html)|
Indicates that all jobs were already complete at the time of the wait request.  
---|---  
[DidSyncRunningJobs](Unity.Collections.LowLevel.Unsafe.EnforceJobResult.DidSyncRunningJobs.html)|
Indicates that the job system waited for at least one job to finish.  
[HandleWasAlreadyDeallocated](Unity.Collections.LowLevel.Unsafe.EnforceJobResult.HandleWasAlreadyDeallocated.html)|
Indicates that the job system didn't wait because the AtomicSafetyHandle was
invalid, likely because the associated container had already been deallocated.  
  
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

