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

# DownloadHandlerAssetBundle Constructor

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

public DownloadHandlerAssetBundle(string url, uint crc);

### Parameters

url | The nominal (pre-redirect) URL at which the asset bundle is located.  
---|---  
crc | A checksum to compare to the downloaded data for integrity checking, or zero to skip integrity checking.  
  
### Description

Standard constructor for non-cached asset bundles.

This constructor will bypass the caching system and simply download the
[AssetBundle](AssetBundle.html) from `url`.  
  
If the `crc` argument is non-zero, then the `crc` argument will be compared to
the checksum of the downloaded data. If the CRCs do not match, an error will
be logged, the asset bundle will not be loaded, and assetBundle will return
`null`.  
  
If you do not wish to use CRC integrity checking, pass zero as the `crc`
argument.

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.Networking;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            string url = "https://website.com/assetbundle";
            using (var uwr = new [UnityWebRequest](Networking.UnityWebRequest.html)(url, [UnityWebRequest.kHttpVerbGET](Networking.UnityWebRequest-kHttpVerbGET.html)))
            {
                uwr.downloadHandler = new [DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html)(url, 0);
                yield return uwr.SendWebRequest();
                [AssetBundle](AssetBundle.html) bundle = [DownloadHandlerAssetBundle.GetContent](Networking.DownloadHandlerAssetBundle.GetContent.html)(uwr);  
      
                //Unload the [AssetBundle](AssetBundle.html)
                bundle.Unload(true);
            }
        }
    }
    

* * *

## Declaration

public DownloadHandlerAssetBundle(string url, uint version, uint crc);

### Parameters

url | The nominal (pre-redirect) URL at which the asset bundle is located.  
---|---  
crc | A checksum to compare to the downloaded data for integrity checking, or zero to skip integrity checking.  
version | Current version number of the asset bundle at `url`. Increment to redownload.  
  
### Description

Simple versioned constructor. Caches downloaded asset bundles.

When this constructor is used, the
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html) will
first check to see if there is a cached [AssetBundle](AssetBundle.html) from
`url`.  
  
If there is no cached asset bundle, or if the cached asset bundle's `version`
matches the `version` argument, then the system will skip downloading the
asset bundle and instead load it from the cache.  
  
If there is a cached asset bundle, but the cached bundle's `version` does not
match the `version` argument, then the system will re-download the asset
bundle from `url`.  
  
If the `crc` argument is non-zero, then the `crc` argument will be compared to
the checksum of the downloaded data. If the CRCs do not match, an error will
be logged, the asset bundle will not be loaded, and assetBundle will return
`null`.  
  
If you do not wish to use CRC integrity checking, pass zero as the `crc`
argument.

* * *

## Declaration

public DownloadHandlerAssetBundle(string url, [Hash128](Hash128.html) hash,
uint crc);

### Parameters

url | The nominal (pre-redirect) URL at which the asset bundle is located.  
---|---  
crc | A checksum to compare to the downloaded data for integrity checking, or zero to skip integrity checking.  
hash | A hash object defining the version of the asset bundle.  
  
### Description

Versioned constructor. Caches downloaded asset bundles.

When this constructor is used, the
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html) will
first check to see if there is a cached [AssetBundle](AssetBundle.html) from
`url`.  
  
If there is no cached asset bundle, or if the cached asset bundle's `hash`
matches the `hash` argument, then the system will skip downloading the asset
bundle and instead load it from the cache.  
  
If there is a cached asset bundle, but the cached bundle's `hash` does not
match the `hash` argument, then the system will re-download the asset bundle
from `url`.  
  
If the `crc` argument is non-zero, then the `crc` argument will be compared to
the checksum of the downloaded data. If the CRCs do not match, an error will
be logged, the asset bundle will not be loaded, and assetBundle will return
`null`.  
  
If you do not wish to use CRC integrity checking, pass zero as the `crc`
argument.

* * *

## Declaration

public DownloadHandlerAssetBundle(string url, string name,
[Hash128](Hash128.html) hash, uint crc);

## Declaration

public DownloadHandlerAssetBundle(string url,
[CachedAssetBundle](CachedAssetBundle.html) cachedBundle, uint crc);

### Parameters

url | The nominal (pre-redirect) URL at which the asset bundle is located.  
---|---  
hash | A hash object defining the version of the asset bundle.  
crc | A checksum to compare to the downloaded data for integrity checking, or zero to skip integrity checking.  
cachedBundle | A structure used to download a given version of AssetBundle to a customized cache path.  
name | AssetBundle name which is used as the customized cache path.  
  
### Description

Versioned constructor. Caches downloaded asset bundles to a customized cache
path.

Cached AssetBundles are uniquely identified solely by the filename and
version. All domain and path information in `url` is ignored by Caching. Since
cached AssetBundles are identified by filename instead of the full URL, you
can change the directory from where the asset bundle is downloaded at any
time. This is useful for pushing out new versions of the game and ensuring
that files are not cached incorrectly by the browser or by a CDN.  
  
Usually using the filename of the AssetBundle to generate the cache path is
fine. But if there are different AssetBundles with the same last file name,
cache conflicts happens. With CachedAssetBundle struct, you can use
[CachedAssetBundle.name](CachedAssetBundle-name.html) to customized the cache
path to avoid the cache conflicts. You can also utilize this to organize the
cache data structure.

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

