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

# SearchService

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

Principal Search API to initiate searches and fetch results.

Make sure to check [SearchService.Request](Search.SearchService.Request.html)
for a complete list of all the different ways to execute a search request.

    
    
    using System.Linq;
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchService
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/Class")]
        public static void Run()
        {
            void OnSearchCompleted([SearchContext](Search.SearchContext.html) context, IList<[SearchItem](Search.SearchItem.html)> items)
            {
                foreach (var item in items)
                    [Debug.Log](Debug.Log.html)(item);
            }
    
            [SearchService.Request](Search.SearchService.Request.html)("*.cs", OnSearchCompleted);
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/Providers")]
        public static void RunProviders()
        {
            // Print special search providers
            foreach (var provider in SearchService.Providers.Where(p => p.isExplicitProvider))
                [Debug.Log](Debug.Log.html)($"Special Search [Provider](VersionControl.Provider.html) {provider.name} ({provider.id})");
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/OrderedProviders")]
        public static void RunOrderedProviders()
        {
            // Print providers by their search priority when a query is executed.
            foreach (var provider in [SearchService.OrderedProviders](Search.SearchService.OrderedProviders.html))
                [Debug.Log](Debug.Log.html)($"[{provider.priority}] {provider.name} ({provider.id})");
        }
    }
    

### Static Properties

[OrderedProviders](Search.SearchService.OrderedProviders.html)| Returns the
list of search providers sorted by priority.  
---|---  
[Providers](Search.SearchService.Providers.html)| Returns the list of all
search providers (active or not).  
  
### Static Methods

[CreateContext](Search.SearchService.CreateContext.html)| Creates context from
a list of search provider IDs.  
---|---  
[CreateIndex](Search.SearchService.CreateIndex.html)| Create a new search
index.  
[EnumerateDatabases](Search.SearchService.EnumerateDatabases.html)| Enumerate
search databases.  
[GetAction](Search.SearchService.GetAction.html)| Returns the search action
for a given search provider and search action ID.  
[GetActiveProviders](Search.SearchService.GetActiveProviders.html)| Returns
all active providers.  
[GetItems](Search.SearchService.GetItems.html)| Initiates a search and returns
all search items matching the search context. Other items can be found later
using asynchronous searches.  
[GetProvider](Search.SearchService.GetProvider.html)| Returns the data of a
search provider given its ID.  
[IsIndexReady](Search.SearchService.IsIndexReady.html)| Indicates if a search
index is ready to be used.  
[Refresh](Search.SearchService.Refresh.html)| Clears everything and reloads
all search providers. Use with care. Useful for unit tests.  
[RefreshWindows](Search.SearchService.RefreshWindows.html)| Refresh all
currently opened Search windows.  
[Request](Search.SearchService.Request.html)| Executes a search request that
will fetch search results asynchronously.  
[SetActive](Search.SearchService.SetActive.html)| Activates or deactivates a
search provider. Call Refresh after this to take effect on the next search.  
[ShowContextual](Search.SearchService.ShowContextual.html)| Open the search
window using a specific context (activating specific filters).  
[ShowObjectPicker](Search.SearchService.ShowObjectPicker.html)| Open a Search
Picker window for Unity objects.  
[ShowPicker](Search.SearchService.ShowPicker.html)| Open a search item picker
window.  
[ShowWindow](Search.SearchService.ShowWindow.html)| Creates a new search
window.  
  
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

