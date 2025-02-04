[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-conflicts-auto.html)
  * [中文](/cn/current/Manual/upm-conflicts-auto.html)
  * [日本語](/ja/current/Manual/upm-conflicts-auto.html)
  * [한국어](/kr/current/Manual/upm-conflicts-auto.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-conflicts-auto.html)
  * [中文](/cn/current/Manual/upm-conflicts-auto.html)
  * [日本語](/ja/current/Manual/upm-conflicts-auto.html)
  * [한국어](/kr/current/Manual/upm-conflicts-auto.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Resolution and conflict](upm-conflicts.html)
  * Lock files

[](upm-conflicts.html)

Resolution and conflict

[](upm-manifestPrj.html)

Project manifest

# Lock files

A lock file contains the results of the Package Manager’s [dependency
resolution](upm-conflicts.html) for a project. Package managers use lock files
to provide a
[deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm) result
when resolving a [package dependency graph](upm-dependencies.html). When the
Unity Package Manager computes a successful resolution, it stores that
resolution inside the project’s `Packages` folder in a JSON file called
`packages-lock.json`. Any modification to the **project manifest** Each Unity
project has a _project manifest_ , which acts as an entry point for the
Package Manager. This file must be available in the `<project>/Packages`
directory. The Package Manager uses it to configure many things, including a
list of dependencies for that project, as well as any package repository to
query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) or to a **mutable** You can
change the contents of a mutable package. This is the opposite of
**immutable**. Only **Local package****s** and **Embedded package****s** are
mutable.  
See in [Glossary](Glossary.html#Mutable) package’s manifest (either
[embedded](upm-concepts.html#Embedded) or [installed from local folder](upm-
concepts.html#Local)) can potentially compel the Package Manager to
recalculate the resolved package versions. But as long as the version of a
package in the lock file satisfies the range implied by the dependency version
and the [resolution strategy](upm-conflicts.html), the package remains locked
at that version.

For example, here is a typical entry in the lock file:

    
    
    "com.unity.textmeshpro": {
      "version": "2.0.1",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.ugui": "2.0.0"
      },
      "url": "https://packages.unity.com"
    },
        etc.
    

When the Package Manager resolves any conflicting [indirect dependencies](upm-
dependencies.html)An **indirect** , or transitive dependency occurs when your
project requests a package which itself “depends on” another package. For
example, if your project depends on the `alembic@1.0.7` package which in turn
depends on the `timeline@1.0.0` package, then your project has an direct
dependency on Alembic and an indirect dependency on Timeline. [More info](upm-
dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency), it tries to re-use as
many locked packages as possible. This guarantees that subsequent dependency
resolution produces the same results for the same set of dependencies. It also
minimizes time-consuming operations such as downloading, extracting, or
copying packages.

If there is no solution that only includes locked packages, then the Package
Manager chooses the set of packages with the least risky upgrades, preferring
patch upgrades over minor or major upgrades, and minor upgrades over major
upgrades. In fact, you can customize the level of risk for upgrading. For more
information, see [Customizing resolution strategies](upm-
manifestPrj.html#resolutionStrategy).

To force a refresh of indirect dependency versions, delete the lock file.

Don’t manually modify the lock file: the Package Manager creates and maintains
the lock file, so it overwrites any changes you make to the file.

Put the lock file under source control so you can consistently reproduce the
same package set to ensure your project remains consistent over time and on
different machines.

## Disabling the lock file

By default, the Package Manager creates or updates the lock file when it
successfully computes a dependency graph. If you see unexpected results, you
can set the [enableLockFile](upm-manifestPrj.html#enableLockFile) property to
`false` in your project manifest to disable locking. However, if you disable
the lock file, the Package Manager clones [Git URL](upm-git.html) packages
again, which leads to reduced performance and additional network usage. It
might also lead to non-deterministic results if you push newer commits to the
remote Git repository between two resolutions.

  

* * *

  

  * SAT solver feature added in Unity [2019.4](https://docs.unity3d.com/2019.4/Documentation/Manual/30_search.html?q=newin20194) NewIn20194

[](upm-conflicts.html)

Resolution and conflict

[](upm-manifestPrj.html)

Project manifest

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

