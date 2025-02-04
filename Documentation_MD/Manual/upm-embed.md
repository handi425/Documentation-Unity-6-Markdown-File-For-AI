[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-embed.html)
  * [中文](/cn/current/Manual/upm-embed.html)
  * [日本語](/ja/current/Manual/upm-embed.html)
  * [한국어](/kr/current/Manual/upm-embed.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-embed.html)
  * [中文](/cn/current/Manual/upm-embed.html)
  * [日本語](/ja/current/Manual/upm-embed.html)
  * [한국어](/kr/current/Manual/upm-embed.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Project manifest](upm-manifestPrj.html)
  * Embedded dependencies

[](upm-manifestPrj.html)

Project manifest

[](upm-git.html)

Git dependencies

# Embedded dependencies

Any package that appears under your project’s `Packages` folder is embedded in
that project. You can create an **embedded package** An _embedded_ package is
a mutable package that you store under the `Packages` directory at the root of
a Unity project. This differs from most packages which you download from a
package server and are immutable. [More info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage) in several ways:

  * Create a new package directly in your project’s `Packages` folder.
  * Manually copy a Unity package from the project’s package cache into your project’s `Packages` folder.
  * [Use a C# script to embed](upm-api.html#Embed) a version of a package that’s already installed.

Embedded packages don’t need to appear in the **project manifest** Each Unity
project has a _project manifest_ , which acts as an entry point for the
Package Manager. This file must be available in the `<project>/Packages`
directory. The Package Manager uses it to configure many things, including a
list of dependencies for that project, as well as any package repository to
query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) as a dependency. However, if
you embedded a version of an installed package, your project manifest still
lists the dependency on the original installed version. In that case, the
package on disk takes priority over the version of the package listed as a
dependency, so it doesn’t need to be removed from the project manifest. For
example, if the project manifest specifies a dependency on version 1.3.1 of
the `com.unity.example` package but the project also has an embedded package
with that name, the Package Manager uses the embedded package, regardless of
its apparent version, instead of downloading version 1.3.1 from the registry.

Make sure you track the contents of your embedded packages, and any changes
you make to it. If your Unity project is under source control, add any
packages embedded in that project to the same source control.

## Creating a new custom package

To embed a new package, create your new package content inside a folder under
the `Packages` folder. For more information, follow the [instructions for
creating your own custom package](CustomPackages.html).

Typically, your new package remains embedded in your project until you are
ready to share it with other users and test it in other projects. Then you can
publish it to a [scoped package registry](upm-scoped.html).

## Copying a Unity package from the cache

A package installed from a registry is **immutable** You cannot change the
contents of an immutable (read-only) package. This is the opposite of
**mutable**. Most packages are immutable, including packages downloaded from
the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable), which means you can’t edit it. If
you want to edit a package, you can make it **mutable** You can change the
contents of a mutable package. This is the opposite of **immutable**. Only
**Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](Glossary.html#Mutable) by copying it to the `Packages`
subfolder in your `Projects` folder. This package type is called an embedded
package, and it overrides what’s in your package cache. Later, you can delete
that embedded package’s folder from the `Packages` subfolder, and the Package
Manager will automatically change to the immutable, cached package.

**Important** : Unity supports the following procedure for creating an
embedded package only. Accessing the package cache folder for any other
purpose is discouraged and not supported by Unity. Don’t manipulate the
contents of the package cache folder.

To find your package’s folder in the cache, locate the installed version
directly in the Unity Editor:

  1. Open the Project window by opening the **Window** menu and selecting **General** > **Project**.

  2. From the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow), find the installed package you
want to embed.

  3. Right-click the folder of the selected package and select **Show in Explorer** (Windows) or **Reveal in Finder** (macOS). That package’s folder opens directly in a file browser and uses the `<package-name>@<fingerprint>` naming convention.

![File browser opened to the package folder under the projects package
cache](../uploads/Main/upm-embed.png) File browser opened to the package
folder under the project’s package cache

  4. Copy the package folder and paste it directly into your project’s `Packages` subfolder, not the `Packages` root folder. Don’t put it inside the `Assets` folder, because the Package Manager doesn’t scan that folder for packages.

  5. Remove the `@<fingerprint>` part of the folder name.

  6. Add the newly embedded package to source control if your project is already under source control.

If you want to delete the embedded package, use your file browser or command
line to locate that package in your `Packages` folder. Consider backing up the
folder for the embedded package, otherwise you’ll lose any changes you made to
the package. Then, delete the folder for that package from your `Packages`
folder. The Package Manager will automatically revert to the immutable, cached
package.

## Additional resources

  * [Use a script to embed a package in your project](upm-api.html#Embed)

[](upm-manifestPrj.html)

Project manifest

[](upm-git.html)

Git dependencies

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

