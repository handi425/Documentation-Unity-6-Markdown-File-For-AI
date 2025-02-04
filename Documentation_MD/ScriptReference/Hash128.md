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

# Hash128

struct in UnityEngine

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

Represents a 128-bit hash value.

Use `Hash128` to uniquely identify a piece of data. A 128-bit hash value has
an extremely low probability of hash collisions, so you can assume that if the
hash values of two pieces of data are identical, then the data is identical
too. For example, to quickly determine whether texture pixel contents have
changed, or if they are identical between several textures, you can use
[Texture.imageContentsHash](Texture-imageContentsHash.html).  
  
To compute the hash values for some data, use the
[Hash128.Compute](Hash128.Compute.html) function. To compute the hash values
incrementally for several pieces of data, use
[Hash128.Append](Hash128.Append.html).

    
    
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
    

The hash algorithm used to compute `Hash128` values is [SpookyHash
V2](https://en.wikipedia.org/wiki/Jenkins_hash_function#SpookyHash). Note that
while this hash algorithm is quite fast to compute and has good hash
distribution qualities, it is not a cryptographic hash function.

### Properties

[isValid](Hash128-isValid.html)| Returns true is the hash value is valid.
(Read Only)  
---|---  
  
### Constructors

[Hash128](Hash128-ctor.html)| Directly initialize a Hash128 with a 128-bit
value.  
---|---  
  
### Public Methods

[Append](Hash128.Append.html)| Hash new input data and combine with the
current hash value.  
---|---  
[ToString](Hash128.ToString.html)| Convert a Hash128 to string.  
  
### Static Methods

[Compute](Hash128.Compute.html)| Compute a hash of input data.  
---|---  
[Parse](Hash128.Parse.html)| Convert a hex-encoded string into Hash128 value.  
  
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

