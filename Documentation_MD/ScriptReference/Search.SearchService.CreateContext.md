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

#  [SearchService](Search.SearchService.html).CreateContext

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

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext(string searchText);

## Declaration

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext(string searchText, [Search.SearchFlags](Search.SearchFlags.html)
flags);

## Declaration

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext([Search.SearchProvider](Search.SearchProvider.html) provider,
string searchText);

## Declaration

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext(string providerId, string searchText,
[Search.SearchFlags](Search.SearchFlags.html) flags);

## Declaration

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext(IEnumerable<string> providerIds, string searchText,
[Search.SearchFlags](Search.SearchFlags.html) flags);

## Declaration

public static [Search.SearchContext](Search.SearchContext.html)
CreateContext(IEnumerable<SearchProvider> providers, string searchText,
[Search.SearchFlags](Search.SearchFlags.html) flags);

### Parameters

searchText | Search Query.  
---|---  
provider | Search provider (This search provider does not need to be active or registered).  
providerId | Unique search provider ID string (i.e. asset, scene, find, etc.)  
providerIds | List of search provider IDs.  
providers | List of search providers.  
flags | Options defining how the query is performed.  
  
### Returns

**SearchContext** Returns a new SearchContext.

### Description

Creates context from a list of search provider IDs.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchService_CreateContext
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchService](Search.SearchService.html)/CreateContext")]
        public static void Run()
        {
            using var searchContext = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("scene", "camera");
            using var results = [SearchService.Request](Search.SearchService.Request.html)(searchContext, [SearchFlags.Synchronous](Search.SearchFlags.Synchronous.html));
            {
                foreach (var label in results.Select(r => r.GetLabel(searchContext)))
                    [Debug.Log](Debug.Log.html)(label);
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

