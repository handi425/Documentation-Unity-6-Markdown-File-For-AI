[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-retrieving-texture.html)
  * [中文](/cn/current/Manual/web-request-retrieving-texture.html)
  * [日本語](/ja/current/Manual/web-request-retrieving-texture.html)
  * [한국어](/kr/current/Manual/web-request-retrieving-texture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-retrieving-texture.html)
  * [中文](/cn/current/Manual/web-request-retrieving-texture.html)
  * [日本語](/ja/current/Manual/web-request-retrieving-texture.html)
  * [한국어](/kr/current/Manual/web-request-retrieving-texture.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Common operations: using the HLAPI](web-request-hlapi.html)
  * Retrieving a Texture from an HTTP Server (GET)

[](web-request-retrieving-text-binary-data.html)

Retrieving text or binary data from an HTTP Server (GET)

[](web-request-downloading-asset-bundle.html)

Downloading an AssetBundle from an HTTP server (GET)

# Retrieving a Texture from an HTTP Server (GET)

To retrieve a Texture file from a remote server, you can use
`UnityWebRequestTexture.GetTexture`. This function is very similar to
`UnityWebRequest.Get`, but is optimized for downloading and storing textures
efficiently.

`UnityWebRequestTexture.GetTexture` takes a string or `Uri` object as an
argument that specifies a URL of an image file to download and use as a
Texture. Additionally, it can take `DownloadedTextureParams` as second
argument, allowing you more control over the texture that will be created.

## Details

  * This function creates a `UnityWebRequest` and sets the target URL to the string argument. This function sets no other flags or custom headers.
  * This function attaches a `DownloadHandlerTexture` object to the `UnityWebRequest`. DownloadHandlerTexture is a specialized Download Handler which is optimized for storing images which are to be used as Textures in the Unity Engine. Using this class significantly reduces memory reallocation compared with downloading raw bytes and creating a Texture manually in script.
  * By default, this function does not attach an Upload Handler. You can add one manually if you wish.

## Example

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Networking;
     
    public class MyBehaviour : MonoBehaviour {
        void Start() {
            StartCoroutine(GetTexture());
        }
     
        IEnumerator GetTexture() {
            UnityWebRequest www = UnityWebRequestTexture.GetTexture("https://www.my-server.com/image.png");
            yield return www.SendWebRequest();
    
            if (www.result != UnityWebRequest.Result.Success) {
                Debug.Log(www.error);
            }
            else {
                Texture myTexture = DownloadHandlerTexture.GetContent(www);
            }
        }
    }
    

[](web-request-retrieving-text-binary-data.html)

Retrieving text or binary data from an HTTP Server (GET)

[](web-request-downloading-asset-bundle.html)

Downloading an AssetBundle from an HTTP server (GET)

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

