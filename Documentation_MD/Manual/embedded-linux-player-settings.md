[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/embedded-linux-player-settings.html)
  * [中文](/cn/current/Manual/embedded-linux-player-settings.html)
  * [日本語](/ja/current/Manual/embedded-linux-player-settings.html)
  * [한국어](/kr/current/Manual/embedded-linux-player-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/embedded-linux-player-settings.html)
  * [中文](/cn/current/Manual/embedded-linux-player-settings.html)
  * [日本語](/ja/current/Manual/embedded-linux-player-settings.html)
  * [한국어](/kr/current/Manual/embedded-linux-player-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Embedded systems](embedded-systems.html)
  * [Embedded Linux](embedded-linux.html)
  * [Get started with Embedded Linux](embedded-linux-get-started.html)
  * Embedded Linux Player settings

[](embedded-linux-environment-setup.html)

Set up your environment for Embedded Linux

[](embedded-linux-develop.html)

Develop for Embedded Linux

# Embedded Linux Player settings

Embedded Linux Player settings lets you customize how Unity builds and
displays your final application. To access the Player settings window for
Embedded Linux, go to **Edit** > **Project Settings** > **Player** and select
the **Embedded Linux** tab. You can use the [PlayerSettings
API](../ScriptReference/PlayerSettings.html) to control most of the settings
available in this window. For a description of the general Player settings,
refer to [Player Settings](class-PlayerSettings.html)Settings that let you set
various player-specific options for the final game built by Unity. [More
info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

## General settings

The Player settings differ between the platform modules that you have
installed. Each platform has its own Player settings which you must set for
each version of your application you want to build. To navigate between them,
click the tabs with the appropriate platform operating system icon.

![The main Player settings window for Embedded
Linux](../uploads/Main/embedded-linux-player-settings.png) The main Player
settings window for Embedded Linux

You can find documentation for the properties in the following sections:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Other Settings

## Icon

Enable the **Override for** **Embedded Linux** setting to assign a custom icon
for your game.

##  Resolution and Presentation

Use the Resolution and Presentation section to customize aspects of the
screen’s appearance in the Resolution section.

### Resolution section

This section allows you to customize the screen mode and default size.

**Property** | **Description**  
---|---  
**Fullscreen Mode** | Choose the full-screen mode. This defines the default window mode at startup. This sets the default window mode at startup.  
| **Fullscreen Window** | The application window fills the full-screen native resolution of the device. To fill the full-screen window, Unity scales the application contents. To match the **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio) of the output device, Unity might
add black bars to the rendered output so the content doesn’t stretch. This
process is called
[letterboxing](https://en.wikipedia.org/wiki/Letterboxing_\\\(filming\\\)). In
this mode, the navigation bar is always hidden.  
| **Windowed** | The application uses a standard, non-full-screen, movable window. The size of the window depends on the application’s resolution. In this mode, the window is resizable by default. To disable this, disable Resizable Window.  
**Default is Native Resolution** | Enable this option to make the game use the default resolution used on the target machine. This option is not available if **Fullscreen Mode** is set to **Windowed**.  
**Use 32-bit Display Buffer** | Embedded Linux only supports 32-bit color buffers.  
**Disable Depth and Stencil** | This feature is not supported on Embedded Linux.  
**Render Over Native**UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI)** | Enable this option only if you want to force your app to render on top of the native iOS or Android UI. For this setting to take effect, set your **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s Clear flags to use a solid color
with an alpha value lower than 1.  
  
##  Splash Image

Use the **Virtual Reality** Virtual Reality (VR) immerses users in an
artificial 3D world of realistic images and sounds, using a headset and motion
tracking. [More info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) Splash Image setting to select
a custom splash image for Virtual Reality displays. For information on common
Splash Image settings, refer to [Splash Image Player settings](class-
PlayerSettingsSplashScreen.html).

##  Other Settings

This section allows you to customize a range of options organized into the
following groups:

  * Rendering
  * Configuration

###  Rendering

Use these settings to customize how Unity renders your game for the Embedded
Linux platform.

