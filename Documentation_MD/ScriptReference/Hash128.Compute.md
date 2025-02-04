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

#  [Hash128](Hash128.html).Compute

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

public static [Hash128](Hash128.html) Compute(ref T val);

## Declaration

public static [Hash128](Hash128.html) Compute(int val);

## Declaration

public static [Hash128](Hash128.html) Compute(float val);

### Parameters

val | Input value.  
---|---  
  
### Returns

**Hash128** The 128-bit hash.

### Description

Compute a hash of input data.

The value must be an "unmanaged" C# type. Primitive types like `int`, `float`,
`bool`, enums, pointers, or structs containing primitive types are all
unmanaged types. See [Unmanaged types](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/builtin-types/unmanaged-types) in C#
language reference.  
  
The `int` and `float` overloads use a dedicated hashing code path that is
optimized for 4-byte data sizes.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var data = new [Vector3](Vector3.html)(1.5f, 7.0f, 42.0f);
            var hash = [Hash128.Compute](Hash128.Compute.html)(ref data);
            // prints "abc99ce06a8d7acca0714cd64d661808"
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
    }
    

* * *

## Declaration

public static [Hash128](Hash128.html) Compute(string data);

### Parameters

data | Input data string. Note that Unity interprets the string as UTF-8 data, even if internally in C# strings are UTF-16.  
---|---  
  
### Returns

**Hash128** The 128-bit hash.

### Description

Compute a hash of input data string.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var hash = [Hash128.Compute](Hash128.Compute.html)("The quick brown fox jumps over the lazy dog");
            // prints "c79306aa46e8122b1b340724747e361d"
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
    }
    

* * *

## Declaration

public static [Hash128](Hash128.html) Compute(T[] data);

## Declaration

public static [Hash128](Hash128.html) Compute(List<T> data);

## Declaration

public static [Hash128](Hash128.html) Compute(NativeArray<T> data);

### Parameters

data | Input data array.  
---|---  
  
### Returns

**Hash128** The 128-bit hash.

### Description

Compute a hash of input data.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var data = new byte[] { 10, 20, 30, 40, 50 };
            var hash = [Hash128.Compute](Hash128.Compute.html)(data);
            // prints "6e8dd00dc1d495a01d9e6dbffcd174b2"
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
    }
    

* * *

## Declaration

public static [Hash128](Hash128.html) Compute(T[] data, int start, int count);

## Declaration

public static [Hash128](Hash128.html) Compute(List<T> data, int start, int
count);

## Declaration

public static [Hash128](Hash128.html) Compute(NativeArray<T> data, int start,
int count);

### Parameters

data | Input data array.  
---|---  
start | The first element in the data to start hashing from.  
count | Number of array elements to hash.  
  
### Returns

**Hash128** The 128-bit hash.

### Description

Compute a hash of a slice of input data.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var data = new byte[] { 0, 10, 20, 30, 40, 50, 60 };
            // will hash bytes: 10, 20, 30, 40, 50
            var hash = [Hash128.Compute](Hash128.Compute.html)(data, 1, 5);
            // prints "6e8dd00dc1d495a01d9e6dbffcd174b2"
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
    }
    

* * *

## Declaration

public static [Hash128](Hash128.html) Compute(void* data, ulong size);

### Parameters

data | Raw data pointer, usually used with C# `stackalloc` data.  
---|---  
size | Data size in bytes.  
  
### Returns

**Hash128** The 128-bit hash.

### Description

Compute a hash of input data.

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

