[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-build-settings.html)
  * [中文](/cn/current/Manual/android-build-settings.html)
  * [日本語](/ja/current/Manual/android-build-settings.html)
  * [한국어](/kr/current/Manual/android-build-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-build-settings.html)
  * [中文](/cn/current/Manual/android-build-settings.html)
  * [日本語](/ja/current/Manual/android-build-settings.html)
  * [한국어](/kr/current/Manual/android-build-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Building and delivering for Android](android-building-and-delivering.html)
  * Android Build Settings reference

[](android-modify-gradle-project-files-android-studio.html)

Modify Gradle project files with Android Studio

[](android-BuildProcess.html)

Build your application for Android

# Android Build Settings reference

Use the Android Build settings to configure and build your application for
Android platform. The Android Build Settings are part of the [Build Profiles
window](BuildSettings.html).

**Property** | **Description**  
---|---  
**Texture Compression** | The texture compression format to use for the build. The options are:  
• **Use Player Settings** : Uses the texture compression format you set in
[Player Settings](class-PlayerSettingsAndroid.html)Settings that let you set
various player-specific options for the final game built by Unity. [More
info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).  
• **ETC (GLES 2.0)** : Uses ETC format.  
• **ETC2 (GLES 3.0)** : Uses ETC2 format.  
• **ASTC** : Uses ASTC format.  
• **DXT (Tegra)** : Uses DXT format.  
• **PVRTC (PowerVR)** : Uses PVRTC format (deprecated).  
  
You can also change this setting from a script or using the
`-setDefaultPlatformTextureFormat` [command-line
switch](CommandLineArguments.html).  
**Note** : If you enable [texture compression targeting](android-distribution-
google-play.html#texture-compression-targeting), Unity disables this setting.  
  
For more information about texture compression formats, refer to [Recommended,
default, and supported texture compression formats, by platform](class-
TextureImporterOverride#android).  
**Export Project** | Exports the Unity project as a Gradle project that you can import into Android Studio. For more information, refer to [Exporting an Android project](android-export-process.html).  
**Symlink Sources** | Indicates whether to share Java, Kotlin, and Android Library Project source files between Unity and the exported Gradle project. Android Library Project source files can be shared only if it includes `build.gradle` file in the plugin folder.   
  
Enable this setting to create [symbolic
links](https://en.wikipedia.org/wiki/Symbolic_link) so the Gradle project
references Java, Kotlin, and Android Library Project (.androidlib) source
files in the Unity project. This helps you test and iterate Java, Kotlin, and
Android Library Project code because it means any changes you make to these
source files in the exported Gradle project persist if you re-export the Unity
project.  
  
Disable this setting to make Unity copy Java, Kotlin, and Android Library
Project source files from the Unity project into the exported Gradle project.  
  
**Note** : You can only interact with this setting if you enable **Export
Project**.  
**Build App Bundle (Google Play)** | Indicates whether to build the application as an[ Android App Bundle](https://developer.android.com/platform/technology/app-bundle/) (AAB) to distribute on Google Play. If you enable this setting, Unity builds the application as an `aab`. If you disable this setting, Unity builds the application as an `apk`.   
  
**Note** : This setting is visible only if you disable **Export Project**.  
**Export for App Bundle** | Configures the exported Gradle project to build as an Android App Bundle.   
  
**Note** : This setting is visible only if you enable **Export Project**.  
**Debug Symbols** | Specifies how Unity generates a [symbols package](android-symbols.html) when it builds your application. You can upload the symbol package with your apk or Android App bundle (aab) in three ways:  
• As a separate zip file for an apk build.  
• Embed directly in the Android App bundle. This requires you to enable the
Build App Bundle option.  
• As a separate zip file for the Android App bundle. This requires you to
enable the Build App Bundle option.  
| **Disabled** | Unity doesn’t generate a symbols package.  
| **Public** | Unity generates the symbols package containing only the symbol table section and not the debugging information.  
| **Debugging** | Unity generates the symbols package containing the symbol table section and debugging information.  
**Symbols output options** | Specifies how Unity includes the symbols with the application build.  
| **.zip** | A separate zip file containing the symbols package. You can upload this zip file with the apk.  
| **App Bundle** | The symbols get embedded in the Android App bundle.  
| **.zip + App Bundle** | A separate zip file containing the symbols package. Additionally, the symbols get embedded in the Android App bundle.  
**Symbol file extension** | Specifies the symbol file extension as per the selected symbols package type. You have an option to create symbol files with the legacy extension.  
| **.so** | Specifies the legacy `.so` extension for the symbols package which you can upload on distribution services that don’t recognize the `.so.sym` or `.so.dbg` extensions.   
| **so.sym** | Specifies the extension for the public symbols package.  
| **.so.dbg** | Specifies the extension for the debugging symbols package.  
**Run Device** | Specifies which attached device to test the build on. Devices connected via USB appear in the list automatically. If you connect a new device or don’t find an attached device in the list, select **Refresh**. To connect a new device wirelessly over Android Debug Bridge, select the **< Enter IP>** option. For more information, refer to [Debug on Android devices](android-debugging-on-an-android-device.html).  
**Build to Device** | A build pipeline that doesn’t create a full build and instead deploys single files that changed since the last patch directly to the device. **Patch** deploys changed files to the devices and **Patch And Run** deploys changed files and then runs the application on the device. For more information, refer to [Application patching](android-AppPatching.html).   
  
You can only interact with this setting if you enable **Development Build**.  
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
PlayerSettings.html), and [GI data](GICache.html).  
| **Default** | On Windows, Mac, Linux Standalone, and iOS, there is no default compression.  
  
On Android, the default compression is ZIP, which gives slightly better
compression results than LZ4HC. However, ZIP data is slower to decompress.  
| **LZ4** | A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](../ScriptReference/BuildOptions.CompressWithLz4.html).  
| **LZ4HC** | A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](../ScriptReference/BuildOptions.CompressWithLz4HC.html).  
  
## Additional resources

  * [How Unity builds Android applications](how-unity-builds-android-applications.html)
  * [Build your application for Android](android-BuildProcess.html)
  * [BuildOptions API reference](../ScriptReference/BuildOptions.html)

[](android-modify-gradle-project-files-android-studio.html)

Modify Gradle project files with Android Studio

[](android-BuildProcess.html)

Build your application for Android

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

