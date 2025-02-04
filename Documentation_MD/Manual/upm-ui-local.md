[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-local.html)
  * [中文](/cn/current/Manual/upm-ui-local.html)
  * [日本語](/ja/current/Manual/upm-ui-local.html)
  * [한국어](/kr/current/Manual/upm-ui-local.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-local.html)
  * [中文](/cn/current/Manual/upm-ui-local.html)
  * [日本語](/ja/current/Manual/upm-ui-local.html)
  * [한국어](/kr/current/Manual/upm-ui-local.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * Install a UPM package from a local folder

[](upm-ui-install2.html)

Install a UPM package from the Asset Store

[](upm-ui-tarball.html)

Install a UPM package from a local tarball file

# Install a UPM package from a local folder

The Package Manager can load a **UPM package** A **Package** managed by the
**Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) from anywhere on your computer
even if you saved it outside your Unity project folder (for example, if you
have a package called **com.unity.my-local-package** and you save it on the
`Desktop` but your Unity project is under the `Documents` folder).

You can also use a folder inside your project folder, provided that it is not
one of the reserved project sub-folders.

To install a UPM package from your local disk:

  1. Open the [Package Manager window](upm-ui-access.html), if it’s not already open.

  2. Click the **install** ![](../uploads/Main/iconAdd.png) button in the toolbar. The options for installing packages appear.

![Install package from disk button](../uploads/Main/upm-ui-local.png) Install
package from disk button

  3. Select **Install package from disk** from the install menu to bring up a file browser.

  4. Navigate to the folder root of your **local package**.

  5. Double-click the `package.json` file in the file browser.

The file browser closes, and the package now appears in the [package
list](upm-ui-list.html) with the ![](../uploads/Main/iconLocal.png) label.

![A package installed from a local folder, with the option to update to a
higher version](../uploads/Main/upm-ui-local-ver.png) A package installed from
a local folder, with the option to update to a higher version

Remember that if you updated to the registry version but you made changes
locally to your project, the registry version will overwrite your local
changes.

## Local packages inside your project

You can place a local package anywhere inside your project except under these
folders:

**Project folder:** | **Reason:**  
---|---  
`Assets` | If you place a package inside this folder, the Asset Database imports any assets under this folder twice: once as assets and once as package contents.  
`Library` | Do not modify the contents of this folder.  
`ProjectSettings` | This folder is for [settings](comp-ManagerGroup.html) assets only.  
`Packages` | If you place a package under this folder, the Package Manager automatically interprets it as an **Embedded package** An _embedded_ package is a mutable package that you store under the `Packages` directory at the root of a Unity project. This differs from most packages which you download from a package server and are immutable. [More info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage), regardless of the reference
in the **project manifest** Each Unity project has a _project manifest_ ,
which acts as an entry point for the Package Manager. This file must be
available in the `<project>/Packages` directory. The Package Manager uses it
to configure many things, including a list of dependencies for that project,
as well as any package repository to query for packages. [More info](upm-
manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest).  
  
## Additional resources

  * [Package types](upm-package-types.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)

[](upm-ui-install2.html)

Install a UPM package from the Asset Store

[](upm-ui-tarball.html)

Install a UPM package from a local tarball file

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

