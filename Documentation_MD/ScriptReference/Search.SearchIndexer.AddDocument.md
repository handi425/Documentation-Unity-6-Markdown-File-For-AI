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

#  [SearchIndexer](Search.SearchIndexer.html).AddDocument

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

public int AddDocument(string document, bool checkIfExists);

## Declaration

public int AddDocument(string document, string name, string source, bool
checkIfExists, [Search.SearchDocumentFlags](Search.SearchDocumentFlags.html)
flags);

### Parameters

document | Unique document ID.  
---|---  
name | Name of path of the document.  
source | Source of the document. In example, if the document is a nested object, the source should be the container asset path.  
checkIfExists | Pass true if this document has some chance of existing already.  
flags | Flags describing the nature of the document.  
  
### Returns

**int** The document index/handle used to add new index entries.

### Description

Adds a new document to be indexed.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_AddDocument
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/AddDocument")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
    
            // The most efficient way of adding a document is by not checking if the
            // document ID was already added if you are sure that all your document IDs are unique.
            var di = si.AddDocument("document1", checkIfExists: false);
    
            // You can set `checkIfExists=true` to check for existing document IDs, and the system
            // will return an index of any existing document IDs.
            [Debug.Assert](Debug.Assert.html)(di == si.AddDocument("document1", checkIfExists: true));
    
            // Once you have added a new document, you need to use the returned handle to index words, numbers and properties.
            si.AddWord("unity", 0, di);
            si.AddProperty("is", "awesome", di);
            si.AddNumber("version", 3.0, score: 0, di);
    
            si.Finish(() =>
            {
                [Debug.Assert](Debug.Assert.html)(si.Search("unity version>=3").Count() == 1, "No result were found");
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

