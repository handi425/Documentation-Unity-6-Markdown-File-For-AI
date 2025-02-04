[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-scoped.html)
  * [中文](/cn/current/Manual/upm-scoped.html)
  * [日本語](/ja/current/Manual/upm-scoped.html)
  * [한국어](/kr/current/Manual/upm-scoped.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-scoped.html)
  * [中文](/cn/current/Manual/upm-scoped.html)
  * [日本語](/ja/current/Manual/upm-scoped.html)
  * [한국어](/kr/current/Manual/upm-scoped.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Scoped registries

[](upm-assets.html)

Accessing package assets

[](upm-conflicts.html)

Resolution and conflict

# Scoped registries

Scoped registries allow Unity to communicate the location of any custom
package registry server to the Package Manager so you can access several
collections of packages at the same time.

Here are some important concepts to help you understand this feature:

**Concept** | **Description**  
---|---  
**package registry server** | An application that keeps track of packages and provides a place to store them. In Unity’s Package Manager window, all packages registered on Unity’s registry appear in the [list panel](upm-ui-list.html) when you select the [Unity Registry](upm-ui-filter.html) context.  
**package manager** | An application that tells the user what packages are available, and downloads and installs whatever package the user requests for their project. Unity has implemented its own version of a package manager, but there are several similar applications in other organizations.  
**scope** | Defines a package name or namespace (in reverse domain format), such as `com.example.mycompany.animation` or `com.example`. When a user requests a package, the Package Manager fetches the package from the registry that best matches the scope. For more information, refer to Managing scoped registries for a project.  
  
  
The way you interact with scoped registries depends on your role:

  * Package providers set up custom registry servers to host and distribute custom packages in addition to the [Unity registry](upm-concepts.html#Registry).
  * Package consumers set up scoped registries for each project to access a custom package provider’s registry server.

## Integrity and security of scoped registries

As a package provider, make sure any package registry servers you set up
conform to Unity’s Terms of Service and [Unity’s Package Guiding Principles &
Guidelines](https://unity.com/legal/terms-of-service/software/package-
guidelines). Unity provides access to the Package Manager to facilitate
sharing knowledge and creations, but not as a marketplace for third-party
products.

As a package consumer, when you install a scoped registry, use the same level
of caution that you use when installing any other third-party software:

  * Install scoped registries only from trusted sources, because the packages in those registries can contain executable code.
  * Beware of third-party registries that might be harmful or capture data without appropriate controls. Also beware of third parties misrepresenting themselves as Unity, or sanctioned or supported by Unity.

## Benefits of scoped registries

Scoped registries can help to:

  * **Provide new functionality by distributing tools, libraries, and other assets**.

As a provider, you can create your own registry to distribute tools and
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) (or other types of assets) with
version numbers that indicate how mature the package is. Version numbers also
indicate whether updates introduce breaking API changes or minor fixes, based
on [Semantic Versioning](upm-semver.html). Your code can depend on code in
other packages, because the Package Manager supports [package
dependencies](upm-dependencies.html).

As a consumer, your experience of browsing and installing third-party custom
packages in the Package Manager is the same as browsing Unity’s packages.

  * **Extend existing Unity’s package features**.

As a consumer, you can have a seamless experience where the custom package
overrides the Unity package without having to manually change registries or
explicitly install a different package version. This is because you can map
packages to a specific registry so that Package Manager fetches from either
the Unity registry or a custom package registry server.

  * **Access packages in a closed network environment**.

Some organizations work inside a closed network, which makes it difficult to
access Unity’s package registry. In these cases, the organization can set up
their own package registry on a server inside their closed network. The
network administrators can then periodically synchronize with Unity’s package
registry to make sure the scoped registry has the latest set of packages
available.

If you’re a package consumer, refer to Managing scoped registries for a
project for information about connecting to an existing custom package
registry server in your Unity project. If you’re a package producer, refer to
[Sharing your package](cus-share.html) for information about supported package
registry servers. This information also includes links to information on how
to set them up to use with scoped registries.

**Note:** If you’re setting up a scoped registry that points to a package
registry server with restricted access, you can configure Package Manager to
pass your `npm` authentication token to the server. For more information,
refer to [Scoped registry authentication](upm-config-scoped.html).

## Adding and removing scoped registries

Use the **Package Manager** category of the [Project Settings](class-
PackageManager.html)A broad collection of settings which allow you to
configure how Physics, Audio, Networking, Graphics, Input and many other areas
of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window to add, modify, or
remove scoped registries for your project.

## Importing scoped registries

If you’re working in a shared project, and another user adds a scoped registry
to the project, Unity warns you that another user added a new scoped registry.

![Unity warns you if theres a change to the list of scoped registries for your
project](../uploads/Main/class-PackageManager-scoped.png) Unity warns you if
there’s a change to the list of scoped registries for your project

When you click **Close** , the Package Manager [project settings](class-
PackageManager.html) window appears so you can [add](class-
PackageManager.html#scoped_add), [modify](class-
PackageManager.html#scoped_modify), or [remove](class-
PackageManager.html#scoped_remove) scoped registries for your project.

If you click **Read more** , Unity opens the page you’re currently reading in
your default web browser.

**Tip:** To access the Package Manager project settings window at any time,
use the main menu in Unity (**Edit > Project Settings**, then the **Package
Manager** category). You can also select **Advanced Project Settings** from
the [advanced settings](upm-ui.html#Advanced) menu in the Package Manager
window.

## Managing scoped registries for a project

To manage the scoped package registries in your project, you can either:

  * Edit your [project manifest](upm-manifestPrj.html)Each Unity project has a _project manifest_ , which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) file directly.

  * Use the Package Manager [project settings](class-PackageManager.html) window to let Unity change the manifest for you.

The project manifest uses a [scopedRegistries](upm-
manifestPrj.html#scopedRegistries) property, which contains an array of scoped
registry configuration objects. Each object has the following properties:

**Property** | **JSON Type** | **Description**  
---|---|---  
**name** | String | The scope name as it appears in the user interface. The Package Manager window displays this name in the [details panel](upm-ui-details.html).   
  
For example, `"name": "Tools"`.  
**url** | String | The URL to the npm-compatible registry server.   
  
For example, `"url": "https://mycompany.example.com/tools-registry"`  
  
**Note** : Not all registry providers are compatible with Unity’s Package
Manager. Make sure the package registry server you’re trying to add implements
the `/-/v1/search` or `/-/all` endpoints.  
**overrideBuiltIns** | Boolean | A `true` or `false` value that determines which version of a built-in package to use, if the package exists in a scoped registry.   
  
If set to `false`, the Package Manager uses the built-in version included with
the Unity Editor. This is the default value.  
  
If set to `true`, and the built-in package also exists in a scoped registry,
the Package Manager downloads the version in the scoped registry.  
  
The scope of this property applies to all packages identified in the **url**
property.  
**scopes** | Array of Strings | Array of scopes that you can map to a package name, either as an exact match on the package name, or as a namespace. Wildcards and other glob patterns aren’t supported.  
  
For example, `"scopes": [ "com.example", "com.example.tools.physics" ]`  
  
**Note** : This configuration type assumes that packages follow the [Reverse
domain name
notation](https://en.wikipedia.org/wiki/Reverse_domain_name_notation). This
ensures that `com.unity` is equivalent to any package name that matches the
`com.unity` namespace, such as `com.unity.timeline` or
`com.unity.2d.animation`.  
  
**Warning:** Unity doesn’t support npm’s scope notation.  
  
## Example

In the project manifest below, there are two scoped registries, `General` and
`Tools`:

    
    
    {
        "scopedRegistries": [
            {
                "name": "General",
                "url": "https://example.com/registry",
                "overrideBuiltIns": false,
                "scopes": [
                    "com.example", "com.example.tools.physics"
                ]
            },
            {
                "name": "Tools",
                "url": "https://mycompany.example.com/tools-registry",
                "overrideBuiltIns": true,
                "scopes": [
                    "com.example.mycompany.tools"
                ]
            }
        ],
        "dependencies": {
            "com.unity.animation": "1.0.0",
            "com.example.mycompany.tools.animation": "1.0.0",
            "com.example.tools.physics": "1.0.0",
            "com.example.animation": "1.0.0"
        }
    }
    
    

When the Package Manager decides which registry to fetch a package from, it
compares the package **name** to the **scopes** values and finds the registry
whose **scopes** value is the closest match.

  * When the Package Manager looks up the `com.example.animation` package, it finds that the `com.example` namespace is the closest match to its name, and fetches that package from the `General` registry.
  * When the Package Manager looks up the `com.example.tools.physics` package, the `General` registry has a scope that exactly matches the package name.
  * When the Package Manager looks up the `com.example.mycompany.tools.animation` package, the Package Manager finds that the `com.example.mycompany.tools` namespace is the closest match to its name and fetches that package from the `Tools` registry. Although it also matches the `General` scope, the `com.example` namespace isn’t as close a match.
  * When the Package Manager looks up the `com.unity.animation` package, the Package Manager doesn’t find a match in any of the scoped registries. In this case, it fetches the package from the default registry.

If the `General` and `Tools` registries have **built-in packages** _Built-in_
packages allow users to toggle Unity features on or off through the Package
Manager. Enabling or disabling a package reduces the run-time build size. For
example, most projects don’t use the legacy Particle System. By removing the
abstracted package of this feature, the related code and resources are not
part of the final built product. Typically, these packages contain only the
package manifest and are bundled with Unity (rather than available on the
package registry).  
See in [Glossary](Glossary.html#Built-inpackage) that also exist in the
Editor, the Package Manager resolves them as follows:

  * The Package Manager skips the built-in packages in the `General` scoped registry because the `overrideBuiltIns` value is `false`. Instead, the Package Manager uses the built-in version included with the Unity Editor.
  * The Package Manager uses the built-in packages in the `Tools` scoped registry instead of the Editor because the `overrideBuiltIns` value is `true`.

## Additional resources

  * [Scoped registry authentication](upm-config-scoped.html)
  * [Project Settings window (Package Manager)](class-PackageManager.html)

[](upm-assets.html)

Accessing package assets

[](upm-conflicts.html)

Resolution and conflict

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

