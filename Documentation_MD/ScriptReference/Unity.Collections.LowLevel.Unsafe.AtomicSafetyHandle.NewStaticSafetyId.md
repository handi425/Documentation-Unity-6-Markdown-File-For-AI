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
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html).NewStaticSafetyId

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

public static int NewStaticSafetyId(byte* ownerTypeNameBytes, int byteCount);

### Parameters

ownerTypeNameBytes | The name of the scripting type that owns the [AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html), to be embedded in error messages involving the handle. This must be a UTF8-encoded byte array, and doesn't have to be null-terminated.  
---|---  
byteCount | The number of bytes in the `ownerTypeNameBytes` array, excluding the optional null terminator.  
  
### Returns

**int** The newly allocated safety ID.

### Description

Allocates a new static safety ID to store information for the provided type.

After creating a new static safety ID, use
[SetStaticSafetyId](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetStaticSafetyId.html)
to assign it to the applicable
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
instances.  
  
The job debugger uses this static safety ID to look up the provided type's
name, and any custom error messages created with
[SetCustomErrorMessage](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetCustomErrorMessage.html).
Without this information, the job debugger can only give general error
messages that might not clearly identify the source of the error.

* * *

## Declaration

public static int NewStaticSafetyId();

### Returns

**int** The newly allocated safety ID.

### Description

Allocates a new static safety ID, to store information for the provided type
T.

After creating a new static safety ID, use
[SetStaticSafetyId](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetStaticSafetyId.html)
to assign it to the applicable
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
instances.  
  
The job debugger uses this static safety ID to look up the provided type's
name, and any custom error messages created with
[SetCustomErrorMessage](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.SetCustomErrorMessage.html).
Without this information, the job debugger can only give general error
messages that might not clearly identify the source of the error.  
  
This variant uses the name of the provided type `T` as the handle's owner type
name.

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

