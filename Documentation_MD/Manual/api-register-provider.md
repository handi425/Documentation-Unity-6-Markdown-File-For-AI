[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/api-register-provider.html)
  * [中文](/cn/current/Manual/api-register-provider.html)
  * [日本語](/ja/current/Manual/api-register-provider.html)
  * [한국어](/kr/current/Manual/api-register-provider.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/api-register-provider.html)
  * [中文](/cn/current/Manual/api-register-provider.html)
  * [日本語](/ja/current/Manual/api-register-provider.html)
  * [한국어](/kr/current/Manual/api-register-provider.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * [Creating a custom Search Provider](api.html)
  * Registering a Search Provider

[](api-search-provider-class.html)

The SearchProvider class

[](api-searching.html)

Performing a search

# Registering a Search Provider

To add a new Search Provider, create a function and tag it with the
[`SearchItemProvider`](../ScriptReference/Search.SearchItemProviderAttribute.html)
attribute, as in the following example:

    
    
    [SearchItemProvider]
    internal static SearchProvider CreateProvider()
    {
        return new SearchProvider(type, displayName)
        {
            filterId = "me:",
            fetchItems = (context, items, provider) =>
            {
                var itemNames = new List<string>();
                var shortcuts = new List<string>();
                GetMenuInfo(itemNames, shortcuts);
    
                items.AddRange(itemNames.Where(menuName =>
                        SearchProvider.MatchSearchGroups(context.searchText, menuName))
                    .Select(menuName => provider.CreateItem(menuName,
                                                Path.GetFileName(menuName), menuName)));
            },
    
            fetchThumbnail = (item, context) => Icons.shortcut
        };
    }
    

  * The function must return a new `SearchProvider` instance.
  * The `SearchProvider` instance must have the following:
  * A unique `type`. For example, **Asset** , **Menu** , or ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)**.

  * A `displayName` to use in the [Filters pane](search-filters.html#persistent-search-filters).
  * The optional `filterId` provides a search token for [text-based filtering](search-filters.html#search-tokens). For example, `p:` is the filter ID for [Asset searches](search-assets.html).

## Registering a Search Provider shortcut

To register a shortcut for a new provider, use:

    
    
    [UsedImplicitly, Shortcut("Help/Quick Search/Assets")]
    private static void PopQuickSearch()
    {
        // Open Search with only the "Asset" provider enabled.
        SearchService.ShowContextual("asset");
    }
    

You can map shortcuts to keys or key combinations using the [shortcuts
manager](https://docs.unity3d.com/Manual/ShortcutsManager.html).

[](api-search-provider-class.html)

The SearchProvider class

[](api-searching.html)

Performing a search

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

