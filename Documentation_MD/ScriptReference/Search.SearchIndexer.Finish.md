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

#  [SearchIndexer](Search.SearchIndexer.html).Finish

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

public void Finish();

## Declaration

public void Finish(string[] removedDocuments);

## Declaration

public void
Finish([Unity.Android.Gradle.Manifest.Action](Unity.Android.Gradle.Manifest.Action.html)
threadCompletedCallback);

## Declaration

public void
Finish([Unity.Android.Gradle.Manifest.Action](Unity.Android.Gradle.Manifest.Action.html)
threadCompletedCallback, string[] removedDocuments);

## Declaration

public void Finish(Action<byte[]> threadCompletedCallback, string[]
removedDocuments);

## Declaration

public void Finish(Action<byte[]> threadCompletedCallback, string[]
removedDocuments, bool saveBytes);

### Parameters

threadCompletedCallback | Callback invoked when the index is ready to be used.  
---|---  
removedDocuments | Documents to be removed from current index (if any).  
saveBytes | Indicates if the system should return the binary stream of the index as a byte array.  
  
### Description

Finalizes the current index, sorting and compiling of all the indexes.

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    /// <summary>
    /// [SearchIndexer.Finish](Search.SearchIndexer.Finish.html) is always a threaded operation, meaning that all indexes
    /// will be computed in a thread and Search will callback when the index is ready
    /// to be used.
    /// </summary>
    static class Example_SearchIndexer_Finish
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/Finish")]
        public static void Run()
        {
            // Create an indexer and wait for indexing to complete in the current thread.
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
            si.AddProperty("wait", "yes", si.AddDocument("Wait"));
            si.Finish();
            while (!si.IsReady())
                ;
            [Debug.Assert](Debug.Assert.html)(si.IsReady());
    
            // Reset the indexer and receive a callback when the indexing is completed.
            si.Start(clear: true);
            si.AddProperty("wait", "callback", si.AddDocument("Callback"));
            si.Finish(() => [Debug.Log](Debug.Log.html)("Indexing is ready."));
            while (!si.IsReady())
                ;
    
            // Reset the indexer and receive a callback when the indexing is completed and backup the index.
            // With that override you can also indicate if you want any documents to be deleted
            si.Start(clear: false);
            si.AddProperty("wait", "callback", si.AddDocument("CallbackBytes"));
            si.AddProperty("wait", "callback", si.AddDocument("DeleteMe"));
            si.Finish((bytes) =>
            {
                [Debug.Log](Debug.Log.html)($"Indexing is ready and its size is {bytes.Length}.");
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
            }, new string[] { "Callback", "DeleteMe" });
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

