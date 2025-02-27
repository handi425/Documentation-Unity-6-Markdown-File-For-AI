[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/search-usage.html)
  * [中文](/cn/current/Manual/search-usage.html)
  * [日本語](/ja/current/Manual/search-usage.html)
  * [한국어](/kr/current/Manual/search-usage.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/search-usage.html)
  * [中文](/cn/current/Manual/search-usage.html)
  * [日本語](/ja/current/Manual/search-usage.html)
  * [한국어](/kr/current/Manual/search-usage.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity Search](search-overview.html)
  * Search usage

[](search-overview.html)

Unity Search

[](search-filters.html)

Filter searches

# Search usage

To use Search, do the following:

  1. Launch Search
  2. Search
  3. Perform actions on items in the results

## Launch Search

There are several ways to open the Search window:

  * From the Unity menu, choose **Edit** > **Search All**.
  * Click the magnifying glass icon in the top right in the **Editor** window.

Shortcuts:

Shortcut: | Function:  
---|---  
**Ctrl + K** | Open Search  
  
> **Tip:** You can change the keyboard shortcuts used to launch Search from
> the [Shortcuts
> Manager](https://docs.unity3d.com/Manual/ShortcutsManager.html).
>
> **Note:** The last search term you used appears in the search field and the
> last changes you made to the [filter configuration](search-
> filters.html#persistent-search-filters) are still in effect.

### Keep the Search window opening

To keep the window open after selecting a search item, select **Keep Open**
from the **More Options** (**:**) menu.

## Perform searches

To perform searches, type a query into the search field.

For most search queries, using the **Search All** window and the default Asset
index created with your project will find your content effectively.

For more refined searches, use specific [Search Providers](search-
providers.html) and [Search Expressions](search-expressions.html).

To include packages in your search, select **Show package results** from the
**More Options** (**:**) menu.

## View search results

Use **Alt + ↑** (up arrow) and **↓** (down arrow) cycle through the search
history, or choose a saved search from the left pane.

### Change the search results view

Use the sizing slider to change from a list to grid view with thumbnails, or
use the List view icon, the Grid view icon, or the Table view icon in the
bottom right of the **Search** window to change the search view.

![](../uploads/Main/search-window-view-settings.png)

### Add favorite search result items

Click the star next to a search result item to tag that item to appear at the
top of the search list the next time you perform the same search to find it
more easily.

### Search status

To see the search time and the number of results at the bottom of the search
window, select **Show Status** from the **More Options** (**:**) menu.

## Save searches

Saving searches allows you to keep useful searches to reuse as needed. Save
the search to your personal Unity for your own use (User), or to project to
save it as an Asset to make the search available to anyone working on the
project.

To save a search to your personal version of Unity:

  1. Create your search.
  2. Click the drop-down menu next to the Save icon at the top-right of the Search window and choose **Save User**.   
Your search is added to the **Saved Searches** panel in the **Search** window.

  3. To save again after making changes, highlight the search in the **Saved Searches** window and from the Save drop-down menu at the top-right of the Search window, choose **Save <search name>**

You may also click the Save icon next to User in the **Saved Searches** panel.

To save a search to the project:

  1. Create your search.
  2. Click the drop-down menu next to the Save icon at the top-right of the **Search** window and choose **Save Project**.
  3. Enter a file name in the **Save search query** window, and chose **Save**.   
Your search is added to the **Saved Searches** panel in the Search window.

  4. To save again after making changes, highlight the search in the **Saved Searches** window and from the Save drop-down menu at the top-right of the Search window, choose **Save <search name>**

You may also click the Save icon next to Project in the **Saved Searches**
panel.

## Find saved searches

To find a saved search:

  1. Click the magnifying glass icon in the **Saved Searches** panel.
  2. Enter your saved search name, or a part of the name. If found, it will appear in the panel.

## Actions

After you search, you can perform actions on the items Search returns in the
Preview **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) pane or through **More Options**
(**⋮**) . The actions you can perform depend on the type of item.

For example, if Search returns a package, you can install/uninstall it. If
Search returns an Asset, you can select, open, or highlight it in the
Hierarchy window.

  * Every type of item has a default action.
  * Some items support additional actions via a context menu.
  * Some items also support drag and drop actions.

To find out which actions you can perform on different types of items, see the
Search Provider pages for individual search filters.

### Default actions

Every type of item has a default action.

To perform the default action for an item do one of the following:

  * Double-click the item.
  * Select the item and use **Enter**.

**Note:** You can edit the default actions in the **Search** section of the
[**Preferences**](Preferences.html) page.

### Additional actions

Some items support additional actions that you access from the Preview
Inspector menu.

To access the additional actions context menu for an item, do one of the
following:

  * Right-click the item.
  * In the item entry, select **More Options** (**⋮**).

You can also use the **Alt + Enter** shortcut to perform a secondary action on
a selected item without opening the context menu:

### Drag and drop actions

Some Search Providers (for example, the [Asset](search-assets.html)Any media
or data that can be used in your game or project. An asset may come from a
file created outside of Unity, such as a 3D Model, an audio file or an image.
You can also create some asset types in Unity, such as an Animator Controller,
an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) and [Scene](search-scene.html)A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) providers) support drag and drop
actions. You can drag items from the results area to any part of Unity that
supports them, for example, the Hierarchy window, the **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView), or the Inspector.

[](search-overview.html)

Unity Search

[](search-filters.html)

Filter searches

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

