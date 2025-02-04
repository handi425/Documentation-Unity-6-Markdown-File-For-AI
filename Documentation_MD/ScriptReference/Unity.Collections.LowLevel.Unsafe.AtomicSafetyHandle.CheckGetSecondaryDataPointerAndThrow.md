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
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html).CheckGetSecondaryDataPointerAndThrow

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

public static void
CheckGetSecondaryDataPointerAndThrow([Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
handle);

### Parameters

handle | The AtomicSafetyHandle to check.  
---|---  
  
### Description

Check whether it's safe to create a memory-aliasing view to a native
container.

Use this method when you implement native container methods that create
memory-aliasing views, such as `GetEnumerator` or `AsArray`. This method
checks whether it is safe to copy the data pointer to the backing memory of
the native container into a new view structure that uses the secondary version
number.  
  
This method checks if there are pending jobs that might affect the size of the
native container and risk reallocating the container's backing memory. This
method doesn't throw an exception if the job writes through an
`AtomicSafetyHandle` that uses a secondary version number.  
  
The difference between this method and
`[AtomicSafetyHandle.CheckReadAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckReadAndThrow.html)`
is that that `CheckReadAndThrow` throws an exception if there are any pending
jobs writing to the native container. `CheckGetSecondaryDataPointerAndThrow`
throws an exception only if there is a risk of a job reallocating the native
container's backing memory, which makes the data pointer copied to the view
invalid.  
  
For more information about secondary version numbers and safe access to
dynamic containers, refer to [Copying NativeContainer
structures](../Manual/job-system-copy-nativecontainer.html).  
  
Additional resources:
[NativeContainerAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html).

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

