[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-update.html)
  * [中文](/cn/current/Manual/upm-ui-update.html)
  * [日本語](/ja/current/Manual/upm-ui-update.html)
  * [한국어](/kr/current/Manual/upm-ui-update.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-update.html)
  * [中文](/cn/current/Manual/upm-ui-update.html)
  * [日本語](/ja/current/Manual/upm-ui-update.html)
  * [한국어](/kr/current/Manual/upm-ui-update.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * Switch to another version of a UPM package

[](upm-ui-remove.html)

Remove a UPM package from a project

[](upm-ui-actions-ap.html)

Add and remove asset packages

# Switch to another version of a UPM package

Use the information on this page to update **UPM packages** A **Package**
managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) that you installed from the [Unity
Registry](upm-ui-install.html) or a [scoped registry](upm-scoped.html), or
from a [local source](upm-ui-local.html). The information on this page also
applies to packages you [installed from the Asset Store](upm-ui-
install2.html), if they’re in the UPM format.

If you want to install a specific version of a package, refer to [install the
package by name](upm-ui-quick.html) and follow its optional step to specify a
version.

If you want to update packages that you installed from a Git URL, you can use
any of the following methods:

  * Locate the package in the **Package Manager** window, select it, then click the **Update** button.
  * [Reinstall the package as a Git dependency](upm-ui-giturl.html) using a new revision. For more information about how to specify revisions with **Git dependencies** The Package Manager retrieves Git dependencies from a Git repository directly rather than from a package registry. Git dependencies use a Git URL reference instead of a version, and there’s no guarantee about the package quality, stability, validity, or even whether the version stated in its `package.json` file respects Semantic Versioning rules with regards to officially published releases of this package. [More info](upm-concepts.html#Git)  
See in [Glossary](Glossary.html#Gitdependency), refer to [Targeting a specific
revision](upm-git.html#revision).

  * Reinstall the package from the Unity Registry.

To update a package:

  1. Open the **Package Manager** window and select **In Project** , **Unity Registry** , or **My Registries** from the [navigation panel](upm-ui-nav.html). You can also select the **Updates** entry, which lists all packages in your project that have updates available. An arrow icon (![](../uploads/Main/iconUpdate.png)) appears next to packages that have updates available.

  2. Select the installed package you want to update from the [list of packages](upm-ui-list.html). The package information appears in the [details panel](upm-ui-details.html). 

  3. The lock icon (![](../uploads/Main/iconLock.png)) indicates that this package and version is locked to an installed **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset). To unlock the package and select
another version, click the **Unlock** button.

**Note** : The package is temporarily unlocked. If you select a different
context in the [navigation panel](upm-ui-nav.html), or close either the
**Package Manager** window or the Unity Editor, the package reverts to a
locked state. However, if you change versions when the package is unlocked
(for example, with the [Install a package from a registry by name](upm-ui-
quick.html) method), the package stays unlocked.

  4. Select a package in the [list of packages](upm-ui-list.html).

![A package that has an available update](../uploads/Main/upm-ui-update-
list.png) A package that has an available update

  5. In the [details panel](upm-ui-details.html), select the **Version History** tab. If multiple versions are available, expand the entries to view information specific to each version.

![Version numbers for installed packages display in multiple places and the
recommended version appears on the Update to #.#.#
button](../uploads/Main/upm-ui-update.png) Version numbers for installed
packages display in multiple places and the recommended version appears on the
**Update to #.#.#** button

  6. Click the **Update to #.#** button, or click the **Update** button beside the version listed in the **Version History** tab.

When the progress bar finishes, any new functionality is immediately
available.

**Notes:**

  * If you switch to an older version of a package, you might have to run the [API Updater](APIUpdater.html) on the package contents.
  * You can switch versions for multiple packages with one click by using the multiple select feature. For more information, refer to [Perform an action on multiple packages or feature sets](upm-ui-multi.html).

## Additional resources

  * [Package types](upm-package-types.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)

[](upm-ui-remove.html)

Remove a UPM package from a project

[](upm-ui-actions-ap.html)

Add and remove asset packages

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

