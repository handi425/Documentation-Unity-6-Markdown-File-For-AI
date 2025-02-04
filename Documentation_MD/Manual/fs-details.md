[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/fs-details.html)
  * [中文](/cn/current/Manual/fs-details.html)
  * [日本語](/ja/current/Manual/fs-details.html)
  * [한국어](/kr/current/Manual/fs-details.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/fs-details.html)
  * [中文](/cn/current/Manual/fs-details.html)
  * [日本語](/ja/current/Manual/fs-details.html)
  * [한국어](/kr/current/Manual/fs-details.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * Features (details panel)

[](upm-ui-details.html)

Details panel

[](upm-ui-find.html)

Finding packages and feature sets

# Features (details panel)

In the Package Manager window, when you select a [feature
set](FeatureSets.html)A feature set is a collection of related packages that
you can use to achieve specific results in the Unity Editor. You can manage
feature sets directly in Unity’s Package Manager. [More
info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset) from the list panel, the details
panel on the right displays details for the selected feature set. The details
panel presents the contents of the feature set as a kind of miniature Package
Manager window:

![For a feature set, the details panel shows a brief description, a link to
the QuickStart guide, and a list of included packages](../uploads/Main/fs-
details.png) For a feature set, the details panel shows a brief description, a
link to the QuickStart guide, and a list of included packages

**(A)** When you select a feature set from the [list panel](upm-ui-list.html),
its information appears in the details panel.

**(B)** The display name of the feature set.

**(C)** The name of the feature set.

**(D)** A button to **Install** or **Remove** the feature set.

**(E)** A link to the **QuickStart** guide for this feature set, containing
details of how you can use this set of packages together.

**(F)** Feature set details tabs:

  * **Description** : A brief overview of the feature set.
  * **Packages Included** : This tab displays the following information: 
    1. The list of included packages.
    2. The details of the selected package. The information shown includes the display name of the package, the recommended or installed version for the feature set, and its description.
    3. A shortcut to load the selected package in the Package Manager window. Selecting this shortcut replaces the feature set in the list panel and details panel. When you access details from the package directly, the Package Manager window provides more information than when you access them from inside the feature set. For example, the package details view shows dependency information and any samples the package has.

## Package version overrides

Feature sets are collections of packages that work well together for a
specific version of Unity, which means the Package Manager installs specific
package versions that your feature set requires. However, there are a couple
of reasons why the Package Manager might actually install a different version
(override the requested version):

  * Another package or feature set requires a different version of the same package and the [Package Manager resolved](upm-conflicts.html) the package version by overriding it.
  * You requested a different package version and it didn’t conflict with the version that the feature set requires. In this case, a **Reset** button displays, which you can click to return to the version that the feature set requires (recommended). 
    * **Note** : The **Reset** button displays only when the major or minor number in the package version changes. The **Reset** button doesn’t display when the patch number in the package version changes. For more information on semantic version schemes, refer to [Versioning](upm-semver.html).

If the Package Manager installs a version other than the one you requested, an
information message explains the reason for the change.

[](upm-ui-details.html)

Details panel

[](upm-ui-find.html)

Finding packages and feature sets

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

