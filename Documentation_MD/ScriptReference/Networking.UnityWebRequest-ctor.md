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

# UnityWebRequest Constructor

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

public UnityWebRequest();

## Declaration

public UnityWebRequest(string url);

## Declaration

public UnityWebRequest(Uri uri);

## Declaration

public UnityWebRequest(string url, string method);

## Declaration

public UnityWebRequest(Uri uri, string method);

## Declaration

public UnityWebRequest(string url, string method,
[Networking.DownloadHandler](Networking.DownloadHandler.html) downloadHandler,
[Networking.UploadHandler](Networking.UploadHandler.html) uploadHandler);

## Declaration

public UnityWebRequest(Uri uri, string method,
[Networking.DownloadHandler](Networking.DownloadHandler.html) downloadHandler,
[Networking.UploadHandler](Networking.UploadHandler.html) uploadHandler);

### Parameters

url | The target URL with which this UnityWebRequest will communicate. Also accessible via the [url](Networking.UnityWebRequest-url.html) property.  
---|---  
uri | The target URI to which form data will be transmitted.  
method | HTTP GET, POST, etc. methods.  
downloadHandler | Replies from the server.  
uploadHandler | Upload data to the server.  
  
### Description

Creates a UnityWebRequest with the default options and no attached
[DownloadHandler](Networking.DownloadHandler.html) or
[UploadHandler](Networking.UploadHandler.html). Default method is `GET`.

The raw constructor is useful for use cases which require detailed custom
configuration of a [UnityWebRequest](Networking.UnityWebRequest.html). Most
use cases will require the attachment of a
[DownloadHandler](Networking.DownloadHandler.html), an
[UploadHandler](Networking.UploadHandler.html) or both in order to function
propertly.  
  
Additional resources: [Get](Networking.UnityWebRequest.Get.html),
[GetTexture](Networking.UnityWebRequest.GetTexture.html),
[GetAudioClip](Networking.UnityWebRequest.GetAudioClip.html),
[GetAssetBundle](Networking.UnityWebRequest.GetAssetBundle.html),
[Head](Networking.UnityWebRequest.Head.html),
[Post](Networking.UnityWebRequest.Post.html),
[Put](Networking.UnityWebRequest.Put.html),
[Delete](Networking.UnityWebRequest.Delete.html).

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

