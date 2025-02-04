[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-request-creating-unity-web-requests.html)
  * [中文](/cn/current/Manual/web-request-creating-unity-web-requests.html)
  * [日本語](/ja/current/Manual/web-request-creating-unity-web-requests.html)
  * [한국어](/kr/current/Manual/web-request-creating-unity-web-requests.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-request-creating-unity-web-requests.html)
  * [中文](/cn/current/Manual/web-request-creating-unity-web-requests.html)
  * [日本語](/ja/current/Manual/web-request-creating-unity-web-requests.html)
  * [한국어](/kr/current/Manual/web-request-creating-unity-web-requests.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Interacting with web servers](web-request.html)
  * [Advanced operations: Using the LLAPI](web-request-llapi.html)
  * Creating UnityWebRequests

[](web-request-llapi.html)

Advanced operations: Using the LLAPI

[](web-request-creating-upload-handlers.html)

Creating UploadHandlers

# Creating UnityWebRequests

WebRequests can be instantiated like any other object. Two constructors are
available:

  * The standard, parameter-less constructor creates a new UnityWebRequest with all settings blank or default. The target URL isn’t set, no custom headers are set, and the redirect limit is set to 32.
  * The second constructor takes a string argument. It assigns the UnityWebRequest’s target URL to the value of the string argument, and is otherwise same as the parameter-less constructor.

Multiple other properties are available for setting up, tracking status and
checking result or UnityWebRequest.

## Example

    
    
    UnityWebRequest wr = new UnityWebRequest(); // Completely blank
    UnityWebRequest wr2 = new UnityWebRequest("https://www.mysite.com"); // Target URL is set
    
    // the following two are required to web requests to work
    wr.url = "https://www.mysite.com";
    wr.method = UnityWebRequest.kHttpVerbGET;   // can be set to any custom method, common constants provided
    
    wr.useHttpContinue = false;
    wr.chunkedTransfer = false;
    wr.redirectLimit = 0;  // disable redirects
    wr.timeout = 60;       // don't make this small, web requests do take some time
    

[](web-request-llapi.html)

Advanced operations: Using the LLAPI

[](web-request-creating-upload-handlers.html)

Creating UploadHandlers

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

