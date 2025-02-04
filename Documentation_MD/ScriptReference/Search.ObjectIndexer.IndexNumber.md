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

#  [ObjectIndexer](Search.ObjectIndexer.html).IndexNumber

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

public void IndexNumber(int documentIndex, string name, double number);

### Parameters

documentIndex | Document where the indexed value was found.  
---|---  
name | Key used to retrieve the value.  
number | Number value to store in the index.  
  
### Description

Adds a key-number value pair to the index. The key won't be added with
variations.

The following example uses `IndexNumber` to index a number `testsize` property
that can be searched using common number operators such as `>=`, i.e.
`testsize>=4.2`.

    
    
    [CustomObjectIndexer(typeof([Collider](Collider.html)), version = 3)]
    static void IndexObjectSize([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) target, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        var collider = target.target as [Collider](Collider.html);
        if (collider == null)
            return;
    
        var totalSize = CustomSelectors.ComputeColliderSize(collider);
        indexer.IndexNumber(target.documentIndex, "collidersize", totalSize);
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

