[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-manifestPrj.html)
  * [中文](/cn/current/Manual/upm-manifestPrj.html)
  * [日本語](/ja/current/Manual/upm-manifestPrj.html)
  * [한국어](/kr/current/Manual/upm-manifestPrj.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-manifestPrj.html)
  * [中文](/cn/current/Manual/upm-manifestPrj.html)
  * [日本語](/ja/current/Manual/upm-manifestPrj.html)
  * [한국어](/kr/current/Manual/upm-manifestPrj.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Project manifest

[](upm-conflicts-auto.html)

Lock files

[](upm-embed.html)

Embedded dependencies

# Project manifest

When Unity loads a project, the Unity Package Manager reads the **project
manifest** so that it can compute a list of which packages to retrieve and
load. When a user installs or uninstalls a package through the [Package
Manager window](upm-ui.html), the Package Manager stores those changes in the
project manifest file. The project manifest file manages the list of packages
through the dependencies object.

In addition, the project manifest serves as a configuration file for the
Package Manager, which uses the manifest to customize the registry URL and
register custom registries.

You can find the project manifest file, called `manifest.json`, in the
`Packages` folder under the root folder of your Unity project. Like the
[package manifest file](upm-manifestPkg.html), the project manifest file uses
JSON (JavaScript Object Notation) syntax.

## Properties

All properties are optional. However, if your project manifest file does not
contain any values, the Package Manager window doesn’t load, and the Package
Manager doesn’t load any packages.

**Key** | **JSON Type** | **Description**  
---|---|---  
**dependencies** | Object | Collection of packages required for your project. This includes only direct dependencies (indirect dependencies are listed in [package manifests](upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest)). Each entry maps the
[package name](upm-manifestPkg.html#name) to the minimum [version](upm-
semver.html) required for the project:  
  
`{`  
`"dependencies": {`  
`"com.my-package": "2.3.1",`  
`"com.my-other-package": "1.0.1-preview.1",`  
`etc.`  
`}`  
`}`  
  
Specifying a version number indicates that you want the Package Manager to
download the package from the package registry (that is, the [source](upm-
concepts.html#Sources) of the package is the registry). However, in addition
to using [versions](upm-manifestPkg.html#version), you can also specify a
[path to a local folder or tarball file](upm-localpath.html), or a [Git
URL](upm-git.html).  
  
**Note** : You do not need to specify [embedded](upm-embed.html) packages here
because the Package Manager finds them inside your project’s `Packages` folder
and loads them automatically. The Package Manager ignores any entry if there
is an embedded package with the same [name](upm-manifestPkg.html#name) in its
own package manifest.  
**enableLockFile** | Boolean | Enables a lock file to ensure that dependencies are resolved in a deterministic manner. This is set to `true` by default. For more information, see [Using lock files](upm-conflicts-auto.html).  
**resolutionStrategy** | String | Upgrades [indirect dependencies](upm-dependencies.html)An **indirect** , or transitive dependency occurs when your project requests a package which itself “depends on” another package. For example, if your project depends on the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package, then your project has an direct dependency on Alembic and an indirect dependency on Timeline. [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) based on Semantic
Versioning rules. This is set to `lowest` by default. For more information,
see Setting a resolution strategy below.  
**scopedRegistries** | Array of Objects | Specify custom registries in addition to the default registry. This allows you to host your own packages.   
  
See [Scoped Registries](upm-scoped.html) for more details.  
**testables** | Array of Strings | Lists the names of packages whose tests you want to load in the Unity [Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)The Test Framework package (formerly called the Test Runner) is a Unity tool that tests your code in both Edit mode and Play mode, and also on target platforms such as Standalone, Android, or iOS. [More info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)  
See in [Glossary](Glossary.html#TestFramework). For more information, see
[Adding tests to a package](cus-tests.html).  
  
**Note** : You do not need to specify [embedded](upm-embed.html) packages here
because the Unity Test Framework assumes they are testable by default.  
  
  

## Example

    
    
    {
      "scopedRegistries": [{
        "name": "My internal registry",
        "url": "https://my.internal.registry.com",
        "scopes": [
          "com.company"
        ]
      }],
      "dependencies": {
        "com.unity.package-1": "1.0.0",
        "com.unity.package-2": "2.0.0",
        "com.company.my-package": "3.0.0",
        "com.unity.my-local-package": "file:<path>/my_package_folder",
        "com.unity.my-local-tarball": "file:<path>/my_package_tarball.tgz",
        "com.unity.my-git-package": "https://my.repository/my-package.git#v1.2.3"
      },
      "enableLockFile": true,
      "resolutionStrategy": "highestMinor",
      "testables": [ "com.unity.package-1", "com.unity.package-2" ]
    }
    

## Setting a resolution strategy

While you can force Unity’s package dependency resolution to use higher
versions of indirect dependencies by adding them explicitly to the project
manifest, this isn’t a good strategy, for two reasons:

  * It puts more responsibility on the project owner to maintain dependency versions.
  * Over time, you might have dependencies that are not required by the project.

A better approach is to customize how the Package Manager selects indirect
dependencies based on Semantic Versioning rules by setting the
**resolutionStrategy** property:

**Value:** | **Description:**  
---|---  
**lowest** | Do not upgrade indirect dependencies. Instead, it uses exactly the requested version. This is the default mode.  
**highestPatch** | Upgrade to the highest version with the same Major and Minor components. For example, with the requested version 1.2.3, this strategy selects the highest version in the range `[1.2.3, 1.3.0)` (that is, `>= 1.2.3` and `< 1.3.0`).  
**highestMinor** | Upgrade to the highest version with the same Major component. For example, with the requested version 1.2.3, this strategy selects the highest version in the range `[1.2.3, 2.0.0)` (that is, `>= 1.2.3` and `< 2.0.0`).  
  
**Note** : Version `1.0.0` marks the first stable, production-ready version.
Below that, versions `0.X.Y` indicate that their API is not yet stable, and
successive minor versions might introduce breaking changes. This part of the
SemVer specification allows releasing early versions of a package without
hampering rapid development. Because of this, when the target version is
`0.X.Y`, **highestMinor** behaves like **highestPatch** in order to ensure
choosing a backward-compatible version. For example, with the requested
version `0.1.3`, this strategy selects the highest version in the range
`[0.1.3,0.2.0)`.  
**highest** | Upgrade to the highest version. For example, with the requested version 1.2.3, this strategy selects the highest version in the range `[1.2.3,)` (that is, `>= 1.2.3` with no upper bound)  
  
**Note** : These ranges never allow a dependency to jump from a stable release
to an [experimental](pack-exp.html) or [pre-release](pack-preview.html)
package.

[](upm-conflicts-auto.html)

Lock files

[](upm-embed.html)

Embedded dependencies

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

