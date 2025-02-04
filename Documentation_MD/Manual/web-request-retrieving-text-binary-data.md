[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-retrieving-text-binary-data.html)
  * [中文](/cn/current/Manual/web-request-retrieving-text-binary-data.html)
  * [日本語](/ja/current/Manual/web-request-retrieving-text-binary-data.html)
  * [한국어](/kr/current/Manual/web-request-retrieving-text-binary-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-retrieving-text-binary-data.html)
  * [中文](/cn/current/Manual/web-request-retrieving-text-binary-data.html)
  * [日本語](/ja/current/Manual/web-request-retrieving-text-binary-data.html)
  * [한국어](/kr/current/Manual/web-request-retrieving-text-binary-data.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Common operations: using the HLAPI](web-request-hlapi.html)
  * Retrieving text or binary data from an HTTP Server (GET)

[](web-request-hlapi.html)

Common operations: using the HLAPI

[](web-request-retrieving-texture.html)

Retrieving a Texture from an HTTP Server (GET)

# Retrieving text or binary data from an HTTP Server (GET)

To retrieve simple data such as textual data or binary data from a standard
HTTP or HTTPS web server, use the `UnityWebRequest.GET` call. This function
takes a single string as an argument, with the string specifying the URL from
which data is retrieved.

This function is analogous to the standard WWW constructor:

    
    
    WWW myWww = new WWW("https://www.myserver.com/foo.txt");
    // ... is analogous to ...
    UnityWebRequest myWr = UnityWebRequest.Get("https://www.myserver.com/foo.txt");
    

## Details

  * This function creates a `UnityWebRequest` and sets the target URL to the string argument. It sets no other custom flags or headers.
  * By default, this function attaches a standard `DownloadHandlerBuffer` to the `UnityWebRequest`. This handler buffers the data received from the server and make it available to your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) when the request is complete.

  * By default, this function attaches no `UploadHandler` to the `UnityWebRequest`. You can attach one manually if you wish.

## Example

    
    
    using UnityEngine;
    using System.Collections;
    using UnityEngine.Networking;
     
    public class MyBehaviour : MonoBehaviour {
        void Start() {
            StartCoroutine(GetText());
        }
     
        IEnumerator GetText() {
            UnityWebRequest www = UnityWebRequest.Get("https://www.my-server.com");
            yield return www.SendWebRequest();
     
            if (www.result != UnityWebRequest.Result.Success) {
                Debug.Log(www.error);
            }
            else {
                // Show results as text
                Debug.Log(www.downloadHandler.text);
     
                // Or retrieve results as binary data
                byte[] results = www.downloadHandler.data;
            }
        }
    }
    

[](web-request-hlapi.html)

Common operations: using the HLAPI

[](web-request-retrieving-texture.html)

Retrieving a Texture from an HTTP Server (GET)

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

