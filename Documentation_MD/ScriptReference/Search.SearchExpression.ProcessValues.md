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

#  [SearchExpression](Search.SearchExpression.html).ProcessValues

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

public static IEnumerable<SearchItem> ProcessValues(IEnumerable<SearchItem>
items, string outputValueFieldName, Func<SearchItem,T> processHandler);

### Parameters

items | Group of items to transform.  
---|---  
outputValueFieldName | Name of the field in the [SearchItem](Search.SearchItem.html) to write the value to. If null, we write to the internal value of the item.  
processHandler | Transformer function that need to returns a new value for the item.  
  
### Returns

**IEnumerable <SearchItem>** Yield a new list of items that have been
transformed.

### Description

Take a group of SearchItems and apply a processHandler transformer function to
the item in order to sets its internal value or an outputValueField. Note that
these items are processed in the main thread thus allowing you to resolve any
kind of selectors.

    
    
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

