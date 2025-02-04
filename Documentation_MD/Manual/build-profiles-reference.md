[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/build-profiles-reference.html)
  * [中文](/cn/current/Manual/build-profiles-reference.html)
  * [日本語](/ja/current/Manual/build-profiles-reference.html)
  * [한국어](/kr/current/Manual/build-profiles-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/build-profiles-reference.html)
  * [中文](/cn/current/Manual/build-profiles-reference.html)
  * [日本語](/ja/current/Manual/build-profiles-reference.html)
  * [한국어](/kr/current/Manual/build-profiles-reference.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Build profiles](BuildSettings.html)
  * Build Profiles window reference

[](override-player-settings.html)

Override Player settings with build profiles

[](incremental-build-pipeline.html)

Incremental build pipeline

# Build Profiles window reference

When you select a profile, Unity displays a list of settings that you can
adjust for the build.

## Build your application

To build your application, select one of the following options:

**Setting** | **Description**  
---|---  
**Build and Run** | Compile a Player and open it on your target platform. This option always uses the incremental build.  
**Build** | Compile a Player, then do nothing. The default build is incremental, except for the first build, which is always a full non-incremental clean build.  
| **Clean build** | Create a clean, [non-incremental](incremental-build-pipeline.html#creating-non-incremental-builds) build.  
| **Force skip data build** | Skip the data build process. Use this setting to build code changes but skip the process of generating scenes and other non-code related assets.  
  
**Note** : The **Build** and **Build and run** settings are visible only for
the active profile.

## Build data

Use the Build Data section to configure the following settings:

**Setting** | **Description**  
---|---  
**Override Global Scene List** | Select **Override Global Scene List** to create a custom scene list for your **build profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile). When selecting **Override
Global Scene List** , scenes are automatically inherited from the global
[scene list](build-profile-scene-list.html).  
**Scripting Defines** | Add custom scripting defines for your build profile. These custom scripting defines are additive and don’t override other scripting defines in your project. For more information, refer to [Custom scripting symbols](custom-scripting-symbols.html).  
  
## Platform settings

Each platform has specific build settings. For more information, refer to the
following platform-specific documentation:

**Platform** | **Documentation**  
---|---  
**Android** | [Android Build Settings reference](android-build-settings.html)  
**iOS** and **tvOS** | [iOS Build Settings reference](BuildSettingsiOS.html)  
**Linux** | [Linux Build Settings reference](Buildsettings-linux.html)  
**macOS** | [macOS Build Settings reference](macosbuildsettings.html)  
**Universal Windows Platform** | [UWP Build Settings reference](windowsstore-buildsettings.html)  
**Web** | [Web Build Settings](web-build-settings.html)  
**Windows** | [Windows Build Settings reference](WindowsStandaloneBinaries.html)  
  
**Note** : For information on build settings for closed platforms, refer to
the included documentation in the Unity installer of each **closed platform**
Includes platforms that require confidentiality and legal agreements with the
platform provider for using their developer tools and hardware. These
platforms aren’t open to development unless you have an established
relationship with the provider. For example PlayStation®, Game Core for Xbox®,
and Nintendo®.  
See in [Glossary](Glossary.html#Closedplatform).

### Shared build settings

The following build settings are available for all profile types. The values
of these settings are shared across platform profiles, but not across build
profiles.

**Note** : Updating shared settings of an active platform profile using
[`EditorUserBuildSettings`](../ScriptReference/EditorUserBuildSettings.html)
applies changes across all platform profiles. However, updating shared
settings of an active build profile with
[`EditorUserBuildSettings`](../ScriptReference/EditorUserBuildSettings.html)
only updates that specific build profile.

**Property** | **Description**  
---|---  
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
  
## Player Settings

Use the **Customize player settings** option to create custom Player settings
for each build profile you want to use. For more information, refer to
[Override Player settings with build profiles](override-player-settings.html).

**Note** : A link to the global Player settings is available in the **Build
Profiles** **toolbar** A row of buttons and basic controls at the top of the
Unity Editor that allows you to interact with the Editor in various ways (e.g.
scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar).

## Asset Import Overrides

Select the **Asset Import Overrides** option from the **Build Profiles**
toolbar. To speed up the time to import and change platforms, you can locally
override all texture import settings. During development, asset overrides can
be useful to speed up iteration time by using lower quality assets.

To set asset import overrides for initial project imports, use the editor
[command line arguments](CommandLineArguments.html) `-overrideMaxTextureSize`
and `-overrideTextureCompression`.

Once you have selected your override options, select **Apply Overides** to
apply the changes. A warning symbol appears next to the **Apply Import
Overrides** button to alert you of any active overrides.

**Note** : The default value for both override options is **No Override**.

**Setting** | **Description**  
---|---  
**Max Texture Size** | Override the maximum imported texture size. Unity imports textures in the lower of two values: this value, or the Max Size value specified in [Texture import settings](class-TextureImporter.html).  
  
The time it takes to import a texture is proportional to the number of pixels
it contains, so a texture size with a lower maximum can speed up import times.
It’s recommended to use this setting only during development as the resulting
textures are lower in resolution.  
**Texture Compression** | Override the texture compression options set in [Texture import settings](class-TextureImporter.html).  
  
Only affects textures that have one of the [compressed texture
formats](texture-compression-formats.html).  
| **Force Fast Compressor** | Use a faster but lower quality texture compression mode for formats that support it (BC7, BC6H, ASTC, ETC, ETC2). Usually this results in more compression artifacts, but for many formats the compression itself is 2 to 20 times faster.  
  
This setting also disables **Crunch** texture compression format on any
textures that have it.  
  
The effect of this setting is the same as if all textures had their
**Compressor Quality** set to a low number in the platforms section of their
[Texture import settings](class-TextureImporter.html).  
| **Force Uncompressed** | Use uncompressed formats. This is faster to import (because it skips the texture compression process), but the resulting textures take up more memory and game data size, and can impact rendering performance.  
  
The effect of this setting is the same as if all textures had their
**Compression** set to **None** in their platforms’ [Texture import
settings](class-TextureImporter.html).  
| **Force No Crunch** | Disable Crunch compression for all textures. Crunch compression can take a long time, so disabling it can speed up the import process significantly. However, the resulting textures take up more disk space.  
  
Selecting this option is the same as disabling **Use Crunch Compression** in
the [Texture import settings](class-TextureImporter.html) for all textures.  
  
## Additional resources

  * [Create a build profile](create-build-profile.html)
  * [Build Profiles scripting API reference](../ScriptReference/Build.Profile.BuildProfile.html)

[](override-player-settings.html)

Override Player settings with build profiles

[](incremental-build-pipeline.html)

Incremental build pipeline

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

