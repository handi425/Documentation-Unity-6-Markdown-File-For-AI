[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-PackageManager.html)
  * [中文](/cn/current/Manual/class-PackageManager.html)
  * [日本語](/ja/current/Manual/class-PackageManager.html)
  * [한국어](/kr/current/Manual/class-PackageManager.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-PackageManager.html)
  * [中文](/cn/current/Manual/class-PackageManager.html)
  * [日本語](/ja/current/Manual/class-PackageManager.html)
  * [한국어](/kr/current/Manual/class-PackageManager.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Project Settings](comp-ManagerGroup.html)
  * Package Manager

[](class-GraphicsSettings.html)

Graphics

[](class-PhysicsManager.html)

Physics

# Package Manager

To access the **Package Manager** settings, open the **Edit** menu, then
select **Project Settings** A broad collection of settings which allow you to
configure how Physics, Audio, Networking, Graphics, Input and many other areas
of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings), then select the **Package
Manager** category. These settings let you manage your scoped registries and
change the advanced settings for your current project.

![Properties for the Package Manager](../uploads/Main/class-
PackageManager.png) Properties for the Package Manager

**(A)** Under the **Advanced Settings** section, toggle whether pre-release
packages are visible in the Package Manager window.

**(B)** Add, change, and remove scoped registries for your project under the
**Scoped Registries** group, which has the following areas:

**(1)** The list of scoped registries currently defined for this project.

**(2)** The details for the selected scoped registry.

  

## Advanced Settings

Use the **Advanced** Settings group to toggle the Show Pre-release Package
Versions setting for your current project.

### Show Pre-release Package Versions

Enable the **Show Pre-release Package Versions** setting to display [pre-
release packages](pack-preview.html) in the Package Manager window. Pre-
release packages appear with the ![](../uploads/Main/iconPre.png) tag in the
[list panel](upm-ui-list.html) and the ![](../uploads/Main/iconPrerelease.png)
tag in the [details panel](upm-ui-details.html). These tags serve as a
reminder of which packages will release with the next long-term support (LTS)
version of the Unity Editor.

**Warning** : By default, this setting is disabled because pre-release
packages are still being verified as stable enough for production, but aren’t
fully released yet. For more information about the lifecycle of packages,
refer to [Package states and lifecycle](upm-lifecycle.html).

  

## Scoped Registries

The **Scoped Registries** group displays a list of scoped registries added to
the current project on the left of the settings group, and the details of the
selected registry on the right.

For detailed information about scoped registries, including how to use and
configure them with the Unity Package Manager, refer to [Scoped
Registries](upm-scoped.html).

**Note** : You might experience an issue when you add a scoped registry, but
it’s not listed in the **My Registries** context or the **My Registries**
context isn’t available at all. This might happen because the package registry
server you added doesn’t implement the `/-/v1/search` or `/-/all` endpoints.
Unity’s Package Manager requires these endpoints.

### Adding a new registry

To add a new scoped registry to your project:

  1. Select the **+** button at the bottom of the list of scoped registries. A new entry appears in the list as **New Scoped Registry** with blank values for the details on the right.
  2. Enter values for the [Name](upm-scoped.html#name), [URL](upm-scoped.html#url), and [Scope(s)](upm-scoped.html#scopes) properties.
  3. If you need to specify more than one scope, select the **+** button underneath the last **Scope(s)** value. Another text box appears.
  4. After you enter the information for the selected scoped registry, click **Save**. To cancel adding the new scoped registry, click **Cancel**.

### Changing an existing registry

To change an existing scoped registry:

  1. Select the registry you want to change from the list on the left. The existing information appears on the right.
  2. Change any of the [Name](upm-scoped.html#name), [URL](upm-scoped.html#url), and [Scope(s)](upm-scoped.html#scopes) properties.
  3. After you update the information for the selected scoped registry, click **Apply**. To cancel your updates, click **Revert**.

### Removing a registry

To delete an existing scoped registry:

  1. Select the registry you want to delete from the list.
  2. Click the **-** button underneath the list. A dialog prompts you to confirm the removal.
  3. Click **Ok** to remove the registry or **Cancel** to leave it intact.

  

[](class-GraphicsSettings.html)

Graphics

[](class-PhysicsManager.html)

Physics

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

