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

#  [SearchIndexer](Search.SearchIndexer.html).Read

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

public bool Read(Stream stream, bool checkVersionOnly);

### Parameters

stream | The stream to read the index from.  
---|---  
checkVersionOnly | If true, verifies the version of the index.  
  
### Returns

**bool** Returns false if the version of the index is not supported.

### Description

Reads a stream and populates the index from it.

    
    
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_SearchIndexer_Read
    {
        [[MenuItem](MenuItem.html)("Examples/[SearchIndexer](Search.SearchIndexer.html)/Read")]
        public static void Run()
        {
            var si = new [SearchIndexer](Search.SearchIndexer.html)();
            si.Start();
            si.AddDocument("document 1");
            si.AddDocument("document 2");
            si.Finish(() =>
            {
                [File.WriteAllBytes](Windows.File.WriteAllBytes.html)("Temp/Read.index", si.SaveBytes());
                // Dispose of the [SearchIndexer](Search.SearchIndexer.html) when you are done with it.
                si.Dispose();
    
                // Stream the index from disk but only check if the stream is valid.
                using (var fileStream = new FileStream("Temp/Read.index", FileMode.Open, FileAccess.Read, FileShare.Read))
                {
                    using var copyIndex = new [SearchIndexer](Search.SearchIndexer.html)();
                    [Debug.Assert](Debug.Assert.html)(copyIndex.Read(fileStream, checkVersionOnly: true));
                }
    
                // Completely stream the index from disk.
                using (var fileStream = new FileStream("Temp/Read.index", FileMode.Open, FileAccess.Read, FileShare.Read))
                {
                    using var copyIndex = new [SearchIndexer](Search.SearchIndexer.html)();
                    [Debug.Assert](Debug.Assert.html)(copyIndex.Read(fileStream, checkVersionOnly: false));
                    [Debug.Assert](Debug.Assert.html)(copyIndex.GetDocument(0).id == "document 1");
                }
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

