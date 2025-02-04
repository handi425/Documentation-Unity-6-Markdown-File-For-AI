[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/qnx-build-settings.html)
  * [中文](/cn/current/Manual/qnx-build-settings.html)
  * [日本語](/ja/current/Manual/qnx-build-settings.html)
  * [한국어](/kr/current/Manual/qnx-build-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/qnx-build-settings.html)
  * [中文](/cn/current/Manual/qnx-build-settings.html)
  * [日本語](/ja/current/Manual/qnx-build-settings.html)
  * [한국어](/kr/current/Manual/qnx-build-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [QNX](qnx.html)
  * [Build and deliver for QNX](qnx-build-and-deliver.html)
  * QNX Build Profiles reference

[](qnx-build-and-deliver.html)

Build and deliver for QNX

[](qnx-build-command-line.html)

Build for QNX from the command line

# QNX Build Profiles reference

Build profiles let you create custom build configurations for the QNX
platform. To create and manage a build profile for QNX, refer to [Create a
build profile](create-build-profile.html). For more information on build
profiles, refer to [Introduction to build profiles](build-profiles.html).

**Property** | **Description**  
---|---  
**QNX Version** | The target OS version for QNX is automatically detected depending on the QNX environment. For example, Neutrino RTOS 7.0 or Neutrino RTOS 7.1.  
**Architecture** | Choose the CPU architecture to build for the QNX platform.  
| **x64** | 64-bit CPU  
| **arm64** | 64-bit ARM CPU  
**Remote Device** | Deploy and launch the app to a connected device on a remote device based on the connection and authentication information you provide.  
| **Address (required)** | The address of the remote device. You can also specify a port by adding a colon after the address (for example, 10.110.91.3:2121).  
| **Username (optional)** | The user name on the remote device.  
| **Exports** | Specify the additional exports, if they’re required to launch the device remotely. Multiple environment variables are separated by a space. For example, `ENV_VAR1=1 ENV_VAR2=2`.  
| **Install Path** | The installation path for the application. If not set, the default value `~tmp/unity/test` will be used.  
**Development Build** | Include scripting debug symbols and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) in your build. Use this setting when
you want to test your application. When you select this option, Unity sets the
`DEVELOPMENT_BUILD` scripting define symbol. Your build then includes
preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  
  
For more information, refer to [Platform dependent
compilation](PlatformDependentCompilation).  
**Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](Profiler.html).  
  
**Note** : This option is available only if you select **Development Build**.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](ProfilerWindow.html#deep-profiling).   
  
This property is available only if you enable **Development Build**.  
  
**Note** : Enabling **Deep Profiling** might slow down script execution.  
**Script Debugging** | Attach script debuggers to the Player remotely.   
  
This property is available only if you enable **Development Build**.  
**Wait for Managed Debugger** | Make the Player wait for a debugger to be attached before it executes any script code.  
  
This property is visible only if you enable **Script Debugging**.  
**Compression Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes [Assets](AssetTypes.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset), [Scenes](CreatingScenes.html)A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), [Player settings](class-
PlayerSettings.html)Settings that let you set various player-specific options
for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings), and [GI data](GICache.html).  
| **Default** | On Windows, Mac, Linux Standalone, and iOS, there is no default compression.  
  
On Android, the default compression is ZIP, which gives slightly better
compression results than LZ4HC. However, ZIP data is slower to decompress.  
| **LZ4** | A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](../ScriptReference/BuildOptions.CompressWithLz4.html).  
| **LZ4HC** | A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](../ScriptReference/BuildOptions.CompressWithLz4HC.html).  
  
## Additional resources

  * [Build Profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)

  * [Build and deliver for QNX](qnx-build-and-deliver.html)
  * [Project Settings](comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings)

[](qnx-build-and-deliver.html)

Build and deliver for QNX

[](qnx-build-command-line.html)

Build for QNX from the command line

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

