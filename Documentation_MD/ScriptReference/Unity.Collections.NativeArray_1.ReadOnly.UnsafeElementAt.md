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
[NativeArray<T0>](Unity.Collections.NativeArray_1.ReadOnly.html).UnsafeElementAt

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

public ref readonly T UnsafeElementAt(int index);

### Parameters

index | The index of the element.  
---|---  
  
### Returns

**T** A `ref readonly` to a value of type `T`.

### Description

Provides read-only access to
[ReadOnly](Unity.Collections.NativeArray_1.ReadOnly.html) elements by index.

This method is dangerous because it returns reference to the memory that can
be destroyed (with Dispose, for instance) and if the `ref local` is accessed
that might lead to undefined results including crashes.

    
    
    public readonly struct BigStruct
    {
        public readonly long a;
        public readonly long b;
        public readonly long c;
        public readonly long d;
    }  
      
    static void ProcessByte(byte b)
    {
        ...
    }  
      
    static void ProcessBigStructWithoutCopy(in BigStruct bigStruct) // see 'in' modificator
    {
        ...
    }  
      
    static void Example()
    {
        const int n = 32;  
      
        var nativeArrayOfBytes = new NativeArray<byte>(n, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
        var nativeArrayOfBigStructures = new NativeArray<FixedString4096Bytes>(n, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
        // ... fill the arrays with some data ...  
      
        var readOnlyBytes = nativeArrayOfBytes.AsReadOnly();
        for (var i = 0; i < n; ++i)
        {
            ProcessByte(readOnlyBytes[i]);
            //ProcessByte(readOnlyBytes.UnsafeElementAt(i)); is more expensive, since pointer on x64 platforms is 8 times bigger than a byte
        }  
      
        var readOnlyBigStructures = nativeArrayOfBigStructures.AsReadOnly();
        for (var i = 0; i < n; ++i)
        {
            //ProcessBigStructWithoutCopy(readOnlyBigStructures[i]); copy - expensive in this case
            ProcessBigStructWithoutCopy(readOnlyBigStructures.UnsafeElementAt(i));
        }  
      
        // dangerous part
        ref var element = ref readOnlyBigStructures.UnsafeElementAt(4);  
      
        // element is valid here
        ProcessBigStructWithoutCopy(element);  
      
        nativeArrayOfBigStructures.Dispose();  
      
        // access to element here is undefined, can lead to a crash or wrong results
        // ProcessBigStructWithoutCopy(element); <-- do not do this!
    }
    

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

