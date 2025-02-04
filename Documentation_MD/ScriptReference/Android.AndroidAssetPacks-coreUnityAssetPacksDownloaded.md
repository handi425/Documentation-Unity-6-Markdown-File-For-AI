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
[AndroidAssetPacks](Android.AndroidAssetPacks.html).coreUnityAssetPacksDownloaded

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

public static bool coreUnityAssetPacksDownloaded;

### Description

Checks if all core Unity asset packs are downloaded.

Returns `true` if all core Unity asset packs are downloaded. Otherwise,
returns `false`. This also returns `false` if the PlayCore plugin is missing.
Core Unity asset packs are asset packs that Unity created automatically when
it built the Android app bundle. Unity only creates core asset packs if you
enable **Split Application Binary** in Player Settings or if you use [Texture
Compression Targeting](../Manual/android-distribution-google-
play.html#texture-compression-targeting). To safely access assets in the
streaming assets path, resources directory, or to safely load any other scenes
than the first, only access them after this method returns `true`. When the
property returns `false`, you can check the download status of the core Unity
asset packs. To do this, call GetCoreUnityAssetPackNames to get the array of
core Unity asset pack names, then call GetAssetPackStatesAsync and pass in the
names array. If the state indicates that the device has not yet downloaded an
asset pack, or the device is not downloading an asset pack, call
DownloadAssetPackAsync passing in the asset pack's name. If there are asset
packs that have the WaitingForWifi status, you can ask the user to allow the
application to download them using mobile data. To do this, call
RequestToUseMobileDataAsync. If this property returns `false` and
GetCoreUnityAssetPackNames returns an empty array, then your application does
not have the PlayCore plugin. Unity should automatically add it as a
dependency in unityLibrary's build.gradle file when it builds the Android
application with asset packs. Read-only. Additional resources:
[AndroidAssetPacks.GetCoreUnityAssetPackNames](Android.AndroidAssetPacks.GetCoreUnityAssetPackNames.html).

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

