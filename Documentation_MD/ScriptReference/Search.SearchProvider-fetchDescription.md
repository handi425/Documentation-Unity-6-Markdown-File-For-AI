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

#  [SearchProvider](Search.SearchProvider.html).fetchDescription

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

public Func<SearchItem,SearchContext,string> fetchDescription;

### Description

Handler to provide an asynchronous description for an item. Is called when the
item is about to be displayed. Allows a plugin provider to only fetch long
descriptions when they are needed.

    
    
    [SearchItemProvider]
    internal static [SearchProvider](Search.SearchProvider.html) CreateProvider()
    {
        return new [SearchProvider](Search.SearchProvider.html)("example_tree", "Trees")
        {
            filterId = "tree:",
            priority = 99999, // Put example provider at a low priority
            showDetailsOptions = [ShowDetailsOptions.Inspector](Search.ShowDetailsOptions.Inspector.html) | [ShowDetailsOptions.Actions](Search.ShowDetailsOptions.Actions.html),
            fetchItems = (context, items, provider) => FetchItems(context, provider),
            fetchThumbnail = (item, context) => [AssetDatabase.GetCachedIcon](AssetDatabase.GetCachedIcon.html)(item.id) as [Texture2D](Texture2D.html),
            fetchPreview = (item, context, size, options) => [AssetDatabase.GetCachedIcon](AssetDatabase.GetCachedIcon.html)(item.id) as [Texture2D](Texture2D.html),
            fetchLabel = (item, context) => [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(item.id).name,
            fetchDescription = (item, context) => [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(item.id).name,
            toObject = (item, type) => [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(item.id),
            trackSelection = TrackSelection,
            startDrag = StartDrag
        };
    }
    
    private static IEnumerable<[SearchItem](Search.SearchItem.html)> FetchItems([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
    {
        if (context.empty)
            yield break;
    
        // Yield items asynchronously which is the recommended way.
        foreach (var guid in [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:Prefab tree " + context.searchQuery))
            yield return provider.CreateItem(context, [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid), null, null, null, null);
    }
    
    private static void TrackSelection([SearchItem](Search.SearchItem.html) searchItem, [SearchContext](Search.SearchContext.html) searchContext)
    {
        [EditorGUIUtility.PingObject](EditorGUIUtility.PingObject.html)([AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(searchItem.id));
    }
    
    private static void StartDrag([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
    {
        if (context.selection.Count > 1)
        {
            var selectedObjects = context.selection.Select(i => [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(i.id));
            var paths = context.selection.Select(i => i.id).ToArray();
            StartDrag(selectedObjects.ToArray(), paths, item.GetLabel(context, true));
        }
        else
            StartDrag(new[] { [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(item.id) }, new[] { item.id }, item.GetLabel(context, true));
    }
    
    public static void StartDrag(UnityEngine.Object[] objects, string[] paths, string label = null)
    {
        if (paths == null || paths.Length == 0)
            return;
        [DragAndDrop.PrepareStartDrag](DragAndDrop.PrepareStartDrag.html)();
        [DragAndDrop.objectReferences](DragAndDrop-objectReferences.html) = objects;
        [DragAndDrop.paths](DragAndDrop-paths.html) = paths;
        [DragAndDrop.StartDrag](DragAndDrop.StartDrag.html)(label);
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

