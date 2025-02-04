[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui.html)
  * [中文](/cn/current/Manual/upm-ui.html)
  * [日本語](/ja/current/Manual/upm-ui.html)
  * [한국어](/kr/current/Manual/upm-ui.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui.html)
  * [中文](/cn/current/Manual/upm-ui.html)
  * [日本語](/ja/current/Manual/upm-ui.html)
  * [한국어](/kr/current/Manual/upm-ui.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Package Manager window

[](upm-config-ssh-git-mac.html)

Loading SSH keys automatically on macOS

[](upm-ui-access.html)

Access the Package Manager window

# Package Manager window

Access the Package Manager window from the Unity Editor’s **Window** menu.

Use the Package Manager window to:

  * View which [packages and feature sets](PackagesList.html) are available for installation or already installed in your project.
  * Check [which package versions are available](upm-ui-find.html#VersionList).
  * Install, update, or remove [UPM packages](upm-ui-actions.html)A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) or [feature sets](fs-
install.html)A feature set is a collection of related packages that you can
use to achieve specific results in the Unity Editor. You can manage feature
sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset).

  * Download and import, update, or remove [asset packages](upm-ui-actions-ap.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage).

  * [Disable built-in packages](upm-ui-disable.html).

![The Package Manager window](../uploads/Main/upm-ui.png) The Package Manager
window

The Package Manager window displays:

**(A)** The experimental package indicator, which warns you if your project
has [experimental packages](pack-exp.html).

**(B)** The **install** ![](../uploads/Main/iconAdd.png) button, which you can
click to [install a package](upm-ui-actions.html) directly into your project
by entering a git URL, a local path, or a package name.

**(C)** The [navigation panel](upm-ui-nav.html), which you can use to select a
context to change what appears in the list panel **(H)**.

**(D)** The [Sort](upm-ui-sort.html) menu, which you can use to sort the list
of packages and feature sets by name or date.

**(E)** The [Filter](upm-ui-filter2.html) menu, which you can use to narrow
down which packages appear in the list panel **(H)**. The **Filters** menu and
the **Clear Filters** button are disabled for the **Built-in** list. They’re
also disabled for the **In Project** context (unless you have subscription-
based packages), because that context in the navigation panel has a nested
item for **Updates**.

![The Filters menu and the Clear Filters button](../uploads/Main/upm-ui-asset-
filters.png) The **Filters** menu and the **Clear Filters** button

**(F)** The [search box](upm-ui-search.html), which you can use to look for
packages and feature sets by name.

**(G)** The **Advanced** menu ![](../uploads/Main/iconSettings.png), which you
can use to access the **project settings** A broad collection of settings
which allow you to configure how Physics, Audio, Networking, Graphics, Input
and many other areas of your project behave. [More info](comp-
ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) for the Package Manager and
more. Refer to Advanced settings for details.

**(H)** The [list panel](upm-ui-list.html), which displays packages for the
type you selected in the navigation panel, limited by any filter and search
parameters you specified.

