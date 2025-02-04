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

#  [SearchService](Search.SearchService.html).ShowPicker

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

public static [Search.ISearchView](Search.ISearchView.html)
ShowPicker([Search.SearchContext](Search.SearchContext.html) context,
Action<SearchItem,bool> selectHandler, Action<SearchItem> trackingHandler,
Func<SearchItem,bool> filterHandler, IEnumerable<SearchItem> subset, string
title, float itemSize, float defaultWidth, float defaultHeight,
[Search.SearchFlags](Search.SearchFlags.html) flags);

### Parameters

context | Search context to start with.  
---|---  
selectHandler | Callback invoked when an item is selected.  
trackingHandler | Callback invoked when an item is clicked without it being the final selection.  
filterHandler | Callback invoked to filter search item results to display.  
title | Topic to search.  
itemSize | Initial result view item size.  
defaultWidth | Initial width of the window.  
defaultHeight | Initial height of the window.  
subset | Initial set of items to be searched.  
flags | Options defining how the query is performed.  
  
### Returns

**ISearchView** Creates a new search window.

### Description

Open a search item picker window.

* * *

## Declaration

public static [Search.ISearchView](Search.ISearchView.html)
ShowPicker([Search.SearchViewState](Search.SearchViewState.html) viewState);

### Parameters

viewState | Search view state used to open the Search Picker window.  
---|---  
  
### Returns

**ISearchView** Creates a new search window.

### Description

Open a Search Picker window.

This example shows how to open a custom search picker to pick a decal
material.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    using UnityEngine.Search;
    
    static class Example_SearchService_ShowPicker
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/ShowPicker")]
        public static void Run()
        {
            var context = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("asset", "t:material");
            var viewState = new [SearchViewState](Search.SearchViewState.html)(context,
                [SearchViewFlags.GridView](Search.SearchViewFlags.GridView.html) |
                [SearchViewFlags.OpenInBuilderMode](Search.SearchViewFlags.OpenInBuilderMode.html) |
                [SearchViewFlags.DisableSavedSearchQuery](Search.SearchViewFlags.DisableSavedSearchQuery.html))
            {
                windowTitle = new [GUIContent](GUIContent.html)("[Material](Material.html) Selector"),
                title = "[Material](Material.html)",
                selectHandler = SelectHandler,
                trackingHandler = TrackingHandler,
                position = [SearchUtils.GetMainWindowCenteredPosition](Search.SearchUtils.GetMainWindowCenteredPosition.html)(new [Vector2](Vector2.html)(600, 400))
            };
            [SearchService.ShowPicker](Search.SearchService.ShowPicker.html)(viewState);
        }
    
        static void SelectHandler([SearchItem](Search.SearchItem.html) searchItem, bool canceled)
        {
            [Debug.Log](Debug.Log.html)($"Selected {searchItem} (canceled: {canceled})");
        }
    
        static void TrackingHandler([SearchItem](Search.SearchItem.html) searchItem)
        {
            [Debug.Log](Debug.Log.html)($"Tracking {searchItem}");
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

