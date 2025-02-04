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

# DownloadAssetPackAsyncOperation

class in UnityEngine.Android

/

Inherits from:[CustomYieldInstruction](CustomYieldInstruction.html)

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

Represents an asynchronous Android asset pack download operation.
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html)
returns an instance of this class.

You can yield until the operation completes, or manually check whether it's
done using isDone or keepWaiting properties. You can also track the progress
of the operation using the progress property. Additional resources:
[AndroidAssetPacks.DownloadAssetPackAsync](Android.AndroidAssetPacks.DownloadAssetPackAsync.html).

### Properties

[downloadedAssetPacks](Android.DownloadAssetPackAsyncOperation-
downloadedAssetPacks.html)| Gets the names of Android asset packs downloaded
by this operation.  
---|---  
[downloadFailedAssetPacks](Android.DownloadAssetPackAsyncOperation-
downloadFailedAssetPacks.html)| Gets the names of Android asset packs that
failed to download.  
[isDone](Android.DownloadAssetPackAsyncOperation-isDone.html)| Checks if the
operation is finished.  
[keepWaiting](Android.DownloadAssetPackAsyncOperation-keepWaiting.html)|
Checks if the operation is still running.  
[progress](Android.DownloadAssetPackAsyncOperation-progress.html)| Gets the
progress of the operation.  
  
### Inherited Members

### Properties

[keepWaiting](CustomYieldInstruction-keepWaiting.html)| Indicates if coroutine
should be kept suspended.  
---|---  
  
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

