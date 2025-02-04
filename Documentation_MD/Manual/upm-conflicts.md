[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-conflicts.html)
  * [中文](/cn/current/Manual/upm-conflicts.html)
  * [日本語](/ja/current/Manual/upm-conflicts.html)
  * [한국어](/kr/current/Manual/upm-conflicts.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-conflicts.html)
  * [中文](/cn/current/Manual/upm-conflicts.html)
  * [日本語](/ja/current/Manual/upm-conflicts.html)
  * [한국어](/kr/current/Manual/upm-conflicts.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Resolution and conflict

[](upm-scoped.html)

Scoped registries

[](upm-conflicts-auto.html)

Lock files

# Resolution and conflict

When you add a package to a **project manifest** Each Unity project has a
_project manifest_ , which acts as an entry point for the Package Manager.
This file must be available in the `<project>/Packages` directory. The Package
Manager uses it to configure many things, including a list of dependencies for
that project, as well as any package repository to query for packages. [More
info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest), Unity considers that package
a [dependency](upm-dependencies.html) of the project (a direct dependency).
However, a package can also have dependencies on other packages, which create
**indirect dependencies** An **indirect** , or transitive dependency occurs
when your project requests a package which itself “depends on” another
package. For example, if your project depends on the `alembic@1.0.7` package
which in turn depends on the `timeline@1.0.0` package, then your project has
an direct dependency on Alembic and an indirect dependency on Timeline. [More
info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) in any projects that
require that package.

Since most projects require more than one package in order to develop games
and apps, the Package Manager has to evaluate all the requested package
versions to retrieve from the registry (whether direct or indirect), and
decide which among those package versions to install. To do this, it computes
the set of packages that satisfies all [direct and indirect dependencies](upm-
dependencies.html) in the project, starting with the project dependencies and
recursively exploring each indirect dependency, collecting all the dependency
information, then picking a set of packages that satisfies the dependency
requirements without any conflict. For example, this dependency graph
represents a project with four **direct dependencies** A **direct** dependency
occurs when your project “requests” a specific package version. To create a
direct dependency, you add that package and version to the **dependencies**
property in your project manifest (expressed in the form
`package_name@package_version`). [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Directdependency) and all of their indirect
dependencies:

![A graph of direct and indirect package dependencies for a
project](../uploads/Main/upm-conflicts.svg) A graph of direct and indirect
package dependencies for a project

In this example:

  * The light blue nodes represent the project’s direct dependencies.
  * The dark blue nodes show the same package and version as indirect dependencies in this project.
  * The red nodes show two different versions of the same package, which is a conflict.

**Note** : Only package dependencies declared with versions need to be
resolved. The Package Manager selects packages installed from other
[sources](upm-concepts.html#Sources), such as [embedded packages](upm-
embed.html)An _embedded_ package is a mutable package that you store under the
`Packages` directory at the root of a Unity project. This differs from most
packages which you download from a package server and are immutable. [More
info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage), and dependencies declared
with [local paths](upm-localpath.html), [Git URLs](upm-git.html), and [built-
in](pack-build.html) packages over version-based dependencies.

## Choosing the best solution

Depending on the set of packages defined in the project manifest, it could
take a long time to evaluate all possible package combinations: a project
could potentially depend on hundreds of packages, each of which depend on
hundreds of other packages, most requiring different versions.

### Lock files and resolutionStrategy

To provide the most efficient solution, the Package Manager prioritizes
package versions that it previously used by tracking them in a [lock
file](upm-conflicts-auto.html). This guarantees that subsequent dependency
resolution using the same inputs results in the same outputs. It also
minimizes time-consuming operations such as downloading, extracting, or
copying packages.

Sometimes, the Package Manager cannot find a solution that only includes
locked packages. In this case, the Package Manager uses the solution with the
least risky upgrades, preferring patch upgrades over minor or major upgrades,
and minor upgrades over major upgrades by default. However, you can customize
how aggressive you want the Package Manager to be when considering a higher
version with the [resolutionStrategy](upm-manifestPrj.html#resolutionStrategy)
property.

## Example

In this example, there are multiple versions of the following packages
requested:

  * `burst@1.2.2` (twice) and `burst@1.3.0-preview.3`
  * `collections@0.5.1-preview.11` and `collections@0.5.2-preview.8`
  * `jobs@0.2.4-preview.11` (twice) and `jobs@0.2.5-preview.20`

Using the set of [direct and indirect dependencies](upm-dependencies.html),
the Package Manager selects the highest version of the burst package
(`burst@1.3.0-preview.3`), which satisfies the `collections@0.5.2-preview.8`
package’s dependency:

![In the dependency graph, the blue nodes indicate which versions the Package
Manager selected](../uploads/Main/upm-resolution.svg) In the dependency graph,
the blue nodes indicate which versions the Package Manager selected

  

* * *

  

  * New package dependency solver (SAT) added in Unity [2019.4](https://docs.unity3d.com/2019.4/Documentation/Manual/30_search.html?q=newin20194) NewIn20194

  

[](upm-scoped.html)

Scoped registries

[](upm-conflicts-auto.html)

Lock files

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

