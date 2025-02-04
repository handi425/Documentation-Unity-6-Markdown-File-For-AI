[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-package-types.html)
  * [中文](/cn/current/Manual/upm-package-types.html)
  * [日本語](/ja/current/Manual/upm-package-types.html)
  * [한국어](/kr/current/Manual/upm-package-types.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-package-types.html)
  * [中文](/cn/current/Manual/upm-package-types.html)
  * [日本語](/ja/current/Manual/upm-package-types.html)
  * [한국어](/kr/current/Manual/upm-package-types.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Concepts](upm-concepts.html)
  * Package types

[](upm-concepts.html)

Concepts

[](upm-lifecycle.html)

Package states and lifecycle

# Package types

Unity’s Package Manager supports two package types:

  * **UPM packages** A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) (Unity Package Manager built-in
format).

  * **Asset packages** A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) (`.unitypackage` format).

The following table compares the differentiating characteristics of these
package types:

**Characteristic** | **UPM packages** | **Asset packages**  
---|---|---  
Format | Collection of files and folders, which might be compressed, depending on the distribution method. | A compressed file with a `.unitypackage` extension.  
Primary source for the package | Unity registry, scoped registry, or **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) | Asset Store  
Uses a [package manifest](upm-manifestPkg.html)Each package has a _manifest_ ,
which provides information about the package to the Package Manager. The
manifest contains information such as the name of the package, its version, a
description for users, dependencies on other packages (if any), and other
details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) file | Yes | No  
UI action for adding the package to a project | Install | Download and import  
Project folder the package is added to | `Packages` | `Assets`  
Cache the package is added to | [Global cache](upm-cache.html) | Asset package cache. Refer to [Location of downloaded asset package files](AssetStorePackages.html#asset-location).  
You can manually remove the package from the cache | No | Yes  
Sets of tabs that appear in the [Details panel](upm-ui-details.html) | Description, Version History, Dependencies, Samples (if provided), Images (if provided) | Overview, Releases, Imported Assets, Images  
  
## Additional resources

  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)

[](upm-concepts.html)

Concepts

[](upm-lifecycle.html)

Package states and lifecycle

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

