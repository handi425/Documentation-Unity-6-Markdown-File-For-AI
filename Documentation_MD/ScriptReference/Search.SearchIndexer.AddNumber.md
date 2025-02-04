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

#  [SearchIndexer](Search.SearchIndexer.html).AddNumber

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

public void AddNumber(string key, double value, int score, int documentIndex);

### Parameters

key | Key used to retrieve the value.  
---|---  
value | Number value to store in the index.  
score | Relevance score of the word.  
documentIndex | Document where the indexed value was found.  
  
### Description

Adds a key-number value pair to the index. The key won't be added with
variations.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_AddNumber
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/AddNumber")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
    
            // Add some documents and index a power value that can be searched.
            si.AddNumber("power", 4.4, score: 0, si.AddDocument("Weak"));
            si.AddNumber("power", 6.42, score: 0, si.AddDocument("Healthy"));
            si.AddNumber("power", 9.9, score: 0, si.AddDocument("Strong"));
    
            si.Finish(() =>
            {
                SearchPowerLevels(si);
                // Dispose the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
            });
        }
    
        private static void SearchPowerLevels([SearchIndexer](Search.SearchIndexer.html) si)
        {
            SearchPowerLevel(si, "power<5", 1);
            SearchPowerLevel(si, "power>=6", 2);
        }
    
        static void SearchPowerLevel([SearchIndexer](Search.SearchIndexer.html) si, string powerQuery, int expectedCount)
        {
            var results = si.Search(powerQuery).ToList();
            [Debug.Assert](Debug.Assert.html)(results.Count == expectedCount, "Invalid query");
            [Debug.Log](Debug.Log.html)($"Document with {powerQuery}: {string.Join(", ", results.Select(r => r.id))}");
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

