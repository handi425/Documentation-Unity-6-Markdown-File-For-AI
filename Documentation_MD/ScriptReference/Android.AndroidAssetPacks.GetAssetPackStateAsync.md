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

#  [AndroidAssetPacks](Android.AndroidAssetPacks.html).GetAssetPackStateAsync

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
[Android.GetAssetPackStateAsyncOperation](Android.GetAssetPackStateAsyncOperation.html)
GetAssetPackStateAsync(string[] assetPackNames);

### Parameters

assetPackNames | The array of names of the Android asset packs to query the state of.  
---|---  
  
### Returns

**GetAssetPackStateAsyncOperation** Returns an object that represents the
query operation. If you yield this object inside a coroutine, the coroutine
pauses until the operation is complete.

### Description

Queries the state of Android asset packs.

This method directly wraps Google's PlayCore plugin API. If the PlayCore
plugin is missing, calling this method throws an InvalidOperationException
exception. Additional resources:
[GetAssetPackStateAsyncOperation](Android.GetAssetPackStateAsyncOperation.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackPath](Android.AndroidAssetPacks.GetAssetPackPath.html).

* * *

## Declaration

public static void GetAssetPackStateAsync(string[] assetPackNames,
Action<ulong,AndroidAssetPackState[]> callback);

### Parameters

assetPackNames | The array of names of the Android asset packs to query the state of.  
---|---  
callback | The callback method to get the result. Unity raises this callback once when the query is complete and the callback receives the state of queried Android asset packs. The callback method must have two parameters: 

  * A ulong type parameter which indicates the total size of the queried asset packs.
  * An array of AndroidAssetPackState which contains the state of each queried asset pack.

  
  
### Description

Queries the state of Android asset packs.

This method directly wraps Google's PlayCore plugin API. If the PlayCore
plugin is missing, calling this method throws an InvalidOperationException
exception. Additional resources:
[AndroidAssetPackState](Android.AndroidAssetPackState.html),
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html),
[AndroidAssetPacks.GetAssetPackPath](Android.AndroidAssetPacks.GetAssetPackPath.html).

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

