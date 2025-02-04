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

#
[SearchExpression](Search.SearchExpression.html).Execute(SearchContext,SearchExpressionExecutionFlags)

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

### Parameters

searchContext | SearchContext used to initialize the SearchExpressionContext that will encapsulate all information relative to expression evaluation.  
---|---  
executionFlags | Execution flags helping define how to evaluate the expression.  
c | SearchExpressionContext that will encapsulate all information relative to expression evaluation.  
  
### Returns

**void** Returns an enumerable list of SearchItem.

### Description

Execute a SearchEXpression givent a certain
[SearchContext](Search.SearchContext.html) Depending on flags the expression
might be valuated in a worker thread (by default) or in the main thread. It
returns a an enumerable list of [SearchItem](Search.SearchItem.html).

    
    
    [SearchExpressionEvaluator([SearchExpressionType.Iterable](Search.SearchExpressionType.Iterable.html) | [SearchExpressionType.Variadic](Search.SearchExpressionType.Variadic.html))]
    [SearchExpressionEvaluatorSignatureOverload([SearchExpressionType.Number](Search.SearchExpressionType.Number.html), [SearchExpressionType.Iterable](Search.SearchExpressionType.Iterable.html) | [SearchExpressionType.Variadic](Search.SearchExpressionType.Variadic.html))]
    [Description("Extract and returns the X first results for each expression.")]
    public static IEnumerable<[SearchItem](Search.SearchItem.html)> TakeXFirst([SearchExpressionContext](Search.SearchExpressionContext.html) c)
    {
        var argIndex = 0;
        var takeNumber = 1;
        if (c.args[0].types.HasFlag([SearchExpressionType.Number](Search.SearchExpressionType.Number.html)))
        {
            ++argIndex;
            takeNumber = Math.Max((int)(c.args[0].GetNumberValue(takeNumber)), 0);
        }
    
        for ( ; argIndex < c.args.Length; ++argIndex)
        {
            var iterable = c.args[argIndex].Execute(c);
            var taken = 0;
            foreach (var item in iterable)
            {
                if (item == null)
                    yield return null;
                else
                {
                    yield return item;
                    ++taken;
                    if (taken == takeNumber)
                    {
                        c.Break();
                        break;
                    }
                }
            }
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

