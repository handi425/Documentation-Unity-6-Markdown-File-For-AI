[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-tarball.html)
  * [中文](/cn/current/Manual/upm-ui-tarball.html)
  * [日本語](/ja/current/Manual/upm-ui-tarball.html)
  * [한국어](/kr/current/Manual/upm-ui-tarball.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-tarball.html)
  * [中文](/cn/current/Manual/upm-ui-tarball.html)
  * [日本語](/ja/current/Manual/upm-ui-tarball.html)
  * [한국어](/kr/current/Manual/upm-ui-tarball.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * Install a UPM package from a local tarball file

[](upm-ui-local.html)

Install a UPM package from a local folder

[](upm-ui-giturl.html)

Install a UPM package from a Git URL

# Install a UPM package from a local tarball file

The Package Manager can load a **UPM package** A **Package** managed by the
**Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) from a tarball file stored
locally. This is for advanced scenarios where you break your package
publishing workflow into parts and your users can use the intermediate product
of one of those parts.

For example, if you’ve set up continuous integration (CI) on your custom
package repository, you can create a
[Gzip](https://www.gnu.org/software/gzip/) tarball file from a package folder.
You can create a `Gzip` tarball file by using the [npm
pack](https://docs.npmjs.com/cli/pack.html) CLI or Unity Package Manager’s
[Pack](../ScriptReference/PackageManager.Client.Pack.html) API. If you create
a `Gzip` tarball file, test it before you publish it to a custom registry.

To install a UPM package from a local tarball file:

  1. Open the [Package Manager window](upm-ui-access.html), if it’s not already open.

  2. Click the **install** ![](../uploads/Main/iconAdd.png) button in the toolbar. The options for installing packages appear.

![Install package from tarball menu item](../uploads/Main/upm-ui-tarball.png)
**Install package from tarball** menu item

  3. Select **Install package from tarball** from the install menu to bring up a file browser.

  4. Go to the folder where you saved your tarball.

**Note** : The Package Manager’s file selection dialog recognizes tarballs
only if they have a `.tgz` extension.

  5. Double-click the tarball file in the file selection dialog.

The file selection dialog closes, and the package now appears in the [list
panel](upm-ui-list.html) with the ![](../uploads/Main/iconLocal.png) label.

## Additional resources

  * [Package types](upm-package-types.html)
  * [Add and remove UPM packages or feature sets](upm-ui-actions.html)
  * [Add and remove asset packages](upm-ui-actions-ap.html)

[](upm-ui-local.html)

Install a UPM package from a local folder

[](upm-ui-giturl.html)

Install a UPM package from a Git URL

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

