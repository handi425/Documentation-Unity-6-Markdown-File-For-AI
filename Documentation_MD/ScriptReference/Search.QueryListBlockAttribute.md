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

# QueryListBlockAttribute

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

This attribute can be used on a class deriving from
[QueryListBlock](Search.QueryListBlock.html) to display in query builder mode
a special block that will propose a fixed set of values when clicked.

The following example shows how to display a custom list block for the
`shader` filter block.

    
    
    [[QueryListBlock](Search.QueryListBlock.html)("Decal", "[Shader](Shader.html)", "shader")]
    class ShaderDecalBlockList : [QueryListBlock](Search.QueryListBlock.html)
    {
        public ShaderDecalBlockList([IQuerySource](Search.IQuerySource.html) source, string id, string value, [QueryListBlockAttribute](Search.QueryListBlockAttribute.html) attr)
            : base(source, id, value, attr)
        {
        }
    
        public override IEnumerable<[SearchProposition](Search.SearchProposition.html)> GetPropositions([SearchPropositionFlags](Search.SearchPropositionFlags.html) flags = [SearchPropositionFlags.None](Search.SearchPropositionFlags.None.html))
        {
            var shaderIcon = [EditorGUIUtility.Load](EditorGUIUtility.Load.html)("[Shader](Shader.html) Icon") as [Texture2D](Texture2D.html);
            yield return new [SearchProposition](Search.SearchProposition.html)(category: null, "HDRP Decal", "Decal", icon: shaderIcon);
            yield return new [SearchProposition](Search.SearchProposition.html)(category: null, "URP Decal", "DecalURP", icon: shaderIcon);
        }
    }
    

### Properties

[category](Search.QueryListBlockAttribute-category.html)| Category.  
---|---  
[id](Search.QueryListBlockAttribute-id.html)| Filter id of the block.  
[ids](Search.QueryListBlockAttribute-ids.html)| A set of IDs for which the
list block will be displayed.  
[name](Search.QueryListBlockAttribute-name.html)| Displayed name of the block.  
[op](Search.QueryListBlockAttribute-op.html)| Default operator assigned to the
filter when the value changes.  
[type](Search.QueryListBlockAttribute-type.html)| The list block type is used
to get the the icon to be displayed instead of the block name.  
  
### Constructors

[QueryListBlockAttribute](Search.QueryListBlockAttribute-ctor.html)| Register
a list block for a given filter.  
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

