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
[SearchContextAttribute](Search.SearchContextAttribute.html).instantiableProviders

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

public Type[] instantiableProviders;

### Description

Search provider concrete types that will be instantiated and assigned to the
Object Picker search context.

    
    
    [[SearchContext](Search.SearchContext.html)("my search", new[] { typeof(MyTextureProvider) })] public [Texture2D](Texture2D.html) mySpecialTexture2D;
    
    class MyTextureProvider : [SearchProvider](Search.SearchProvider.html)
    {
        static string ProviderId = "myTexture";
    
        public MyTextureProvider()
            : base(ProviderId)
        {
            fetchItems = (context, items, provider) => SearchItems(context, provider);
            fetchLabel = (item, context) =>
            {
                var assetPath = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)((string)item.data);
                return GetNameFromPath(assetPath);
            };
            fetchThumbnail = (item, context) =>
            {
                var obj = toObject(item, typeof([Texture2D](Texture2D.html)));
                return [AssetPreview.GetAssetPreview](AssetPreview.GetAssetPreview.html)(obj);
            };
            toObject = (item, type) =>
            {
                var assetPath = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)((string)item.data);
                return [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)(assetPath, type);
            };
        }
    
        static IEnumerator SearchItems([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
        {
            foreach (var texture2DGuid in GetMyTextures())
            {
                yield return provider.CreateItem(context, texture2DGuid, texture2DGuid.GetHashCode(), null, null, null, texture2DGuid);
            }
        }
    
        static IEnumerable<string> GetMyTextures()
        {
            return [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:texture2d");
        }
    
        static string GetNameFromPath(string path)
        {
            var lastSep = path.LastIndexOf('/');
            if (lastSep == -1)
                return path;
    
            return path.Substring(lastSep + 1);
        }
    }
    

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

