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

#  [NativeArray<T0>](Unity.Collections.NativeArray_1.html).Copy

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

public static void Copy(NativeArray<T> src, NativeArray<T> dst);

## Declaration

public static void Copy(T[] src, NativeArray<T> dst);

## Declaration

public static void Copy(ReadOnly<T> src, NativeArray<T> dst);

## Declaration

public static void Copy(NativeArray<T> src, T[] dst);

## Declaration

public static void Copy(ReadOnly<T> src, T[] dst);

## Declaration

public static void Copy(NativeArray<T> src, NativeArray<T> dst, int length);

## Declaration

public static void Copy(ReadOnly<T> src, NativeArray<T> dst, int length);

## Declaration

public static void Copy(T[] src, NativeArray<T> dst, int length);

## Declaration

public static void Copy(NativeArray<T> src, T[] dst, int length);

## Declaration

public static void Copy(ReadOnly<T> src, T[] dst, int length);

## Declaration

public static void Copy(NativeArray<T> src, int srcIndex, NativeArray<T> dst,
int dstIndex, int length);

## Declaration

public static void Copy(ReadOnly<T> src, int srcIndex, T[] dst, int dstIndex,
int length);

## Declaration

public static void Copy(T[] src, int srcIndex, NativeArray<T> dst, int
dstIndex, int length);

## Declaration

public static void Copy(NativeArray<T> src, int srcIndex, T[] dst, int
dstIndex, int length);

## Declaration

public static void Copy(ReadOnly<T> src, int srcIndex, NativeArray<T> dst, int
dstIndex, int length);

### Parameters

src | The data to copy.  
---|---  
dst | The array that receives the data.  
length | A 32-bit integer that represents the number of elements to copy. The integer must be equal to or greater than zero.  
srcIndex | A 32-bit integer that represents the index in the `src` array where copying begins.  
dstIndex | A 32-bit integer that represents the index in the `dst` array where storing begins.  
  
### Description

Copies a range of elements from a source array to a destination array,
starting from the source index and copying them to the destination index.

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

