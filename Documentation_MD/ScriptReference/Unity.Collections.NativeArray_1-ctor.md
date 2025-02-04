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

# NativeArray<T0> Constructor

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

public NativeArray<T0>(T[] array,
[Unity.Collections.Allocator](Unity.Collections.Allocator.html) allocator);

### Parameters

array | An array to copy the data from.  
---|---  
allocator | The [Allocator](Unity.Collections.Allocator.html) to use for the data.  
  
### Description

Creates a NativeArray from an array of elements.

* * *

## Declaration

public NativeArray<T0>(NativeArray<T> array,
[Unity.Collections.Allocator](Unity.Collections.Allocator.html) allocator);

### Parameters

array | The [NativeArray<T0>](Unity.Collections.NativeArray_1.html) to copy the data from.  
---|---  
allocator | The [Allocator](Unity.Collections.Allocator.html) to use for the data.  
  
### Description

Creates a NativeArray from an existing NativeArray.

* * *

## Declaration

public NativeArray<T0>(int length,
[Unity.Collections.Allocator](Unity.Collections.Allocator.html) allocator,
[Unity.Collections.NativeArrayOptions](Unity.Collections.NativeArrayOptions.html)
options);

### Parameters

length | Number of elements to allocate.  
---|---  
allocator | The [Allocator](Unity.Collections.Allocator.html) to use for the data.  
options | The [NativeArrayOptions](Unity.Collections.NativeArrayOptions.html) to use for the data.  
  
### Description

Creates a new NativeArray and allocates enough memory to fit the provided
amount of elements.

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

