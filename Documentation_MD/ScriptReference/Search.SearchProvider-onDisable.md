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

#  [SearchProvider](Search.SearchProvider.html).onDisable

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

public
[Unity.Android.Gradle.Manifest.Action](Unity.Android.Gradle.Manifest.Action.html)
onDisable;

### Description

Called when the SearchWindow is closed. Allows the search provider to release
cached resources.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class LightsSearchProvider
    {
        [SearchItemProvider]
        internal static [SearchProvider](Search.SearchProvider.html) CreateProvider()
        {
            return new [SearchProvider](Search.SearchProvider.html)("example_lights", "Lights")
            {
                filterId = "z:",
                priority = 99999, // Put example provider at a low priority
                showDetailsOptions = [ShowDetailsOptions.Inspector](Search.ShowDetailsOptions.Inspector.html),
                fetchItems = (context, items, provider) => FetchItems(context, provider),
                toObject = (item, type) => item.data as [Light](Light.html),
                onEnable = () => { /*[Cache](Cache.html) some data in here*/ },
                onDisable = () => { /*Clear the cache*/ },
    
                // This provider can be used in the scene view contextually.
                isEnabledForContextualSearch = () => IsFocusedWindowTypeName("[SceneView](SceneView.html)")
            };
        }
    
        static IEnumerable<[SearchItem](Search.SearchItem.html)> FetchItems([SearchContext](Search.SearchContext.html) context, [SearchProvider](Search.SearchProvider.html) provider)
        {
            if (context.empty)
                yield break;
    
            var sceneProvider = [SearchService.GetProvider](Search.SearchService.GetProvider.html)("scene");
            using (var sceneQuery = [SearchService.CreateContext](Search.SearchService.CreateContext.html)(sceneProvider, $"t:light {context.searchQuery}"))
            using (var results = [SearchService.Request](Search.SearchService.Request.html)(sceneQuery))
            {
                var lightIcon = [EditorGUIUtility.FindTexture](EditorGUIUtility.FindTexture.html)("Lighting");
                foreach (var r in results)
                {
                    if (r == null)
                    {
                        // ***IMPORTANT***: Make sure to yield so you do not block the main thread waiting for results.
                        yield return null;
                    }
                    else
                    {
                        yield return provider.CreateItem(context, r.id,
                            r.GetLabel(sceneQuery, true), r.GetDescription(sceneQuery, true),
                            lightIcon, r.ToObject<[GameObject](GameObject.html)>().GetComponent<[Light](Light.html)>());
                    }
                }
            }
        }
    
        static bool IsFocusedWindowTypeName(string focusWindowName)
        {
            return [EditorWindow.focusedWindow](EditorWindow-focusedWindow.html) != null && EditorWindow.focusedWindow.GetType().ToString().EndsWith("." + focusWindowName);
        }
    
        [[MenuItem](MenuItem.html)("Examples/[SearchProvider](Search.SearchProvider.html)/Show lights")]
        public static void ShowLights()
        {
            // Search for directional lights (lights with "directional" in their name)
            [SearchService.ShowWindow](Search.SearchService.ShowWindow.html)([SearchService.CreateContext](Search.SearchService.CreateContext.html)("z:directional"));
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

