[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xr-configure-providers.html)
  * [中文](/cn/current/Manual/xr-configure-providers.html)
  * [日本語](/ja/current/Manual/xr-configure-providers.html)
  * [한국어](/kr/current/Manual/xr-configure-providers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xr-configure-providers.html)
  * [中文](/cn/current/Manual/xr-configure-providers.html)
  * [日本語](/ja/current/Manual/xr-configure-providers.html)
  * [한국어](/kr/current/Manual/xr-configure-providers.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [XR project set up](configuring-project-for-xr.html)
  * Choose XR provider plug-ins

[](configuring-project-for-xr.html)

XR project set up

[](xr-create-projects.html)

Create an XR project

# Choose XR provider plug-ins

Provider **plug-ins** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) are packages created to support
**XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality
(AR) and Mixed Reality (MR) applications. Devices supporting these forms of
interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) devices and platforms.

Use the **XR Plug-in Management** settings to manage which XR devices and
platforms your project supports. You can also configure key settings for these
XR provider plug-ins.

See [XR provider plug-in framework](XRPluginArchitecture.html#xr-provider-
plug-ins) for information about provider plug-ins and how they work.

## Prerequisites

Before you can enable XR plug-ins, you must install the XR Plug-in Management
package. You can install the package directly from the **Project Settings** A
broad collection of settings which allow you to configure how Physics, Audio,
Networking, Graphics, Input and many other areas of your project behave. [More
info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window:

  1. Open the Project Settings window (menu: **Edit > Project Settings**).

  2. Select **XR Plug-in Management** from the list of settings areas along the left side of the settings window.

![](../uploads/Main/xr-management-before.png)  
_Before installing the XR Plug-in Management package_

  3. If necessary, click **Install XR Plug-in Management**.

![](../uploads/Main/xr-management-installed.png)  
_After installing the XR Plug-in Management package_

The XR Plug-in Management settings page displays a tab for each available
build target. Each tab displays the list of available XR provider plug-ins for
that platform. This list contains the plug-ins officially supported by Unity
or its partners and also any third-party provider plug-ins you have installed
with the Package Manager.

**Tip:** Use the Unity Hub to install platform modules, such as Android or
iOS, to add support for additional build targets. See [Add
modules](https://docs.unity3d.com/hub/manual/AddModules.html) in the Unity Hub
documentation for instructions.

## Enable provider plug-ins

When you enable a plug-in, XR Plug-in Management installs the associated
package.

To enable a provider plug-in:

  1. Open the Project Settings window (menu: **Edit > Project Settings**) and select the **XR Plug-in Management** section.

  2. Select the tab for the target build platform. For example, to enable a plug-in for a device that runs the Android operating system, click the tab with the Android icon.

![](../uploads/Main/xr-management-enable-plugin.png)  
_Android build platform with the ARCore provider enabled_

  3. Enable the desired provider plug-in.

  4. Repeat for additional plug-ins.

**Notes:**

  * Disabling a provider does not remove the package; to remove a provider plug-in, remove the associated package with the [Package Manager](upm-ui-remove.html).
  * If you do not see a provider in the list, you might need to install the associated package with the [Package Manager](upm-ui-install.html). Some provider plug-in packages are distributed by the device maker, not by Unity.

## Set provider plug-in options

After you enable a provider plug-in and Unity installs the associated package,
any settings for the provider are displayed as subsections under the **XR
Plug-in Management** settings.

![](../uploads/Main/xr-management-settings.png)  
_Oculus provider plug-in settings under XR Plug-in Management_

If a plug-in supports more than one build target, its settings page includes a
tab so that you can configure the settings for each target independently.

To configure the settings for a provider plug-in:

  1. Open the Project Settings window (menu: **Edit > Project Settings**).
  2. Under **XR Plug-in Management** , select the name of the provider plug-in.
  3. If present, select the tab for the platform build target. For example, to configure settings for Android devices, click the tab with the Android icon. (The tabs are only shown when a plug-in supports more than one build target.)
  4. Configure the settings as required.

See the documentation of individual plug-ins for information about plug-in
settings. You can access the documentation using the **View documentation**
link in the Package Manager.

![](../uploads/Main/xr-plugin-docs.png)  
_Use the**View documentation** link to access plug-in documentation_

## Project validation

Some provider plug-ins and other packages implement project validation checks
to help ensure that your project is set up correctly. You can view the status
of these checks on the **Project Validation** section underneath **XR Plug-in
Management** on the ****Player Settings** Settings that let you set various
player-specific options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings)** window.

![](../uploads/Main/xr-project-validation.png)  
_Project validation checks_

If a validation check is followed by a **Fix** button, you can click the
button to automatically fix the issue. Otherwise, you must fix the issue
manually. Clicking **Edit** opens the settings **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) to the appropriate section so that you can
make any needed changes. Validation checks marked with a red stop icon must be
corrected. Checks marked with a yellow warning icon can be ignored or
deferred, but you should fix them if possible for best performance or
compatibility.

Refer to [XR project validation window](xr-plugin-management.html#project-
validation) for additional information.

## Support multiple provider plug-ins

You can enable more than one provider plug-in to support multiple XR devices
and platforms in the same project.

**Note:** In some cases, one provider plug-in can support more than one device
and operating system. For example, the OpenXR plug-in supports multiple XR
devices, operating systems, and build targets.

Unity includes all the enabled plug-ins for the current build target when you
make a build. At runtime, Unity uses the first plug-in that loads
successfully. Unity attempts to load provider plug-ins in the order they are
shown in the XR Plug-in Management list, which is in alphabetical order by
default. If you need more control over which plug-in is loaded, you can do one
of the following:

  * Disable **Initialize XR at startup** and include your own application logic for selecting the provider at runtime.
  * Include your own custom build script to sort the list of providers in the desired order.
  * Manually enable only the desired provider before building.

See [XR
loading](https://docs.unity3d.com/Packages/com.unity.xr.management@4.3/manual/index.html#automatic-
xr-loading) for more information about customizing how provider plug-ins are
loaded and initialized.

**Note** : The **Mock HMD Loader** plug-in only works in the Unity Editor
during Play mode and does not affect builds.

[](configuring-project-for-xr.html)

XR project set up

[](xr-create-projects.html)

Create an XR project

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

