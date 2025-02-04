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

# Hash128 Constructor

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

public Hash128(uint u32_0, uint u32_1, uint u32_2, uint u32_3);

## Declaration

public Hash128(ulong u64_0, ulong u64_1);

### Parameters

u32_0 | First 32 bits of hash value.  
---|---  
u32_1 | Second 32 bits of hash value.  
u32_2 | Third 32 bits of hash value.  
u32_3 | Fourth 32 bits of hash value.  
u64_0 | First 64 bits of hash value.  
u64_1 | Second 64 bits of hash value.  
  
### Description

Directly initialize a Hash128 with a 128-bit value.

To compute hash value of some data, use
[Hash128.Compute](Hash128.Compute.html) function.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var hash = new [Hash128](Hash128.html)(0x01020304, 0xaabbccdd, 0x12345678, 0xbaadc0de);
            // prints "04030201ddccbbaa78563412dec0adba",
            // because the hash values are in little-endian byte order
            [Debug.Log](Debug.Log.html)(hash.ToString());
        }
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

