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

#  [AssetBundle](AssetBundle.html).LoadFromMemoryAsync

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

public static [AssetBundleCreateRequest](AssetBundleCreateRequest.html)
LoadFromMemoryAsync(byte[] binary);

## Declaration

public static [AssetBundleCreateRequest](AssetBundleCreateRequest.html)
LoadFromMemoryAsync(byte[] binary, uint crc);

### Parameters

binary | Array of bytes with the AssetBundle data.  
---|---  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
  
### Returns

**AssetBundleCreateRequest** Asynchronous load request for an AssetBundle. Use
[assetBundle](AssetBundleCreateRequest-assetBundle.html) property to get an
AssetBundle once it is loaded.

### Description

Asynchronously load an AssetBundle from a memory region.

Use this method to load an AssetBundle from an array of bytes asynchronously.
This is useful when you have downloaded the data with encryption using
UnityWebRequest and have the unencrypted bytes in memory instead of stored in
a file.  
  
Compared to [LoadFromMemory](AssetBundle.LoadFromMemory.html), this version
will perform AssetBundle decompression on a background thread, and will not
create the AssetBundle object immediately.  
  
The content of the provided byte array is copied to create a temporary
AssetBundle file in Memory, and that file is then loaded. Depending on the
compression of the original AssetBundle, and the setting for
[Caching.compressionEnabled](Caching-compressionEnabled.html), this may also
involve converting the content to LZ4 or uncompressed format. See
[AssetBundles compression](../Manual/AssetBundles-Cache.html) for more
details.  
  
The following example shows how to use this method. Note, for the sake of
keeping the example simple it reads the bytes from disk, which means it has no
advantage over calling AssetBundle.LoadFromFileAsync directly.

    
    
    using UnityEngine;
    using System.Collections;
    using System.IO;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator LoadFromMemoryAsync(string path)
        {
            [AssetBundleCreateRequest](AssetBundleCreateRequest.html) createRequest = [AssetBundle.LoadFromMemoryAsync](AssetBundle.LoadFromMemoryAsync.html)([File.ReadAllBytes](Windows.File.ReadAllBytes.html)(path));
            yield return createRequest;
            [AssetBundle](AssetBundle.html) bundle = createRequest.assetBundle;
            var prefab = bundle.LoadAsset<[GameObject](GameObject.html)>("MyObject");
            Instantiate(prefab);  
      
            bundle.Unload(true);
        }
    }
    

Additional resources:
[AssetBundleCreateRequest](AssetBundleCreateRequest.html),
[LoadFromMemory](AssetBundle.LoadFromMemory.html),
[LoadFromFileAsync](AssetBundle.LoadFromFileAsync.html).

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

