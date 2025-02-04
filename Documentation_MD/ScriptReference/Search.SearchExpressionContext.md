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

# SearchExpressionContext

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

This context encapsulate all the datas needed to evaluate a
[SearchExpression](Search.SearchExpression.html) and it allows user to
interact with the evaluation runtime of an expression. A
SearchExpressionContext is created automatically with a
[SearchExpressionRuntime](Search.SearchExpressionRuntime.html) anytime
[SearchExpression.Execute](Search.SearchExpression.Execute.html) is called.

Here is an example showing ow the SearchExpressionContext is used during
evaluation:

    
    
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
    

### Properties

[args](Search.SearchExpressionContext-args.html)| Arguments of passed to the
SearchExpression being evaluated.  
---|---  
[expression](Search.SearchExpressionContext-expression.html)|
[[]SearchExpression] being evaluated.  
[items](Search.SearchExpressionContext-items.html)|  SearchItems yielded by
the evaluation of a searchExpression.  
[runtime](Search.SearchExpressionContext-runtime.html)|
SearchExpressionRuntime associated with this context. The runtime stores all
runtime data (stack frames, stack of contex and items) necessary for
evaluation of a SearchExpression.  
[search](Search.SearchExpressionContext-search.html)| SearchContex containing
the search query that was parsed to create the SearchExpression.  
[valid](Search.SearchExpressionContext-valid.html)| Is the current context
valid or not. If invalid it means the associated SearchExpression is null or
the SearchExiressionRuntime is invalid.  
  
### Public Methods

[Break](Search.SearchExpressionContext.Break.html)| Break the evaluation of a
SearchExpression meaning items won't be yielded anymore.  
---|---  
[Continue](Search.SearchExpressionContext.Continue.html)| Tell
SearchExpression evaluation to continue.  
[IsBreaking](Search.SearchExpressionContext.IsBreaking.html)| Has the current
context being flagged to break execution?  
[IsContinuing](Search.SearchExpressionContext.IsContinuing.html)| Has the
current context being flagged to continue execution?  
[ResetIterationControl](Search.SearchExpressionContext.ResetIterationControl.html)|
Restart evaluation and iteration of SearchExpression.  
[ResolveAlias](Search.SearchExpressionContext.ResolveAlias.html)| Try to
resolve an alias value using the SearchExpressionRuntime attached to this
context. Each frame if asked to resolve a SearchExpression.alias.  
[ThrowError](Search.SearchExpressionContext.ThrowError.html)| Stop a
SearchExpression evaluation by throwing a SearchExceptionEvaluatorException.
User writing an evaluator can decide to throw thse exceptions if the
parameters passed to evaluation are not valid or if a problem happens during
evaluation.  
[ToString](Search.SearchExpressionContext.ToString.html)| Get string
representation of a context.  
  
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

