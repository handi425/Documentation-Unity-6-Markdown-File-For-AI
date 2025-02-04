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

#  [SearchService](Search.SearchService.html).GetItems

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

public static List<SearchItem>
GetItems([Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchFlags](Search.SearchFlags.html) options);

### Parameters

context | The current search context.  
---|---  
options | Options defining how the query is performed.  
  
### Returns

**List <SearchItem>** A list of search items matching the search query.

### Description

Initiates a search and returns all search items matching the search context.
Other items can be found later using asynchronous searches.

Unity suggests using
[SearchService.Request](Search.SearchService.Request.html) to execute a search
query. `GetItems` usually requires setting up more context to achieve a good
result. The following is a small example that uses `GetItems`.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchService_GetItems
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/GetItems")]
        public static void Run()
        {
            // Create a container to hold found items.
            var results = new List<[SearchItem](Search.SearchItem.html)>();
    
            // Create the search context that will be used to execute the query.
            using (var searchContext = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("scene", "is:leaf"))
            {
                // Initiate the query and get the results.
                // Note: it is recommended to use [SearchService.Request](Search.SearchService.Request.html) if you wish to fetch the items asynchronously.
                results = [SearchService.GetItems](Search.SearchService.GetItems.html)(searchContext, [SearchFlags.WantsMore](Search.SearchFlags.WantsMore.html) | [SearchFlags.Synchronous](Search.SearchFlags.Synchronous.html));
    
                // Print results
                foreach (var searchItem in results)
                    [Debug.Log](Debug.Log.html)(searchItem.GetDescription(searchContext));
            }
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

