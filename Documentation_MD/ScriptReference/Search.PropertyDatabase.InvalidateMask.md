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

#  [PropertyDatabase](Search.PropertyDatabase.html).InvalidateMask

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

public void InvalidateMask(ulong documentKeyMask);

### Parameters

documentKeyMask | A document key mask.  
---|---  
  
### Description

Invalidate all properties stored from multiple documents that match a document
key mask.

This operation is slower than the simpler
[PropertyDatabase.Invalidate](Search.PropertyDatabase.Invalidate.html) since
we cannot rely on a binary search to find all keys that match the mask.

    
    
    // Store properties of multiple documents.
    for (ulong i = 0; i < 10; ++i)
    {
        for (var j = 0; j < 10; ++j)
            propertyDatabase.Store(i, [PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html)($"prop{j}"), $"value{j}");
    }
    // Invalidate all documents that match any set bits of the mask.
    ulong invalidatedDocumentMask = 2;
    propertyDatabase.InvalidateMask(invalidatedDocumentMask);
    
    // The invalidated documents can no longer be retrieved.
    for (ulong i = 0; i < 10; ++i)
    {
        if ((i & invalidatedDocumentMask) == 0)
            continue;
        if (propertyDatabase.TryLoad(i, out IEnumerable<object> invalidatedDocumentValues))
            Assert.Fail("TryLoad should have failed to retrieve the invalidated document values.");
    }
    

Additional resources:
[PropertyDatabase.CreateDocumentKey](Search.PropertyDatabase.CreateDocumentKey.html).

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

