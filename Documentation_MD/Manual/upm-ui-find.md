[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-find.html)
  * [中文](/cn/current/Manual/upm-ui-find.html)
  * [日本語](/ja/current/Manual/upm-ui-find.html)
  * [한국어](/kr/current/Manual/upm-ui-find.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-find.html)
  * [中文](/cn/current/Manual/upm-ui-find.html)
  * [日本語](/ja/current/Manual/upm-ui-find.html)
  * [한국어](/kr/current/Manual/upm-ui-find.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * Finding packages and feature sets

[](fs-details.html)

Features (details panel)

[](upm-ui-filter.html)

Packages list context

# Finding packages and feature sets

The Package Manager window provides several ways to help you find a specific
package or **feature set** A feature set is a collection of related packages
that you can use to achieve specific results in the Unity Editor. You can
manage feature sets directly in Unity’s Package Manager. [More
info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset):

![The navigation panel and several controls at the top of the Package Manager
window help you narrow down the list of packages](../uploads/Main/upm-ui-
find.png) The navigation panel and several controls at the top of the Package
Manager window help you narrow down the list of packages  
---  
**(A)** | [Packages list context](upm-ui-filter.html) | Choose a “context” from the navigation panel to determine which list of packages display. The context might be the source of the package, such as a registry server, the Asset Store, or the Unity Editor itself (for built-in packages). However, the **In Project** context displays only those packages and feature sets that are already installed in the current project, regardless of their origin.  
  
For example, you can choose the **My Assets** context to display only Asset
Store packages available to you in the list, or choose the **In Project**
context to display Asset Store packages, Unity packages, and feature sets that
are already installed in your project.  
**(B)** | [**Sort**](upm-ui-sort.html) | Sort the list in either ascending or descending order by name, published date (**Unity Registry** , **My Registries** , **In Project** only), purchased date (Asset Store packages only), or recently updated (**My Assets** only).   
  
For example, if you want to find an Asset Store package that had a recent
update but you can’t remember the name of it, select **My Assets** , then sort
by **Recently updated** and browse the list to find it.  
  
Sorting affects the items under each collapsible section, but leaves the
sections in place. If you sort from Z-A, the Package Manager reorders all the
feature sets from Z-A inside the **Features** section, and all the packages
under each section, but doesn’t mix the content in the list.  
**(C)** | [**Filters**](upm-ui-filter2.html) | Select options to narrow down the packages listed. Packages listed in **My Assets** have enhanced filtering options:  
  
\- **Status** (Downloaded, Imported, Update available, Unlabeled, Hidden,
Deprecated)  
\- **Categories** (3D, Add-Ons, 2D, Audio, etc.)  
\- **Labels** (Custom labels you define in the Asset Store)  
**(D)** | [Search](upm-ui-search.html) | Use the search box to look for a Unity package or an **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) package by name.  
  
Use these controls to narrow down which packages and feature sets appear in
the [list panel](upm-ui-list.html) and in what order. This makes it easier to
find what you’re looking for, or help you browse when you don’t know exactly
what you want.

When you use several of these controls together, you narrow the set of matches
that appears in the list.

After you find a package from a registry (not Asset Store), you can select it,
then potentially locate a specific version in the [details panel](upm-ui-
details.html). For feature sets, there’s always only one version available, so
you can either [install it or remove it](fs-install.html).

## Finding a specific version

To find a specific package version:

  1. In Unity, open the **Package Manager** window by opening the **Window** menu and selecting **Package Manager**.

  2. If you are looking for a [pre-release package](pack-preview.html), follow these steps:

     * Select **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) under the [Advanced](upm-
ui.html#Advanced) ![](../uploads/Main/iconSettings.png) menu.

![Project Settings opens the Package Manager project settings
window](../uploads/Main/upm-settings.png) Project Settings opens the Package
Manager project settings window

The Package Manager [Project Settings](class-PackageManager.html) window
appears.

     * Under the **Advanced Settings** group, select **Show Pre-release Package Versions**.

     * Close the **Project Settings** window. Any [pre-release packages](pack-preview.html) now appear in the list with the ![](../uploads/Main/iconPre.png) label.

  3. You can either browse the [list of packages](upm-ui-list.html) or find a specific package using one of these methods:

     * [Search for a package](upm-ui-search.html) by name or keyword. **Note:** The context you selected in the navigation panel limits the search scope. For example, if you’re searching for an Asset Store package, make sure you select the **My Assets** context before starting your search. When you switch contexts, the Package Manager window clears the search box. But if you return to the previous context, the Package Manager window restores your search term.
     * [Sort the list](upm-ui-sort.html) (for example, by **Recently updated** , to find the most recently updated packages).
     * [Apply filters](upm-ui-filter2.html) to the list.
  4. Select a package from the [list of packages](upm-ui-list.html).

  5. For packages from the Unity Registry, select the **Version History** tab in the [details panel](upm-ui-details.html). If multiple versions are available, expand the entries to display information specific to each version.

![Version numbers for installed packages display in multiple places and the
recommended version appears on the Update button](../uploads/Main/upm-ui-
update.png) Version numbers for installed packages display in multiple places
and the recommended version appears on the **Update** button

  6. When the **Version History** tab displays, you can perform a variety of actions when you expand a specific version:

     * You can view the changelog for that version and click **Changelog** to view the full list of changes across versions.
     * If you don’t already have this package installed in your project, you can [install](upm-ui-install.html) this version.
     * If another version of this package is already installed in your project, you can [update](upm-ui-update.html) the package to this version.
     * If you installed this package in your project but don’t want it anymore, you can [remove](upm-ui-remove.html) the package from your project.

[](fs-details.html)

Features (details panel)

[](upm-ui-filter.html)

Packages list context

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

