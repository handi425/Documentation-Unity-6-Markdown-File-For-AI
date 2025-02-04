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

#  [SearchService](Search.SearchService.html).ShowWindow

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
ShowWindow([Search.SearchContext](Search.SearchContext.html) context, string
topic, float defaultWidth, float defaultHeight, bool saveFilters, bool
reuseExisting, bool multiselect, bool dockable);

### Parameters

context | Search context to start with.  
---|---  
topic | Topic to search.  
saveFilters | True if user search provider filters should be saved for next search session.  
reuseExisting | True if the active providers should be saved for the next session.  
multiselect | True if the search supports multi-selection.  
defaultWidth | Initial width of the window.  
defaultHeight | Initial height of the window.  
dockable | If true, creates a dockable search window (that is closed when an item is activated). If false, it creates a dropdown (borderless, undockable and unmovable) version of the search window.  
  
### Returns

**ISearchView** Returns the search view window instance.

### Description

Creates a new search window.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    
    static class Example_SearchService_ShowWindow
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/ShowWindowEmpty")]
        public static void Run1()
        {
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)()
                .SetSearchText(string.Empty);
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/ShowWindowWithSearchText")]
        public static void Run2()
        {
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)([SearchService.CreateContext](Search.SearchService.CreateContext.html)("m: [Profiler](Profiling.Profiler.html)"));
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/ShowWindowCustomTopic")]
        public static void Run3()
        {
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(topic: "My Things")
                .SetSearchText(string.Empty);
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/ShowPopupWindow")]
        public static void Run4()
        {
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(defaultWidth: 1300, defaultHeight: 700, dockable: false);
        }
    }
    
    

* * *

## Declaration

public static [Search.ISearchView](Search.ISearchView.html)
ShowWindow([Search.SearchViewState](Search.SearchViewState.html) viewState);

### Parameters

viewState | Search view state used to open the Search window.  
---|---  
  
### Returns

**ISearchView** Returns the search view window instance.

### Description

Creates a new search window.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine.Search;  
      
    static class SearchWindows
    {
        [[MenuItem](MenuItem.html)("Search/Views/Simple Search Bar 1")] public static void SearchViewFlags1() => CreateWindow([SearchViewFlags.None](Search.SearchViewFlags.None.html));
        [[MenuItem](MenuItem.html)("Search/Views/Simple Search Bar 2")] public static void SearchViewFlags2() => CreateWindow([SearchViewFlags.EnableSearchQuery](Search.SearchViewFlags.EnableSearchQuery.html));
        [[MenuItem](MenuItem.html)("Search/Views/Simple Search Bar 3")] public static void SearchViewFlags3() => CreateWindow([SearchViewFlags.DisableInspectorPreview](Search.SearchViewFlags.DisableInspectorPreview.html));
        [[MenuItem](MenuItem.html)("Search/Views/Simple Search Bar 4")] public static void SearchViewFlags4() => CreateWindow([SearchViewFlags.EnableSearchQuery](Search.SearchViewFlags.EnableSearchQuery.html) | [SearchViewFlags.DisableInspectorPreview](Search.SearchViewFlags.DisableInspectorPreview.html));  
      
        static void CreateWindow([SearchViewFlags](Search.SearchViewFlags.html) flags)
        {
            var searchContext = [SearchService.CreateContext](Search.SearchService.CreateContext.html)(string.Empty);
            var viewArgs = new [SearchViewState](Search.SearchViewState.html)(searchContext, [SearchViewFlags.CompactView](Search.SearchViewFlags.CompactView.html) | flags) { title = flags.ToString() };
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(viewArgs);
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

