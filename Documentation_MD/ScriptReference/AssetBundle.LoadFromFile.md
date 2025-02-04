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

#  [AssetBundle](AssetBundle.html).LoadFromFile

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

public static [AssetBundle](AssetBundle.html) LoadFromFile(string path);

## Declaration

public static [AssetBundle](AssetBundle.html) LoadFromFile(string path, uint
crc);

## Declaration

public static [AssetBundle](AssetBundle.html) LoadFromFile(string path, uint
crc, ulong offset);

### Parameters

path | Path of the file on disk.  
---|---  
crc | An optional CRC-32 checksum of the uncompressed content. If this is non-zero, then the content will be compared against the checksum before loading it, and give an error if it does not match.  
offset | An optional byte offset. This value specifies where to start reading the AssetBundle from.  
  
### Returns

**AssetBundle** Loaded AssetBundle object or null if failed.

### Description

Synchronously loads an AssetBundle from a file on disk.

The function supports bundles of any compression type. In case of **LZMA**
compression, the file content will be fully decompressed into memory and
loaded from there. See [AssetBundles compression](../Manual/AssetBundles-
Cache.html) for more details.  
  
Compared to [LoadFromFileAsync](AssetBundle.LoadFromFileAsync.html), this
version is synchronous and will not return until it is done creating the
AssetBundle object.  
  
This is the fastest way to load an AssetBundle.

    
    
    using UnityEngine;
    using System.Collections;
    using System.IO;  
      
    public class LoadFromFileExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            var myLoadedAssetBundle = [AssetBundle.LoadFromFile](AssetBundle.LoadFromFile.html)(Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "myassetBundle"));
            if (myLoadedAssetBundle == null)
            {
                [Debug.Log](Debug.Log.html)("Failed to load [AssetBundle](AssetBundle.html)!");
                return;
            }  
      
            var prefab = myLoadedAssetBundle.LoadAsset<[GameObject](GameObject.html)>("MyObject");
            Instantiate(prefab);  
      
            myLoadedAssetBundle.Unload(false);
        }
    }
    

Additional resources: [AssetBundle](AssetBundle.html),
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

