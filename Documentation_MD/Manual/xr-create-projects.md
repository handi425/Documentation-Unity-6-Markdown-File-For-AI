[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-create-projects.html)
  * [中文](/cn/current/Manual/xr-create-projects.html)
  * [日本語](/ja/current/Manual/xr-create-projects.html)
  * [한국어](/kr/current/Manual/xr-create-projects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-create-projects.html)
  * [中文](/cn/current/Manual/xr-create-projects.html)
  * [日本語](/ja/current/Manual/xr-create-projects.html)
  * [한국어](/kr/current/Manual/xr-create-projects.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR project set up](configuring-project-for-xr.html)
  * Create an XR project

[](xr-configure-providers.html)

Choose XR provider plug-ins

[](xr-scene-setup.html)

Set up an XR scene

# Create an XR project

To create an **XR** An umbrella term encompassing Virtual Reality (VR),
Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting
these forms of interactive applications can be referred to as XR devices.
[More info](XR.html)  
See in [Glossary](Glossary.html#XR) project, you can use an XR template from
the Unity Hub or start with a non-XR project.

  * Create a new XR project
  * Start from a non-XR project

## Prerequisites

To create an XR project, you must first perform the following tasks:

  * [Install the Unity Editor](https://docs.unity3d.com/hub/manual/AddEditor.html#install-an-editor-via-the-hub).
  * [Add Editor modules](https://docs.unity3d.com/hub/manual/AddModules.html) to support the platform build targets on which the XR devices that you want to support run. For example, to support Android devices with ARCore or Meta Quest devices, you must add the Android module to your Editor using the Unity Hub.

**Note:** The makers of some XR devices might impose additional requirements,
such as signing up for a developer account, in order to create applications
for their platform. Such requirements are outside the scope of Unity
documentation.

## XR templates

The quickest way to create a new XR project is with one of the XR templates in
the Unity Hub. Projects you create with these templates are already configured
with the XR **Plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) Management system, common XR plug-in
and support packages, and a starting **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) set up with the XR components.

The XR templates available for this version of Unity include:

Template | Version | Description  
---|---|---  
[AR Mobile template](https://docs.unity3d.com/Packages/com.unity.template.ar-mobile@2.0) | 2.0 | For mobile **augmented reality** Augmented Reality (AR) uses computer graphics or video composited on top of a live video feed to augment the view and create interaction with real and virtual objects. [More info](AROverview.html)  
See in [Glossary](Glossary.html#AugmentedReality) projects. The template
configures the project for URP, **AR** Augmented Reality [More
info](AROverview.html)  
See in [Glossary](Glossary.html#AR) Foundation, iOS, Android and the XR
Interaction Toolkit. It includes an example scene and assets to demonstrate
how to set up a project that’s ready for AR development on mobile devices.  
[Mixed Reality template](https://docs.unity3d.com/Packages/com.unity.template.mixed-reality@2.1) | 2.1 | For **mixed reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](Glossary.html#MixedReality) projects. The template
configures the project for URP, OpenXR, AR Foundation, and the XR Interaction
Toolkit. It includes an example scene and assets to demonstrate how to set up
a project that’s ready for Mixed Reality.  
[Mixed Reality multiplayer tabletop template](https://docs.unity3d.com/Packages/com.unity.template.mr-multiplayer@1.0/manual/index.html) | 1.0 | For multiplayer mixed reality projects. This template combines XRI, ARF, NGO, and UGS to create a starting point for Tabletop **MR** Mixed Reality  
See in [Glossary](Glossary.html#MR) Multiplayer apps.  
[VR template](https://docs.unity3d.com/Packages/com.unity.template.vr@9.1) | 9.1 | For **virtual reality** Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) projects. The template
configures the project for URP, OpenXR, and the XR Interaction Toolkit. It
includes an example scene and assets to demonstrate how to set up a project
that’s ready for interactive **VR** Virtual Reality [More
info](VROverview.html)  
See in [Glossary](Glossary.html#VR).  
[VR Multiplayer template](https://docs.unity3d.com/Packages/com.unity.template.vr-multiplayer@2.0) | 2.0 | For virtual reality projects with multiplayer functionality. The template configures the project for URP, Netcode for Game Objects, Unity Cloud Gaming Services, and XR Interaction Toolkit. It includes example scenes and assets to demonstrate how to set up a project that’s ready for multiplayer VR experiences.  
  
Choose a template in the Unity Hub when you create a new project.

## Create a new XR project

To create an XR project using a template:

  1. Open the Unity Hub.
  2. In the Hub, click the **New Project** button.
  3. Select the desired template: **Mixed Reality** , **VR** , or **AR Mobile**.
  4. If necessary, click **Download template**.
  5. Set a project name and save location.
  6. Click **Create project**. Refer to the [Unity Hub documentation](https://docs.unity3d.com/hub/manual/AddProject.html) for more information about creating projects in the Unity Hub.
  7. After the project opens in the Editor, [configure the project’s XR plug-ins](configuring-project-for-xr.html) with the **XR Plug-in Management** system.
  8. Add additional XR packages, such as [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/) and the [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/), using the Package Manager. (A template might include these and other packages already.)
  9. [Set up an XR scene](xr-scene-setup.html).

**Tip:** After you create an XR project, go to the **XR Plug-in Management**
section in your ****Project Settings** A broad collection of settings which
allow you to configure how Physics, Audio, Networking, Graphics, Input and
many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)** and enable the plug-ins for
the platforms you want to support. If the tab for a platform is missing on the
XR Plug-in Management page, add the platform module to your Editor
installation using the [Unity
Hub](https://docs.unity3d.com/hub/manual/AddModules.html).

## Start from a non-XR project

You can always convert an existing non-XR project:

  1. Use the Unity Hub to open the project.
  2. In the Editor, [configure the project’s XR plug-ins](configuring-project-for-xr.html) with the **XR Plug-in Management** system.
  3. Add additional XR packages, such as [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/) and the [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/), using the Package Manager.
  4. [Set up an XR scene](xr-scene-setup.html).

[](xr-configure-providers.html)

Choose XR provider plug-ins

[](xr-scene-setup.html)

Set up an XR scene

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

