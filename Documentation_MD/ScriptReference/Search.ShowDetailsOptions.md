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

# ShowDetailsOptions

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

Defines what details are shown in the preview inspector panel for the search
view.

![](../StaticFiles/ScriptRefImages/Example_ShowDetailsOptions.png).

    
    
    [SearchItemProvider]
    internal static [SearchProvider](Search.SearchProvider.html) CreateProvider()
    {
        return new [SearchProvider](Search.SearchProvider.html)(id, name)
        {
            filterId = "hex:",
            priority = 99999, // put example provider at a low priority
            showDetailsOptions = [ShowDetailsOptions.Description](Search.ShowDetailsOptions.Description.html) | [ShowDetailsOptions.Preview](Search.ShowDetailsOptions.Preview.html),
            fetchItems = (context, items, provider) =>
            {
                var expression = context.searchQuery;
                if (expression.Length == 6 && IsHex(expression))
                {
                    expression = "#" + expression;
                    items.Add(provider.CreateItem(context, expression, GetColorName(expression),
                        "Look at this " + GetColorName(expression) + " color!",
                        CreateTextureFromColor(expression, 64, 64), null));
                }
                return null;
            },
            fetchPreview = (item, context, size, options) =>
            {
                return CreateTextureFromColor(item.id, (int)size.x, (int)size.y);
            },
        };
    }
    

### Properties

[None](Search.ShowDetailsOptions.None.html)| No options are defined.  
---|---  
[Preview](Search.ShowDetailsOptions.Preview.html)| Show a large preview.  
[Inspector](Search.ShowDetailsOptions.Inspector.html)| Show an embedded
inspector for the selected object.  
[Actions](Search.ShowDetailsOptions.Actions.html)| Shows selected item
possible actions.  
[Description](Search.ShowDetailsOptions.Description.html)| Show an extended
item description.  
[ListView](Search.ShowDetailsOptions.ListView.html)| Indicates that this
search provider wants to display its items in a list view if possible.  
[DefaultGroup](Search.ShowDetailsOptions.DefaultGroup.html)| Indicates that
the provider will always be displayed as a group (tab) even if the result set
is empty.  
[InspectorWithoutHeader](Search.ShowDetailsOptions.InspectorWithoutHeader.html)|
Show an embedded inspector for the selected object. Won't show the editor
header.  
[Default](Search.ShowDetailsOptions.Default.html)| Default set of options used
when SearchProvider.showDetails is set to true.  
  
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

