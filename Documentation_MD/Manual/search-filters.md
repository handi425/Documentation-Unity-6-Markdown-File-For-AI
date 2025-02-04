[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/search-filters.html)
  * [中文](/cn/current/Manual/search-filters.html)
  * [日本語](/ja/current/Manual/search-filters.html)
  * [한국어](/kr/current/Manual/search-filters.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/search-filters.html)
  * [中文](/cn/current/Manual/search-filters.html)
  * [日本語](/ja/current/Manual/search-filters.html)
  * [한국어](/kr/current/Manual/search-filters.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * [Search usage](search-usage.html)
  * Filter searches

[](search-usage.html)

Search usage

[](search-query-operators.html)

Search query operators

# Filter searches

Filtering narrows the scope of your searches to specific providers. You can
filter searches in the following ways:

  * Set up persistent search filters to control which providers Search uses for regular searches.

  * Use a Search Provider’s search token in the search field to only display results from that provider.

  * Limit your search results by using sub-filters and [query operators](search-query-operators.html) and using the [keywords](search-index-manager.html#index-results) available for your index.

  * See a list of additional search filters [here](search-additional-searchfilters.html).

## Persistent search filters

You can temporarily toggle Search Providers on and off from the Filters pane.
This can help reduce the number of items that a search returns, which is
convenient if you already know what type of item you are looking for. The
providers that are toggled on at any given time are the active Search
Providers.

![](../uploads/Main/search-filter-search-providers-1.png)  
_Search Providers drop-down menu_

To set persistent search filters:

  1. In the main menu, go to **Edit** > **Search** > **Search All** to launch Search.
  2. In the Search Providers area select **More Options** (**⋮**)
  3. Enable or disable any Search Providers you want to include/exclude from subsequent searches.

## Search tokens

Every Search Provider has a unique text string called a search token, also
called a filter ID. When you prefix a search query with a provider’s search
token, Search limits the scope of the search to that provider.

For example, `p:` is the search token for the Asset Search Provider. When you
enter `p:Player` in the search field, Search searches for Assets that match
the term “Player” (for example, assets with “Player” in their names).

See [Search Providers](search-providers.html) for a list of search tokens for
Search Providers.

See [Additional search tokens](search-additional-searchfilters.html) for a
list of search tokens for **Prefabs** An asset type that allows you to store a
GameObject complete with components and properties. The prefab acts as a
template from which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab), Files, Types, Properties, and
Dependencies searches.

## Combining search tokens

You can combine search tokens to create more complex queries.

  * The queries are written on one line with one character space between tokens.
  * The character space between each new token is an “And” operation, so both filters must be true for the query to return a result. Add another [operator](search-query-operators.html) (or, <, >) to return different results.
  * If a Search Provider filter token (h:, p:) is used, it must be the first component in the query.

Here are a few examples:

Query | Description  
---|---  
`h: t:meshrenderer p(castshadows)!="Off"` | Searches all static meshes in a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that cast a shadow.  
`h: t:light p(color)=#FFFFFF p(intensity)>7.4` | Searches all lights in a Scene with a specific color with brightness higher than 7.4.  
`h: path:/Collectables t:collectable` | Find all objects with a component `Collectable` located in the path `/Collectables.`  
  
## Search expressions

Search expressions allow you to add to the search query language to express
complex queries that cross-reference multiple providers, for example, to
search for all objects in a scene that use a **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that doesn’t compile. See [Search
expressions](search-expressions.html) for more information.

[](search-usage.html)

Search usage

[](search-query-operators.html)

Search query operators

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

