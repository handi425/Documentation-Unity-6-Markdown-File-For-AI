[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-deviceportal.html)
  * [中文](/cn/current/Manual/windowsstore-deviceportal.html)
  * [日本語](/ja/current/Manual/windowsstore-deviceportal.html)
  * [한국어](/kr/current/Manual/windowsstore-deviceportal.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-deviceportal.html)
  * [中文](/cn/current/Manual/windowsstore-deviceportal.html)
  * [日本語](/ja/current/Manual/windowsstore-deviceportal.html)
  * [한국어](/kr/current/Manual/windowsstore-deviceportal.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Build and deliver for Universal Windows Platform](uwp-building-and-delivering.html)
  * Deploy a Windows or UWP app with the Windows Device Portal

[](windowsstore-deployment.html)

Deploy a UWP application

[](visionOS.html)

visionOS

# Deploy a Windows or UWP app with the Windows Device Portal

You can use the [Windows Device Portal](https://learn.microsoft.com/en-
us/windows/uwp/debug-test-perf/device-portal) to build and run Windows or
Universal Windows Platform (UWP) applications to a remote Windows 10+ device
directly from the Unity Editor, alleviating the need to generate a Visual
Studio project. Being connected remotely to a remote Windows device allows you
to make faster iterations for testing your Unity Project.

## Set up the Device Portal

Before you set up the Device Portal in Unity, make sure that you [enable
Developer Mode and Device Portal on your Windows
device](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-
portal) using the **For Developer** section in Settings (Settings > Privacy &
security > For developers).

To access the Device Portal settings for your Unity project:

  1. Go to **File** > **Build Settings**.
  2. From the list of platforms in the Platform panel, select **Windows, Mac, Linux** and set the Target Platform as **Windows**. To build **UWP** , select **Universal Windows Platform** from the platform panel.
  3. Set **Build and Run on** as **Remote Device (via Device Portal)**.
  4. Fill in the following fields that appear.

**Setting** | **Description**  
---|---  
**Device Portal Address** | Enter the IP address and port number for the Device Portal. On Windows, locate the address in **Privacy & security** > **For Developers** > **Device Portal** > **Connect using**.  
**Device Portal Username** | Enter the username for the Device Portal. This is optional if you [enable WDP authentication](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal).  
**Device Portal Password** | Enter the password for the Device Portal. This is optional if you [enable WDP authentication](https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal).  
  
Unity saves the **Device Portal Address** and **Device Portal Username**
fields in ****Project settings** A broad collection of settings which allow
you to configure how Physics, Audio, Networking, Graphics, Input and many
other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)**. For security purposes,
Unity doesn’t save your Device Portal password, so you might need to re-enter
your password when you restart the Editor or load a new project.

**Tip:** You can also use the Executable Only build type with Device Portal
deployment for **UWP**. This makes iteration times faster on devices like
HoloLens.

## Run your app on the remote device

When you have completed the setup for the Device Portal, select **Build and
Run**. This builds the UWP/Windows app, deploys it to the remote device, and
then launches it.

[](windowsstore-deployment.html)

Deploy a UWP application

[](visionOS.html)

visionOS

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

