[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-details.html)
  * [中文](/cn/current/Manual/upm-ui-details.html)
  * [日本語](/ja/current/Manual/upm-ui-details.html)
  * [한국어](/kr/current/Manual/upm-ui-details.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-details.html)
  * [中文](/cn/current/Manual/upm-ui-details.html)
  * [日本語](/ja/current/Manual/upm-ui-details.html)
  * [한국어](/kr/current/Manual/upm-ui-details.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * Details panel

[](upm-ui-list.html)

List panel

[](fs-details.html)

Features (details panel)

# Details panel

The right panel of the Package Manager window displays details for the
selected package.

![Package details for a Unity Package Manager \(UPM\) package \(left\) and an
asset package \(right\)](../uploads/Main/upm-ui-details.png) Package details
for a Unity Package Manager (UPM) package (left) and an asset package (right)

These details include the following information:

**(A)** The display name.

**(B)** The [package version](upm-ui-find.html#VersionList), the date the
package was published to the registry or the Asset Store, and any [source or
asset labels](upm-ui-details.html#Tags). Other information might display, if
applicable:

  * An information tooltip (![](../uploads/Main/iconInfo.png)) might also appear before the version. You can click the tooltip for more information about the package. This tooltip can appear, for example, if the package version [you requested doesn’t match](upm-dependencies.html#overridden-version) the version installed.
  * For Unity Package Manager (UPM) packages, a lock icon (![](../uploads/Main/iconLock.png)) appears before the version number when an installed **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset) requires the selected package.
Locking the package prevents you from accidentally [changing the version](upm-
ui-update.html) of the package so the feature set continues to work
effectively.

**(C)** The registry that hosts the package and the package author (UPM
packages), or the package publisher (Asset Store).

**(D)** The package name (UPM packages only).

**(E)** Links to additional resources:

  * For **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage): links to [open the package
documentation](upm-docs.html) page, the package changelog (if available), and
the license information.

  * For **asset packages** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage): links to open the package’s
official page on the Asset Store, and links to the publisher’s support page
and their website (if available).

**(F)** Package details tabs, which vary by package type:

  * For UPM packages: 
    * **Description** : A brief description of the package.
    * **Version History** : Package Manager always lists the installed or recommended package versions, with action buttons to [install](upm-ui-install.html), [update](upm-ui-update.html), or [remove](upm-ui-remove.html). If other supported versions are available and compatible with your version of the Unity Editor, the Package Manager lists those as well. Expand each entry to check the release date, changelog for that version, and a link to the full changelog.
    * **Dependencies** : Dependency information for the package. This section lists dependencies in two directions: 
      * **Is using** : Whether this package depends on another package, and if so, which version. Installed packages display the status of the dependencies after the version number.
      * **Used by** : Whether another package depends on this one, and if so, which version.
    * **Samples** : This tab displays only if the package author provided samples. The tab displays a description and an **Import** button next to the sample.
  * For asset packages: 
    * **Overview** : Information about the package: 
      * Any [custom labels](AssetPackagesLabels.html) you assigned to this package on the Asset Store.
      * The supported versions of Unity.
      * The disk space required.
      * The date you acquired this package from the Asset Store.
      * A brief description of the package.
    * **Releases** : Release information, including the release date of the original package and the release date of the current package.
    * **Imported Assets** : Lists the items from the asset package that you imported into your project. This tab appears only after you download a package and import it into your project.
    * **Images** : Thumbnails of the marketing images, audio, and video available on the Asset Store.

**(G)** Button(s) to [unlock](upm-ui-update.html#fs-lock), [install](upm-ui-
install.html), [update](upm-ui-update.html), [remove](upm-ui-remove.html), or
[disable](upm-ui-disable.html) a Unity package.

**(H)** Controls to [download and import](upm-ui-import.html), or
[remove](upm-ui-remove-asset.html) an asset package, and controls to [update
an asset package](upm-ui-update2.html). Sometimes these controls are buttons.
Other times, the control is a menu with the most common action displayed
first. The **Package Manager** window displays **In Project** (and a check
mark) when your project and cache are up-to-date with the latest version of an
asset package. Specifically, it means at least one item from that package is
at the latest level. However, you can still select other actions from the menu
when **In Project** is displayed.

## Labels

Some packages display labels next to the package name or version number. These
labels offer information about the source or state of the package:

  * [Source](upm-concepts.html#Sources) label types indicate where the package originates from (for example, whether it comes from a local folder or if you downloaded it from a package registry).
  * [State](upm-lifecycle.html) label types indicate the package’s stage of the development cycle. For example, whether it’s an experimental package or on the release track for a specific Unity version. If the Package Manager window displays a package without any state-based labels, it means the package is in the Released state.
  * [Asset Store](AssetStore.html)A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) labels indicate that the package
originated from the Asset Store. These labels might also indicate a special
status (for example, deprecated).

Some source labels imply state labels and vice versa. For example, if you
embedded a package in your project, then Unity automatically assumes it’s a
custom package in development, so only the **custom** label appears in the
[details panel](upm-ui-details.html).

The Package Manager window displays the following values:

**Label** | **Type** | **Meaning**  
---|---|---  
[Release Candidate](pack-releasecandidate.html) | state | This version of the package is on track to be fully released within the next Tech Stream of the current release cycle.  
[Pre-Release](pack-preview.html) | state | This version of the package is at an earlier stage of development, but Unity guarantees to release it by the end of the Long Term Support (LTS) release cycle. It might not yet have complete documentation or be fully validated by either the development team or Unity’s Quality Assurance team.  
[Experimental](pack-exp.html) | state | These packages are either new packages or contain experimental modifications. Unity doesn’t support Experimental packages because they’re in the early stages of development.  
[Deprecated](pack-deprecated.html) | state | These packages are no longer under development for that Unity Editor version, or a specific version of a package has a critical issue. Unity doesn’t support Deprecated packages.  
[Custom](upm-lifecycle.html) | state,  
source | This package is [embedded](upm-concepts.html#Embedded) in your project. Most custom package developers start by embedding a new package in their project, which is why the **Custom** label appears.  
[local](upm-concepts.html#Local) | source | The Package Manager installed this package from a folder or tarball file on your local disk external to your Unity project folder.  
[git](upm-git.html) | source | The Package Manager installed this package in your project directly from a Git repository.  
[asset store](AssetPackagesPurchase.html) | asset | This is an asset package that you purchased or downloaded from the Asset Store.  
[deprecated](AssetStoreAdmin.html#pkg-status) | asset | This package is no longer available on the Asset Store, unless you have downloaded or purchased it before. In other words, it’s no longer discoverable by new customers.  
  
## Additional resources

  * [Package types](upm-package-types.html)

[](upm-ui-list.html)

List panel

[](fs-details.html)

Features (details panel)

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

