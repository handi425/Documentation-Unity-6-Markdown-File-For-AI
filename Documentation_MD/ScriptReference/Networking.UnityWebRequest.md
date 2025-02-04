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

# UnityWebRequest

class in UnityEngine.Networking

/

Implemented
in:[UnityEngine.UnityWebRequestModule](UnityEngine.UnityWebRequestModule.html)

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

### Description

Provides methods to communicate with web servers.

`UnityWebRequest` handles the flow of HTTP communication with web servers. To
download and upload data, use
[DownloadHandler](Networking.DownloadHandler.html) and
[UploadHandler](Networking.UploadHandler.html) respectively.  
  
`UnityWebRequest` includes static utility functions that return
`UnityWebRequest` instances configured for common use cases. For example:

  * [UnityWebRequest.Get](Networking.UnityWebRequest.Get.html)
  * [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)
  * [UnityWebRequest.Put](Networking.UnityWebRequest.Put.html)

To send a web request from a `UnityWebRequest` instance, call
[UnityWebRequest.SendWebRequest](Networking.UnityWebRequest.SendWebRequest.html).
After the `UnityWebRequest` begins to communicate with a remote server, you
can't change any of the properties in that `UnityWebRequest` instance. HTTPS
is supported, server certificate is validated against the root certificate
store available on the system the app runs on. Validation can be disabled (for
example for development server using self-signed certificate) or changed to a
custom handling by assigning
[UnityWebRequest.certificateHandler](Networking.UnityWebRequest-
certificateHandler.html) property.  
  
Depending on the platform your application runs on, `UnityWebRequest` either
sets the [User-Agent header](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Headers/User-Agent) itself or leaves it for the operating
system to set. `UnityWebRequest` sets the `User-Agent` header for all
platforms except iOS and WebGL.  
  
**Note** : From Unity 2019.2, `UnityWebRequest` sets the `User-Agent` header
for Android devices. In earlier releases, the operating system set the `User-
Agent` header.  
  
**Note** : If the device that the application runs on uses proxy settings,
`UnityWebRequest` applies the proxy settings after the application sends the
request.

### Static Properties

[kHttpVerbCREATE](Networking.UnityWebRequest-kHttpVerbCREATE.html)| The string
"CREATE", commonly used as the verb for an HTTP CREATE request.  
---|---  
[kHttpVerbDELETE](Networking.UnityWebRequest-kHttpVerbDELETE.html)| The string
"DELETE", commonly used as the verb for an HTTP DELETE request.  
[kHttpVerbGET](Networking.UnityWebRequest-kHttpVerbGET.html)| The string
"GET", commonly used as the verb for an HTTP GET request.  
[kHttpVerbHEAD](Networking.UnityWebRequest-kHttpVerbHEAD.html)| The string
"HEAD", commonly used as the verb for an HTTP HEAD request.  
[kHttpVerbPOST](Networking.UnityWebRequest-kHttpVerbPOST.html)| The string
"POST", commonly used as the verb for an HTTP POST request.  
[kHttpVerbPUT](Networking.UnityWebRequest-kHttpVerbPUT.html)| The string
"PUT", commonly used as the verb for an HTTP PUT request.  
  
### Properties

