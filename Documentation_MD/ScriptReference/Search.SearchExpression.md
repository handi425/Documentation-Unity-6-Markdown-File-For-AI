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

# SearchExpression

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

Search expressions allow you to add to the search query language to express
complex queries that cross-reference multiple providers, for example, to
search for all objects in a scene that use a shader that doesn’t compile.  
  
Search expressions can be chained together to transform or perform set
manipulations on Search Items.  
  
The manual contains example on [How to use Search
Expression](https://docs.unity3d.com/Documentation/Manual/search-
expressions.html) .

These examples show how SearchExpression are used in an evaluator:

    
    
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
    

### Properties

[alias](Search.SearchExpression-alias.html)| Alias name of an expression. This
is useful to assign a more readable results to methematic expression (lile
Count).  
---|---  
[innerText](Search.SearchExpression-innerText.html)| This is the inner text of
the expression. This means the text without any special delimiters. Ex: the
expression [1, 2, 3] which is a set expression would have an innerText of
1,2,3.  
[name](Search.SearchExpression-name.html)| The name of the evaluator function
or hte outer text. This is mostly a debuggin field.  
[outerText](Search.SearchExpression-outerText.html)| This is the outer text of
the expression. This means the full text with any special delimiters. Ex: the
expression [1, 2, 3] which is a set expression would have an outerText of
[1,2,3].  
[parameters](Search.SearchExpression-parameters.html)| The parameter list of
the expression. Note that each parameter is an expression in itself.  
[types](Search.SearchExpression-types.html)| Aggrregate types of the
expression. This is mostly used to validate parameters of an expression.  
  
### Public Methods

[Execute](Search.SearchExpression.Execute.html)| Execute a SearchEXpression
givent a certain SearchContext Depending on flags the expression might be
valuated in a worker thread (by default) or in the main thread. It returns a
an enumerable list of SearchItem.  
---|---  
[GetBooleanValue](Search.SearchExpression.GetBooleanValue.html)| Try to parse
the innerText and convert it to a boolean value.  
[GetNumberValue](Search.SearchExpression.GetNumberValue.html)| Try to parse
the innerText and convert it to a double value.  
[IsKeyword](Search.SearchExpression.IsKeyword.html)| Check if the innerText of
an expression is a builtin SearchExpressionKeyword.  
[ToString](Search.SearchExpression.ToString.html)| Convert an expression to a
string representation.  
  
### Static Methods

[Check](Search.SearchExpression.Check.html)| Execute a SearchExpression and
checks if the internal value of the first yielded SearchItem is truish. Not 0,
not null, not "" and not false.  
---|---  
[CreateId](Search.SearchExpression.CreateId.html)| Generate a unique id. This
is useful when creating new SearchItem.  
[CreateItem](Search.SearchExpression.CreateItem.html)| Create a new SearchItem
from a value with an optional label.  
[FormatItem](Search.SearchExpression.FormatItem.html)| Take a format string
and replace all selectors in it with the selected values obtained from a
SearchItem.  
[GetFormatString](Search.SearchExpression.GetFormatString.html)| Extract a
format string from a given expression. This function should be used to extract
a format string from an input parameter of a SearchExpression. For example:
the evaluator print{"this is it: @label"} takes a format string as its first
parameter.  
[IsTrue](Search.SearchExpression.IsTrue.html)| Check if the internal value of
a SearchItem is truish. It means the value is not 0, not null, not "" and not
false.  
[ProcessValues](Search.SearchExpression.ProcessValues.html)| Take a group of
SearchItems and apply a processHandler transformer function to the item in
order to sets its internal value or an outputValueField. Note that these items
are processed in the main thread thus allowing you to resolve any kind of
selectors.  
[TryConvertToDouble](Search.SearchExpression.TryConvertToDouble.html)| Resolve
a selector on an item and try to convert the selected value to a double.  
  
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

