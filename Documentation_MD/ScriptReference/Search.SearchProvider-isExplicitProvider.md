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

#  [SearchProvider](Search.SearchProvider.html).isExplicitProvider

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

public bool isExplicitProvider;

### Description

This search provider is only active when specified explicitly using the
filterId.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class SearchProvider_isExplicitProvider
    {
        internal static string type = "example_uppercase_isExplicitProvider";
        internal static string displayName = "example_UpperCase_isExplicitProvider";
    
        [SearchItemProvider]
        internal static [SearchProvider](Search.SearchProvider.html) CreateProvider()
        {
            return new [SearchProvider](Search.SearchProvider.html)(type, displayName)
            {
                filterId = "+",
                priority = 99999, // put example provider at a low priority
                isExplicitProvider = true,
                fetchItems = (context, items, provider) =>
                {
                    var expression = context.searchQuery;
                    expression += " -> " + expression.ToUpper();
    
                    items.Add(provider.CreateItem(context, context.searchQuery.ToUpper(), context.searchQuery.ToUpper(), expression, null, null));
                    return null;
                }
            };
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchProvider](Search.SearchProvider.html)/isExplicitProvider")]
        public static void Run()
        {
            [SearchService.SetActive](Search.SearchService.SetActive.html)(type);
            using (var context = [SearchService.CreateContext](Search.SearchService.CreateContext.html)(""))
            {
                // For the context of this example, we set the flag synchronous so we can get the results right away.
                context.options |= [SearchFlags.Synchronous](Search.SearchFlags.Synchronous.html);
                // If we don't specify the filterId for an explicit provider, there will be no results.
                context.searchText = "uppercase String";
    
                var results = [SearchService.GetItems](Search.SearchService.GetItems.html)(context);
                [Debug.Log](Debug.Log.html)(results.Count); // 0;
    
                // Use the filterId for an explicit provider
                context.searchText = "+uppercase String";
                results = [SearchService.GetItems](Search.SearchService.GetItems.html)(context);
                // There should be only one result with that specific description
                [Debug.Log](Debug.Log.html)(results.Count); // 1;
                [Debug.Log](Debug.Log.html)(results[0].description); // "uppercase String -> UPPERCASE STRING";
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

