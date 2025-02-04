[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/tvos-building-your-application.html)
  * [中文](/cn/current/Manual/tvos-building-your-application.html)
  * [日本語](/ja/current/Manual/tvos-building-your-application.html)
  * [한국어](/kr/current/Manual/tvos-building-your-application.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/tvos-building-your-application.html)
  * [中文](/cn/current/Manual/tvos-building-your-application.html)
  * [日本語](/ja/current/Manual/tvos-building-your-application.html)
  * [한국어](/kr/current/Manual/tvos-building-your-application.html)

  * [Platform development ](PlatformSpecific.html)
  * [tvOS](tvOS-introducing.html)
  * Build your application for tvOS

[](tvos-debugging.html)

Debugging Your Application

[](WindowsStore.html)

Universal Windows Platform

# Build your application for tvOS

To build your Unity application for tvOS, use the following steps:

  1. Open the [Build Profiles window](BuildSettings.html) from **File** > **Build Profiles**.
  2. Select **Add**Build Profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)** to open the **Platform
Browser** window.

  3. Select **tvOS** from the list of available platforms. If **tvOS** isn’t an option, select **Install with Unity Hub** and follow the installation instructions. For information on how to install modules, refer to [Add modules](https://docs.unity3d.com/hub/manual/AddModules.html).
  4. Set **Architecture** to the architecture type you want Unity to build your application for.
  5. If you want to create an [Xcode project](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Projects.html) for your application, enable **Create Xcode Project**.
  6. Select **Switch Profile** to set the new build profile as the active profile.
  7. Click **Build**.

Similar to iOS, building your application to a tvOS device involves two steps:

  1. Unity builds an [Xcode project](https://docs.unity3d.com/2021.2/Documentation/Manual/StructureOfXcodeProject.html).
  2. Xcode builds that project to your device.

To select the device that Xcode builds to, follow these steps:

  1. Connect the device to your computer.
  2. From Xcode’s main menu, go to **Product** > **Destination** , and select your device from the Devices list.

tvOS build settings are the exact same as those for iOS. Refer to [iOS build
settings](BuildSettingsiOS.html) to check which settings you can configure for
your build.

## Incremental build pipeline

Unity uses the [incremental build pipeline](incremental-build-pipeline.html)
when it builds the Player for tvOS. This means that Unity incrementally
builds/generates files such as [Information Property
List](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html)
(plist) files and
[Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements)
files. If you implement callbacks that modify or move any iOS file or asset
that the incremental build pipeline uses, see [Creating non-incremental
builds](incremental-build-pipeline.html#creating-non-incremental-builds).

[](tvos-debugging.html)

Debugging Your Application

[](WindowsStore.html)

Universal Windows Platform

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

