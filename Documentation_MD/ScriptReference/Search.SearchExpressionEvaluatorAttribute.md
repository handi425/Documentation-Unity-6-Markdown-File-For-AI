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

# SearchExpressionEvaluatorAttribute

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

Attribute used to register new SearchExpressionEvaluator. This will allow to
use new function in [SearchExpression](Search.SearchExpression.html). As a
side note all builtin evaluators (count{}, select{}, ...) are defined using
this attribute.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    public class SearchExpressionEvaluator_Example
    {
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
    
    
        [[MenuItem](MenuItem.html)("Examples/[ExpressionEvaluator](ExpressionEvaluator.html)/Take First")]
        static void TestTakeFirst()
        {
            var ctx = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("takexfirst{[1,2,3,4], [34, 45, 66], t:script}");
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(ctx);
        }
    
        [[MenuItem](MenuItem.html)("Examples/[ExpressionEvaluator](ExpressionEvaluator.html)/Take 2 First")]
        static void TestTake2First()
        {
            var ctx = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("takexfirst{2, [1,2,3,4], [34, 45, 66], t:script}");
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(ctx);
        }
    
        [Description("Returns ids of current selection")]
        [SearchExpressionEvaluator([SearchExpressionEvaluationHints.ThreadNotSupported](Search.SearchExpressionEvaluationHints.ThreadNotSupported.html))]
        public static IEnumerable<[SearchItem](Search.SearchItem.html)> SelectionIds([SearchExpressionContext](Search.SearchExpressionContext.html) c)
        {
            var instanceIds = UnityEditor.Selection.instanceIDs;
            foreach (var id in instanceIds)
            {
                yield return [SearchExpression.CreateItem](Search.SearchExpression.CreateItem.html)(id, c.ResolveAlias("selected id"));
            }
        }
    
        [[MenuItem](MenuItem.html)("Examples/[ExpressionEvaluator](ExpressionEvaluator.html)/[Selection](Selection.html) ids")]
        static void SelectionIds()
        {
            var ctx = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("selectionids{}");
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(ctx);
        }
    
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
    
        [[MenuItem](MenuItem.html)("Examples/[ExpressionEvaluator](ExpressionEvaluator.html)/[Selection](Selection.html) ids to Paths")]
        static void IdsToPaths()
        {
            var ctx = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("IdsToPaths{selectionids{}}");
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(ctx);
        }
    
        [Description("Convert arguments to a string allowing you to format the result.")]
        [SearchExpressionEvaluator([SearchExpressionType.Selector](Search.SearchExpressionType.Selector.html) | [SearchExpressionType.Text](Search.SearchExpressionType.Text.html), [SearchExpressionType.Iterable](Search.SearchExpressionType.Iterable.html) | [SearchExpressionType.Literal](Search.SearchExpressionType.Literal.html) | [SearchExpressionType.Variadic](Search.SearchExpressionType.Variadic.html))]
        [SearchExpressionEvaluatorSignatureOverload([SearchExpressionType.Iterable](Search.SearchExpressionType.Iterable.html) | [SearchExpressionType.Literal](Search.SearchExpressionType.Literal.html) | [SearchExpressionType.Variadic](Search.SearchExpressionType.Variadic.html))]
        public static IEnumerable<[SearchItem](Search.SearchItem.html)> FormatItems([SearchExpressionContext](Search.SearchExpressionContext.html) c)
        {
            var skipCount = 0;
            if ([SearchExpression.GetFormatString](Search.SearchExpression.GetFormatString.html)(c.args[0], out var formatStr))
                skipCount++;
            var items = c.args.Skip(skipCount).SelectMany(e => e.Execute(c));
            var dataSet = [SearchExpression.ProcessValues](Search.SearchExpression.ProcessValues.html)(items, null, item => [SearchExpression.FormatItem](Search.SearchExpression.FormatItem.html)(c.search, item, formatStr));
            return dataSet;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[ExpressionEvaluator](ExpressionEvaluator.html)/Get Script Paths")]
        static void GetScriptPaths()
        {
            var ctx = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("formatitems{t:script search}");
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)(ctx);
        }
    }
    

### Constructors

[SearchExpressionEvaluatorAttribute](Search.SearchExpressionEvaluatorAttribute-
ctor.html)| Use this attribute to register a static C# function as a new
evaluator. SearchExpressionEvaluator when use within a SearchExpression can
have a signature that is validated against the passed parameters.  
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

