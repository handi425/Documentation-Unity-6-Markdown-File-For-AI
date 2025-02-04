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

# DownloadHandlerAssetBundle

class in UnityEngine.Networking

/

Inherits from:[Networking.DownloadHandler](Networking.DownloadHandler.html)

/

Implemented
in:[UnityEngine.UnityWebRequestAssetBundleModule](UnityEngine.UnityWebRequestAssetBundleModule.html)

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

A [DownloadHandler](Networking.DownloadHandler.html) subclass specialized for
downloading [AssetBundle](AssetBundle.html)s.

This subclass streams downloaded data into Unity's asset bundle decompression
and decoding system on worker threads, providing efficient downloading and
processing for [AssetBundle](AssetBundle.html) objects. Additional resources:
[UnityWebRequestAssetBundle](Networking.UnityWebRequestAssetBundle.html)

### Properties

[assetBundle](Networking.DownloadHandlerAssetBundle-assetBundle.html)| Returns
the downloaded AssetBundle, or null. (Read Only)  
---|---  
[autoLoadAssetBundle](Networking.DownloadHandlerAssetBundle-
autoLoadAssetBundle.html)| If true, the AssetBundle will be loaded as part of
the UnityWebRequest process. If false, the AssetBundle will be loaded on
demand when accessing the DownloadHandlerAssetBundle.assetBundle property.  
[isDownloadComplete](Networking.DownloadHandlerAssetBundle-
isDownloadComplete.html)| Returns true if the data downloading portion of the
operation is complete.  
  
### Constructors

[DownloadHandlerAssetBundle](Networking.DownloadHandlerAssetBundle-ctor.html)|
Standard constructor for non-cached asset bundles.  
---|---  
  
### Protected Methods

[GetData](Networking.DownloadHandlerAssetBundle.GetData.html)| Not
implemented. Throws NotSupportedException.  
---|---  
[GetText](Networking.DownloadHandlerAssetBundle.GetText.html)| Not
implemented. Throws NotSupportedException.  
  
### Static Methods

[GetContent](Networking.DownloadHandlerAssetBundle.GetContent.html)| Returns
the downloaded AssetBundle, or null.  
---|---  
  
### Inherited Members

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
[GetNativeData](Networking.DownloadHandler.GetNativeData.html)| Provides
allocation-free access to the downloaded data as a NativeArray.  
[GetProgress](Networking.DownloadHandler.GetProgress.html)| Callback, invoked
when UnityWebRequest.downloadProgress is accessed.  
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

