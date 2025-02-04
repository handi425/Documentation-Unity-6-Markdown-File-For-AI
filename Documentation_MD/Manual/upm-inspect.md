[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-inspect.html)
  * [中文](/cn/current/Manual/upm-inspect.html)
  * [日本語](/ja/current/Manual/upm-inspect.html)
  * [한국어](/kr/current/Manual/upm-inspect.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-inspect.html)
  * [中文](/cn/current/Manual/upm-inspect.html)
  * [日本語](/ja/current/Manual/upm-inspect.html)
  * [한국어](/kr/current/Manual/upm-inspect.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Inspecting packages

[](upm-docs.html)

Finding package documentation

[](class-PackageManifestImporter.html)

Package Manifest window

# Inspecting packages

The Project view displays the list of packages currently installed in your
project from all sources. This means that **immutable** You cannot change the
contents of an immutable (read-only) package. This is the opposite of
**mutable**. Most packages are immutable, including packages downloaded from
the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable) packages that you installed from a
package registry are visible, as well as **mutable** You can change the
contents of a mutable package. This is the opposite of **immutable**. Only
**Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](Glossary.html#Mutable) packages (such as embedded and local
packages).

![Registry package \(immutable\) on the left and an embedded package
\(mutable\) on the right](../uploads/Main/upm-inspect.png) Registry package
(immutable) on the left and an embedded package (mutable) on the right

You can inspect the contents of any package that appears in the Project view.
You can also inspect the **package manifest** Each package has a _manifest_ ,
which provides information about the package to the Package Manager. The
manifest contains information such as the name of the package, its version, a
description for users, dependencies on other packages (if any), and other
details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) through a dedicated
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

To inspect a package manifest, click on it in the Project view.

![Inspecting a package manifest](../uploads/Main/upm-project-view.png)
Inspecting a package manifest

For [embedded](upm-concepts.html#Embedded) or [local](upm-concepts.html#Local)
packages, you can change the package contents and [edit the package
manifest](class-PackageManifestImporter.html).

  

[](upm-docs.html)

Finding package documentation

[](class-PackageManifestImporter.html)

Package Manifest window

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

