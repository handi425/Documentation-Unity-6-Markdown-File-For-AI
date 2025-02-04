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

#  [ObjectIndexer](Search.ObjectIndexer.html).IndexProperty

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

public void IndexProperty(int documentIndex, string name, string value, bool
saveKeyword, bool exact);

### Parameters

documentIndex | Document where the indexed word was found.  
---|---  
name | Key used to retrieve the value.  
value | Value to add to the index.  
saveKeyword | Define if we store this key in the keyword registry of the index.  
exact | If exact is true, only the exact match of the value will be stored in the index (not the variations).  
  
### Description

Adds a property value to the index. A property is specified with a key and a
string value. The value will be stored with multiple variations.

The following example indexes a new boolean property named
`testismobilefriendly` that will be used to search textures that match
`testismobilefriendly=true` or `testismobilefriendly=false`.

    
    
    [CustomObjectIndexer(typeof([Texture2D](Texture2D.html)))]
    static void IndexMobileFriendlyTexture([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) target, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        var texture = target.target as [Texture2D](Texture2D.html);
        if (texture == null)
            return;
    
        bool isMobileFriendly = texture.width < 64 && texture.height < 64;
        indexer.IndexProperty(target.documentIndex, "testismobilefriendly", isMobileFriendly.ToString(), true);
    }
    
    [CustomObjectIndexer(typeof([Texture2D](Texture2D.html)))]
    static void CrashingIndexer([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) target, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
        if (enableCrashingIndexer)
            throw new System.Exception("Crash");
    }
    

See [SearchIndexer.AddProperty](Search.SearchIndexer.AddProperty.html) for
more information and examples about indexing properties.

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

