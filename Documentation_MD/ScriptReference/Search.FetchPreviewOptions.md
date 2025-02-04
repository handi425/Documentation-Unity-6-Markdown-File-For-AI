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

# FetchPreviewOptions

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

Options for the search provider on how the preview should be fetched.

These options are used by the
[SearchProvider.fetchPreview](Search.SearchProvider-fetchPreview.html)
functor.

    
    
    static [Texture2D](Texture2D.html) FetchPreview([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context, [Vector2](Vector2.html) size, [FetchPreviewOptions](Search.FetchPreviewOptions.html) options)
    {
        var obj = ObjectFromItem(item);
        if (obj == null)
            return item.thumbnail;
    
        var assetPath = [SearchUtils.GetHierarchyAssetPath](Search.SearchUtils.GetHierarchyAssetPath.html)(obj, true);
        if (string.IsNullOrEmpty(assetPath))
            return item.thumbnail;
    
        if (options.HasFlag([FetchPreviewOptions.Large](Search.FetchPreviewOptions.Large.html)))
        {
            if ([AssetPreview.GetAssetPreview](AssetPreview.GetAssetPreview.html)(obj) is [Texture2D](Texture2D.html) tex)
                return tex;
        }
        return GetAssetPreviewFromPath(assetPath, size, options);
    }
    

### Properties

[None](Search.FetchPreviewOptions.None.html)| No options are defined.  
---|---  
[Preview2D](Search.FetchPreviewOptions.Preview2D.html)| Indicates that the
search provider should generate a 2D preview.  
[Preview3D](Search.FetchPreviewOptions.Preview3D.html)| Indicates that the
search provider should generate a 3D preview.  
[Normal](Search.FetchPreviewOptions.Normal.html)| Indicates that the preview
size should be around 128x128.  
[Large](Search.FetchPreviewOptions.Large.html)| Indicates that the preview
resolution should be higher than 256x256.  
  
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

