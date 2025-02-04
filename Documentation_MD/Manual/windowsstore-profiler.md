[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-profiler.html)
  * [中文](/cn/current/Manual/windowsstore-profiler.html)
  * [日本語](/ja/current/Manual/windowsstore-profiler.html)
  * [한국어](/kr/current/Manual/windowsstore-profiler.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-profiler.html)
  * [中文](/cn/current/Manual/windowsstore-profiler.html)
  * [日本語](/ja/current/Manual/windowsstore-profiler.html)
  * [한국어](/kr/current/Manual/windowsstore-profiler.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * Connect the profiler to UWP

[](deep-linking-universal-windows-platform.html)

Use deep linking on UWP

[](uwp-defines.html)

UWP scripting symbols

# Connect the profiler to UWP

You can use the Unity **profiler** A window that helps you to optimize your
game. It shows how much time is spent in the various areas of your game. For
example, it can report the percentage of time spent rendering, animating, or
in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) to get performance information about
your application. For more information, refer to [Profiling your
application](profiler-profiling-applications.html).

Due to restrictions with UWP, you won’t be able to connect the profiler if the
Unity Editor is running on the same machine as UWP. Therefore, make sure to
run the Unity Editor and UWP on separate machines. For example, if you’re
running the Unity Editor and UWP on the same PC, you won’t be able to connect
the profiler. The only exception to this rule is the **Autoconnect Profiler**
build option, which makes the application connect to the Editor instead.

You must also ensure that the machine where the Unity Editor is running and
the machine where the Universal Windows App is running are on the same subnet.

**Note:** The profiler doesn’t work on Master configuration.

## Connect the Unity profiler

To connect the Unity profiler to a running Universal Windows application,
perform the following steps:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. Select the **Publishing Settings** > **Capabilities** section.
  3. Enable **Private Networks Capability**.
  4. Enable **Internet (Client & Server) Capability**.
  5. If you’ve already selected the **Autoconnect Profiler** checkbox in [Build Settings](windowsstore-buildsettings.html), the profiler should connect automatically to the Universal Windows App. If not, you have to explicitly select it in Unity in **Window** > **Analysis** > **Profiler** > **Active Profiler**.
  6. Build the Universal Windows App Visual Studio solution from Unity.
  7. Select **Build and Run**.

[](deep-linking-universal-windows-platform.html)

Use deep linking on UWP

[](uwp-defines.html)

UWP scripting symbols

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

