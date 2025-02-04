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
[NativeArrayUnsafeUtility](Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.html).GetUnsafeReadOnlyPtr

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

public static void* GetUnsafeReadOnlyPtr(NativeArray<T> nativeArray);

## Declaration

public static void* GetUnsafeReadOnlyPtr(ReadOnly<T> nativeArray);

### Parameters

nativeArray | The NativeArray to check.  
---|---  
  
### Returns

**void*** The memory buffer pointer of the NativeArray.

### Description

Gets a pointer to the memory buffer of a NativeArray or NativeArray.ReadOnly.

When ENABLE_UNITY_COLLECTIONS_CHECKS is set (which is always the case in the
Editor, but never in a built player), this method checks that the
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)
associated with the NativeContainer can be read from and isn't written to from
another thread. If it can't be read, a System.InvalidOperationException is
raised. While you can write to the returned pointer, this is generally unsafe.
When this method call succeeds, you're only guaranteed that reading from this
pointer is safe. Writing to this pointer might lead to race conditions and
crashes later during program execution.

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