[certificateHandler](Networking.UnityWebRequest-certificateHandler.html)|
Holds a reference to a CertificateHandler object, which manages certificate
validation for this UnityWebRequest.  
---|---  
[disposeCertificateHandlerOnDispose](Networking.UnityWebRequest-
disposeCertificateHandlerOnDispose.html)| If true, any CertificateHandler
attached to this UnityWebRequest will have CertificateHandler.Dispose called
automatically when UnityWebRequest.Dispose is called.  
[disposeDownloadHandlerOnDispose](Networking.UnityWebRequest-
disposeDownloadHandlerOnDispose.html)| If true, any DownloadHandler attached
to this UnityWebRequest will have DownloadHandler.Dispose called automatically
when UnityWebRequest.Dispose is called.  
[disposeUploadHandlerOnDispose](Networking.UnityWebRequest-
disposeUploadHandlerOnDispose.html)| If true, any UploadHandler attached to
this UnityWebRequest will have UploadHandler.Dispose called automatically when
UnityWebRequest.Dispose is called.  
[downloadedBytes](Networking.UnityWebRequest-downloadedBytes.html)| Returns
the number of bytes of body data the system has downloaded from the remote
server. (Read Only)  
[downloadHandler](Networking.UnityWebRequest-downloadHandler.html)| Holds a
reference to a DownloadHandler object, which manages body data received from
the remote server by this UnityWebRequest.  
[downloadProgress](Networking.UnityWebRequest-downloadProgress.html)| Returns
a floating-point value between 0.0 and 1.0, indicating the progress of
downloading body data from the server. (Read Only)  
[error](Networking.UnityWebRequest-error.html)| A human-readable string
describing any system errors encountered by this UnityWebRequest object while
handling HTTP requests or responses. The default value is null. (Read Only)  
[isDone](Networking.UnityWebRequest-isDone.html)| Returns true after the
UnityWebRequest has finished communicating with the remote server. (Read Only)  
[isModifiable](Networking.UnityWebRequest-isModifiable.html)| Returns true
while a UnityWebRequest’s configuration properties can be altered. (Read Only)  
[method](Networking.UnityWebRequest-method.html)| Defines the HTTP verb used
by this UnityWebRequest, such as GET or POST.  
[redirectLimit](Networking.UnityWebRequest-redirectLimit.html)| Indicates the
number of redirects that this UnityWebRequest follows before halting with a
Redirect Limit Exceeded system error.  
[responseCode](Networking.UnityWebRequest-responseCode.html)| The numeric HTTP
response code returned by the server, such as 200, 404 or 500. (Read Only)  
[result](Networking.UnityWebRequest-result.html)| The result of this
UnityWebRequest.  
[timeout](Networking.UnityWebRequest-timeout.html)| Sets UnityWebRequest to
attempt to abort after the number of seconds in timeout have passed.  
[uploadedBytes](Networking.UnityWebRequest-uploadedBytes.html)| Returns the
number of bytes of body data the system has uploaded to the remote server.
(Read Only)  
[uploadHandler](Networking.UnityWebRequest-uploadHandler.html)| Holds a
reference to the UploadHandler object which manages body data to be uploaded
to the remote server.  
[uploadProgress](Networking.UnityWebRequest-uploadProgress.html)| Returns a
floating-point value between 0.0 and 1.0, indicating the progress of uploading
body data to the server.  
[uri](Networking.UnityWebRequest-uri.html)| Defines the target URI for the
UnityWebRequest to communicate with.  
[url](Networking.UnityWebRequest-url.html)| Defines the target URL for the
UnityWebRequest to communicate with.  
[useHttpContinue](Networking.UnityWebRequest-useHttpContinue.html)| Determines
whether this UnityWebRequest will include Expect: 100-Continue in its outgoing
request headers. (Default: true).  
  
### Constructors

[UnityWebRequest](Networking.UnityWebRequest-ctor.html)| Creates a
UnityWebRequest with the default options and no attached DownloadHandler or
UploadHandler. Default method is GET.  
---|---  
  
### Public Methods

[Abort](Networking.UnityWebRequest.Abort.html)| If in progress, halts the
UnityWebRequest as soon as possible.  
---|---  
[Dispose](Networking.UnityWebRequest.Dispose.html)| Signals that this
UnityWebRequest is no longer being used, and should clean up any resources it
is using.  
[GetRequestHeader](Networking.UnityWebRequest.GetRequestHeader.html)|
Retrieves the value of a custom request header.  
[GetResponseHeader](Networking.UnityWebRequest.GetResponseHeader.html)|
Retrieves the value of a response header from the latest HTTP response
received.  
[GetResponseHeaders](Networking.UnityWebRequest.GetResponseHeaders.html)|
Retrieves a dictionary containing all the response headers received by this
UnityWebRequest in the latest HTTP response.  
[SendWebRequest](Networking.UnityWebRequest.SendWebRequest.html)| Begin
communicating with the remote server.  
[SetRequestHeader](Networking.UnityWebRequest.SetRequestHeader.html)| Set a
HTTP request header to a custom value.  
  
### Static Methods

[ClearCookieCache](Networking.UnityWebRequest.ClearCookieCache.html)| Clears
stored cookies from the cache.  
---|---  
[Delete](Networking.UnityWebRequest.Delete.html)| Creates a UnityWebRequest
configured for HTTP DELETE.  
[EscapeURL](Networking.UnityWebRequest.EscapeURL.html)| Escapes characters in
a string to ensure they are URL-friendly.  
[GenerateBoundary](Networking.UnityWebRequest.GenerateBoundary.html)| Generate
a random 40-byte array for use as a multipart form boundary.  
[Get](Networking.UnityWebRequest.Get.html)| Create a UnityWebRequest for HTTP
GET.  
[Head](Networking.UnityWebRequest.Head.html)| Creates a UnityWebRequest
configured to send a HTTP HEAD request.  
[Post](Networking.UnityWebRequest.Post.html)| Creates a UnityWebRequest
configured to send form data to a server via HTTP POST.  
[PostWwwForm](Networking.UnityWebRequest.PostWwwForm.html)| Creates a
UnityWebRequest configured to send form data to a server via HTTP POST.  
[Put](Networking.UnityWebRequest.Put.html)| Creates a UnityWebRequest
configured to upload raw data to a remote server via HTTP PUT.  
[SerializeFormSections](Networking.UnityWebRequest.SerializeFormSections.html)|
Converts a List of IMultipartFormSection objects into a byte array containing
raw multipart form data.  
[SerializeSimpleForm](Networking.UnityWebRequest.SerializeSimpleForm.html)|
Serialize a dictionary of strings into a byte array containing URL-encoded
UTF8 characters.  
[UnEscapeURL](Networking.UnityWebRequest.UnEscapeURL.html)| Converts URL-
friendly escape sequences back to normal text.  
  
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

