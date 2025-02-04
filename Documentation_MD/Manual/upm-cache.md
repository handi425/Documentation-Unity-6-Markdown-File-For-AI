[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-cache.html)
  * [中文](/cn/current/Manual/upm-cache.html)
  * [日本語](/ja/current/Manual/upm-cache.html)
  * [한국어](/kr/current/Manual/upm-cache.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-cache.html)
  * [中文](/cn/current/Manual/upm-cache.html)
  * [日本語](/ja/current/Manual/upm-cache.html)
  * [한국어](/kr/current/Manual/upm-cache.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Concepts](upm-concepts.html)
  * Global cache

[](upm-dependencies.html)

Dependency and resolution

[](upm-config.html)

Configuration

# Global cache

When the Unity Package Manager fetches **UPM packages** A **Package** managed
by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage), it stores the package contents
and metadata in a global cache. This makes reusing and sharing packages more
efficient, and allows you to install and update stored packages even when
offline.

**Note** : Storing packages in the global cache applies to UPM packages
fetched from a registry. Packages in the UPM format that come from the **Asset
Store** A growing library of free and commercial assets created by Unity and
members of the community. Offers a wide variety of assets, from textures,
models and animations to whole project examples, tutorials and Editor
extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) are also stored in the global
cache. However, [asset packages](AssetPackages.html)A collection of files and
data from Unity projects, or elements of projects, which are compressed and
stored in one file, similar to Zip files, with the `.unitypackage` extension.
Asset packages are a handy way of sharing and re-using Unity projects and
collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) in the `.unitypackage` format
that come from the Asset Store aren’t stored in the global cache. The Package
Manager stores asset packages in a separate cache. For more information, refer
to [Asset Store packages](AssetStorePackages.html).

## Location

By default, Unity stores the global cache in a root directory that depends on
the operating system (and the user account type on Windows):

**Operating system** | **Default root directory** | **Example**  
---|---|---  
Windows (user account) | `%LOCALAPPDATA%\Unity\cache\upm` | `C:\Users\yourname\AppData\Local\Unity\cache\upm`  
Windows ([system user account](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts#default-local-system-accounts)) | `%ALLUSERSPROFILE%\Unity\cache\upm` | `C:\ProgramData\Unity\cache\upm`  
macOS | `$HOME/Library/Caches/Unity/upm` | `/Users/yourname/Library/Caches/Unity/upm`  
Linux | `$HOME/.cache/Unity/upm` | `/home/yourname/.cache/Unity/upm`  
  
**Tip** : You can override the location of this root directory. Refer to
[Customize the global cache](upm-config-cache.html) for more information.

## Structure

The Package Manager global cache uses subsidiary caches, each serving a
different purpose. The Package Manager stores these subsidiary caches in
subfolders under the folder of the global cache:

**Subfolder** | **Description**  
---|---  
`db` | Registry data cache used for storing package content and metadata.  
`git-lfs` | Contains downloaded Git Large File Storage (LFS) files, if you’ve enabled Git LFS.  
`packages` (obsolete) | If you’ve created projects with Unity Editor 2023.2, this subfolder might exist. However, starting with Unity 6, the Package Manager doesn’t use this subfolder.  
  
Inside each of these subfolders, each registry has its own path so that
packages hosted on different registries aren’t mixed up.

**Tip** : You can override the location of these folders. Refer to [Customize
the global cache](upm-config-cache.html) for more information.

## Size

Starting with version 2023.2.0f1 of the Unity Editor, the size of the registry
data cache (the `db` subfolder) is limited to 10 gigabytes (GB). When that
limit is reached, the Package Manager prunes the registry data cache by
evicting the least recently used content (based on oldest date a package was
installed into a project). In other words, the first packages the Package
Manager evicts are the ones you added to a project the longest time ago.
However, although the Package Manager evicts these packages from the cache,
they remain in any projects where you installed them. The next time you add
these packages to a different project, the Package Manager will fetch them
from the appropriate registry, rather than from your cache.

You can override the size of the registry data cache limit. For information,
refer to [Customize the global cache](upm-config-cache.html).

## Requirements

The user account running the Unity Editor process must have full write
permissions on the root directory and its contents. Without these permissions,
the Package Manager can’t download and save the package metadata and contents
in the cache.

## Additional resources

  * [Package types](upm-package-types.html)

[](upm-dependencies.html)

Dependency and resolution

[](upm-config.html)

Configuration

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

