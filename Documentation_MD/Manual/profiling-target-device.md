[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiling-target-device.html)
  * [中文](/cn/current/Manual/profiling-target-device.html)
  * [日本語](/ja/current/Manual/profiling-target-device.html)
  * [한국어](/kr/current/Manual/profiling-target-device.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiling-target-device.html)
  * [中文](/cn/current/Manual/profiling-target-device.html)
  * [日本語](/ja/current/Manual/profiling-target-device.html)
  * [한국어](/kr/current/Manual/profiling-target-device.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Connecting the Profiler to a data source](profiler-profiling-applications.html)
  * Collect performance data on a target platform

[](profiler-profiling-applications.html)

Connecting the Profiler to a data source

[](profiling-play-mode.html)

Collect performance data in Play mode

# Collect performance data on a target platform

Record performance data with the Unity **Profiler** A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) on a target platform.

You can record the performance of your application on your chosen release
platform to discover realistic performance metrics about your application. The
Profiler can connect to your application when it’s running on a target device
in the following ways:

  * Via the local network
  * Directly via cable
  * Via IP address

## Connect your application to the Profiler

To connect your application to the Profiler:

  1. Open the **Build Profiles** window (menu: **File > Build Profiles**)
  2. Select your application’s target platform
  3. Enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)** setting

  4. Optionally enable the **Autoconnect Profiler** setting to automatically connect to the Profiler
  5. Optionally enable **Deep Profiling Support** to use [Deep Profiling](profiler-deep-profiling.html)
  6. Select **Build and Run** , and make sure your application is running on your target device.
  7. Open the Profiler window (menu: **Window > Analysis > Profiler**). If you enabled the **Autoconnect Profiler** setting, the Profiler automatically collects data.
  8. If the **Autoconnect Profiler** setting is disabled, Select the Target Selection dropdown menu, next to the Record icon (⏺), and select the target player from the list.
  9. Select the Record icon

![Profiler windows Target Selection dropdown](../uploads/Main/profiler-target-
player.png) Profiler window’s Target Selection dropdown

If you’ve enabled the **Autoconnect Profiler** setting, the Profiler collects
data as soon as you open the Profiler window, as long as your application is
running. Otherwise, the Profiler window collects data when you select the
target from the Target Selection dropdown and select Record.

### Connect to an application via IP address

To connect via IP address:

  1. Open the Profiler window (menu: **Window > Analysis > Profiler**)
  2. Select the Target Selection dropdown menu, next to the Record icon (⏺)
  3. Select **< Enter IP>** in the dropdown.
  4. Enter the IP address in the dialog that appears, and optionally the port of the player you want to connect to.
  5. Select the Record icon

## Continuously collect data

To continuously collect data while your application runs:

  1. Open Player Settings (menu: **Edit > Project Settings > Player**)
  2. Under Resolution and Presentation, enable **Run In Background**

## Additional resources

  * [Collecting performance data on an Android device](android-profile-on-an-android-device.html)
  * [Collecting performance data on an iOS device](ios-profile-device.html)
  * [Collecting performance data in Play mode](profiling-play-mode.html)
  * [Collecting performance data about the Unity Editor](profiling-edit-mode.html)

[](profiler-profiling-applications.html)

Connecting the Profiler to a data source

[](profiling-play-mode.html)

Collect performance data in Play mode

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

