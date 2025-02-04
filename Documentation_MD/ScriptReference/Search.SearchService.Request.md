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

#  [SearchService](Search.SearchService.html).Request

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

public static [Search.ISearchList](Search.ISearchList.html) Request(string
searchText, [Search.SearchFlags](Search.SearchFlags.html) options);

## Declaration

public static [Search.ISearchList](Search.ISearchList.html)
Request([Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchFlags](Search.SearchFlags.html) options);

### Parameters

searchText | Search query to be executed.  
---|---  
context | Search context used to track asynchronous requests. You need to dispose of the context yourself.  
options | Options defining how the query is performed.  
  
### Returns

**ISearchList** Asynchronous list of search items.

### Description

Executes a search request that will fetch search results asynchronously.

The following example executes a query and print results over many frames
using [EditorApplication.update](EditorApplication-update.html).

    
    
    [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/[Request](PackageManager.Requests.Request.html) List")]
    public static void RequestList()
    {
        [ISearchList](Search.ISearchList.html) results = [SearchService.Request](Search.SearchService.Request.html)("*.cs");
    
        // It is important to note that when you request some search results,
        // that you need to enumerate them asynchronously using the returned search list.
        AsyncResultEnumerator.Fetch(results, item => [Debug.Log](Debug.Log.html)(item));
    }
    
    struct AsyncResultEnumerator
    {
        private [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> m_OnEnumerate;
        private IEnumerator<[SearchItem](Search.SearchItem.html)> m_Iterator;
    
        public static AsyncResultEnumerator Fetch([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
        {
            return new AsyncResultEnumerator(results, onEnumerate);
        }
    
        public AsyncResultEnumerator([ISearchList](Search.ISearchList.html) results, [Action](Unity.Android.Gradle.Manifest.Action.html)<[SearchItem](Search.SearchItem.html)> onEnumerate)
        {
            m_OnEnumerate = onEnumerate;
            m_Iterator = results.GetEnumerator();
            [EditorApplication.update](EditorApplication-update.html) += EnumerateResults;
        }
    
        private void EnumerateResults()
        {
            if (m_Iterator == null || !m_Iterator.MoveNext())
            {
                m_Iterator = null;
                [EditorApplication.update](EditorApplication-update.html) -= EnumerateResults;
            }
            else if (m_Iterator.Current != null)
                m_OnEnumerate(m_Iterator.Current);
        }
    }
    

If you are running a coroutine you can yield results like the following:

    
    
    public static IEnumerable<[SearchItem](Search.SearchItem.html)> YieldResults()
    {
        [ISearchList](Search.ISearchList.html) results = [SearchService.Request](Search.SearchService.Request.html)("*.cs");
        foreach (var result in results)
            yield return result;
    }
    

* * *

## Declaration

public static void Request(string searchText,
Action<SearchContext,IList<SearchItem>> onSearchCompleted,
[Search.SearchFlags](Search.SearchFlags.html) options);

## Declaration

public static void Request([Search.SearchContext](Search.SearchContext.html)
context, Action<SearchContext,IList<SearchItem>> onSearchCompleted,
[Search.SearchFlags](Search.SearchFlags.html) options);

### Parameters

onSearchCompleted | Callback invoked when the search request is completed and all results are available.  
---|---  
  
### Description

Executes a search request and calls back the specified function when all
results are available.

    
    
    [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/[Request](PackageManager.Requests.Request.html) All")]
    public static void RequestAll()
    {
        [SearchService.Request](Search.SearchService.Request.html)("t:texture", ([SearchContext](Search.SearchContext.html) context, IList<[SearchItem](Search.SearchItem.html)> items) =>
        {
            [Debug.Log](Debug.Log.html)("All Textures");
            foreach (var item in items)
                [Debug.Log](Debug.Log.html)(item);
        }, [SearchFlags.Debug](Search.SearchFlags.Debug.html));
    }
    

* * *

## Declaration

public static void Request(string searchText,
Action<SearchContext,IEnumerable<SearchItem>> onIncomingItems,
Action<SearchContext> onSearchCompleted,
[Search.SearchFlags](Search.SearchFlags.html) options);

## Declaration

public static void Request([Search.SearchContext](Search.SearchContext.html)
context, Action<SearchContext,IEnumerable<SearchItem>> onIncomingItems,
Action<SearchContext> onSearchCompleted,
[Search.SearchFlags](Search.SearchFlags.html) options);

### Parameters

onIncomingItems | Callback invoked everytime a batch of results are found and available.  
---|---  
onSearchCompleted | Callback invoked when the search request is completed.  
  
### Description

Executes a search request and callbacks for every batch of incoming results.
It is possible to get duplicate items, so filter the final list if needed.

    
    
    [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/[Request](PackageManager.Requests.Request.html) Async")]
    public static void RequestAsync()
    {
        var batchCount = 0;
        var totalItemCount = 0;
    
        void OnIncomingResults([SearchContext](Search.SearchContext.html) context, IEnumerable<[SearchItem](Search.SearchItem.html)> items)
        {
            var batchItemCount = items.Count();
            totalItemCount += batchItemCount;
            [Debug.Log](Debug.Log.html)($"#{++batchCount} Incoming materials ({batchItemCount}): {string.Join("\n", items)}");
        }
    
        void OnSearchCompleted([SearchContext](Search.SearchContext.html) context)
        {
            [Debug.Log](Debug.Log.html)($"Query <b>\"{context.searchText}\"</b> completed with a total of {totalItemCount}");
        }
    
        [SearchService.Request](Search.SearchService.Request.html)("t:material", OnIncomingResults, OnSearchCompleted, [SearchFlags.Debug](Search.SearchFlags.Debug.html));
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

