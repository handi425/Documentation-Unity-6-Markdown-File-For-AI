[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/search-providers.html)
  * [中文](/cn/current/Manual/search-providers.html)
  * [日本語](/ja/current/Manual/search-providers.html)
  * [한국어](/kr/current/Manual/search-providers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/search-providers.html)
  * [中文](/cn/current/Manual/search-providers.html)
  * [日本語](/ja/current/Manual/search-providers.html)
  * [한국어](/kr/current/Manual/search-providers.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * Search Providers

[](search-tables.html)

Search tables

[](search-assets.html)

Search Project Assets

# Search Providers

Each type of search has its own Search Provider. A Search Provider allows you
to search and filter content. Each Search Provider has a unique [search
token](search-filters.html#search-tokens). A search token is a text string
that you can use in the search field to search using only a specific Search
Provider.

By default, all searches use Project, Hierarchy, and Settings Search Providers
unless you exclude them.

Search provides additional opt-in Search Providers. Search ignores opt-in
Search Providers unless you explicitly use them. Opt-in Search Providers
differ from default Search Providers in the following ways:

You can only execute them using their search tokens. You cannot combine an
opt-in Search Provider with any other Search Provider.

  * To perform a search using all default Search Providers, enter the search terms in the search field. Results appear as you type.

  * To perform a search using an opt-in Search Provider, prefix the search terms with the Search Provider’s search token.  
  
Open the **More**(**⋮**) menu to view a list of Search Providers and their
prefixes.  

## Default Search Providers

Provider: | Function: | Search token: | Example:  
---|---|---|---  
[Project](search-assets.html)In Unity, you use a project to design and develop
a game. A project stores all of the files that are related to a game, such as
the asset and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) | Searches Project Assets. |  `p:` (for “project”) |  `p:Player`   
  
Searches for Assets that match the term “Player”.  
[Hierarchy](search-scene.html) | Searches GameObjects in the Scene. |  `h:` (for “hierarchy”) |  `h:Main Camera`   
  
Searches the current Scene for GameObjects that match the term “Main Camera”.  
[Settings](search-settings.html) | Searches all [Project Settings](comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) and [Preferences](Preferences.html). | `set:` |  `set:VFX`   
  
Finds Project Settings and Preferences pages that match the term “VFX”.  
  
## Opt-in Search Providers

Provider: | Function: | Search token: | Example:  
---|---|---|---  
[Expression](search-expressions.html) | This token is not required. Search expressions are recognized without a token. |  |   
[Menus](search-menu.html) | Searches the Unity main menu. | `m:` |  `m:TextMesh Pro`  
  
Searches the Unity main menu for commands that contain “TextMesh Pro.”  
Asset Database | Searches the AssetDatabase. This is useful when searching the Editor resource bundle (containing all icons/resources used to build the editor) because those binary resources are not indexed. | `adb:`  
[Calculator](search-calculator.html) | Computes mathematical expressions. | `=` |  `=2*3+29/2`   
  
Calculates the answer to the expression `2*3+29/2`.  
[Files](search-files.html) | Searches for files | `find:` |  `find:Paint Mat`  
  
Searches for all assets paths containing the words paint AND the word mat
(e.g.: PaintBrush_Mat.mat, DryWallPainted_Mat.mat)  
[Static API Method](search-api.html) | Finds and executes static API methods. | `api` |  `#Mesh`   
  
Searches for static API methods with “Mesh” in their names.  
[Packages](search-packages.html)Packages are collections of assets to be
shared and re-used in Unity. The [Unity Package Manager](upm-ui.html) (UPM)
can display, add, and remove packages from your project. These packages are
native to the Unity Package Manager and provide a fundamental method of
delivering Unity functionality. However, the Unity Package Manager can also
display [Asset Store packages](AssetStorePackages.html) that you downloaded
from the Asset Store. [More info](Packages.html)  
See in [Glossary](Glossary.html#Packages) | Searches the Unity package database. | `pkg:` |  `pkg:vector`  
  
Searches the Unity package database for packages that match the term “vector”.  
[Asset Store](search-asset-store.html)A growing library of free and commercial
assets created by Unity and members of the community. Offers a wide variety of
assets, from textures, models and animations to whole project examples,
tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) | Searches the [Unity Asset Store](https://assetstore.unity.com). | `store:` |  `store:texture`   
  
Searches the Unity Asset Store for Assets that match the term “texture”.  
Performance | Searches all the performance trackers available in Unity. This is useful for searching for performance bottlenecks. | `performance:` |   
Logs | Searches the `Editor.log` file | `log:` |  `log:cache`  
  
Searches the `Editor.log` file for information that matches “cache”. |   
  
You can also [create your own Search Providers](api.html).

## Exclude Search Providers

You can exclude specific Search Providers from a regular search. To exclude a
provider, do one of the following:

  * [Mute a provider from the Filters pane](search-filters.html#persistent-search-filters). When you mute a provider, Search does not use it in searches, but its background activities (such as indexing parts of Unity) continue to run.
  * [Disable a provider from the preferences](Preferences.html#search). When you disable a provider, Search does not use it at all, and stops all of its background activities.

[](search-tables.html)

Search tables

[](search-assets.html)

Search Project Assets

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

