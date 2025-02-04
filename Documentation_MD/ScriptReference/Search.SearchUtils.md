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

# SearchUtils

class in UnityEditor.Search

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

Provides various utility functions that are used by
[SearchProvider](Search.SearchProvider.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Globalization;
    using System.Linq;
    using UnityEditor.Search;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    
    /// <summary>
    /// Custom provider showing how to implement a custom Query Engine supporting a Spatial search filter.
    /// </summary>
    public static class SpatialProvider
    {
        internal static string type = "spl";
        internal static string displayName = "Spatial";
    
        static [GameObject](GameObject.html)[] s_GameObjects;
        static [QueryEngine](Search.QueryEngine.html)<[GameObject](GameObject.html)> s_QueryEngine;
    
        [SearchItemProvider]
        internal static [SearchProvider](Search.SearchProvider.html) CreateProvider()
        {
            return new [SearchProvider](Search.SearchProvider.html)(type, displayName)
            {
                active = false,
                filterId = "spl:",
                onEnable = OnEnable,
                fetchItems = (context, items, provider) => SearchItems(context, provider),
                fetchLabel = FetchLabel,
                fetchDescription = FetchDescription,
                fetchThumbnail = FetchThumbnail,
                fetchPreview = FetchPreview,
                trackSelection = TrackSelection,
                isExplicitProvider = false,
            };
        }
    
        static void OnEnable()
        {
            s_GameObjects = [SearchUtils.FetchGameObjects](Search.SearchUtils.FetchGameObjects.html)().ToArray();
            s_QueryEngine = new [QueryEngine](Search.QueryEngine.html)<[GameObject](GameObject.html)>();
    
            // Id supports all operators
            s_QueryEngine.AddFilter("id", go => go.GetInstanceID());
            // Name supports only :, = and !=
            s_QueryEngine.AddFilter("n", go => go.name, new[] {":", "=", "!="});
    
            // Add distance filtering. Does not support :.
            s_QueryEngine.AddFilter("dist", DistanceHandler, DistanceParamHandler, new[] {"=", "!=", "<", ">", "<=", ">="});
        }
    
    
        static IEnumerator SearchItems([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
        {
            var query = s_QueryEngine.ParseQuery(context.searchQuery);
            if (!query.valid)
                yield break;
    
            var filteredObjects = query.Apply(s_GameObjects);
            foreach (var filteredObject in filteredObjects)
            {
                yield return provider.CreateItem(filteredObject.GetInstanceID().ToString(), null, null, null, filteredObject.GetInstanceID());
            }
        }
    
    
        static string FetchLabel([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
        {
            if (item.label != null)
                return item.label;
    
            var go = ObjectFromItem(item);
            if (!go)
                return item.id;
    
            var transformPath = [SearchUtils.GetTransformPath](Search.SearchUtils.GetTransformPath.html)(go.transform);
            var components = go.GetComponents<[Component](Component.html)>();
            if (components.Length > 2 && components[1] && components[components.Length - 1])
                item.label = $"{transformPath} ({components[1].GetType().Name}..{components[components.Length - 1].GetType().Name})";
            else if (components.Length > 1 && components[1])
                item.label = $"{transformPath} ({components[1].GetType().Name})";
            else
                item.label = $"{transformPath} ({item.id})";
    
            return item.label;
        }
    
    
        static string FetchDescription([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
        {
            var go = ObjectFromItem(item);
            return (item.description = [SearchUtils.GetHierarchyPath](Search.SearchUtils.GetHierarchyPath.html)(go));
        }
    
    
        static [Texture2D](Texture2D.html) FetchThumbnail([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
        {
            var obj = ObjectFromItem(item);
            if (obj == null)
                return null;
    
            return item.thumbnail = GetThumbnailForGameObject(obj);
        }
    
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
    
    
        static void TrackSelection([SearchItem](Search.SearchItem.html) item, [SearchContext](Search.SearchContext.html) context)
        {
            var obj = ObjectFromItem(item);
            if (obj)
                [Selection.activeGameObject](Selection-activeGameObject.html) = obj;
            if ([SceneView.lastActiveSceneView](SceneView-lastActiveSceneView.html) != null)
                SceneView.lastActiveSceneView.FrameSelected();
        }
    
        static float DistanceHandler([GameObject](GameObject.html) go, [Vector3](Vector3.html) p)
        {
            return (go.transform.position - p).magnitude;
        }
    
        static [Vector3](Vector3.html) DistanceParamHandler(string param)
        {
            if (param == "selection")
            {
                var centerPoint = Selection.gameObjects.Select(go => go.transform.position).Aggregate((v1, v2) => v1 + v2);
                centerPoint /= Selection.gameObjects.Length;
                return centerPoint;
            }
    
            if (param.StartsWith("[") && param.EndsWith("]"))
            {
                param = param.Trim('[', ']');
                var vectorTokens = param.Split(',');
                var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
                while (vectorValues.Count < 3)
                    vectorValues.Add(0f);
                return new [Vector3](Vector3.html)(vectorValues[0], vectorValues[1], vectorValues[2]);
            }
    
            var obj = s_GameObjects.FirstOrDefault(go => go.name == param);
            if (!obj)
                return [Vector3.zero](Vector3-zero.html);
            return obj.transform.position;
        }
    
        static [GameObject](GameObject.html) ObjectFromItem([SearchItem](Search.SearchItem.html) item)
        {
            var instanceID = Convert.ToInt32(item.id);
            var obj = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(instanceID) as [GameObject](GameObject.html);
            return obj;
        }
    
        static [Texture2D](Texture2D.html) GetThumbnailForGameObject([GameObject](GameObject.html) go)
        {
            var thumbnail = [PrefabUtility.GetIconForGameObject](PrefabUtility.GetIconForGameObject.html)(go);
            if (thumbnail)
                return thumbnail;
            return [EditorGUIUtility.ObjectContent](EditorGUIUtility.ObjectContent.html)(go, go.GetType()).image as [Texture2D](Texture2D.html);
        }
    
        static [Texture2D](Texture2D.html) GetAssetPreviewFromPath(string path, [Vector2](Vector2.html) previewSize, [FetchPreviewOptions](Search.FetchPreviewOptions.html) previewOptions)
        {
            var obj = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(path);
            if (obj == null)
                return null;
            var preview = [AssetPreview.GetAssetPreview](AssetPreview.GetAssetPreview.html)(obj);
            if (preview == null || previewOptions.HasFlag([FetchPreviewOptions.Large](Search.FetchPreviewOptions.Large.html)))
            {
                var largePreview = [AssetPreview.GetMiniThumbnail](AssetPreview.GetMiniThumbnail.html)(obj);
                if (preview == null || (largePreview != null && largePreview.width > preview.width))
                    preview = largePreview;
            }
            return preview;
        }
    }
    

### Static Properties

[entrySeparators](Search.SearchUtils-entrySeparators.html)| Separators used to
split an entry into indexable tokens.  
---|---  
  
### Static Methods

[CreateGroupProvider](Search.SearchUtils.CreateGroupProvider.html)| Copy of a
search provider to create a new group copy.  
---|---  
[CreateQuery](Search.SearchUtils.CreateQuery.html)| Creates a new search
query.  
[CreateSceneResult](Search.SearchUtils.CreateSceneResult.html)| Creates a
search item compatible with the scene provider.  
[EnumerateAllQueries](Search.SearchUtils.EnumerateAllQueries.html)| Enumerate
all user and project search queries.  
[FetchGameObjects](Search.SearchUtils.FetchGameObjects.html)| Utility function
to fetch all the game objects in a particular scene.  
[FindQuery](Search.SearchUtils.FindQuery.html)| Find a given search query
given its GUID.  
[FindShiftLeftVariations](Search.SearchUtils.FindShiftLeftVariations.html)|
Extract all variations on a word. As an example: the word hello would have the
following variations: h, he, hel, hell, hello.  
[FormatBytes](Search.SearchUtils.FormatBytes.html)| Formats a number into a
file size in bytes string.  
[FormatCount](Search.SearchUtils.FormatCount.html)| Formats a number into a
shorten number string.  
[FrameAssetFromPath](Search.SearchUtils.FrameAssetFromPath.html)| Ping an
asset in the project browser.  
[GetAssetPath](Search.SearchUtils.GetAssetPath.html)| Returns the asset path
of a search item if any.  
[GetAssetPreviewFromPath](Search.SearchUtils.GetAssetPreviewFromPath.html)|
Returns a preview texture to be used in the search view.  
[GetAssetThumbnailFromPath](Search.SearchUtils.GetAssetThumbnailFromPath.html)|
Returns a thumbnail texture to be used in the search view.  
[GetHierarchyAssetPath](Search.SearchUtils.GetHierarchyAssetPath.html)| Get
the path of the scene (or prefab) containing a GameObject.  
[GetHierarchyPath](Search.SearchUtils.GetHierarchyPath.html)| Get the
hierarchy path of a GameObject including the scene name if includeScene is set
to true.  
[GetMainAssetInstanceID](Search.SearchUtils.GetMainAssetInstanceID.html)|
Returns an asset instance ID.  
[GetMainWindowCenteredPosition](Search.SearchUtils.GetMainWindowCenteredPosition.html)|
Returns a UnityEngine.Rect to center a window on the main Unity Editor window.  
[GetObjectPath](Search.SearchUtils.GetObjectPath.html)| Get the path of a
Unity Object. If it is a GameObject or a Component it is the . Else it is the
asset name.  
[GetSceneObjectPreview](Search.SearchUtils.GetSceneObjectPreview.html)|
Returns a scene object preview to be used in the search view.  
[GetTransformPath](Search.SearchUtils.GetTransformPath.html)| Format the
pretty name of a Transform component by appending all the parent hierarchy
names.  
[GetTypeIcon](Search.SearchUtils.GetTypeIcon.html)| Returns a thumbnail for a
given type that can be displayed in a search view. See
SearchProvider.fetchThumbnail.  
[MatchSearchGroups](Search.SearchUtils.MatchSearchGroups.html)| Helper
function to match a string against the SearchContext. This will try to match
the search query against each token of content (similar to the AddComponent
menu workflow).  
[OpenQuery](Search.SearchUtils.OpenQuery.html)| Open a search view for a given
query.  
[PingAsset](Search.SearchUtils.PingAsset.html)| Ping an object.  
[SelectMultipleItems](Search.SearchUtils.SelectMultipleItems.html)| Select and
ping multiple objects in the Project Browser.  
[ShowColumnSelector](Search.SearchUtils.ShowColumnSelector.html)| Opens an
auxiliary column selector window to allow the user to search for a column to
be added.  
[ShowIconPicker](Search.SearchUtils.ShowIconPicker.html)| Opens a search
picker to select an icon.  
[SplitCamelCase](Search.SearchUtils.SplitCamelCase.html)| Tokenize a string
each capital letter.  
[SplitEntryComponents](Search.SearchUtils.SplitEntryComponents.html)| Split an
entry according to a specified list of separators.  
[SplitFileEntryComponents](Search.SearchUtils.SplitFileEntryComponents.html)|
Split a file entry according to a list of separators and find all the
variations on the entry name.  
[StartDrag](Search.SearchUtils.StartDrag.html)| Utility function used to
initiate a drag operation from a search view.  
[TryParse](Search.SearchUtils.TryParse.html)| Try to parse an expression into
a number.  
  
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

