[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-overview.html)
  * [中文](/cn/current/Manual/upm-overview.html)
  * [日本語](/ja/current/Manual/upm-overview.html)
  * [한국어](/kr/current/Manual/upm-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-overview.html)
  * [中文](/cn/current/Manual/upm-overview.html)
  * [日本語](/ja/current/Manual/upm-overview.html)
  * [한국어](/kr/current/Manual/upm-overview.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * How Unity works with packages

[](Packages.html)

Unity's Package Manager

[](upm-concepts.html)

Concepts

# How Unity works with packages

When Unity opens a Project, the Unity Package Manager reads the [Project
manifest](upm-manifestPrj.html)Each Unity project has a _project manifest_ ,
which acts as an entry point for the Package Manager. This file must be
available in the `<project>/Packages` directory. The Package Manager uses it
to configure many things, including a list of dependencies for that project,
as well as any package repository to query for packages. [More info](upm-
manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) (**1**) to figure out what
packages to load in the Project. Then it sends a request (**2**) to the
[package registry server](upm-concepts.html#Registry) (**3**) for each package
that appears as a dependency in the manifest. The package registry then sends
the requested information and data back to the Package Manager (**4**), which
then installs those packages (**5**) in the Project. Each Project has its own
manifest which lists the packages to load as “dependencies” of the Project.

![How the Unity Package Manager installs packages](../uploads/Main/upm-
overview.png) How the Unity Package Manager installs packages

Adding a package to a project requires an update to the project manifest, to
ensure the Package Manager includes the package in the list of dependencies.
Although you can modify the project manifest directly, it’s safer and easier
to work with the [Package Manager window](upm-ui.html), which manages the
project manifest modifications for you.

## Additional resources

  * [Unity’s Package Manager](Packages.html)
  * [Package Manager concepts](upm-concepts.html)

[](Packages.html)

Unity's Package Manager

[](upm-concepts.html)

Concepts

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

