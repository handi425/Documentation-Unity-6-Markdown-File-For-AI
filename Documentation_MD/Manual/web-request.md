[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request.html)
  * [中文](/cn/current/Manual/web-request.html)
  * [日本語](/ja/current/Manual/web-request.html)
  * [한국어](/kr/current/Manual/web-request.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request.html)
  * [中文](/cn/current/Manual/web-request.html)
  * [日本語](/ja/current/Manual/web-request.html)
  * [한국어](/kr/current/Manual/web-request.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Interacting with web servers

[](coroutines.html)

Splitting tasks across frames

[](web-request-hlapi.html)

Common operations: using the HLAPI

# Interacting with web servers

UnityWebRequest provides a modular system for composing HTTP requests and
handling HTTP responses. The primary goal of the UnityWebRequest system is to
allow Unity games to interact with web browser back-ends. It also supports
high-demand features such as chunked HTTP requests, streaming POST/PUT
operations, and full control over HTTP headers and verbs.

The system consists of two layers:

  * A [High-Level API](web-request-hlapi.html) (HLAPI) wraps the Low-Level API and provides a convenient interface for performing common operations
  * A [Low-Level API](web-request-llapi.html) (LLAPI) provides maximum flexibility for more advanced users

## Supported platforms

The UnityWebRequest system supports most Unity platforms:

  * All versions of the Editor and Standalone players
  * Web
  * Mobile platforms: iOS, Android
  * Universal Windows Platform

## Architecture

The UnityWebRequest ecosystem breaks down an HTTP transaction into three
distinct operations:

  * Supplying data to the server
  * Receiving data from the server
  * HTTP flow control (for example, redirects and error handling)

To provide a better interface for advanced users, these operations are each
governed by their own objects:

  * An `UploadHandler` object handles transmission of data to the server
  * A `DownloadHandler` object handles receipt, buffering and postprocessing of data received from the server
  * A `UnityWebRequest` object manages the other two objects, and also handles HTTP flow control. This object is where custom headers and URLs are defined, and where error and redirect information is stored.

![](../uploads/Main/UnityWebRequestArchitecture.png)

For any HTTP transaction, the normal code flow is:

  * Create a Web Request object
  * Configure the Web Request object 
    * Set custom headers
    * Set HTTP verb (such as GET, POST, HEAD - custom verbs are permitted on all platforms except for Android)
    * Set URL
  * (Optional) Create an Upload Handler and attach it to the Web Request 
    * Provide data to be uploaded
    * Provide HTTP form to be uploaded
  * (Optional) Create a Download Handler and attach it to the Web Request
  * Send the Web Request 
    * If inside a coroutine, you may Yield the result of the `Send()` call to wait for the request to complete
  * (Optional) Read received data from the Download Handler
  * (Optional) Read error information, HTTP status code and response headers from the UnityWebRequest object

[](coroutines.html)

Splitting tasks across frames

[](web-request-hlapi.html)

Common operations: using the HLAPI

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

