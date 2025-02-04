[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-buildsettings.html)
  * [中文](/cn/current/Manual/windowsstore-buildsettings.html)
  * [日本語](/ja/current/Manual/windowsstore-buildsettings.html)
  * [한국어](/kr/current/Manual/windowsstore-buildsettings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-buildsettings.html)
  * [中文](/cn/current/Manual/windowsstore-buildsettings.html)
  * [日本語](/ja/current/Manual/windowsstore-buildsettings.html)
  * [한국어](/kr/current/Manual/windowsstore-buildsettings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Build and deliver for Universal Windows Platform](uwp-building-and-delivering.html)
  * UWP Build Settings reference

[](uwp-building-and-delivering.html)

Build and deliver for Universal Windows Platform

[](windowsstore-generatedproject-il2cpp.html)

Generate your Visual Studio C++ solution

# UWP Build Settings reference

Use the Universal Windows Platform (UWP) Build Settings to configure and build
your application for UWP platform. The UWP Build Settings are part of the
[Build Profiles window](BuildSettings.html).

To build your application for UWP:

  1. Select **File** > **Build Profiles**.
  2. Select **Add**Build Profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile)** to open the **Platform
Browser** window. The Platform Browser window presents a list of supported
platforms that include desktop, mobile, web, and **closed platforms** Includes
platforms that require confidentiality and legal agreements with the platform
provider for using their developer tools and hardware. These platforms aren’t
open to development unless you have an established relationship with the
provider. For example PlayStation®, Game Core for Xbox®, and Nintendo®.  
See in [Glossary](Glossary.html#Closedplatform).

  3. Select **UWP** from the list of available platforms. If **UWP** isn’t an option, select **Install with Unity Hub** and follow the installation instructions. Before installing any platform module, refer to the [system requirements](system-requirements.html) page.
  4. Select **Add Build Profile**.
  5. Select **Switch Profile** to set the new build profile as the active profile.
  6. Click either **Build** or **Build and Run**.
  7. Select the destination for Unity to place the application.  
If you selected **Build and Run** , Unity also installs the application on the
run device.

  8. Click **Save**. This starts the build.

Use these settings to configure how Unity builds your application for UWP
platform.

**Property** | **Description**  
---|---  
**Architecture** | Select the CPU to build for (only applies to Build And Run).  
| **Intel 64-bit** | Use Intel/AMD 64-bit CPU architecture.  
| **Intel 32-bit** | Use 32-bit Intel CPU architecture.  
| **ARM 64-bit** | Use 64-bit ARM CPU architecture.  
| **ARM 32-bit** | Use 32-bit ARM CPU architecture.  
**Build Type** | Select the Visual Studio project or build type to generate.  
| **XAML Project** | Integrates Unity within a full XAML environment. This results in some performance loss, but lets you use XAML elements in your application.  
| **D3D Project** | Integrates Unity in a basic app window. This results in the best performance.  
| **Executable Only** | Hosts the project in a pre-built executable for rapid iteration. This setting has the quickest iteration speed because it doesn’t require you to build the generated project in Visual Studio. It offers the same performance as D3D Project builds.  
**Target SDK Version** | Select the Windows 10 SDK installed on the local PC to build the application against. This setting is relevant only when calling Windows 10 APIs directly from scripts.  
  
**Note** : Unity requires the base Windows 10 SDK version 10.0.10240.0 or
higher for building UWP apps, and doesn’t support Windows 8/8.1 SDKs.  
**Minimum Platform Version** | Select the minimum Windows 10 release version required to run the app.  
  
**Note** : This setting is only relevant if you’re using Windows features or
APIs that aren’t available in the base Windows 10 version (10.0.10240).  
**Visual Studio Version** | Specify the Visual Studio version if you have multiple versions installed.  
**Build and Run on** | Select the target device or transport to deploy and launch the app during **Build And Run**.  
| **Local Machine** | Deploys and launches the app on the local PC.  
| **Remote Device (via Device Portal)** | Deploys and launches the app to a connected device over the Device Portal transport. For more information, refer to [Windows Device Portal deployment](windowsstore-deviceportal.html).  
**Build Configuration** | Select the build configuration (only applies to **Build And Run**).  
  
**Note** : These build configurations are the same as those available in the
Visual Studio project that Unity generates.  
| **Debug** | Produces a build that contains additional code you can use for debugging, and enables the [Profiler](windowsstore-profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) for your build.  
| **Release** | Produces a build that has debug code stripped out, and enables the [Profiler](windowsstore-profiler.html) for your build.  
| **Master** | Produces a build that’s fully optimized for release.  
**Copy References** | Disable this setting to allow the generated solution to reference Unity files from Unity’s installation folder instead of copying them to the build folder. This can save up to 10 GB of disk space, but you can’t copy the build folder to another PC. Unity also builds your application faster when you disable this setting.  
**Copy PDB files** | Enable this setting to include Microsoft program database (PDB) files in the built Player. PDB files contain debugging information for your application, but might increase the size of your Player.  
**Development Build** | Include scripting debug symbols and the [Profiler](Profiler.html) in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define symbol. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  
  
For more information, refer to [Platform dependent
compilation](PlatformDependentCompilation).  
**Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](Profiler.html).  
  
**Note** : This option is available only if you select **Development Build**.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](ProfilerWindow.html#deep-profiling).   
  
This property is available only if you enable **Development Build**.  
  
**Note** : Enabling **Deep Profiling** might slow down script execution.  
**Script Debugging** | Attach script debuggers to the Player remotely.   
  
This property is available only if you enable **Development Build**.  
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

  * [Integrate Unity into UWP applications](UnityasaLibrary-UWP.html)
  * [BuildOptions API reference](../ScriptReference/BuildOptions.html)

[](uwp-building-and-delivering.html)

Build and deliver for Universal Windows Platform

[](windowsstore-generatedproject-il2cpp.html)

Generate your Visual Studio C++ solution

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

