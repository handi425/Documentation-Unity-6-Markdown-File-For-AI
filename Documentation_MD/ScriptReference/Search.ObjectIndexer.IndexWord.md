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

#  [ObjectIndexer](Search.ObjectIndexer.html).IndexWord

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

public void IndexWord(int documentIndex, ref string word, bool exact, int
scoreModifier);

### Parameters

documentIndex | Document where the indexed word was found.  
---|---  
word | Word to add to the index.  
exact | If true, we will also store an exact match entry for this word.  
scoreModifier | Modified to apply to the base match score for a specific word.  
  
### Description

Adds a new word coming from a specific document to the index. The word will be
added with multiple variations allowing partial search.

The following example indexes a word that can be used to search indexed
prefabs with `myawesomeword`, `myawe`, etc.

    
    
    [CustomObjectIndexer(typeof([GameObject](GameObject.html)))]
    static void IndexGameObject([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) target, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        var go = target.target as [GameObject](GameObject.html);
        if (go == null)
            return;
    
        indexer.AddWord("myawesomeword", 0, target.documentIndex);
    }
    

* * *

## Declaration

public void IndexWord(int documentIndex, ref string word, int maxVariations,
bool exact, int scoreModifier);

### Parameters

documentIndex | Document where the indexed word was found.  
---|---  
word | Word to add to the index.  
maxVariations |  **Maximum number of variations to compute. Cannot be higher than the length of the word.**  
exact | If true, the indexer will also store an exact match entry for this word.  
scoreModifier | Modified to apply to the base match score for a specific word.  
  
### Description

The word will be added with a maximum of variation. This can be used to save
some space for very large words.

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

