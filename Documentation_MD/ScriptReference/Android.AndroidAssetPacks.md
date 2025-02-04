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

# AndroidAssetPacks

class in UnityEngine.Android

/

Implemented
in:[UnityEngine.AndroidJNIModule](UnityEngine.AndroidJNIModule.html)

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

Provides methods for handling Android asset packs.

Methods in this class are either direct wrappers of java APIs in Google's
PlayCore plugin, or depend on values that the PlayCore API returns. Therefore
to use it, the gradle project must include the "com.google.android.play:core"
dependency. If your project contains custom asset packs or you enable **Split
Application Binary** in Player Settings, Unity automatically adds this
dependency to the unityLibrary submodule's build.gradle file. If the PlayCore
plugin is missing, calling any wrapper throws an InvalidOperationException
exception. Note that PlayCore APIs only work with fast-follow and on-demand
delivery type asset packs, therefore methods in this class have the same
limitation.

### Static Properties

[coreUnityAssetPacksDownloaded](Android.AndroidAssetPacks-
coreUnityAssetPacksDownloaded.html)| Checks if all core Unity asset packs are
downloaded.  
---|---  
  
### Static Methods

[CancelAssetPackDownload](Android.AndroidAssetPacks.CancelAssetPackDownload.html)|
Cancels Android asset pack downloads.  
---|---  
[DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html)|
Downloads Android asset packs.  
[GetAssetPackPath](Android.AndroidAssetPacks.GetAssetPackPath.html)| Gets the
full path to the location where the device stores the assets for the Android
asset pack.  
[GetAssetPackStateAsync](Android.AndroidAssetPacks.GetAssetPackStateAsync.html)|
Queries the state of Android asset packs.  
[GetCoreUnityAssetPackNames](Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html)|
Gets the name of every core Unity asset pack built for this application that
use either the fast-follow or on-demand delivery type.  
[RemoveAssetPack](Android.AndroidAssetPacks.RemoveAssetPack.html)| Removes
Android asset pack.  
[RequestToUseMobileDataAsync](Android.AndroidAssetPacks.RequestToUseMobileDataAsync.html)|
Requests to use mobile data to download Android asset packs.  
  
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

