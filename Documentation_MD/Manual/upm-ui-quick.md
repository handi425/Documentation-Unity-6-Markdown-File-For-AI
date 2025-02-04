[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-quick.html)
  * [中文](/cn/current/Manual/upm-ui-quick.html)
  * [日本語](/ja/current/Manual/upm-ui-quick.html)
  * [한국어](/kr/current/Manual/upm-ui-quick.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-quick.html)
  * [中文](/cn/current/Manual/upm-ui-quick.html)
  * [日本語](/ja/current/Manual/upm-ui-quick.html)
  * [한국어](/kr/current/Manual/upm-ui-quick.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * Install a UPM package by name

[](upm-ui-giturl.html)

Install a UPM package from a Git URL

[](upm-ui-remove.html)

Remove a UPM package from a project

# Install a UPM package by name

If you know the exact name of a **UPM package** A **Package** managed by the
**Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) you want to install, you can use
the **Install package by name** option to install it. This is a quick way to
install a UPM package that comes from a registry.

This method works for any UPM package and version that’s currently hosted on
the Unity package registry or any [scoped package registry](upm-scoped.html)
you have set up for the current project. It also applies to any UPM package in
the Unity registry that came from the **Asset Store** A growing library of
free and commercial assets created by Unity and members of the community.
Offers a wide variety of assets, from textures, models and animations to whole
project examples, tutorials and Editor extensions. [More
info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore).

Specifying the version is optional. If you don’t know which version to
install, or want to install the latest compatible version, enter only the
package name.

**Note:** The latest compatible version might not be the latest published
package. If there is a [released](pack-safe.html) package version and a newer
[pre-release](pack-preview.html) or [experimental](pack-exp.html) version,
Package Manager selects the released package version, unless you explicitly
input a value in the optional **Version** field.

## Before you begin

Make sure you know the package’s name. The package name is a unique
identifier, not the display name used on user interfaces and documentation.

![Inspector window showing the name and display name](../uploads/Main/upm-ui-
name-v-dname.png) Inspector window showing the name and display name

For packages in the Unity registry, the name’s unique identifier uses reverse
domain name notation. Examples include `com.unity.example` and
`com.meta.example`. For packages in a scoped registry, the name might not
follow the same pattern.

For any package in the UPM format, if you can view the package in Package
Manager, select it and view its details in the ****Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window. The **Name** value is the
package name.

Other ways of determining a package name vary, depending on the registry that
hosts it:

  * For a package in the Unity registry: 
    * Use the lists in [Released packages](pack-safe.html) and [Pre-release packages](pack-preview.html) to identify a package by its display name, such as `2D Animation`. The hyperlink value is the name of that package; in this case, `com.unity.2d.animation`.
    * The [package documentation](upm-docs.html) might have installation instructions that explicitly provide the `name` value.
    * The [package documentation](upm-docs.html) URL often nests the package name in its address. Using the **AR** Augmented Reality [More info](AROverview.html)  
See in [Glossary](Glossary.html#AR) Foundation package as an example, its
package documentation URL is
`https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/manual/index.html`;
the `com.unity.xr.arfoundation` component is that package’s name.

  * For a package in a scoped registry, if you can’t determine its name by using the Package Manager and Inspector windows, contact the package creator and request the package name. The package creator recorded this value as a required property in the [package manifest](upm-manifestPkg.html)Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) file (`package.json`).

## Procedure

To install a UPM package by name, follow these steps:

  1. Open the [Package Manager window](upm-ui-access.html), if it’s not already open.

  2. Click the **install** ![](../uploads/Main/iconAdd.png) button in the toolbar. The options for installing packages appear.

![Install package by name option](../uploads/Main/upm-ui-quick.png) Install
package by name option

  3. Select **Install package by name** from the install menu. Two text boxes and an **Install** button appear.

  4. Enter the package **Name** , as determined in the Before you begin section.

![Enter the package name and package version \(optional\) then click
Install](../uploads/Main/upm-ui-quick-add.png) Enter the package name and
package version (optional) then click Install

**Note** : If you enter an invalid package name or version, Package Manager
warns you that it can’t find that name or version. Verify that the package
name and version are correct and try again.

  5. (Optional) If you know which version you want to install, enter the [full package version](upm-manifestPkg.html#version), such as `1.3.0-pre.2`, in the **Version (optional)** box.

  6. Click **Install**. If Unity was able to install the package successfully, the package now appears in the [package list](upm-ui-list.html) like any other installed UPM package.

## Additional resources

  * [Package types](upm-package-types.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)

[](upm-ui-giturl.html)

Install a UPM package from a Git URL

[](upm-ui-remove.html)

Remove a UPM package from a project

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