**(I)** The details panel, which displays information specific to the
[package](upm-ui-details.html)A container that stores various types of
features and assets for Unity, including Editor or Runtime tools and
libraries, Asset collections, and project templates. Packages are self-
contained units that the Unity Package Manager can share across Unity
projects. Most of the time these are called _packages_ , but occasionally they
are called **Unity Package Manager (UPM) packages**. [More
info](Packages.html)  
See in [Glossary](Glossary.html#Package) or [feature set](fs-details.html)
selected in the list panel.

**(J)** The package details tabs, which display further information about the
selected package or feature set. The tabs are dynamic, based on the selected
item. For information about these tabs, refer to [Details panel](upm-ui-
details.html).

**(K)** Buttons to perform any of the following actions at the project level:

  * [Install or remove feature sets](fs-install.html)
  * [Install](upm-ui-install.html), [update](upm-ui-update.html), or [remove](upm-ui-remove.html) UPM packages
  * [Download and import](upm-ui-import.html), [update](upm-ui-update2.html), or [remove](upm-ui-remove-asset.html) asset packages
  * [Disable or enable](upm-ui-disable.html) built-in packages
  * Install or remove [services](UnityServices.html)A Unity facility that provides a growing range of complimentary services to help you make games and engage, retain and monetize audiences. [More info](UnityServices.html)  
See in [Glossary](Glossary.html#Services)

**(L)** The status bar, which displays information when the Package Manager
loads packages and feature sets. This information includes errors and warning
messages, the number of **Asset Store** A growing library of free and
commercial assets created by Unity and members of the community. Offers a wide
variety of assets, from textures, models and animations to whole project
examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) packages available, and a link to
load more packages from the Asset Store.

**(M)** The **Refresh list** ![](../uploads/Main/iconReload.png) button lets
you refresh the list of packages displayed. In the **My Assets** context,
**Refresh list** is a menu, which has a **Check for updates** option. You can
use **Check for updates** to check for updates to all packages on your
computer, not just the ones that are visible in the **My Assets** context.

## Advanced settings

The advanced settings ![](../uploads/Main/iconSettings.png) menu allows you to
perform these actions:

**Menu item** | **Action results**  
---|---  
**Project Settings** | Select this item to open the [Package Manager project settings](class-PackageManager.html), where you can:  
  
\- List [pre-release packages](pack-preview.html) when browsing the Unity
Registry.  
\- Add, edit, and remove [scoped registries](upm-scoped.html) in your project.  
**Preferences** | Select this item to view and set [Preferences](Preferences.html) for the Unity Editor and related windows and tools.  
**Manual resolve** | Select this item to force the Package Manager to resolve the project’s packages. If needed, it re-installs altered or missing packages and removes extraneous packages.  
  
## Status bar

The Package Manager displays messages in the status bar at the bottom of the
Package Manager window.

There are typically four status messages that the Package Manager might
display:

  * The first time you open the Package Manager window in a new project, the **Refreshing list** message appears briefly:

![Message for refreshing packages and features](../uploads/Main/upm-ui-
loading.png) Message for refreshing packages and features

This message also appears when you click **Refresh list**
![](../uploads/Main/iconReload.png)

  * When you select the **My Assets** context in the navigation panel, the load bar appears above the date. It displays the number of packages from the Asset Store. Select **Load** to load more packages.

![On the left, the load bar displays the number of My Assets packages loaded
and the total number available.](../uploads/Main/upm-ui-assets-loadbar.png) On
the left, the load bar displays the number of **My Assets** packages loaded
and the total number available.

  * Most of the time, the status bar displays the date and time of when the Package Manager window last refreshed its information. However, if the Package Manager [detects a problem](https://docs.unity3d.com/Manual/upm-errors.html), such as a network issue, the Package Manager prompts you to sign in:

![Network error message](../uploads/Main/upm-ui-errors.png) Network error
message

  * If your network connection is working, but you aren’t signed into your [Unity account](https://id.unity.com/), the Package Manager doesn’t display any packages from the Asset Store. When you select **My Assets** in the navigation panel, the Package Manager prompts you to sign in:

![Logged out of Unity account](../uploads/Main/upm-ui-unityid.png) Logged out
of Unity account

In the list panel, click **Sign in** to sign in to your Unity account through
the [Unity Hub](https://docs.unity3d.com/hub/manual/index.html).

For information on how to resolve these errors and more, refer to [Package
Manager troubleshooting](upm-errors.html).  

## Additional resources

  * [Unity’s Package Manager](Packages.html)
  * [Packages and feature sets](PackagesList.html)
  * [Finding package documentation](upm-docs.html)

[](upm-config-ssh-git-mac.html)

Loading SSH keys automatically on macOS

[](upm-ui-access.html)

Access the Package Manager window

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