![Rendering settings for Embedded Linux](../uploads/Main/embedded-linux-other-rendering.png) Rendering settings for Embedded Linux **Property** | **Description**  
---|---  
**Color Space** | Choose which color space Unity uses for rendering: Gamma or Linear. Refer to the [Linear rendering overview](LinearLighting) for an explanation of the difference between the two.  
| **Gamma** | Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.  
| **Linear** | Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using sRGB sampling. If your Textures are in linear color space, you need to work in linear color space and disable sRGB sampling for each Texture.  
**Force SRGB**blit** A shorthand term for “bit block transfer”. A blit
operation is the process of transferring blocks of data from one place in
memory to another.  
See in [Glossary](Glossary.html#blit)** | Enable this to use Force SRGB blit for Linear color space. If your graphics drivers don’t support the linear color space, selecting this option will convert Linear color space to Gamma (SRGB) color space.  
**Auto Graphics API** | Enable this option to use the best Graphics API on the device the application is running on. Disable it to add and remove supported Graphics APIs.  
**Multithreaded Rendering** | Enable this option to use multithreaded rendering.  
****Static Batching** A technique Unity uses to draw GameObjects on the screen
that combines static (non-moving) GameObjects into big Meshes, and renders
them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching)** | Enable this option to use Static batching.  
**Static Batching Threshold** | Controls the maximum vertex threshold used when batching. For more information, refer to [Sprite Batch Vertex Threshold](../ScriptReference/PlayerSettings-spriteBatchVertexThreshold.html).  
**GPU Compute**Skinning** The process of binding bone joints to the vertices
of a character’s mesh or ‘skin’. Performed with an external tool, such as
Blender or Autodesk Maya. [More info](UsingHumanoidChars.html)  
See in [Glossary](Glossary.html#Skinning)** | Enable this option to enable DX11/ES3 GPU compute skinning, freeing up CPU resources.  
**Graphics Jobs** | Enable this option to instruct Unity to offload graphics tasks (render loops) to worker threads running on other CPU cores. This is intended to reduce the time spent in `Camera.Render` on the main thread, which is often a bottleneck.  
**Texture**compression** A method of storing data that reduces the amount of
storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) format** | Choose the **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression) format to use for textures
in your Project. The options are ETC, ETC2, ASTC, DXT, and PVRTC. For more
information on each of these compression formats, refer to
[TextureImporterOverride](class-TextureImporterOverride).  
****Normal Map** A type of Bump Map texture that allows you to add surface
detail such as bumps, grooves, and scratches to a model which catch the light
as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) Encoding** | Choose Normal Quality or High Quality to set the **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) encoding. This setting affects the
encoding scheme and compression format of the lightmaps.  
**Lightmap Streaming** | Enable this option to load only the lightmap mipmaps as needed to render the current game Cameras. This value applies to the lightmap textures as they are generated. Note: To use this setting, you must enable the Texture Streaming Quality setting.  
| **Streaming Priority** | Set the lightmap mip map streaming priority to resolve resource conflicts. These values are applied to the light map textures as they’re generated. Positive numbers give higher priority. Valid values range from –128 to 127.  
**Frame Timing Stats** | Enable this option to gather CPU/GPU frame timing statistics.  
**OpenGL:**Profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) GPU Recorders** | Enable profiler recorders when rendering with OpenGL.  
**Virtual Texturing (Experimental)** | Indicates whether to enable [Virtual Texturing](svt-streaming-virtual-texturing.html). **Note:** The Unity Editor requires a restart for this setting to take effect.  
**Load/Store Action Debug Mode** | Highlights undefined **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) that might cause rendering problems on
mobile platforms. This affects the Unity Editor Game view, and your built
application if you select **Development Build** A development build includes
debug symbols and enables the Profiler. [More
info](https://docs.unity.com/devops/en/manual/build-target-
configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild) in Build Settings. Refer to
[LoadStoreActionDebugModeSettings](../ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html)
for more information.  
**360 Stereo Capture** | Indicates whether Unity can capture stereoscopic 360 images and videos. When enabled, Unity compiles additional **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) variants to support 360 capture
(currently only on Windows/macOS). When enabled, enable_360_capture keyword is
added during the Stereo RenderCubemap call. Note that this keyword isn’t
triggered outside the Stereo RenderCubemap function. For more information,
refer to [Stereo 360 Image and Video
Capture](https://blog.unity.com/technology/stereo-360-image-and-video-
capture?_ga=2.228952412.1984266774.1645442174-1855761588.1624871061).  
  
###  Vulkan settings

