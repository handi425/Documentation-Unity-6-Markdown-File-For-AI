[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/webgl-networking.html)
  * [中文](/cn/current/Manual/webgl-networking.html)
  * [日本語](/ja/current/Manual/webgl-networking.html)
  * [한국어](/kr/current/Manual/webgl-networking.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/webgl-networking.html)
  * [中文](/cn/current/Manual/webgl-networking.html)
  * [日本語](/ja/current/Manual/webgl-networking.html)
  * [한국어](/kr/current/Manual/webgl-networking.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * Web networking

[](webgl-browser-access-device.html)

Web browser access to device features

[](webassembly-2023.html)

WebAssembly 2023

# Web networking

You can use **networking** The Unity system that enables multiplayer gaming
across a computer network. [More info](multiplayer.html)  
See in [Glossary](Glossary.html#Networking) in Web in the following ways:

  * Use the [UnityWebRequest](./web-request.html) class.
  * Use the Unity Netcode networking package.

## Use the UnityWebRequest class in Web

Unity supports the
[UnityWebRequest](../ScriptReference/Networking.UnityWebRequest.html) class in
Web. To implement the UnityWebRequest class, Unity uses the JavaScript Fetch
API, which uses the browser to handle web requests. This imposes security
restrictions on accessing cross-domain resources.

If you send a web request to a server other than the one that hosts the Unity
content, the server you’re sending it to must authorize the Unity content.

To access cross-domain web resources in Web, the server you are trying to
access needs to use [cross-origin resource sharing
(CORS)](https://fetch.spec.whatwg.org/#http-cors-protocol) to authorize cross-
domain web resources.

If you try to access content using UnityWebRequest, and the remote server
doesn’t have CORS set up or configured correctly, an error like the following
appears in the browser console:

    
    
    Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://myserver.com/. This can be fixed by moving the resource to the same domain or enabling CORS.
    

The server needs to add Access-Control headers to the http responses it sends
out, to indicate which web pages have permission to read that information from
a web browser.

For a demonstration of how to add Access-Control headers that allow Unity Web
to access resources on a web server from any origin, refer to the following
example. This example includes common request headers and allows the GET, POST
or OPTIONS methods:

    
    
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Headers": "Accept, X-Access-Token, X-Application-Name, X-Request-Sent-Time",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Origin": "*",
    

### **UnityWebRequest downloads**

Don’t use code that blocks a UnityWebRequest download, such as this:

    
    
    while(!www.isDone) {}
    

Web browsers do not allow synchronously blocking code execution to wait for a
network transfer. Therefore, if you need to perform a synchronous style
UnityWebRequest, use a [Coroutine](coroutines.html) and a yield statement to
wait for the download to finish. For more information, see [Examples of
coroutines using UnityWebRequest](web-request-hlapi.html).

## Use the Unity Netcode networking package

Due to security restrictions, web browsers do not allow direct access to TCP
or UDP sockets. Instead, you can use the Unity Netcode networking package,
which supports Web platform. For more information, refer to the documentation
[About Netcode for GameObjects](https://docs-
multiplayer.unity3d.com/netcode/current/about/) (Unity Multiplayer
Networking).

For more information on web browser networking standards, you might want to
explore the following:

  * [The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455) (Datatracker)
  * [WebRTC: Real-Time Communication in Browsers](https://www.w3.org/TR/webrtc/) (W3)
  * [WebTransport](https://www.w3.org/TR/webtransport/) (W3).

## Limitations of Web networking

There are a few networking features that Web platform doesn’t support.

### No support for .NET networking classes

You can’t use any .NET networking classes within the Web platform because
JavaScript code doesn’t have direct access to internet protocol (IP) sockets
to implement network connectivity. Specifically, Web doesn’t support any .NET
classes within the `System.Net` namespace.

### No support for native socket access

Web platform does not support native socket access because of security
limitations within browsers. Therefore, Web also doesn’t support features like
[UnityEngine.Ping](../ScriptReference/Ping.html) (ICMP).

[](webgl-browser-access-device.html)

Web browser access to device features

[](webassembly-2023.html)

WebAssembly 2023

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

