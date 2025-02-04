[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-ui-filter.html)
  * [中文](/cn/current/Manual/upm-ui-filter.html)
  * [日本語](/ja/current/Manual/upm-ui-filter.html)
  * [한국어](/kr/current/Manual/upm-ui-filter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-ui-filter.html)
  * [中文](/cn/current/Manual/upm-ui-filter.html)
  * [日本語](/ja/current/Manual/upm-ui-filter.html)
  * [한국어](/kr/current/Manual/upm-ui-filter.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * [Package Manager window](upm-ui.html)
  * [Finding packages and feature sets](upm-ui-find.html)
  * Packages list context

[](upm-ui-find.html)

Finding packages and feature sets

[](upm-ui-sort.html)

Sorting the list

# Packages list context

To change which packages appear in the list panel of the Package Manager
window, select the context you want from the navigation panel.

![Set the context for the packages you want to appear in the
list](../uploads/Main/upm-ui-unityregistry.png) Set the context for the
packages you want to appear in the list

You can select from these options:

**Context** | **Description**  
---|---  
**In Project** | Displays all feature sets and packages installed in your project, including [local](upm-localpath.html), [git](upm-git.html), and [embedded](upm-embed.html) packages, and packages installed from any registry. The list also includes any packages from the Asset Store that you added from the **My Assets** context.   
**In Project** has a nested entry, **Updates** , which lists all packages in
your project that you can update, including Asset Store packages.  
**Unity Registry** | Displays all **feature sets** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset) and packages on the [Unity package
registry](upm-concepts.html#Registry), regardless of whether they’re already
installed in your project. This doesn’t include packages installed from any
other location or from any [scoped registry](upm-scoped.html).  
**My Assets** | Displays all [Asset Store packages](AssetStorePackages.html) that you have purchased using the Unity ID you are currently logged in with.  
**Built-in** | Displays only built-in Unity packages, which represent core Unity features. You can use these packages to [turn Unity modules on and off](upm-ui-disable.html).  
  
**Tip** : You can find out more about what each built-in package (module)
implements in the [Unity Scripting API](upm-api.html). Each module assembly
page lists which APIs the built-in package implements.  
**Services** A Unity facility that provides a growing range of complimentary
services to help you make games and engage, retain and monetize audiences.
[More info](UnityServices.html)  
See in [Glossary](Glossary.html#Services) | Displays integrated [services](UnityServices.html) to help you to engage, retain, and monetize audiences.  
**My Registries** | Displays any packages available from any [scoped registry](upm-scoped.html) installed in this project.  
  
This context appears only if you installed a scoped registry in this project.  
  
If you installed a scoped registry but it’s not listed in the **My
Registries** context or the **My Registries** context isn’t available at all,
it might be because the package registry server you added doesn’t implement
either of the `/-/v1/search` or `/-/all` endpoints, which means that it’s not
compatible with Unity’s Package Manager.  
  
When you select a context in the navigation panel, the [list panel](upm-ui-
list.html) displays the feature sets and packages that match your choice.

**Note** : If you entered any text in the [search box](upm-ui-search.html) or
set any [filters](upm-ui-filter2.html), the list panel displays only feature
sets and packages which match the context, the search criteria, and the active
filters.

[](upm-ui-find.html)

Finding packages and feature sets

[](upm-ui-sort.html)

Sorting the list

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

