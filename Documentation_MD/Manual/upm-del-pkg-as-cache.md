[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-del-pkg-as-cache.html)
  * [中文](/cn/current/Manual/upm-del-pkg-as-cache.html)
  * [日本語](/ja/current/Manual/upm-del-pkg-as-cache.html)
  * [한국어](/kr/current/Manual/upm-del-pkg-as-cache.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-del-pkg-as-cache.html)
  * [中文](/cn/current/Manual/upm-del-pkg-as-cache.html)
  * [日本語](/ja/current/Manual/upm-del-pkg-as-cache.html)
  * [한국어](/kr/current/Manual/upm-del-pkg-as-cache.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)
  * Delete an asset package from the cache

[](upm-ui-remove-asset.html)

Remove imported assets from a project

[](upm-ui-disable.html)

Disable a built-in package

# Delete an asset package from the cache

When you download an asset package (`.unitypackage` file), the Unity Package
Manager stores it in a cache for asset packages. Each time you import a
downloaded package or a custom package, the Unity Package Manager stores it in
the `Assets` directory in your project.

You might want to delete a package from the asset package cache to free up
space on your local hard drive. If drive space is your main reason for
deleting packages from the cache, consider [changing the asset package cache
location](upm-config-cache-as.html).

**Important** :

  * This procedure applies only to [asset packages](AssetPackages.html)A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) that you [downloaded and
imported](upm-ui-import.html) into your project. This procedure doesn’t apply
to **UPM packages** A **Package** managed by the **Unity Package Manager**.
Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) that you installed from a
registry. Some UPM packages also come from the **Asset Store** A growing
library of free and commercial assets created by Unity and members of the
community. Offers a wide variety of assets, from textures, models and
animations to whole project examples, tutorials and Editor extensions. [More
info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore). There is no equivalent procedure
for removing UPM packages from the global cache.

  * Deleting an asset package from the asset package cache doesn’t remove the same package from any projects where you use that package. If you also want to remove the same package from a project, refer to [Remove imported assets from a project](upm-ui-remove-asset.html).

To delete a package from the asset package cache:

  1. Open the **Package Manager** window.

  2. Select the **My Assets** context from the [navigation panel](upm-ui-nav.html).

  3. Select the asset package you want to delete from the [list panel](upm-ui-list.html).

  4. Take note of two important values, which you need for a later step: 
     * The publisher’s name, located below the display name in the [details panel](upm-ui-details.html) of the **Package Manager** window.

     * The **Display name** value, located in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window.

![The publisher name in the Package Manager window \(left\) and the Display
name in the Inspector window \(right\)](../uploads/Main/upm-details-and-
inspector.png) The publisher name in the Package Manager window (left) and the
**Display name** in the Inspector window (right)

  5. Go to the root of the asset package cache: 
     * For Unity Editor 2022.1 or later:

a) Open the Unity Editor’s [Preferences](Preferences.html) window.

b) Select the **Package Manager** category.

c) Click the folder icon beside **My Assets** > **Cache Location**.

d) Select **Show in Explorer** (Windows) or **Reveal in Finder** (macOS).

     * For Unity Editor 2021.3 or earlier:

a) Refer to [Location of downloaded asset package
files](AssetStorePackages.html#asset-location) to determine the cache location
for your operating system.

b) Use your operating system’s file manager application to go to that
directory.

  6. Select the subdirectory that corresponds to the publisher’s name, which you recorded in an earlier step.

![Select the folder for the publisher name to find the .unitypackage
file](../uploads/Main/upm-as-cache.png) Select the folder for the publisher
name to find the .unitypackage file

  7. The publisher’s directory has one or more subdirectories. The publisher determines the names of these subdirectories: 
     * If there is one subdirectory, go into it.
     * If there is more than one subdirectory, explore the subdirectories until you find the one that contains the package you want to delete.
  8. Select the `<name>.unitypackage` file, where `<name>` corresponds to the **Inspector** window’s **Display name** value that you identified in an earlier step.

  9. Delete the file.

This package is now removed from the asset package cache, but any imported
assets remain in any projects where they’re in use.

## Adding the deleted package back to the asset package cache

If the package that you deleted was an asset package, and you want to add this
package back to your cache, refer to [Download and import an asset
package](upm-ui-import.html).

## Additional resources

  * [Package types](upm-package-types.html)
  * [Asset Store packages](AssetStorePackages.html)
  * [Remove imported assets from a project](upm-ui-remove-asset.html)
  * [Download and import an asset package](upm-ui-import.html)

[](upm-ui-remove-asset.html)

Remove imported assets from a project

[](upm-ui-disable.html)

Disable a built-in package

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

