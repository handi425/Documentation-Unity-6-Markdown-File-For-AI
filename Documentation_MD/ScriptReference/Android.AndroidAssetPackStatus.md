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

# AndroidAssetPackStatus

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

Values that indicate the status of an Android asset pack.

Unity always returns the status value and the error together in
AndroidAssetPackInfo or AndroidAssetPackState objects. Unity returns these
objects via callback methods after you call either
AndroidAssetPacks.DownloadAssetPackAsync or
AndroidAssetPacks.GetAssetPackStateAsync. When the status value is
AndroidAssetPackStatus.Failed or AndroidAssetPackStatus.Unknown, the error
value indicates the cause of the failure. For any other status value, the
error value should always be AndroidAssetPackError.NoError. This enum directly
wraps the
[AssetPackStatus](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus)
values in the PlayCore API. Additional resources:
[AndroidAssetPackInfo](Android.AndroidAssetPackInfo.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackStateAsync](Android.AndroidAssetPacks.GetAssetPackStateAsync.html),
[AndroidAssetPackState](Android.AndroidAssetPackState.html).

### Properties

[Unknown](Android.AndroidAssetPackStatus.Unknown.html)| Indicates that the
Android asset pack is not available for the application.  
---|---  
[Pending](Android.AndroidAssetPackStatus.Pending.html)| Indicates that the
Android asset pack status should soon change.  
[Downloading](Android.AndroidAssetPackStatus.Downloading.html)| Indicates that
the device is downloading the Android asset pack.  
[Transferring](Android.AndroidAssetPackStatus.Transferring.html)| Indicates
that the device has downloaded the Android asset pack and is unpacking the
asset pack to its final location.  
[Completed](Android.AndroidAssetPackStatus.Completed.html)| Indicates that the
device has downloaded the Android asset pack and the asset pack is available
to the application.  
[Failed](Android.AndroidAssetPackStatus.Failed.html)| Indicates that the
device failed to download the Android asset pack.  
[Canceled](Android.AndroidAssetPackStatus.Canceled.html)| Indicates that the
Android asset pack download is canceled.  
[WaitingForWifi](Android.AndroidAssetPackStatus.WaitingForWifi.html)|
Indicates that the device has paused the Android asset pack download until it
connects to the WiFi network.  
[NotInstalled](Android.AndroidAssetPackStatus.NotInstalled.html)| Indicates
that the Android asset pack is not installed.  
  
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

