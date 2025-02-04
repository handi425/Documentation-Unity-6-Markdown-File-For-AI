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

# AtomicSafetyHandle

struct in Unity.Collections.LowLevel.Unsafe

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

Coordinate safe access to native container memory inside the job system.

`AtomicSafetyHandle` holds a reference to the central information that the
safety system stores for a given native container. When a job contains a
`NativeContainer` instance, the job system automatically configures the flags
in `AtomicSafetyHandle` to reflect the way that the native container can be
used in that job. Each job has a separate `AtomicSafetyHandle` instance for a
given native container.  
  
Use this class when you implement a custom `NativeContainer` type. Every
`NativeContainer` instance must contain an `AtomicSafetyHandle` field named
`m_Safety`. For a conceptual overview of AtomicSafetyHandle and the role it
plays in the job system, refer to [Implement a custom native
container](../Manual/job-system-custom-nativecontainer.html).

### Static Methods

[CheckDeallocateAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckDeallocateAndThrow.html)|
Check if an AtomicSafetyHandle can be deallocated.  
---|---  
[CheckExistsAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckExistsAndThrow.html)|
Check if an AtomicSafetyHandle is valid.  
[CheckGetSecondaryDataPointerAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckGetSecondaryDataPointerAndThrow.html)|
Check whether it's safe to create a memory-aliasing view to a native
container.  
[CheckReadAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckReadAndThrow.html)|
Check whether the referenced native container can be read from.  
[CheckWriteAndBumpSecondaryVersion](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckWriteAndBumpSecondaryVersion.html)|
Check whether the referenced native container can be written to and increment
the secondary version number if so.  
[CheckWriteAndThrow](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.CheckWriteAndThrow.html)|
Check whether the referenced native container can be written to.  
[Create](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.Create.html)|
Creates a new AtomicSafetyHandle.  
[EnforceAllBufferJobsHaveCompleted](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompleted.html)|
Waits for all jobs running against the AtomicSafetyHandle to complete.  
[EnforceAllBufferJobsHaveCompletedAndDisableReadWrite](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndDisableReadWrite.html)|
Waits for all jobs running against an AtomicSafetyHandle to complete and then
disables the read and write access on the AtomicSafetyHandle.  
[EnforceAllBufferJobsHaveCompletedAndRelease](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.EnforceAllBufferJobsHaveCompletedAndRelease.html)|
Waits for all jobs running against an AtomicSafetyHandle to complete and then
releases the AtomicSafetyHandle.  
[GetAllowReadOrWriteAccess](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetAllowReadOrWriteAccess.html)|
Checks if the AtomicSafetyHandle is configured to allow reading or writing.  
[GetNestedContainer](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetNestedContainer.html)|
Checks whether an AtomicSafetyHandle represents a nested container.  
[GetReaderArray](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetReaderArray.html)|
Fetches the job handles of all jobs that read from an AtomicSafetyHandle.  
[GetReaderName](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetReaderName.html)|
Gets the name of a specified job that reads from an AtomicSafetyHandle.  
[GetTempMemoryHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetTempMemoryHandle.html)|
Gets an AtomicSafetyHandle for the temporary memory allocations in a temporary
memory scope.  
[GetTempUnsafePtrSliceHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetTempUnsafePtrSliceHandle.html)|
Gets a single shared AtomicSafetyHandle.  
[GetWriter](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetWriter.html)|
Gets any writers on an AtomicSafetyHandle.  
[GetWriterName](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.GetWriterName.html)|
Gets the debug name of the current writer on an AtomicSafetyHandle.  
[IsDefaultValue](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.IsDefaultValue.html)|
Checks if an AtomicSafetyHandle has its default value.  
[IsHandleValid](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.IsHandleValid.html)|
Checks if an AtomicSafetyHandle is valid.  
[IsTempMemoryHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.IsTempMemoryHandle.html)|
Checks if an AtomicSafetyHandle is the temporary memory safety handle for the
active temporary memory scope.  
[IsValidNonDefaultHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.IsValidNonDefaultHandle.html)|
Checks if an AtomicSafetyHandle has been initialized and is valid.  
[NewStaticSafetyId](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.NewStaticSafetyId.html)|
Allocates a new static safety ID to store information for the provided type.  
[PrepareUndisposable](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.PrepareUndisposable.html)|
Marks an AtomicSafetyHandle so that it can't be disposed of.  
[Release](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.Release.html)|
Releases a previously created AtomicSafetyHandle.  
[SetAllowReadOrWriteAccess](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetAllowReadOrWriteAccess.html)|
Sets the read or write access on an AtomicSafetyHandle.  
[SetAllowSecondaryVersionWriting](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetAllowSecondaryVersionWriting.html)|
Sets whether other AtomicSafetyHandles that use a secondary version number can
write to the NativeContainer protected by a given AtomicSafetyHandle.  
[SetBumpSecondaryVersionOnScheduleWrite](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetBumpSecondaryVersionOnScheduleWrite.html)|
Sets whether to automatically bump the secondary version when scheduling a job
that has write access to the AtomicSafetyHandle.  
[SetCustomErrorMessage](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetCustomErrorMessage.html)|
Provides a custom error message for a specific job debugger error type, in
cases where additional context can be provided.  
[SetNestedContainer](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetNestedContainer.html)|
Sets the nested container flag on an AtomicSafetyHandle.  
[SetStaticSafetyId](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetStaticSafetyId.html)|
Assigns a provided static safety ID to an AtomicSafetyHandle.  
[UseSecondaryVersion](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.UseSecondaryVersion.html)|
Switches the AtomicSafetyHandle to the secondary version number.  
[ValidateNonDefaultHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.ValidateNonDefaultHandle.html)|
Checks that the handle has been initialized, and if so, checks that it is
still valid.  
  
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