![Vulkan Player settings for Embedded Linux.](../uploads/Main/embedded-linux-vulkan.png) Vulkan Player settings for Embedded Linux. **Property** | **Description**  
---|---  
**SRGB Write Mode** | Enable this option to allow `Graphics.SetSRGBWrite()` renderer to toggle the sRGB write mode during runtime. That is, if you want to temporarily turn off Linear-to-sRGB write color conversion, you can use this property to achieve that. Enabling this has a negative impact on performance on mobile tile-based GPUs; therefore, do NOT enable this for mobile.  
**Number of swapchain buffers** | Set this option to 2 for double-buffering, or 3 for triple-buffering to use with Vulkan renderer. This setting may help with latency on some platforms, but in most cases you should not change this from the default value of 3. Double-buffering might have a negative impact on performance. Do not use this setting on Android.  
**Acquire swapchain image late as possible** | If enabled, Vulkan delays acquiring the backbuffer until after it renders the frame to an offscreen image. Vulkan uses a staging image to achieve this. Enabling this setting causes an extra blit when presenting the backbuffer. This setting, in combination with double-buffering, can improve performance. However, it also can cause performance issues because the additional blit takes up bandwidth.  
**Recycle command buffers** | Indicates whether to recycle or free after Unity executes them.  
  
###  Configuration

Use this section to specify configuration settings for the Embedded Linux
platform.

