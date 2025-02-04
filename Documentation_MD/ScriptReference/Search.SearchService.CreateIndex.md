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

#  [SearchService](Search.SearchService.html).CreateIndex

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

public static void CreateIndex(ref string name, ref
[Search.IndexingOptions](Search.IndexingOptions.html) options,
IEnumerable<string> roots, IEnumerable<string> includes, IEnumerable<string>
excludes, Action<string,string,Action> onIndexReady);

### Parameters

name | Unique name of the search index.  
---|---  
options | Indexing option set.  
roots | Search index roots, for example "Assets" to index all Assets under Assets.  
includes | Exclusive list of assets to be indexed. If this list is empty, everything will be indexed.  
excludes | Patterns to exclude assets to be indexed under roots.  
onIndexReady | Callback that gets invoked when the index is created and ready to be used.  
  
### Description

Create a new search index.

    
    
    static string EnsureDecalPropertyIndexing()
    {
        var materialDb = [SearchService.EnumerateDatabases](Search.SearchService.EnumerateDatabases.html)().FirstOrDefault(IsIndexingMaterialProperties);
        if (materialDb != null)
            return materialDb.name;
    
        if (![EditorUtility.DisplayDialog](EditorUtility.DisplayDialog.html)("Create decal material index",
            "Your project does not contain an index with decal material properties." +
            "\n\n" +
            "Do you want to create one now?", "Yes", "No"))
            return null;
    
        var dbName = "Decals";
        [SearchService.CreateIndex](Search.SearchService.CreateIndex.html)(dbName,
            [IndexingOptions.Properties](Search.IndexingOptions.Properties.html) | [IndexingOptions.Dependencies](Search.IndexingOptions.Dependencies.html) |
            [IndexingOptions.Types](Search.IndexingOptions.Types.html) | [IndexingOptions.Keep](Search.IndexingOptions.Keep.html),
            roots: null,
            includes: new string[] { ".mat" },
            excludes: null,
            (name, path, finished) =>
            {
                [Debug.Log](Debug.Log.html)($"[Material](Material.html) index {name} created at {path}");
                finished();
            });
        return dbName;
    }
    
    static bool IsIndexingMaterialProperties([ISearchDatabase](Search.ISearchDatabase.html) db)
    {
        if (string.Equals(db.name, "Materials", StringComparison.OrdinalIgnoreCase))
            return true;
        return (db.indexingOptions & [IndexingOptions.Properties](Search.IndexingOptions.Properties.html)) == [IndexingOptions.Properties](Search.IndexingOptions.Properties.html)
            && (db.includePatterns.Count == 0 || db.includePatterns.Contains(".mat"));
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

