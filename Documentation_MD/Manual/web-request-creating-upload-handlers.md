[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-creating-upload-handlers.html)
  * [中文](/cn/current/Manual/web-request-creating-upload-handlers.html)
  * [日本語](/ja/current/Manual/web-request-creating-upload-handlers.html)
  * [한국어](/kr/current/Manual/web-request-creating-upload-handlers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-creating-upload-handlers.html)
  * [中文](/cn/current/Manual/web-request-creating-upload-handlers.html)
  * [日本語](/ja/current/Manual/web-request-creating-upload-handlers.html)
  * [한국어](/kr/current/Manual/web-request-creating-upload-handlers.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Advanced operations: Using the LLAPI](web-request-llapi.html)
  * Creating UploadHandlers

[](web-request-creating-unity-web-requests.html)

Creating UnityWebRequests

[](web-request-creating-download-handlers.html)

Creating DownloadHandlers

# Creating UploadHandlers

Currently, there are two types of upload handlers available:
`UploadHandlerRaw` and `UploadHandlerFile`.

`UploadHandlerRaw` class accepts a data buffer at construction time. When this
buffer is an array of bytes, it’s copied internally into native code memory.
`UnityWebRequest` system uses this buffer when the remote server is ready to
receive the request body data. When the buffer is provided as a `NativeArray`,
no copying is performed.

`UploadHandlerFile` allows you to send the contents of a file as the request
body. Using this handler, you can send a large file to a server without using
a lot of memory. As the handler reads data from the file and then sends it,
only a small fraction of the file is kept in memory at any given time.

Upload Handlers also accept a Content Type string. This string is used for the
value of the UnityWebRequest’s `Content-Type` header if you set no `Content-
Type` header on the UnityWebRequest itself. If you manually set a `Content-
Type` header on the UnityWebRequest object, the `Content-Type` on the Upload
Handler object is ignored.

If you do not set a `Content-Type` on either the UnityWebRequest or the
`UploadHandler`, the system defaults to setting a `Content-Type` of
`application/octet-stream`.

`UnityWebRequest` has a property `disposeUploadHandlerOnDispose`, which
defaults to true. If this property is true, when UnityWebRequest object is
disposed, Dispose() will also be called on attached upload handler rendering
it useless. If you keep a reference to upload handler longer than the
reference to UnityWebRequest, you should set disposeUploadHandlerOnDispose to
false.

## Example

    
    
    byte[] payload = new byte[1024];
    // ... fill payload with data ...
    
    UnityWebRequest wr = new UnityWebRequest("https://www.mysite.com/data-upload");
    UploadHandler uploader = new UploadHandlerRaw(payload);
    
    // Sends header: "Content-Type: custom/content-type";
    uploader.contentType = "custom/content-type";
    
    wr.uploadHandler = uploader;
    

[](web-request-creating-unity-web-requests.html)

Creating UnityWebRequests

[](web-request-creating-download-handlers.html)

Creating DownloadHandlers

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

