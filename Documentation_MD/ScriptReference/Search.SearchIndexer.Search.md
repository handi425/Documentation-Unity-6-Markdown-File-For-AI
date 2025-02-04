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

#  [SearchIndexer](Search.SearchIndexer.html).Search

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

public IEnumerable<SearchResult>
Search([Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchProvider](Search.SearchProvider.html) provider, int maxScore,
int patternMatchLimit);

## Declaration

public IEnumerable<SearchResult> Search(string query,
[Search.SearchContext](Search.SearchContext.html) context,
[Search.SearchProvider](Search.SearchProvider.html) provider, int maxScore,
int patternMatchLimit);

## Declaration

public IEnumerable<SearchResult> Search(string query, int maxScore, int
patternMatchLimit);

### Parameters

query | Search query to look for. If if matches any of the indexed variations, a result is returned.  
---|---  
context | The search context on which the query is applied.  
provider | The search provider that initiated the search.  
maxScore | Maximum match score of any matched Search Result. See [SearchResult.score](Search.SearchResult-score.html).  
patternMatchLimit | Maximum number of matched Search Results that can be returned. See [SearchResult](Search.SearchResult.html).  
  
### Returns

**IEnumerable <SearchResult>** Returns a collection of Search Results matching
the query.

### Description

Runs a search query in the index.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_Search
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/Search")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
    
            // Index some documents and properties
            si.AddProperty("color", "red", si.AddDocument("RGB 55"));
            si.AddProperty("color", "reddish", si.AddDocument("RGB 45"));
            si.AddProperty("color", "yellow", si.AddDocument("RGB 66"));
    
            si.Finish(() =>
            {
                // Search document with property color=red*
                var results = si.Search("color:red").ToList();
                [Debug.Assert](Debug.Assert.html)(results.Count == 2);
                if (results.Count > 0)
                    [Debug.Log](Debug.Log.html)(string.Join(", ", results.Select(r => $"{r.id} [{r.score}]")));
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
            });
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

