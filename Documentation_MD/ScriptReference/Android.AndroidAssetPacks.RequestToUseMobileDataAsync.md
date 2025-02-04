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

#
[AndroidAssetPacks](Android.AndroidAssetPacks.html).RequestToUseMobileDataAsync

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

public static
[Android.RequestToUseMobileDataAsyncOperation](Android.RequestToUseMobileDataAsyncOperation.html)
RequestToUseMobileDataAsync();

### Returns

**RequestToUseMobileDataAsyncOperation** Returns an object that represents the
request operation. If you yield this object inside a coroutine, the coroutine
pauses until the operation is complete.

### Description

Requests to use mobile data to download Android asset packs.

If the device is not connected to WiFi, it pauses large Android asset pack
downloads until a WiFi connection is available. If this is the case, the asset
pack has the AndroidAssetPackStatus.WaitingForWifi status. In this situation,
you can call RequestToUseMobileDataAsync to give the end user the option to
download your application's asset packs using mobile data. This method
directly wraps Google's PlayCore plugin API. If the PlayCore plugin is
missing, calling this method throws an InvalidOperationException exception.
Additional resources:
[RequestToUseMobileDataAsyncOperation](Android.RequestToUseMobileDataAsyncOperation.html),
[AndroidAssetPacks.CancelAssetPackDownload](Android.AndroidAssetPacks.CancelAssetPackDownload.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackStateAsync](Android.AndroidAssetPacks.GetAssetPackStateAsync.html).

* * *

## Declaration

public static void
RequestToUseMobileDataAsync(Action<AndroidAssetPackUseMobileDataRequestResult>
callback);

### Parameters

callback | The callback method to get the result. The callback method must have an AndroidAssetPackUseMobileDataRequestResult parameter. This contains the value that indicates the end user's choice. The application raises this callback a single time after the end user submits their decision.  
---|---  
  
### Description

Requests to use mobile data to download Android asset packs.

If the device is not connected to WiFi, it pauses large Android asset pack
downloads until a WiFi connection is available. If this is the case, the asset
pack has the AndroidAssetPackStatus.WaitingForWifi status. In this situation,
you can call RequestToUseMobileDataAsync to give the end user the option to
download your application's asset packs using mobile data. This method
directly wraps Google's PlayCore plugin API. If the PlayCore plugin is
missing, calling this method throws an InvalidOperationException exception.
Additional resources:
[AndroidAssetPackUseMobileDataRequestResult](Android.AndroidAssetPackUseMobileDataRequestResult.html),
[AndroidAssetPacks.CancelAssetPackDownload](Android.AndroidAssetPacks.CancelAssetPackDownload.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackStateAsync](Android.AndroidAssetPacks.GetAssetPackStateAsync.html).

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

