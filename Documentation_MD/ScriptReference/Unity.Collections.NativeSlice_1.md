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

# NativeSlice<T0>

struct in Unity.Collections

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

Provides a view on a buffer of native memory most commonly acquired from a
[NativeArray<T0>](Unity.Collections.NativeArray_1.html).

A NativeSlice provides systems that means they can be used safely with jobs.
In contrast to a [NativeArray<T0>](Unity.Collections.NativeArray_1.html), a
NativeSlice doesn't own any memory allocations and can't be disposed. A
NativeSlice supports a stride value and doesn't necessarily represent a
contiguous memory range. The stride value determines the number of bytes from
the first byte of the element to the first byte of the next element. The
stride value must always be a multiple of the size of the type of the slice in
bytes. The stride value allows you to skip elements from the underlying
buffer. By default, the stride is set to the size of the type of slice in
bytes. This means that the slice represents a contiguous memory range. If you
don't need a stride and are only working with contiguous memory ranges, use
[NativeArray<T0>](Unity.Collections.NativeArray_1.html) instead.

### Properties

[Length](Unity.Collections.NativeSlice_1.Length.html)| Represents the number
of elements in a NativeSlice<T0>.  
---|---  
[Stride](Unity.Collections.NativeSlice_1.Stride.html)| Gets the stride value
for the NativeSlice<T0> instance.  
[this[int]](Unity.Collections.NativeSlice_1.Index_operator.html)| Accesses
NativeSlice<T0> elements by index.  
  
### Constructors

[NativeSlice_1](Unity.Collections.NativeSlice_1-ctor.html)| Constructs a new
NativeSlice from a NativeArray or NativeSlice.  
---|---  
  
### Public Methods

[CopyFrom](Unity.Collections.NativeSlice_1.CopyFrom.html)| Copies all the
elements from a NativeSlice<T0> or managed array of the same length.  
---|---  
[CopyTo](Unity.Collections.NativeSlice_1.CopyTo.html)| Copies all the elements
of a NativeSlice<T0> to a NativeArray<T0> or managed array of the same length.  
[GetEnumerator](Unity.Collections.NativeSlice_1.GetEnumerator.html)| Gets an
enumerator to iterate through the elements of a NativeSlice<T0>.  
[SliceConvert](Unity.Collections.NativeSlice_1.SliceConvert.html)|
Reinterprets a NativeSlice with a different data type (type punning).  
[SliceWithStride](Unity.Collections.NativeSlice_1.SliceWithStride.html)|
SliceWithStride.  
[ToArray](Unity.Collections.NativeSlice_1.ToArray.html)| Converts a
NativeSlice<T0> to managed array.  
  
### Operators

[NativeSlice<T>](Unity.Collections.NativeSlice_1-operator_NativeArrayT.html)|
Implicit operator to create a NativeSlice<T0> from a NativeArray<T0>.  
---|---  
  
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

