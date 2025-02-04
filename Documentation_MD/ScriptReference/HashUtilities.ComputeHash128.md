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

#  [HashUtilities](HashUtilities.html).ComputeHash128

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

public static void ComputeHash128(byte[] value, ref [Hash128](Hash128.html)
hash);

## Declaration

public static void ComputeHash128(ref T value, ref [Hash128](Hash128.html)
hash);

### Parameters

value | A reference to the value to hash.  
---|---  
hash | A reference to the Hash128 to updated with the computed hash.  
  
### Description

Compute a 128 bit hash based on a value. the type of the value must be a value
type.

    
    
    using UnityEngine;
    using System.Runtime.InteropServices;  
      
    public class HashUtilitiesSample
    {
        [StructLayout(LayoutKind.Sequential)]
        struct TestData
        {
            public ulong V1;
            public ulong V2;
        }  
      
        public void ComputeHash128_ToHash128()
        {
            var message = new TestData
            {
                V1 = 0x73BC2A67F,
                V2 = 0x54B1A5C2C
            };  
      
            [Hash128](Hash128.html) hash = new [Hash128](Hash128.html)();
            [HashUtilities.ComputeHash128](HashUtilities.ComputeHash128.html)(ref message, ref hash);
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

