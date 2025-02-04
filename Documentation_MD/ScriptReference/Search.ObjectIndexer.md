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

# ObjectIndexer

class in UnityEditor.Search

/

Inherits from:[Search.SearchIndexer](Search.SearchIndexer.html)

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

A specialized [SearchIndexer](Search.SearchIndexer.html) which provides
methods to index a [Unity Object](UnityEngine.Object.html) from custom
indexers.

The [ObjectIndexer](Search.ObjectIndexer.html) can only be used in the context
of a [CustomObjectIndexerAttribute](Search.CustomObjectIndexerAttribute.html)
and therefore cannot be instanciated explicitly.

    
    
    [CustomObjectIndexer(typeof([Collider](Collider.html)), version = 3)]
    static void IndexObjectSize([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) target, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        var collider = target.target as [Collider](Collider.html);
        if (collider == null)
            return;
    
        var totalSize = CustomSelectors.ComputeColliderSize(collider);
        indexer.IndexNumber(target.documentIndex, "collidersize", totalSize);
    }
    

Note that you can use all of the [SearchIndexer](Search.SearchIndexer.html)
`Add*` indexing methods to add words, properties and numbers to the search
index database. You can also use the following higher level functions (i.e.
[IndexWord](Search.ObjectIndexer.IndexWord.html),
[IndexNumber](Search.ObjectIndexer.IndexNumber.html),
[IndexProperty](Search.ObjectIndexer.IndexProperty.html),
[IndexWordComponents](Search.ObjectIndexer.IndexWordComponents.html) and
[IndexPropertyComponents](Search.ObjectIndexer.IndexPropertyComponents.html))
to index common [Unity Object](UnityEngine.Object.html) properties.

### Public Methods

[IndexNumber](Search.ObjectIndexer.IndexNumber.html)| Adds a key-number value
pair to the index. The key won't be added with variations.  
---|---  
[IndexProperty](Search.ObjectIndexer.IndexProperty.html)| Adds a property
value to the index. A property is specified with a key and a string value. The
value will be stored with multiple variations.  
[IndexPropertyComponents](Search.ObjectIndexer.IndexPropertyComponents.html)|
Indexes multiple variations of a property value.  
[IndexWord](Search.ObjectIndexer.IndexWord.html)| Adds a new word coming from
a specific document to the index. The word will be added with multiple
variations allowing partial search.  
[IndexWordComponents](Search.ObjectIndexer.IndexWordComponents.html)| Splits a
word into multiple variations.  
  
### Inherited Members

### Properties

[documentCount](Search.SearchIndexer-documentCount.html)| Returns the number
of documents in the index.  
---|---  
[keywordCount](Search.SearchIndexer-keywordCount.html)| Returns the number
keywords in the index.  
[minQueryLength](Search.SearchIndexer-minQueryLength.html)| Minimal length of
a query. By default it is 1 character.  
[minWordIndexationLength](Search.SearchIndexer-minWordIndexationLength.html)|
Minimal indexed word size. Default is 2.  
[name](Search.SearchIndexer-name.html)| Name of the index. Generally this name
is set by a user from SearchDatabase.Settings.  
[resolveDocumentHandler](Search.SearchIndexer-resolveDocumentHandler.html)|
Handler used to resolve a document ID to some other data string.  
[skipEntryHandler](Search.SearchIndexer-skipEntryHandler.html)| Handler used
to skip entries.  
[timestamp](Search.SearchIndexer-timestamp.html)| Indicates when the search
index was last modified.  
  
### Public Methods

[AddDocument](Search.SearchIndexer.AddDocument.html)| Adds a new document to
be indexed.  
---|---  
[AddExactWord](Search.SearchIndexer.AddExactWord.html)| Adds a new word coming
from a document to the index. The word is added with multiple variations
allowing partial search.  
[AddNumber](Search.SearchIndexer.AddNumber.html)| Adds a key-number value pair
to the index. The key won't be added with variations.  
[AddProperty](Search.SearchIndexer.AddProperty.html)| Adds a property value to
the index. A property is specified with a key and a string value. The value
will be stored with multiple variations.  
[AddWord](Search.SearchIndexer.AddWord.html)| Adds a new word coming from a
document to the index. The word is added with multiple variations allowing
partial search.  
[Dispose](Search.SearchIndexer.Dispose.html)| Dispose of the SearchIndexer.  
[Finish](Search.SearchIndexer.Finish.html)| Finalizes the current index,
sorting and compiling of all the indexes.  
[GetDocument](Search.SearchIndexer.GetDocument.html)| Returns a search
document by its index.  
[GetMetaInfo](Search.SearchIndexer.GetMetaInfo.html)| Get metadata of a
specific document.  
[IndexDocument](Search.SearchIndexer.IndexDocument.html)| Function to override
in a concrete SearchIndexer to index the content of a document.  
[IsReady](Search.SearchIndexer.IsReady.html)| Indicates if the index is fully
built, up to date, and ready for search.  
[LoadBytes](Search.SearchIndexer.LoadBytes.html)| Loads the index
asynchronously (in another thread) from a binary buffer.  
[Merge](Search.SearchIndexer.Merge.html)| Merge a search index content into
the current index.  
[Read](Search.SearchIndexer.Read.html)| Reads a stream and populates the index
from it.  
[SaveBytes](Search.SearchIndexer.SaveBytes.html)| Get the bytes representation
of this index. See SearchIndexer.Write.  
[Search](Search.SearchIndexer.Search.html)| Runs a search query in the index.  
[SetMetaInfo](Search.SearchIndexer.SetMetaInfo.html)| Set arbiraty metadata on
a specific document.  
[SkipEntry](Search.SearchIndexer.SkipEntry.html)| Called when the index is
built to see if a specified document needs to be indexed. See
SearchIndexer.skipEntryHandler.  
[Start](Search.SearchIndexer.Start.html)| Starts indexing entries.  
[Write](Search.SearchIndexer.Write.html)| Writes a binary representation of
the index on a stream.  
  
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

