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

#  [Hash128](Hash128.html).Append

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

public void Append(int val);

## Declaration

public void Append(float val);

## Declaration

public void Append(ref T val);

### Parameters

val | Input value.  
---|---  
  
### Description

Hash new input data and combine with the current hash value.

The value must be an "unmanaged" C# type. Primitive types like int, float,
bool, enums, pointers, or structs containing primitive types are all unmanaged
types. See [Unmanaged types](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/builtin-types/unmanaged-types) in C#
language reference.  
  
The int and float overloads use a dedicated code path that is optimized for
4-byte data sizes.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var hash = new [Hash128](Hash128.html)();
            hash.Append(42);
            hash.Append(13.0f);
            hash.Append("Hello");
            hash.Append(new int[] {1, 2, 3, 4, 5});
            // prints "2d6e582c3fcfb4b8f3c16650a75dc37b"
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
    }
    

* * *

## Declaration

public void Append(string data);

### Parameters

data | Input data string. Note that Unity interprets the string as UTF-8 data, even if internally in C# strings are UTF-16.  
---|---  
  
### Description

Hash new input string and combine with the current hash value.

* * *

## Declaration

public void Append(T[] data);

## Declaration

public void Append(List<T> data);

## Declaration

public void Append(NativeArray<T> data);

### Parameters

data | Input data array.  
---|---  
  
### Description

Hash new input data array and combine with the current hash value.

* * *

## Declaration

public void Append(T[] data, int start, int count);

## Declaration

public void Append(List<T> data, int start, int count);

## Declaration

public void Append(NativeArray<T> data, int start, int count);

### Parameters

data | Input data array.  
---|---  
start | The first element in the data to start hashing from.  
count | Number of array elements to hash.  
  
### Description

Hash a slice of new input data array and combine with the current hash value.

* * *

## Declaration

public void Append(void* data, ulong size);

### Parameters

data | Raw data pointer, usually used with C# `stackalloc` data.  
---|---  
size | Data size in bytes.  
  
### Description

Hash new input data and combine with the current hash value.

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

