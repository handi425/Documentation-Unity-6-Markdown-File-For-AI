[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-dependencies.html)
  * [中文](/cn/current/Manual/upm-dependencies.html)
  * [日本語](/ja/current/Manual/upm-dependencies.html)
  * [한국어](/kr/current/Manual/upm-dependencies.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-dependencies.html)
  * [中文](/cn/current/Manual/upm-dependencies.html)
  * [日本語](/ja/current/Manual/upm-dependencies.html)
  * [한국어](/kr/current/Manual/upm-dependencies.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Concepts](upm-concepts.html)
  * Dependency and resolution

[](upm-lifecycle.html)

Package states and lifecycle

[](upm-cache.html)

Global cache

# Dependency and resolution

When you work in the Package Manager window, you can install a package from
several sources (a [registry](upm-ui-install.html), a local [folder](upm-ui-
local.html) or [tarball](upm-ui-tarball.html), a [Git URL](upm-ui-
giturl.html), and by [name](upm-ui-quick.html)). However, while the Package
Manager installs packages from these sources seamlessly, it first has to make
a series of calculations to decide which version to install. It also has to
decide which other packages and versions to install to support the package you
selected.

****Direct dependencies****

When you select a package version to install through the Package Manager
window, you are adding a “dependency” to your [project manifest](upm-
manifestPrj.html)Each Unity project has a _project manifest_ , which acts as
an entry point for the Package Manager. This file must be available in the
`<project>/Packages` directory. The Package Manager uses it to configure many
things, including a list of dependencies for that project, as well as any
package repository to query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest). This is a declaration that
you need a specific version of a particular package in order for the project
to work. To add a dependency to your project, you add a reference to the
package and version in the form `package-name@package-version` to the
[dependencies](upm-manifestPrj.html#dependencies) property of the `<project-
root>/Packages/manifest.json` file. These are called “direct” dependencies
because your project directly depends on them.

****Indirect dependencies****

Packages can also require other packages to work. These are called “indirect”
(or transitive) dependencies. The package developer adds these to the
[dependencies](upm-manifestPkg.html#dependencies) property of the package
manifest file during development (`<package-root>/package.json`). For example,
in the diagram below, the `alembic@1.0.7` package has a dependency on the
`timeline@1.0.0` package, so the timeline package is an “indirect” dependency.
Conversely, the project has dependencies on the `cinemachine@2.6.0` and
`alembic@1.0.7` packages, so those are both “direct” dependencies.

![A diagram showing both direct and indirect
dependencies](../uploads/Main/upm-dependencies.svg) A diagram showing both
direct and indirect dependencies

**Version overrides**

When you add a package version as a dependency, that version isn’t necessarily
the version that the Package Manager installs. The reason is because the
Package Manager has to consider all dependencies in your project, whether
direct or indirect. In the following example, the ****XR** An umbrella term
encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality
(MR) applications. Devices supporting these forms of interactive applications
can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) Plugin Management** package requested was
version `4.0.3`. However, the Package Manager installed version `4.0.6`
because another package depended on the higher version, as indicated in the
information message **(B)** :

![When you click the information button in the details panel \(A\), a text box
appears \(B\) explaining why this version was installed instead of the one you
requested](../uploads/Main/upm-solver-visual-cues.png) When you click the
information button in the details panel (A), a text box appears (B) explaining
why this version was installed instead of the one you requested

**Dependency graph**

The Package Manager can install only one package version at a time, so it has
to construct a [dependency graph](upm-conflicts.html). This graph is a list of
every direct and indirect dependency for the project. The dependency graph
determines which version of each package to install.

**Lock file**

When the Package Manager resolves all version conflicts, it saves the
resolution in a [lock file](upm-conflicts-auto.html) for two reasons:

  * Determinism, to make sure that the same packages are reliably installed every time.
  * Efficiency, to reduce the amount of time and resources it takes to compute the dependency graph again.

  

[](upm-lifecycle.html)

Package states and lifecycle

[](upm-cache.html)

Global cache

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

