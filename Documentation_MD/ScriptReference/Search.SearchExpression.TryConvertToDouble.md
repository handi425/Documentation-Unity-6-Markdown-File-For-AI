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

#  [SearchExpression](Search.SearchExpression.html).TryConvertToDouble

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

public static bool
TryConvertToDouble([Search.SearchItem](Search.SearchItem.html) item, out
double value, string selector);

### Parameters

item | SearchItem to extract the value from.  
---|---  
value | Resulting value.  
selector | Selector use to access an item value. If null, we will use the internal item value.  
  
### Returns

**bool** Returns true if we were able to select the value and convert it to a
double.

### Description

Resolve a selector on an item and try to convert the selected value to a
double.

    
    
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

