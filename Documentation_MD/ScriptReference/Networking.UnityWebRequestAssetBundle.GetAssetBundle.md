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
[UnityWebRequestAssetBundle](Networking.UnityWebRequestAssetBundle.html).GetAssetBundle

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

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(string uri);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(Uri uri);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(string uri, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(Uri uri, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(string uri, uint version, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(Uri uri, uint version, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(string uri, [Hash128](Hash128.html) hash, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(Uri uri, [Hash128](Hash128.html) hash, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(string uri, [CachedAssetBundle](CachedAssetBundle.html)
cachedAssetBundle, uint crc);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
GetAssetBundle(Uri uri, [CachedAssetBundle](CachedAssetBundle.html)
cachedAssetBundle, uint crc);

### Parameters

uri | The URI of the asset bundle to download.  
---|---  
crc | If nonzero, this number will be compared to the checksum of the downloaded asset bundle data. If the CRCs do not match, an error will be logged and the asset bundle will not be loaded. If set to zero, CRC checking will be skipped.  
version | An integer version number, which will be compared to the cached version of the asset bundle to download. Increment this number to force Unity to redownload a cached asset bundle.  
  
Analogous to the `version` parameter for WWW.LoadFromCacheOrDownload.  
hash | A version hash. If this hash does not match the hash for the cached version of this asset bundle, the asset bundle will be redownloaded.  
cachedAssetBundle | A structure used to download a given version of AssetBundle to a customized cache path.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to downloading a Unity Asset
Bundle.

### Description

Creates a UnityWebRequest optimized for downloading a Unity Asset Bundle via
HTTP GET.

This method creates a UnityWebRequest, sets the method to `GET` and sets the
target URL to the string `uri` argument. Sets no other flags or custom
headers.  
  
This method attaches a
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html) to
the [UnityWebRequest](Networking.UnityWebRequest.html). This
[DownloadHandler](Networking.DownloadHandler.html) has a special
[DownloadHandlerAssetBundle.assetBundle](Networking.DownloadHandlerAssetBundle-
assetBundle.html) property, which can be used to extract the asset bundle once
enough data has been downloaded and decoded to permit access to the resources
inside the bundle.  
  
In addition, the
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html)
streams data into a ringbuffer and decompresses the data on a worker thread,
saving many memory allocations compared to downloading the data all at once.  
  
If supplied with an integer `version` or Hash128 `hash` argument, the
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html) will
employ the Asset Bundle caching system. If an Asset Bundle has been cached and
does not need to be redownloaded, then the
[UnityWebRequest](Networking.UnityWebRequest.html) will complete once the
Asset Bundle has finished loading from the cache.  
  
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
  
**Note** , that while you can use this API to load Asset Bundle from local
storage (using file:// URI or jar:file// on Android), this is not recommended,
use [AssetBundle.LoadFromFileAsync](AssetBundle.LoadFromFileAsync.html)
instead.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(GetText());
        }  
      
        IEnumerator GetText()
        {
            using ([UnityWebRequest](Networking.UnityWebRequest.html) uwr = [UnityWebRequestAssetBundle.GetAssetBundle](Networking.UnityWebRequestAssetBundle.GetAssetBundle.html)("https://www.my-server.com/mybundle"))
            {
                yield return uwr.SendWebRequest();  
      
                if (uwr.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.Log](Debug.Log.html)(uwr.error);
                }
                else
                {
                    // Get downloaded asset bundle
                    [AssetBundle](AssetBundle.html) bundle = [DownloadHandlerAssetBundle.GetContent](Networking.DownloadHandlerAssetBundle.GetContent.html)(uwr);  
      
                    // Unload the [AssetBundle](AssetBundle.html) 
                    bundle.Unload(true);
                }
            }
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

