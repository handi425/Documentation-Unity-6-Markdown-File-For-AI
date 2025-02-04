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

# AndroidAssetPackError

enumeration

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

Values that indicate the type of Android asset pack error when the status is
either AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown.

Unity always returns the error value and the status together in
AndroidAssetPackInfo or AndroidAssetPackState objects. Unity returns these
objects via callback methods after you call either
AndroidAssetPacks.DownloadAssetPackAsync or
AndroidAssetPacks.GetAssetPackStateAsync. When the status value is
AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown, the error
value indicates the cause of the failure. For any other status value, the
error value should always be AndroidAssetPackError.NoError. This enum directly
wraps the
[AssetPackErrorCode](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackErrorCode)
values in the PlayCore API. Additional resources:
[AndroidAssetPackInfo](Android.AndroidAssetPackInfo.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackStateAsync](Android.AndroidAssetPacks.GetAssetPackStateAsync.html),
[AndroidAssetPackState](Android.AndroidAssetPackState.html).

### Properties

[NoError](Android.AndroidAssetPackError.NoError.html)| Indicates that there is
no error.  
---|---  
[AppUnavailable](Android.AndroidAssetPackError.AppUnavailable.html)| Indicates
that this application is unavailable in the Google's Play Store.  
[PackUnavailable](Android.AndroidAssetPackError.PackUnavailable.html)|
Indicates that the requested Android asset pack is not available in the Google
Play Store.  
[InvalidRequest](Android.AndroidAssetPackError.InvalidRequest.html)| Indicates
that the request was invalid.  
[DownloadNotFound](Android.AndroidAssetPackError.DownloadNotFound.html)|
Indicates that the requested download is not found.  
[ApiNotAvailable](Android.AndroidAssetPackError.ApiNotAvailable.html)|
Indicates that the Asset Delivery API is not available.  
[NetworkError](Android.AndroidAssetPackError.NetworkError.html)| Indicates
that the Android asset pack is not accessible because there was an error
related to the network connection.  
[AccessDenied](Android.AndroidAssetPackError.AccessDenied.html)| Indicates
that the application does not have permission to download asset packs under
the current device circumstances.  
[InsufficientStorage](Android.AndroidAssetPackError.InsufficientStorage.html)|
Indicates that there is not enough storage space on the device to download the
Android asset pack.  
[PlayStoreNotFound](Android.AndroidAssetPackError.PlayStoreNotFound.html)|
Indicates that the device does not have the Play Store application installed
or has an unofficial version.  
[NetworkUnrestricted](Android.AndroidAssetPackError.NetworkUnrestricted.html)|
Indicates that the app requested to use mobile data while there were no
Android asset packs waiting for WiFi.  
[AppNotOwned](Android.AndroidAssetPackError.AppNotOwned.html)| Indicates that
the end user does not own the application on the device.  
[InternalError](Android.AndroidAssetPackError.InternalError.html)| Indicates
that unknown error occured while downloading an asset pack.  
  
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

