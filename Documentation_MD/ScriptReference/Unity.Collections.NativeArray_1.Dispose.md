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

#  [NativeArray<T0>](Unity.Collections.NativeArray_1.html).Dispose

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

public void Dispose();

### Description

Disposes a [NativeArray<T0>](Unity.Collections.NativeArray_1.html).

This methods disposes the memory owned by a
[NativeArray<T0>](Unity.Collections.NativeArray_1.html). The behavior of this
methods depends on the [Allocator](Unity.Collections.Allocator.html) used when
the NativeArray was created.

* * *

## Declaration

public [Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
Dispose([Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) inputDeps);

### Parameters

inputDeps | The dependency of the new job.  
---|---  
  
### Returns

**JobHandle** The [JobHandle](Unity.Jobs.JobHandle.html)] of the new job. The
job depends upon `inputDeps` and releases all resources (memory and safety
handles) of the [NativeArray<T0>](Unity.Collections.NativeArray_1.html).

### Description

Creates and schedules a job that releases all resources (memory and safety
handles) of a [NativeArray<T0>](Unity.Collections.NativeArray_1.html).

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

