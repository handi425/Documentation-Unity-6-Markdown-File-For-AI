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

# DownloadHandler

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

Manage and process HTTP response body data received from a remote server.

DownloadHandler objects are helper objects. When attached to a
[UnityWebRequest](Networking.UnityWebRequest.html), they define how to handle
HTTP response body data received from a remote server. Generally, they are
used to buffer, stream and/or process response bodies.  
  
DownloadHandler is a base class. Depending on usage scenario, different
specialized classes are available.
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) provides basic
buffering, while
[DownloadHandlerTexture](Networking.DownloadHandlerTexture.html) and
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html)
provide more efficient solutions for [Texture](Texture.html) and
[AssetBundle](AssetBundle.html) downloads.  
  
For custom use cases, see
[DownloadHandlerScript](Networking.DownloadHandlerScript.html).  
  
Additional resources: [UnityWebRequest](Networking.UnityWebRequest.html),
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html),
[DownloadHandlerTexture](Networking.DownloadHandlerTexture.html),
[DownloadHandlerAudioClip](Networking.DownloadHandlerAudioClip.html),
[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle.html),
[DownloadHandlerScript](Networking.DownloadHandlerScript.html).

### Properties

[data](Networking.DownloadHandler-data.html)| Returns the raw bytes downloaded
from the remote server, or null. (Read Only)  
---|---  
[error](Networking.DownloadHandler-error.html)| Error message describing a
failure that occurred inside the download handler.  
[isDone](Networking.DownloadHandler-isDone.html)| Returns true if this
DownloadHandler has been informed by its parent UnityWebRequest that all data
has been received, and this DownloadHandler has completed any necessary post-
download processing. (Read Only)  
[nativeData](Networking.DownloadHandler-nativeData.html)| Provides direct
access to downloaded data.  
[text](Networking.DownloadHandler-text.html)| Convenience property. Returns
the bytes from data interpreted as a UTF8 string. (Read Only)  
  
### Public Methods

[Dispose](Networking.DownloadHandler.Dispose.html)| Signals that this
DownloadHandler is no longer being used, and should clean up any resources it
is using.  
---|---  
  
### Protected Methods

[CompleteContent](Networking.DownloadHandler.CompleteContent.html)| Callback,
invoked when all data has been received from the remote server.  
---|---  
[GetData](Networking.DownloadHandler.GetData.html)| Callback, invoked when the
data property is accessed.  
[GetNativeData](Networking.DownloadHandler.GetNativeData.html)| Provides
allocation-free access to the downloaded data as a NativeArray.  
[GetProgress](Networking.DownloadHandler.GetProgress.html)| Callback, invoked
when UnityWebRequest.downloadProgress is accessed.  
[GetText](Networking.DownloadHandler.GetText.html)| Callback, invoked when the
text property is accessed.  
[ReceiveContentLengthHeader](Networking.DownloadHandler.ReceiveContentLengthHeader.html)|
Callback, invoked with a Content-Length header is received.  
[ReceiveData](Networking.DownloadHandler.ReceiveData.html)| Callback, invoked
as data is received from the remote server.  
  
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

