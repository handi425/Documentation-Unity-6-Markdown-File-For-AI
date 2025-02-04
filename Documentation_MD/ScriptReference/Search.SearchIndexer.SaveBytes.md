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

#  [SearchIndexer](Search.SearchIndexer.html).SaveBytes

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

public byte[] SaveBytes();

### Returns

**byte[]** Bytes representation of the index.

### Description

Get the bytes representation of this index. See
[SearchIndexer.Write](Search.SearchIndexer.Write.html).

    
    
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_LoadBytes
    {
        const string tempIndexPath = "Temp/LoadBytes.db";
    
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/LoadBytes")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
            var di = si.AddDocument("document 1");
            si.AddNumber("test", 2, 0, di);
            si.Finish(() =>
            {
                [File.WriteAllBytes](Windows.File.WriteAllBytes.html)(tempIndexPath, si.SaveBytes());
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
                ReloadIndex();
            });
        }
    
        private static void ReloadIndex()
        {
            var indexBytes = [File.ReadAllBytes](Windows.File.ReadAllBytes.html)(tempIndexPath);
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
    
            // Load the search index from a binary stream.
            si.LoadBytes(indexBytes, (success) =>
            {
                [Debug.Assert](Debug.Assert.html)(success);
                [Debug.Log](Debug.Log.html)($"Index loaded from {indexBytes} bytes");
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