![Configuration settings for Embedded Linux](../uploads/Main/embedded-linux-other-config.png) Configuration settings for Embedded Linux **Property** | **Description**  
---|---  
****Scripting Backend** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend)** | The scripting backend determines how Unity compiles and executes C# code in your application. The default scripting backend for Embedded Linux is [IL2CPP](IL2CPP)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP).  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with 3rd-party libraries.  
| **.Net Standard 2.0** | Compatible with [.NET Standard 2.0](https://docs.microsoft.com/en-us/dotnet/standard/net-standard?tabs=net-standard-2-0). Produces smaller builds and has full cross-platform support.  
| **.Net Framework 4.x** | Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile as well as additional APIs). Choose this option when usng libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available are not necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](dotnetProfileAssemblies).  
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
**Use incremental GC** | Enable this to use the incremental garbage collector, which spreads garbage collection over several frames to reduce gc-related spikes in frame duration.  
**Assembly Version Validation** | This is an Editor setting that doesn’t apply in runtime.  
**Player Data path** | Enter the directory path on the system where you want to save the .`config` and log files. You can also change this from the command line of the player by adding the following arguments:`-platform-hmi-player-data-path <pathname>`.  
**Enable**Game Controllers** A device to control objects and characters in a
game.  
See in [Glossary](Glossary.html#gamecontroller)** | When selected, this setting enables game controllers. You can disable this if you don’t need game controllers, to help reduce the player startup time.  
**CPU Configuration** | Set the target CPU configuration for the player runtime. The default number of cores is 0, but you can increase it by entering a number. The options for each CPU are: **Disabled** , **High Performance** , and **Low Performance**.  
**Loading image** | Use this setting to select a custom splash image for the loading screen.  
**Active Input Handling** | Choose how you want to handle input from users.  
| ****Input Manager** Settings where you can define all the different input
axes, buttons and controls for your project. [More info](class-
InputManager.html)  
See in [Glossary](Glossary.html#InputManager) (old)** | Use the default Input window.  
| **Input System (Preview)** | Use the newer Input system. The Input System is provided as a **preview package** A _preview_ package is in development and not yet ready for production. A package in preview might be at any stage of development, from the initial stages to near completion.  
See in [Glossary](Glossary.html#Previewpackage) for this release. To try a
preview of the Input System, install the InputSystem package.  
| **Both** | Use both systems side-by-side.  
  
###  Shader Settings and Shader Variant Loading Settings

Use these settings to control how much memory shaders use at runtime.

![Shader settings for Embedded Linux](../uploads/Main/embedded-linux-shader-settings.png) Shader settings for Embedded Linux **Property** | **Description**  
---|---  
**Shader precision model** | Select the default precision of samplers used in shaders. For more information, refer to [HLSL data types](SL-DataTypesAndPrecision.html).  
**Strict shader variant matching** | Use the error shader if a shader variant is missing and display an error in the console.  
**Keep Loaded Shaders Alive** | When enabled, you can’t unload a shader. For more information, refer to [Shader loading](shader-loading.html).  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is 16. For more information, refer to [Shader loading](shader-loading.html).  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is 0, which means there’s no limit.  
**Override** | Enable this to override Default chunk size and Default chunk count for this build target.  
  
###  Script Compilation

![Script Compilation settings for Embedded Linux](../uploads/Main/embedded-linux-script-compilation.png) Script Compilation settings for Embedded Linux **Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more details, refer to [Platform dependent
compilation](PlatformDependentCompilation).  
**Additional Compiler Arguments** | Adds entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, click **Add** (**+**). To remove an entry, click
**Remove** (**-**).  
  
When you have added all desired arguments, click **Apply** to include your
additional arguments in future compilations. Click **Revert** to reset this
list to the most recent applied state.  
**Suppress Common Warnings** | Indicates whether to display the C# warnings [CS0169](https://docs.microsoft.com/en-us/dotnet/csharp/misc/cs0169) and [CS0649](https://docs.microsoft.com/en-us/dotnet/csharp/misc/CS0649).  
**Allow ‘unsafe’ Code** | Enables support for compiling [‘unsafe’ C# code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef`
files and enable the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Indicates whether to prevent compilation with the -deterministic C# flag. With this setting enabled, compiled assemblies are byte-for-byte the same each time they’re compiled.  
  
For more information, refer to [C# Compiler Options that control code
generation](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/compiler-options/deterministic-compiler-option).  
  
### Optimization

**Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to [Meshes](class-Mesh.html) at build time.  
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a
reference to the Asset to load in the new **Element** box that appears.  
**Managed Stripping Level** | Chooses how aggressively Unity strips unused managed (C#) code. When Unity builds your app, the Unity Linker process can strip unused code from the managed DLLs your Project uses. Stripping code can make the resulting executable smaller, but can sometimes remove code that’s in use.   
  
For more information about these options and bytecode stripping with IL2CPP,
refer to
[ManagedStrippingLevel](../ScriptReference/ManagedStrippingLevel.html).  
**Minimal** | Use this to strip class libraries, UnityEngine, Windows Runtime assemblies, and copy all other assemblies.  
**Low** | Remove unreachable managed code to reduce build size and Mono/IL2CPP build times.  
**Medium** | Run UnityLinker to reduce code size beyond what **Low** can achieve. You might need to support a custom link.xml file, and some reflection code paths might not behave the same.  
**High** | UnityLinker will strip as much code as possible. This will further reduce code size beyond what Medium can achieve but managed code debugging of some methods might no longer work. You might need to support a custom link.xml file, and some reflection code paths might not behave the same.  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in
memory, reduce file size, and improve GPU performance.  
  
For more information on how to configure vertex compression and limitations of
this setting, refer to [Compressing mesh data](mesh-compression).  
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, don’t change material or shader
settings at runtime.  
  
For more information, refer to
[PlayerSettings.stripUnusedMeshComponents](../ScriptReference/PlayerSettings-
stripUnusedMeshComponents.html).  
**Texture Mipmap Stripping** | Enables mipmap stripping for all platforms. It strips unused mipmap levels from Textures at build time.   
Unity determines unused mipmap levels by comparing the mipmap level against
the quality settings for the current platform. If a mipmap level is excluded
from every quality setting for the current platform, then Unity strips those
mipmap levels from the build at build time. If
`QualitySettings.globalTextureMipmapLimit` is set to a mipmap level that has
been stripped, Unity will set the value to the closest mipmap level that
hasn’t been stripped.  
  
### Logging

Select what type of logging you want to allow for Embedded Linux builds.

  * Select your preferred logging method from the available options.

  * Check a box that corresponds to each Log Type (Error, Assert, Warning, Log, and Exception) based on the type of logging you require. For example:

    * **ScriptOnly -** Logs only when running **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

    * **Full** **-** Logs all the time.
    * **None** **-** No logs are ever recorded.

### Legacy

This section covers the legacy player settings.

Property | Description  
---|---  
**Clamp BlendShapes (Deprecated)** | Enable the option to clamp the range of blend shape weights in [SkinnedMeshRenderers](class-SkinnedMeshRenderer.html).  
**Upload Cleared Texture Data** | This is a legacy feature and currently not needed because it uses up the bandwidth. By default, this is enabled for debugging purposes. Enabling this setting clears the initial data and automatically uploads the texture from script to the video memory.  
  
### Additional resources:

  * [Player settings](class-PlayerSettings.html)
  * [IL2CPP overview](IL2CPP)

[](embedded-linux-environment-setup.html)

Set up your environment for Embedded Linux

[](embedded-linux-develop.html)

Develop for Embedded Linux

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

