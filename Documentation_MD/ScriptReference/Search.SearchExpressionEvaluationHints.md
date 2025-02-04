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

# SearchExpressionEvaluationHints

enumeration

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

Hints provided to the [SearchExpression](Search.SearchExpression.html) runtime
to specify how a certain
[SearchExpressionEvaluatorAttribute](Search.SearchExpressionEvaluatorAttribute.html)
should be executed.

Here is an example of an evaluator not supporting thread evaluation:

    
    
    [Description("Returns asset paths corresponding to a list of instance ids")]
    [SearchExpressionEvaluator("IdsToPaths", [SearchExpressionEvaluationHints.ThreadNotSupported](Search.SearchExpressionEvaluationHints.ThreadNotSupported.html), [SearchExpressionType.Iterable](Search.SearchExpressionType.Iterable.html))]
    public static IEnumerable<[SearchItem](Search.SearchItem.html)> IdsToPath([SearchExpressionContext](Search.SearchExpressionContext.html) c)
    {
        foreach (var idItem in c.args[0].Execute(c))
        {
            if ([SearchExpression.TryConvertToDouble](Search.SearchExpression.TryConvertToDouble.html)(idItem, out var idNum))
            {
                var id = (int)idNum;
                var path = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(id);
                if (!string.IsNullOrEmpty(path))
                {
                    yield return [SearchExpression.CreateItem](Search.SearchExpression.CreateItem.html)(path, c.ResolveAlias("asset path"));
                }
            }
        }
    }
    

### Properties

[ThreadSupported](Search.SearchExpressionEvaluationHints.ThreadSupported.html)|
Specifies that an evaluator supports being evaluated in a worker thread (that
is not the main thread). This is the default evaluation hint.  
---|---  
[ThreadNotSupported](Search.SearchExpressionEvaluationHints.ThreadNotSupported.html)|
Specifies that an evaluator does not support worker thread evaluation and
should only be evaluated in the main thread. This could be the case if an
evaluator is using non-tread safe Unity API (like AssetDatabase).  
[ExpandSupported](Search.SearchExpressionEvaluationHints.ExpandSupported.html)|
Specifies that an evaluator might return SearchItem containing
SearchExpression that supports expansin like groupBy{}.  
[AlwaysExpand](Search.SearchExpressionEvaluationHints.AlwaysExpand.html)| Wehn
evaluating a SearchExpression signifies that each ielded items could be
another SearchExpression that needs evaluation.  
[DoNotValidateSignature](Search.SearchExpressionEvaluationHints.DoNotValidateSignature.html)|
Specifies that the parameters of a SearchExpression shouldn't have their
signature be validated. This is used mostly for meta programming evaluator
lile apply{} where partial evaluator can be used as parameter.  
[DoNotValidateArgsSignature](Search.SearchExpressionEvaluationHints.DoNotValidateArgsSignature.html)|
Specifies that the evaluator signature shouldn't be validated by the
SearchExpression runtime thus allowing any number of parameters with any types
to be passed to the evaluator. It becomes the job of the evaluator itself to
validate its parameters.  
[ImplicitArgsLiterals](Search.SearchExpressionEvaluationHints.ImplicitArgsLiterals.html)|
Specifies that an evaluator assumes its arguments are literal and will be used
as such.  
[Default](Search.SearchExpressionEvaluationHints.Default.html)| Default
evaluation hints. Currently Default is that thread evaluation is supported
(SearchExpressionEvaluationHints.ThreadSupported).  
  
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

