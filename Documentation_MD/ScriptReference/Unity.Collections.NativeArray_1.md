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

# NativeArray<T0>

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

Provides a buffer of native memory to managed code, making it possible to
share data between managed and native code without marshalling costs.

A NativeArray instance provides systems that means you can use them safely in
jobs. A NativeArray also has automatic memory leak tracking.

### Properties

[IsCreated](Unity.Collections.NativeArray_1.IsCreated.html)| Indicates that a
NativeArray<T0> has an allocated memory buffer.  
---|---  
[Length](Unity.Collections.NativeArray_1.Length.html)| Number of elements in a
NativeArray<T0>.  
[this[int]](Unity.Collections.NativeArray_1.Index_operator.html)| Access
NativeArray<T0> elements by index.  
  
### Constructors

[NativeArray_1](Unity.Collections.NativeArray_1-ctor.html)| Creates a
NativeArray from an array of elements.  
---|---  
  
### Public Methods

[AsReadOnly](Unity.Collections.NativeArray_1.AsReadOnly.html)| Casts a
NativeArray<T0> to read-only array.  
---|---  
[AsReadOnlySpan](Unity.Collections.NativeArray_1.AsReadOnlySpan.html)| Exposes
NativeArray<T0> data as a System.ReadOnlySpan<T>.  
[AsSpan](Unity.Collections.NativeArray_1.AsSpan.html)| Exposes NativeArray<T0>
data as a System.Span<T>.  
[CopyFrom](Unity.Collections.NativeArray_1.CopyFrom.html)| Copies all the
elements from a NativeArray<T0> or a managed array of the same length.  
[CopyTo](Unity.Collections.NativeArray_1.CopyTo.html)| Copies all the elements
to another NativeArray<T0> or a managed array of the same length.  
[Dispose](Unity.Collections.NativeArray_1.Dispose.html)| Disposes a
NativeArray<T0>.  
[Equals](Unity.Collections.NativeArray_1.Equals.html)| Compares two
NativeArray<T0> instances.  
[GetEnumerator](Unity.Collections.NativeArray_1.GetEnumerator.html)| Gets an
enumerator.  
[GetHashCode](Unity.Collections.NativeArray_1.GetHashCode.html)| Gets a hash
code for the current instance.  
[GetSubArray](Unity.Collections.NativeArray_1.GetSubArray.html)| Gets a view
into an array starting at the specified index.  
[Reinterpret](Unity.Collections.NativeArray_1.Reinterpret.html)| Reinterpret a
NativeArray<T0> with a different data type (type punning).  
[ReinterpretLoad](Unity.Collections.NativeArray_1.ReinterpretLoad.html)|
Reinterpret and load data starting at underlying index as a different type.  
[ReinterpretStore](Unity.Collections.NativeArray_1.ReinterpretStore.html)|
Reinterpret and store data starting at underlying index as a different type.  
[ToArray](Unity.Collections.NativeArray_1.ToArray.html)| Convert a
NativeArray<T0> to an array.  
  
### Static Methods

[Copy](Unity.Collections.NativeArray_1.Copy.html)| Copies a range of elements
from a source array to a destination array, starting from the source index and
copying them to the destination index.  
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

