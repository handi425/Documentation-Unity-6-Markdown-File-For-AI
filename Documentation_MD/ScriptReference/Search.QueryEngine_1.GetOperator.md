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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).GetOperator

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
GetOperator(string op);

### Parameters

op | The operator identifier.  
---|---  
  
### Returns

**QueryFilterOperator** The global
[QueryFilterOperator](Search.QueryFilterOperator.html).

### Description

Get a custom operator added on the [QueryEngine](Search.QueryEngine_1.html).

This method returns a [QueryFilterOperator](Search.QueryFilterOperator.html)
that was added on the [QueryEngine](Search.QueryEngine_1.html). If the
operator does not exist, the
[QueryFilterOperator](Search.QueryFilterOperator.html) will be invalid (see
[QueryFilterOperator.valid](Search.QueryFilterOperator-valid.html)).

    
    
    // Get an operator based on its token and add some handlers on it.
    var operatorToken = "%";
    var operatorObject = queryEngine.GetOperator(operatorToken);
    if (operatorObject.valid)
        operatorObject.AddHandler((float ev, float fv) => Math.Abs(ev % fv) < 0.0000001f);
    

See [AddOperator](Search.QueryEngine_1.AddOperator.html) for a complete
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

