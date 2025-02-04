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
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html).SetCustomErrorMessage

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

public static void SetCustomErrorMessage(int staticSafetyId,
[Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.html)
errorType, byte* messageBytes, int byteCount);

### Parameters

staticSafetyId | The static safety ID with which the provided custom error message should be associated. This ID must have been allocated with [NewStaticSafetyId](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.NewStaticSafetyId.html). Passing 0 is invalid because 0 is the default static safety ID, and its error messages cann't be modified.  
---|---  
errorType | The class of error that should use the provided custom error message instead of the default job debugger error message.  
messageBytes | The error message to use for the specified error type. This should be a UTF8-encoded byte array, and doesn't have to be null-terminated.  
byteCount | The number of bytes in the `messageBytes` array, excluding the optional null terminator.  
  
### Description

Provides a custom error message for a specific job debugger error type, in
cases where additional context can be provided.

The job debugger uses the specified static safety ID and error type to look up
error messages for
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
instances. You should provide a message for each applicable type of error
defined in
[AtomicSafetyErrorType](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.html).
Without a specific error message, the job debugger only gives general error
messages that might not clearly identify the source of the error.  
  
If the message contains any of the following sequences, they are replaced with
the corresponding context-specific data (if available) when the message is
emitted:

  * {2} = this job name. example: "BoidsJob"
  * {3} = this job field. example: "BoidsJob.boidsBuffer"
  * {5} = this owner type. example: "NativeArray<int>"

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

