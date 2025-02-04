[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-downloading-asset-bundle.html)
  * [中文](/cn/current/Manual/web-request-downloading-asset-bundle.html)
  * [日本語](/ja/current/Manual/web-request-downloading-asset-bundle.html)
  * [한국어](/kr/current/Manual/web-request-downloading-asset-bundle.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-downloading-asset-bundle.html)
  * [中文](/cn/current/Manual/web-request-downloading-asset-bundle.html)
  * [日本語](/ja/current/Manual/web-request-downloading-asset-bundle.html)
  * [한국어](/kr/current/Manual/web-request-downloading-asset-bundle.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Common operations: using the HLAPI](web-request-hlapi.html)
  * Downloading an AssetBundle from an HTTP server (GET)

[](web-request-retrieving-texture.html)

Retrieving a Texture from an HTTP Server (GET)

[](web-request-sending-form.html)

Sending a form to an HTTP server (POST)

# Downloading an AssetBundle from an HTTP server (GET)

To download an AssetBundle from a remote server, you can use
`UnityWebRequest.GetAssetBundle`. This function streams data into an internal
buffer, which decodes and decompresses the AssetBundle’s data on a worker
thread.

The function’s arguments take several forms. In its simplest form, it takes
only the URL from which the AssetBundle should be downloaded. You may
optionally provide a checksum to verify the integrity of the downloaded data.

Alternately, if you wish to use the AssetBundle caching system, you may
provide either a version number or a Hash128 data structure. These are
identical to the version numbers or `Hash128 objects` provided to the old
system via `WWW.LoadFromCacheOrDownload`.

## Details

  * This function creates a `UnityWebRequest` and sets the target URL to the supplied URL argument. It also sets the HTTP verb to `GET`, but sets no other flags or custom headers.
  * This function attaches a `DownloadHandlerAssetBundle` to the `UnityWebRequest`. This download handler has a special `assetBundle` property, which can be used to extract the AssetBundle once enough data has been downloaded and decoded to permit access to the resources inside the AssetBundle.
  * If you supply a version number or `Hash128` object as arguments, it also passes those arguments to the `DownloadHandlerAssetBundle`. The download handler then employs the caching system.

## Example

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;
     
    public class MyBehaviour : MonoBehaviour {
        void Start() {
            StartCoroutine(GetAssetBundle());
        }
     
        IEnumerator GetAssetBundle() {
            UnityWebRequest www = UnityWebRequestAssetBundle.GetAssetBundle("https://www.my-server.com/myData.unity3d");
            yield return www.SendWebRequest();
     
            if (www.result != UnityWebRequest.Result.Success) {
                Debug.Log(www.error);
            }
            else {
                AssetBundle bundle = DownloadHandlerAssetBundle.GetContent(www);
            }
        }
    }
    

[](web-request-retrieving-texture.html)

Retrieving a Texture from an HTTP Server (GET)

[](web-request-sending-form.html)

Sending a form to an HTTP server (POST)

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

