[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-PackageManifestImporter.html)
  * [中文](/cn/current/Manual/class-PackageManifestImporter.html)
  * [日本語](/ja/current/Manual/class-PackageManifestImporter.html)
  * [한국어](/kr/current/Manual/class-PackageManifestImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-PackageManifestImporter.html)
  * [中文](/cn/current/Manual/class-PackageManifestImporter.html)
  * [日本語](/ja/current/Manual/class-PackageManifestImporter.html)
  * [한국어](/kr/current/Manual/class-PackageManifestImporter.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Inspecting packages](upm-inspect.html)
  * Package Manifest window

[](upm-inspect.html)

Inspecting packages

[](upm-api.html)

Scripting API for packages

# Package Manifest window

The **Package Manifest** Each package has a _manifest_ , which provides
information about the package to the Package Manager. The manifest contains
information such as the name of the package, its version, a description for
users, dependencies on other packages (if any), and other details. [More
info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) window opens when you select
the package manifest file (`package.json`) in a `Packages` subfolder in the
**Project** window.

![Inspecting a package manifest in the Editor](../uploads/Main/class-
PackageManifestImporter.png) Inspecting a package manifest in the Editor

**(A)** Select **Open** to load this package manifest in your default code
editor, such as Visual Studio. Select **View in Package Manager** to open the
Package Manager window and load this package in its [details panel](upm-ui-
details.html). If you want to choose a different importer, select the
**Importer** drop-down menu and select the package importer you want to use.

**(B)** The Information section has details about this specific package
version.

**(C)** Use the **Brief Description** text box to specify the text that you
want to appear in the [details panel](upm-ui-details.html) of the Package
Manager window. For more information, refer to the documentation for the
[description](upm-manifestPkg.html#description) property.

**(D)** Use the Dependencies section to manage the list of packages that this
package depends on.

**(E)** Select **Revert** to discard any changes you’ve made to the manifest.
Select **Apply** to save any changes you’ve made to the manifest.

## Information

![Information section](../uploads/Main/class-PackageManifestImporter-Info.png) Information section **Property** | **Description**  
---|---  
**Name** | The official [name](upm-manifestPkg.html#name) for this package. For Unity packages, this is the short name (the official name without the `com.unity.` string at the beginning.)  
**Organization name** | The identifier of the [Unity Organization](https://docs.unity.com/cloud/en-us/organizations) that created this package.  
**Display name** | The user-facing name on display in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow) and the Package Manager window.
For more information, refer to the documentation for the [displayName](upm-
manifestPkg.html#displayName) property.  
**Version** | The package version number. For more information, refer to the documentation for the [version](upm-manifestPkg.html#version) property.  
**Minimal Unity version** | Enable this option to specify the lowest Unity version this package is compatible with. When you enable this option, the **Major** , **Minor** , and **Release** properties appear.   
  
If this package is compatible with all Unity versions, clear this checkbox and
remove the **Major** , **Minor** , and **Release** properties.  
  
For more information, refer to the documentation for the [unity](upm-
manifestPkg.html#unity) property.  
**Major** | Specify the MAJOR portion of the minimal Unity version. For more information, refer to the documentation for the [unity](upm-manifestPkg.html#unity) property.  
**Minor** | Specify the MINOR portion of the minimal Unity version. For more information, refer to the documentation for the [unity](upm-manifestPkg.html#unity) property.  
**Release** | Specify the UPDATE and RELEASE portion of the minimal Unity version. For more information, refer to the documentation for the [unityRelease](upm-manifestPkg.html#unityRelease) property.  
  
## Dependencies

![Dependencies section](../uploads/Main/class-PackageManifestImporter-
Depend.png) Dependencies section

Lists the other packages that are dependencies for this package. Each entry
consists of the official package name (for example, `com.unity.probuilder`)
and its version number.

To add a new dependency:

  1. Select **Add** ![](../uploads/Main/iconAdd.png). A new row appears in the list.
  2. Enter the package name on the left and the version on the right. For more information, refer to the documentation for the [dependencies](upm-manifestPkg.html#dependencies) property.

To remove a dependency:

  1. Click the selector ![](../uploads/Main/iconSelect.png) to the left of the package you want to remove.
  2. Select **Remove** ![](../uploads/Main/iconRemove.png). The row disappears from the list.

[](upm-inspect.html)

Inspecting packages

[](upm-api.html)

Scripting API for packages

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

