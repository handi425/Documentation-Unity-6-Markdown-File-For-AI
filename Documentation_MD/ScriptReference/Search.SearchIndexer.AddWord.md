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

#  [SearchIndexer](Search.SearchIndexer.html).AddWord

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

public void AddWord(string word, int score, int documentIndex);

## Declaration

public void AddWord(string word, int size, int score, int documentIndex);

## Declaration

public void AddWord(string word, int minVariations, int maxVariations, int
score, int documentIndex);

### Parameters

word | Word to add to the index.  
---|---  
score | Relevance score of the word.  
documentIndex | Document where the indexed word was found.  
size | Number of variations to compute.  
minVariations | Minimum number of variations to compute. Cannot be higher than the length of the word.  
maxVariations | Maximum number of variations to compute. Cannot be higher than the length of the word.  
  
### Description

Adds a new word coming from a document to the index. The word is added with
multiple variations allowing partial search.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_AddWord
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/AddWord")]
        public static void Run()
        {
            // Create a search indexer
            var searchIndexer = new [SearchIndexer](Search.SearchIndexer.html)("SearchIndexerAddWordExample");
    
            // Indicate that Search is about to index documents.
            searchIndexer.Start();
    
            // Add a document
            var di = searchIndexer.AddDocument("My/[File](Windows.File.html)/Path");
    
            // Index some words
            var baseScore = 42;
    
            // This will index all variation of the word awesome, i.e. aw, awe, awes, aweso, awesom and awesome
            searchIndexer.AddWord("awesome", baseScore, di);
    
            // This will index an exact match for "unity", so no variation.
            searchIndexer.AddWord("unity", "unity".[Length](UIElements.Length.html), baseScore, di);
    
            // This will only index variations for the word from character indexes 3 to 6, e.g. thi, this, thisi and thisis
            searchIndexer.AddWord("thisisitasuperlongword", 3, 6, baseScore, di);
    
            // Indicate that searchIndexer is finished indexing a document and is ready to search.
            searchIndexer.Finish(() =>
            {
                // Search the index
                foreach (var result in searchIndexer.Search("unity awes this"))
                    [Debug.Log](Debug.Log.html)($"Found document [{result.index}] {result.id} ({result.score})");
    
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                searchIndexer.Dispose();
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

