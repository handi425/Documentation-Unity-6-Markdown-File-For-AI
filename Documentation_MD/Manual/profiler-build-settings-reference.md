[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-build-settings-reference.html)
  * [中文](/cn/current/Manual/profiler-build-settings-reference.html)
  * [日本語](/ja/current/Manual/profiler-build-settings-reference.html)
  * [한국어](/kr/current/Manual/profiler-build-settings-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-build-settings-reference.html)
  * [中文](/cn/current/Manual/profiler-build-settings-reference.html)
  * [日本語](/ja/current/Manual/profiler-build-settings-reference.html)
  * [한국어](/kr/current/Manual/profiler-build-settings-reference.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Connecting the Profiler to a data source](profiler-profiling-applications.html)
  * Build Profiles Profiler settings

[](profiling-edit-mode.html)

Collect performance data about the Unity Editor

[](profiler-visualizing-data.html)

Data visualization

# Build Profiles Profiler settings

Configure the way the **Profiler** A window that helps you to optimize your
game. It shows how much time is spent in the various areas of your game. For
example, it can report the percentage of time spent rendering, animating, or
in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) collects data when you build your
application.

The [Build Profiles window](build-profiles.html) has settings which you can
enable to change how the Profiler measures data.

## Prerequisites

To enable the Profiler specific settings, you must enable the ****Development
Build** A development build includes debug symbols and enables the Profiler.
[More info](https://docs.unity.com/devops/en/manual/build-target-
configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)** setting:

  1. Open the **Build Profiles** window (menu: **File > Build Profiles**)
  2. Select your application’s target platform
  3. Enable the **Development Build** setting

![Build Profiles with Development Build enabled](../uploads/Main/profiler-
build-profiles.png) Build Profiles with Development Build enabled

## Profiler Build Profiles settings

There are two settings related to how the Profiler collects data.

**Setting** | **Description**  
---|---  
**Autoconnect Profiler** | Enable this setting to automatically connect to the Profiler when your application starts. The Unity Editor bakes its IP address into the built player during the build process. When you start the player, it attempts to connect to the Profiler in the Editor located at the baked IP address.  
**Deep Profiling Support** | Unity performs [Deep Profiling](profiler-deep-profiling.html) when the built Player starts, which means that the Profiler profiles every part of your code, and not just code timings explicitly wrapped in [Profiler markers](profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](profiler-markers.html)  
See in [Glossary](Glossary.html#Profilermarker). This is useful to get
profiling information on your application’s start up times, however, this adds
a small amount of overhead to your build.  
  
## Additional resources

  * [Connecting the Profiler to a data source](profiler-profiling-applications.html)
  * [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)

  * [Instrument all function calls](profiler-deep-profiling.html)
  * [Profiler markers introduction](profiler-markers.html)

[](profiling-edit-mode.html)

Collect performance data about the Unity Editor

[](profiler-visualizing-data.html)

Data visualization

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

