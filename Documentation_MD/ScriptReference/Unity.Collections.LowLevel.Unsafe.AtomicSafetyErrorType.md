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

# AtomicSafetyErrorType

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

Error code for errors related to accessing native container instances in
different situations.

Each [NativeContainer](../Manual/JobSystemNativeContainer.html) instance is
monitored by an `AtomicSafetyHandle`, which coordinates safe access to the
container. If the container can't be accessed safely, then the
`AtomicSafetyHandle` generates an error. The values of this enumeration
classify the errors that are generated in each type of access situation.  
  
You can set custom error messages for each of these error types on a per-type
basis. Use `SetCustomErrorMessage` for each value in this enumeration.  
  
Additional resources:
[AtomicSafetyHandle.SetCustomErrorMessage](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetCustomErrorMessage.html)

### Properties

[Deallocated](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.Deallocated.html)|
Error caused by main thread attempting to access the native container after
the container memory is deallocated.  
---|---  
[DeallocatedFromJob](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.DeallocatedFromJob.html)|
Error caused by worker thread attempting to access the native container after
the container memory is deallocated  
[NotAllocatedFromJob](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.NotAllocatedFromJob.html)|
Error caused by worker thread attempting to access the native container before
the container memory is allocated.  
  
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

