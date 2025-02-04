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

# SearchExpressionRuntime

struct in UnityEditor.Search

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

Encapsulate all the runtime data needed to evaluate a root expression and all
its parameters. This class contains the
[SearchContext](Search.SearchContext.html) that created the root
[SearchExpression](Search.SearchExpression.html) and all the stack frames
needed to evaluate all the nested
[SearchExpression](Search.SearchExpression.html).

### Properties

[current](Search.SearchExpressionRuntime-current.html)| Current
SearchExpressionContext corresponding to the stack frame being evaluated.  
---|---  
[frames](Search.SearchExpressionRuntime-frames.html)| The stack of all
SearchExpressionContext being evaluated.  
[items](Search.SearchExpressionRuntime-items.html)| The stack of SearchItems
that have been yielded by each execution frame.  
[search](Search.SearchExpressionRuntime-search.html)| Initial SearchContext
contaning the text that was used to parse the initial root SearchExpression.  
[valid](Search.SearchExpressionRuntime-valid.html)| Is the current runtime
valid. This means are there any SearchExpressionContext being evaluated.  
  
### Public Methods

[Push](Search.SearchExpressionRuntime.Push.html)| Push a new SearchExpression
with its arguments to be evaluated. This is useful if a user defined evaluator
needs to generate a new Context of evaluation.  
---|---  
[ToString](Search.SearchExpressionRuntime.ToString.html)| Get a string
representation of the current SearchExpressionRuntime.  
  
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

