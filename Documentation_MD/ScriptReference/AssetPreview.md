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

# AssetPreview

class in UnityEditor

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

Utility for fetching asset previews by instance ID of assets, See
[AssetPreview.GetAssetPreview](AssetPreview.GetAssetPreview.html). Since
previews are loaded asynchronously methods are provided for requesting if all
previews have been fully loaded, see
[AssetPreview.IsLoadingAssetPreviews](AssetPreview.IsLoadingAssetPreviews.html).
Loaded previews are stored in a cache, the size of the cache can be controlled
by calling [AssetPreview.SetPreviewTextureCacheSize].

### Static Methods

[GetAssetPreview](AssetPreview.GetAssetPreview.html)| Returns a preview
texture for an asset.  
---|---  
[GetMiniThumbnail](AssetPreview.GetMiniThumbnail.html)| Returns the thumbnail
for an object (like the ones you see in the project view).  
[GetMiniTypeThumbnail](AssetPreview.GetMiniTypeThumbnail.html)| Returns the
thumbnail for the type.  
[IsLoadingAssetPreview](AssetPreview.IsLoadingAssetPreview.html)| Loading
previews is asynchronous so it is useful to know if a specific asset preview
is in the process of being loaded so client code e.g can repaint while waiting
for the loading to finish.  
[IsLoadingAssetPreviews](AssetPreview.IsLoadingAssetPreviews.html)| Loading
previews is asynchronous so it is useful to know if any requested previews are
in the process of being loaded so client code e.g can repaint while waiting.  
[SetPreviewTextureCacheSize](AssetPreview.SetPreviewTextureCacheSize.html)|
Set the asset preview cache to a size that can hold all visible previews on
the screen at once.  
  
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

