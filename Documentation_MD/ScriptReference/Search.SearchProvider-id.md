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

#  [SearchProvider](Search.SearchProvider.html).id

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

public string id;

### Description

Search provider unique ID.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Globalization;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class SearchProvider_id
    {
        internal static string id = "example_colors";
        internal static string name = "example_Colors";
    
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
    
    
        [[MenuItem](MenuItem.html)("Examples/[SearchProvider](Search.SearchProvider.html)/id")]
        public static void Run()
        {
            var context = [SearchService.CreateContext](Search.SearchService.CreateContext.html)([SearchService.GetProvider](Search.SearchService.GetProvider.html)(id));
    
            [Debug.Log](Debug.Log.html)(context.providers.First().id);
        }
    
        private static [Texture2D](Texture2D.html) CreateTextureFromColor(string color, int width, int height)
        {
            [Color](Color.html) fillColor;
            if (![ColorUtility.TryParseHtmlString](ColorUtility.TryParseHtmlString.html)(color, out fillColor))
                return null;
            var texture = new [Texture2D](Texture2D.html)(width, height, [TextureFormat.ARGB32](TextureFormat.ARGB32.html), false);
            var fillColorArray = texture.GetPixels32();
    
            for (var i = 0; i < fillColorArray.Length; ++i)
                fillColorArray[i] = fillColor;
    
            texture.SetPixels32(fillColorArray);
    
            texture.Apply();
            return texture;
        }
    
        private static bool IsHex(string expression)
        {
            foreach (var c in expression)
            {
                if (!Uri.IsHexDigit(c))
                    return false;
            }
            return true;
        }
    
        private static string GetColorName(string color)
        {
            if (color[1] > color[3] && color[1] > color[5])
                return "reddish";
            else if (color[3] > color[1] && color[3] > color[5])
                return "greenish";
            else if (color[5] > color[1] && color[5] > color[3])
                return "bluish";
            return "undefined";
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

