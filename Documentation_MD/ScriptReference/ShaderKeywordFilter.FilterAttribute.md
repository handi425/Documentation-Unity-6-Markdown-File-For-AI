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

# FilterAttribute

class in UnityEditor.ShaderKeywordFilter

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

Tell the shader system which shader keywords to include or remove from the
build, based on the data field underneath.

This is the base filter attribute class. Use the derived attributes instead:

  * [SelectIfAttribute](ShaderKeywordFilter.SelectIfAttribute.html)
  * [SelectIfNotAttribute](ShaderKeywordFilter.SelectIfNotAttribute.html)
  * [RemoveIfAttribute](ShaderKeywordFilter.RemoveIfAttribute.html)
  * [RemoveIfNotAttribute](ShaderKeywordFilter.RemoveIfNotAttribute.html)
  * [SelectOrRemoveAttribute](ShaderKeywordFilter.SelectOrRemoveAttribute.html)
  * [RemoveOrSelectAttribute](ShaderKeywordFilter.RemoveOrSelectAttribute.html)

These filter attributes only apply to the build if they're attached to a
serialized data field that's part of the type tree of a
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html) referenced by
[QualitySettings](QualitySettings.html). The attributes give you control over
which shader keywords Unity uses to build shader variants, based on render
pipeline settings.  
  
For example, by default the following shader code generates four different
shader variants during the build:

    
    
    #pragma multi_compile __ SHADOWS_LOW SHADOWS_MEDIUM SHADOWS_HIGH

If you use filter attributes, this can be adjusted to better suit the settings
configuration of the project.  
  
In the following example, when `forceLowShadows` is `true`, the `SelectIf`
filter attribute forces the `multi_compile` keyword set to only contain the
`SHADOWS_LOW` variant during the build.

    
    
    using UnityEditor.ShaderKeywordFilter;  
      
    [SelectIf(true, keywordNames: "SHADOWS_LOW")]
    bool forceLowShadows;

You can also exclude keywords from the build. In the following example, when
`enableHighShadows` is `false`, the `RemoveIf` filter attribute removes
`SHADOWS_HIGH`.

    
    
    [RemoveIf(false, keywordNames: "SHADOWS_HIGH")]
    bool enableHighShadows;

You can also select or remove more than one keyword at a time. In the
following example, when `onlyHighOrNoShadows` is `true`, the `SelectIf` filter
attribute selects only the `SHADOWS_HIGH` variant and a no shadows variant.  
  
The empty string `""` denotes the empty keyword. You can only select and
remove the empty keyword together with another keyword, because `""` on its
own applies to all `multi_compile` keyword sets with an empty keyword.

    
    
    [SelectIf(true, keywordNames: new string[] {"", "SHADOWS_HIGH"})]
    bool onlyHighOrNoShadows;

You can use `RemoveIfNot` with enum data. The following example removes the
`SHADOWS_LOW` variant if `shadowMode` is set to anything except `Low`.

    
    
    public enum ShadowMode
    {
        Low,
        Med,
        High
    }  
      
    [RemoveIfNot(ShadowMode.Low, keywordNames: "SHADOWS_LOW")]
    ShadowMode shadowMode;

You can use the `overridePriority` argument to use filter attributes to
override filtering you've previously set. Normally the first filter rule
encountered in the type tree targeting a specific keyword takes effect, and
Unity ignores any later attributes. If you use `overridePriority`, attributes
can force the later filter rule to be active instead.  
  
You can add constraint attributes to filter attributes, to determine whether
the filter rule is active in the current context. See
[GraphicsAPIConstraintAttribute](ShaderKeywordFilter.GraphicsAPIConstraintAttribute.html)
and [TagConstraintAttribute](ShaderKeywordFilter.TagConstraintAttribute.html)
for more information.

### Constructors

[FilterAttribute](ShaderKeywordFilter.FilterAttribute-ctor.html)| Tell the
shader system which shader keywords to include in or exclude from the build,
based on the data field underneath.  
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

