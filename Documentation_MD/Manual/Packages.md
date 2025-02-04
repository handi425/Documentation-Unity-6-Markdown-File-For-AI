[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Packages.html)
  * [中文](/cn/current/Manual/Packages.html)
  * [日本語](/ja/current/Manual/Packages.html)
  * [한국어](/kr/current/Manual/Packages.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Packages.html)
  * [中文](/cn/current/Manual/Packages.html)
  * [日本語](/ja/current/Manual/Packages.html)
  * [한국어](/kr/current/Manual/Packages.html)

  * [Packages and feature sets](PackagesList.html)
  * Unity's Package Manager

[](PackagesList.html)

Packages and feature sets

[](upm-overview.html)

How Unity works with packages

# Unity’s Package Manager

A _package_ is a container that stores various types of features or assets,
such as:

  * Editor tools and libraries, such as a text editor, an animation viewer, or test frameworks.
  * Runtime tools and libraries, such as the Physics API or a Graphics pipeline.
  * Asset collections, such as Textures or animations.
  * Project templates to share common project types with others.

Packages deliver a wide range of enhancements to Unity through the Package
Manager. To help find and use these packages, the Package Manager window
provides collections of packages that you can use together, called _feature
sets_.

In the Editor, you can access the [Package Manager window](upm-ui.html)
through this menu: **Window** > **Package Manager**.

The Package Manager also supports management of packages you download or
import from the Unity **Asset Store** A growing library of free and commercial
assets created by Unity and members of the community. Offers a wide variety of
assets, from textures, models and animations to whole project examples,
tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore).

Unity provides three Package Manager interfaces: Package Manager window,
Scripting API, and manifest files. The following table contains introductions
to each interface, and more.

**Topic** | **Description**  
---|---  
**[How Unity works with packages](upm-overview.html)** | Get an overview of Unity’s Package Manager.  
**[Concepts](upm-concepts.html)** | Learn the principles and features of the Package Manager, including concepts like versions, manifests, registries, states, sources, the package lifecycle, and dependency and resolution.  
**[Package Manager window](upm-ui.html)** | Find packages and manage them in your project, and resolve conflicts in package dependencies. The Package Manager provides a user interface that makes changes to the [Project manifest](upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) directly.  
**[Scripting API for packages](upm-api.html)** | Use the Scripting API to interact with the Package Manager using C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). View samples to see how to query the
package registry, install, embed, and remove packages, and list packages using
a variety of criteria.  
**[Project manifest](upm-manifestPrj.html)** | Learn about the file that the Unity Package Manager reads so it can compute a list of packages to retrieve and load. See also [Package manifest](upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest).  
**[Inspecting packages](upm-inspect.html)** | Use a dedicated **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to view any [package
manifest](upm-manifestPkg.html). Use this window to directly edit package
manifests for embedded or local packages.  
**[Scoped Registries](upm-scoped.html)** | Learn how to set up or access a custom registry server. Use this registry server to host and distribute (or consume) custom packages, in addition to the registry that Unity provides.  
**[Configuration](upm-config.html)** | Learn how configure scoped registry authentication, solve network issues, customize cache locations, and more.  
**[Resolution and conflict](upm-conflicts.html)** | Learn how the Package Manager determines the direct and **indirect dependencies** An **indirect** , or transitive dependency occurs when your project requests a package which itself “depends on” another package. For example, if your project depends on the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package, then your project has an direct dependency on Alembic and an indirect dependency on Timeline. [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) of a project and evaluates
all the requested package versions before retrieving the best version from the
registry.  
**[Troubleshooting](upm-errors.html)** | Match a symptom to a possible solution if any of your project’s packages, including the Package Manager window itself, fails to load.  
  
## Additional resources

  * [Asset Store packages](AssetStorePackages.html)
  * [Embedded packages](upm-concepts.html#Embedded)An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage)

  * [Local packages](upm-concepts.html#Local)A _local_ package already exists on the file system, usually outside the project folder. To install the package, notify the Package Manager of its location through the **Packages** window. [More info](upm-ui-local.html)  
See in [Glossary](Glossary.html#Localpackage)

  * [Package manifest](upm-manifestPkg.html)

[](PackagesList.html)

Packages and feature sets

[](upm-overview.html)

How Unity works with packages

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

