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

# CustomObjectIndexerAttribute

class in UnityEditor.Search

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

Allows a user to register a custom Indexing function for a specific type.

When you have special properties you would like to index for an asset or a
Unity Object, Unity suggests Writing a custom indexer routine . The newly
indexed words or properties will allow the user to search for them using the
[Search Query Language](Search.QueryEngine.html). The registered function must
be of type: `static void MyCustomIndexer(CustomObjectIndexerTarget context,
ObjectIndexer indexer);`  
  
See [ObjectIndexer](Search.ObjectIndexer.html) for the various methods you can
invoke on `indexer`.  
  
The [CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html)
`context` argument can be used to access additional information about what is
about to be indexed.

    
    
    [CustomObjectIndexer(typeof([Material](Material.html)))]
    internal static void MaterialShaderReferences([CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html) context, [ObjectIndexer](Search.ObjectIndexer.html) indexer)
    {
       var material = context.target as [Material](Material.html);
       if (material == null)
           return;  
      
       if (material.shader)
       {
           var fullShaderName = material.shader.name.ToLowerInvariant();
           var shortShaderName = System.IO.Path.GetFileNameWithoutExtension(fullShaderName);
           indexer.AddProperty("ref", shortShaderName, context.documentIndex);
           indexer.AddProperty("ref", fullShaderName, context.documentIndex);
       }
    }

### Properties

[type](Search.CustomObjectIndexerAttribute-type.html)| Each time an object of
a specific type is indexed, the registered function is called.  
---|---  
[version](Search.CustomObjectIndexerAttribute-version.html)| Version of the
custom indexer. Increment this number to have the indexer re-index the
indexes.  
  
### Constructors

[CustomObjectIndexerAttribute](Search.CustomObjectIndexerAttribute-ctor.html)|
Register a new Indexing function bound to the specific type.  
---|---  
  
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

