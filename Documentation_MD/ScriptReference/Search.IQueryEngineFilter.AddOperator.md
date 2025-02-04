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

#  [IQueryEngineFilter](Search.IQueryEngineFilter.html).AddOperator

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

public [Search.QueryFilterOperator](Search.QueryFilterOperator.html)
AddOperator(string op);

### Parameters

op | The operator identifier.  
---|---  
  
### Returns

**QueryFilterOperator** The added, or existing,
[QueryFilterOperator](Search.QueryFilterOperator.html).

### Description

Add a custom filter operator specific to the filter.

Custom operators defined on a filter take precedence over operators defined
globally on the [QueryEngine](Search.QueryEngine_1.html). This is useful if
you wish to have a custom operator only for a specific filter, or if you wish
to override the default behavior of a built-in operator for a specific filter.
If the operator already exists, the existing operator is returned.

    
    
    // Override global operators with specific operator handlers for this filter
    filter.AddOperator("=").AddHandler(([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev == fv);
    filter.AddOperator("!=").AddHandler(([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev != fv);
    

See [IQueryEngineFilter](Search.IQueryEngineFilter.html) for a complete
example.

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

