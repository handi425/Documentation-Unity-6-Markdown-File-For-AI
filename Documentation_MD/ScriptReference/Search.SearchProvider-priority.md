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

#  [SearchProvider](Search.SearchProvider.html).priority

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

public int priority;

### Description

Hint to sort the search provider. Affects the order of search results and the
order in which search providers are shown in the FilterWindow.

The lowest priority is first.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class SearchProvider_priority
    {
        static string typeColors = "example_colors_priority";
        static string displayNameColors = "example_Colors_priority";
        static string typeFruits = "example_fruits_priority";
        static string displayNameFruits = "example_Fruits_priority";
    
        static List<string> colors = new List<string> { "orange", "red", "green", "blue" };
        static List<string> fruits = new List<string> { "orange", "apple", "banana", "strawberry" };
    
        [SearchItemProvider]
        internal static [SearchProvider](Search.SearchProvider.html) CreateProviderColors()
        {
            return new [SearchProvider](Search.SearchProvider.html)(typeColors, displayNameColors)
            {
                priority = 99991,
                filterId = "c:",
                isExplicitProvider = false,
                fetchItems = (context, items, provider) =>
                {
                    var expression = context.searchQuery;
                    if (colors.Contains(expression))
                    {
                        var id = expression + "(color)";
                        items.Add(provider.CreateItem(context, id, id, id, null, null));
                    }
                    return null;
                }
            };
        }
    
        [SearchItemProvider]
        internal static [SearchProvider](Search.SearchProvider.html) CreateProviderFruits()
        {
            return new [SearchProvider](Search.SearchProvider.html)(typeFruits, displayNameFruits)
            {
                priority = 99992,
                filterId = "f:",
                isExplicitProvider = false,
                fetchItems = (context, items, provider) =>
                {
                    var expression = context.searchQuery;
                    if (fruits.Contains(expression))
                    {
                        var id = expression + "(fruit)";
                        items.Add(provider.CreateItem(context, id, id, id, null, null));
                    }
                    return null;
                }
            };
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchProvider](Search.SearchProvider.html)/priority")]
        public static void Run()
        {
            [SearchService.SetActive](Search.SearchService.SetActive.html)(typeColors);
            [SearchService.SetActive](Search.SearchService.SetActive.html)(typeFruits);
    
            using (var context = [SearchService.CreateContext](Search.SearchService.CreateContext.html)("orange"))
            {
                // For the purpose if this example, we use the flag synchronous to get the items immediately.
                var results = [SearchService.GetItems](Search.SearchService.GetItems.html)(context, [SearchFlags.Synchronous](Search.SearchFlags.Synchronous.html));
                // [Color](Color.html) should be the first one (both items have the same score but color provider has the lowest priority).
                [Debug.Log](Debug.Log.html)(results.Count);
                [Debug.Log](Debug.Log.html)(results[0].description); // "orange(color)";
                [Debug.Log](Debug.Log.html)(results[1].description); // "orange(fruit)";
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

