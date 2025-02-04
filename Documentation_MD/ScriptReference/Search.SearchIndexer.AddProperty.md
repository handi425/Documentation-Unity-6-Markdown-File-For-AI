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

#  [SearchIndexer](Search.SearchIndexer.html).AddProperty

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

public void AddProperty(string key, string value, int documentIndex, bool
saveKeyword, bool exact);

## Declaration

public void AddProperty(string key, string value, int score, int
documentIndex, bool saveKeyword, bool exact);

## Declaration

public void AddProperty(string name, string value, int minVariations, int
maxVariations, int score, int documentIndex, bool saveKeyword, bool exact);

### Parameters

key | Key used to retrieve the value.  
---|---  
value | String value to store in the index.  
documentIndex | Document where the indexed value was found.  
saveKeyword | Indicates if we store this key in the keyword registry of the index. See SearchIndexer.GetKeywords.  
exact | If true, index stores an exact match entry for this word.  
score | Relevance score of the word.  
name | Key used to retrieve the value.  
minVariations | Minimum number of variations to compute for the value. Cannot be higher than the length of the word.  
maxVariations | Maximum number of variations to compute for the value. Cannot be higher than the length of the word.  
  
### Description

Adds a property value to the index. A property is specified with a key and a
string value. The value will be stored with multiple variations.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_AddProperty
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/AddProperty")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
    
            // Add a property with exact:true, meaning that you can either use is: or is= to search for results
            // These items are given a high score, so they will not be displayed first in the result list.
            si.AddProperty("is", "broken", score: 20, si.AddDocument("Bocument 1"), exact: true);
            si.AddProperty("is", "broken", score: 30, si.AddDocument("Bocument 4"), exact: true);
    
            // Use exact:false, so color=red won't match any result, just color:red, same for color:yel
            si.AddProperty("color", "red", si.AddDocument("RGB 55"), exact: false);
            si.AddProperty("color", "reddish", si.AddDocument("RGB 45"), exact: false);
            si.AddProperty("color", "yellow", si.AddDocument("RGB 66"), exact: false);
    
            // Use this version of AddProperty if you want to minimize how many index variations are computed.
            // In the example, if you want is:secret to match, but not is:secr
            si.AddProperty("is", "secret", minVariations: "secret".[Length](UIElements.Length.html), maxVariations: "secret".[Length](UIElements.Length.html), score: -99, si.AddDocument("Top Secret"), exact: true);
    
            si.Finish(() =>
            {
                SearchDocuments(si, "Broken documents (Invalid query)", "is=broke", 0);
                SearchDocuments(si, "Broken documents", "is=broken", 2);
    
                SearchDocuments(si, "[Color](Color.html) documents", "color=red", 0);
                SearchDocuments(si, "[Color](Color.html) documents", "color:red", 2);
                SearchDocuments(si, "[Color](Color.html) documents", "color:yel", 1);
    
                SearchDocuments(si, "Top documents", "is:secr", 0);
                SearchDocuments(si, "Top documents", "is:secret", 1);
                SearchDocuments(si, "Top documents", "is=secret", 1);
    
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
            });
        }
    
        private static void SearchDocuments([SearchIndexer](Search.SearchIndexer.html) si, string label, string query, int expectedCount)
        {
            var results = si.Search(query).ToList();
            [Debug.Assert](Debug.Assert.html)(results.Count == expectedCount, $"Invalid {label} with {query}, expected {expectedCount} results but got {results.Count}");
            if (results.Count > 0)
                [Debug.Log](Debug.Log.html)($"{label} ({query}): {string.Join(", ", results.Select(r => $"{r.id} [{r.score}]"))}");
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

