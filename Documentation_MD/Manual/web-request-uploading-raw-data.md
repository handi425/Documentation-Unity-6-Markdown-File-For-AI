[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-uploading-raw-data.html)
  * [中文](/cn/current/Manual/web-request-uploading-raw-data.html)
  * [日本語](/ja/current/Manual/web-request-uploading-raw-data.html)
  * [한국어](/kr/current/Manual/web-request-uploading-raw-data.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-uploading-raw-data.html)
  * [中文](/cn/current/Manual/web-request-uploading-raw-data.html)
  * [日本語](/ja/current/Manual/web-request-uploading-raw-data.html)
  * [한국어](/kr/current/Manual/web-request-uploading-raw-data.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Common operations: using the HLAPI](web-request-hlapi.html)
  * Uploading raw data to an HTTP server (PUT)

[](web-request-sending-form.html)

Sending a form to an HTTP server (POST)

[](web-request-llapi.html)

Advanced operations: Using the LLAPI

# Uploading raw data to an HTTP server (PUT)

Some modern web applications prefer that files be uploaded via the HTTP PUT
verb. For this scenario, Unity provides the `UnityWebRequest.PUT` function.

This function takes two arguments. The first argument is a string and
specifies the target URL for the request. The second argument may be either a
string or a byte array, and specifies the payload data to be sent to the
server.

Function signatures:

    
    
    WebRequest.Put(string url, string data);
    WebRequest.Put(string url, byte[] data);
    

## Details

  * This function creates a `UnityWebRequest` and sets the content type to `application/octet-stream`.
  * This function attaches a standard `DownloadHandlerBuffer` to the `UnityWebRequest`. As with the POST functions, you can use this to return result data from your applications.
  * This function stores the input upload data in a standard `UploadHandlerRaw` object and attaches it to the `UnityWebRequest`. As a result, if using the `byte[]` function, changes made to the byte array performed after the `UnityWebRequest.PUT` call are not reflected in the data uploaded to the server.

## Example

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;
     
    public class MyBehavior : MonoBehaviour {
        void Start() {
            StartCoroutine(Upload());
        }
     
        IEnumerator Upload() {
            byte[] myData = System.Text.Encoding.UTF8.GetBytes("This is some test data");
            UnityWebRequest www = UnityWebRequest.Put("https://www.my-server.com/upload", myData);
            yield return www.SendWebRequest();
     
            if (www.result != UnityWebRequest.Result.Success) {
                Debug.Log(www.error);
            }
            else {
                Debug.Log("Upload complete!");
            }
        }
    }
    

[](web-request-sending-form.html)

Sending a form to an HTTP server (POST)

[](web-request-llapi.html)

Advanced operations: Using the LLAPI

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

