[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/cus-naming.html)
  * [中文](/cn/current/Manual/cus-naming.html)
  * [日本語](/ja/current/Manual/cus-naming.html)
  * [한국어](/kr/current/Manual/cus-naming.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/cus-naming.html)
  * [中文](/cn/current/Manual/cus-naming.html)
  * [日本語](/ja/current/Manual/cus-naming.html)
  * [한국어](/kr/current/Manual/cus-naming.html)

  * [Packages and feature sets](PackagesList.html)
  * [Creating custom packages](CustomPackages.html)
  * Naming your package

[](CustomPackages.html)

Creating custom packages

[](cus-layout.html)

Package layout

# Naming your package

There are two names for a package: the [official name](upm-
manifestPkg.html#name) you register the package with; and the user-facing
[display name](upm-manifestPkg.html#displayName) that users can see in the
Editor.

The display name should be brief but provide some indication of what the
package contains. Otherwise, the Unity Package Manager imposes no restrictions
on the display name.

The official name must conform to the Unity Package Manager naming convention,
which uses reverse domain name notation. The name must:

  * Start with **< domain-name-extension>.<company-name>** (for example, `com.example` or `net.example`), even if your company or website name begins with a digit.
  * Be no more than 50 characters if you want it to be visible in the Editor. If the package name does not need to appear in the Editor, the Unity Package Manager imposes a limit of 214 characters or less.
  * Contain only lowercase letters, digits, hyphens(-), underscores (_), and periods (.)
  * To indicate nested namespaces, suffix the namespace with an additional period. For example, “**com.unity.2d.animation** ” and “**com.unity.2d.ik** ”.

For example, “**com.unity.2d.animation** ” and “**com.unity.2d.ik** ” are the
names of two Unity 2D packages, but a custom package developer at
https://example.net might create a package named “**net.example.physics** ”.
Use your own company name in your package names. Do not use the “unity” prefix
in your own package names.

**Note** : These naming restrictions apply only to the package names
themselves and do not need to match the namespace in your code. For example,
you could use `Project3dBase` as a namespace in a package called
**net.example.3d.base**.

  

[](CustomPackages.html)

Creating custom packages

[](cus-layout.html)

Package layout

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

