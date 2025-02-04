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

#  [AssetBundle](AssetBundle.html).LoadFromMemory

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

public static [AssetBundle](AssetBundle.html) LoadFromMemory(byte[] binary);

## Declaration

public static [AssetBundle](AssetBundle.html) LoadFromMemory(byte[] binary,
uint crc);

### Parameters

binary | Array of bytes with the AssetBundle data.  
---|---  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
  
### Returns

**AssetBundle** Loaded AssetBundle object or null if failed.

### Description

Synchronously load an AssetBundle from a memory region.

Use this method to load an AssetBundle from an array of bytes. This is useful
when you have downloaded the data with encryption and need to load the
AssetBundle from the decrypted bytes.  
  
Compared to [LoadFromMemoryAsync](AssetBundle.LoadFromMemoryAsync.html), this
version is synchronous and will not return until it is done creating the
AssetBundle object.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        byte[] MyDecrypt(byte[] binary)
        {
            // ...Perform some decryption process here to transform the input...
            return binary;
        }  
      
        IEnumerator Start()
        {
            var uwr = [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html)("https://myserver/myBundle.unity3d");
            yield return uwr.SendWebRequest();
            byte[] decryptedBytes = MyDecrypt(uwr.downloadHandler.data);
            [AssetBundle.LoadFromMemory](AssetBundle.LoadFromMemory.html)(decryptedBytes);
        }
    }
    

Additional resources: [AssetBundle](AssetBundle.html),
[LoadFromMemoryAsync](AssetBundle.LoadFromMemoryAsync.html),
[LoadFromFile](AssetBundle.LoadFromFile.html).

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

