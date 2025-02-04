[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-giturl.html)
  * [中文](/cn/current/Manual/upm-ui-giturl.html)
  * [日本語](/ja/current/Manual/upm-ui-giturl.html)
  * [한국어](/kr/current/Manual/upm-ui-giturl.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-giturl.html)
  * [中文](/cn/current/Manual/upm-ui-giturl.html)
  * [日本語](/ja/current/Manual/upm-ui-giturl.html)
  * [한국어](/kr/current/Manual/upm-ui-giturl.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * Install a UPM package from a Git URL

[](upm-ui-tarball.html)

Install a UPM package from a local tarball file

[](upm-ui-quick.html)

Install a UPM package by name

# Install a UPM package from a Git URL

The Package Manager can load a **UPM package** A **Package** managed by the
**Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) from a Git repository on a remote
server.

## Prerequisites

  * Install the [Git client](https://git-scm.com/) (minimum version 2.14.0) on your computer.
  * On Windows, add the Git executable path to the `PATH` system environment variable.
  * If the target repository tracks files with Git LFS, install the [Git LFS client](https://git-lfs.com/) on your computer.
  * Read the information about using [Git dependencies](upm-git.html)The Package Manager retrieves Git dependencies from a Git repository directly rather than from a package registry. Git dependencies use a Git URL reference instead of a version, and there’s no guarantee about the package quality, stability, validity, or even whether the version stated in its `package.json` file respects Semantic Versioning rules with regards to officially published releases of this package. [More info](upm-concepts.html#Git)  
See in [Glossary](Glossary.html#Gitdependency) in your project.

## Procedure

To install a UPM package from a Git URL:

  1. Open the [Package Manager window](upm-ui-access.html), if it’s not already open.

  2. Open the **install** ![](../uploads/Main/iconAdd.png) menu in the Package Manager’s toolbar.

  3. The options for installing packages appear.

![Install package from git URL button](../uploads/Main/upm-ui-giturl.png)
Install package from git URL button

  4. Select **Install package from git URL** from the install menu. A text box and an **Install** button appear.

  5. Enter a valid Git URL in the text box. For information about how to construct a valid Git URL, refer to [Git URLs and extended syntax](upm-git.html#syntax). Examples of valid Git URLs include: 
     * `https://github.example.com/myuser/myrepo.git` (if your package is in the root of the repository).
     * `https://github.example.com/myuser/myrepo.git?path=/subfolder` (if your package is in a [subfolder](upm-git.html#subfolder) within the repository).
  6. Select **Install**.

If Unity was able to install the package successfully, the package now appears
in the [package list](upm-ui-list.html) with the
![](../uploads/Main/iconGit.png) label. If Unity wasn’t able to install the
package, the [Unity Console](Console.html) displays an error message, such as:

  * [No ‘Git’ executable was found](upm-errors.html#git-not-found)
  * [Git-lfs: command not found](upm-errors.html#git-lfs)
  * [Repository not found](upm-errors.html#bad-url)
  * [Couldn’t read Username: terminal prompts disabled](upm-errors.html#prompts-disabled)

Click on an error message link to get some help for it on the
[Troubleshooting](upm-errors.html) page.

**Tip** : If you want to check for updates and update your Git dependency to
the latest version from the repository, click **Update**. You can also use the
[Install package from git URL](upm-ui-giturl.html) menu item to update your
Git dependency. For information on Git dependencies, refer to [Locked Git
dependencies](upm-git.html#git-locks).

## Additional resources

  * [Package types](upm-package-types.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)

[](upm-ui-tarball.html)

Install a UPM package from a local tarball file

[](upm-ui-quick.html)

Install a UPM package by name

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

