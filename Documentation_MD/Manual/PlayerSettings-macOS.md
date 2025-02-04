[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PlayerSettings-macOS.html)
  * [中文](/cn/current/Manual/PlayerSettings-macOS.html)
  * [日本語](/ja/current/Manual/PlayerSettings-macOS.html)
  * [한국어](/kr/current/Manual/PlayerSettings-macOS.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PlayerSettings-macOS.html)
  * [中文](/cn/current/Manual/PlayerSettings-macOS.html)
  * [日本語](/ja/current/Manual/PlayerSettings-macOS.html)
  * [한국어](/kr/current/Manual/PlayerSettings-macOS.html)

  * [Platform development ](PlatformSpecific.html)
  * [macOS](AppleMac.html)
  * macOS Player settings reference

[](macos-requirements-and-compatibility.html)

macOS requirements and compatibility

[](macosdevelopment.html)

Developing for macOS

# macOS Player settings reference

This page details the **Player** settings specific to macOS. For a description
of the general **Player** settings, refer to [Player Settings](class-
PlayerSettings.html#general)Settings that let you set various player-specific
options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

You can find documentation for the properties in the following sections:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Other Settings

## Icon

Activate the **Override for Windows, Mac, Linux** setting to assign a custom
icon for your desktop game. You can upload different sizes of the icon to fit
each of the squares provided.

## Resolution and presentation

Use the **Resolution and Presentation** section to customize aspects of the
screen’s appearance.

### Resolution

This section allows you to customize the screen mode and default size.

**Property** | **Description**  
---|---  
**Run In background** | Enable this option to allow the application to run in the background when it loses focus. When disabled, the application pauses when it loses focus.  
**Fullscreen Mode** | Choose the full-screen mode. This defines the default window mode at startup.  
| **Fullscreen Window** | Set your app window to the full-screen native display resolution, covering the whole screen. This mode is also known as borderless full-screen. Unity renders the app content at the resolution set by a script, or the native display resolution if none is set and scales it to fill the window. When scaling, Unity adds black bars to the rendered output to match the display **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#AspectRatio) to prevent content stretching.
This process is called
[letterboxing](https://en.wikipedia.org/wiki/Letterboxing_\(filming\)). The OS
overlay **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) displays on top of the full-screen window
(such as IME input windows). All platforms support this mode.  
| **Exclusive Fullscreen (Windows only)** | Set your app to maintain sole full-screen use of a display. Unlike **Fullscreen Window** , this mode changes the OS resolution of the display to match the app’s chosen resolution. This option is only supported on Windows.  
| **Maximized Window (Windows and Mac only)** | Set the app window to the operating system’s definition of **maximized**. On Windows, it is a full-screen window with a title bar. On macOS, it is a full-screen window with a hidden menu bar and dock. **Fullscreen Window** is the default setting for other platforms.  
| **Windowed** | Set your app to a standard, non-full-screen movable window, the size of which is dependent on the app resolution. In this mode, the window is resizable by default. Use the Resizable Window setting to disable this. All desktop platforms support this full-screen mode.  
**Default Is Native Resolution** | Enable this option to make the game use the default resolution used on the target machine.   
**Note** : This property isn’t visible if you set **Fullscreen Mode** to
**Windowed**.  
**Default Screen Width** | Set the default width of the game screen in pixels.   
  
**Note** : This property is visible only if you set **Fullscreen Mode** to
**Windowed**.  
**Default Screen Height** | Set the default height of the game screen in pixels.   
  
**Note** : This property is visible only if you set **Fullscreen Mode** to
**Windowed**.  
**Mac Retina Support** | Enable this option to enable support for high DPI (Retina) screens on a Mac. Unity enables this by default. This enhances Projects on a Retina display, but it’s somewhat resource-intensive when active.  
  
### Standalone Player Options

Use this section to specify the settings to customize the screen. For example,
you can set options for users to resize the screen and specify the number of
instances that can run concurrently.

**Property** | **Description**  
---|---  
**Use Player Log** | Activate this option to write a log file with debugging information.  
**Warning:** If you plan to submit your application to the Mac App Store,
leave this option deactivated. For more information, refer to Publishing to
the Mac App Store.  
**Resizable Window** | Activate this option to allow resizing of the desktop player window.  
**Note:** If you deactivate this option, your application can’t use the
**Windowed** Fullscreen Mode.  
**Visible in Background** | Activate this option to display the application in the background when using **Windowed** Fullscreen Mode. This option isn’t supported on macOS.  
**Allow Fullscreen Switch** | Activate this option to allow default OS full-screen key presses to toggle between full-screen and windowed modes.  
**Force Single Instance** | Activate this option to restrict desktop players to a single concurrent running instance.  
**Use DXGI flip model swap chain for D3D11** | Using the flip model ensures the best performance. This setting affects the D3D11 graphics API. Deactivate this option to fall back to the Windows 7-style BitBlt model. For more information, refer to [PlayerSettings.useFlipModelSwapchain](../ScriptReference/PlayerSettings-useFlipModelSwapchain.html).  
  
## Splash Image

Use the **Virtual Reality Splash Image** setting to select a custom splash
image for [Virtual Reality](XR.html)Virtual Reality (VR) immerses users in an
artificial 3D world of realistic images and sounds, using a headset and motion
tracking. [More info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) displays. For information on
common Splash Screen settings, refer to [Splash Screen](class-
PlayerSettingsSplashScreen.html).

## Other Settings

  * Rendering
  * Vulkan Settings
  * Mac App Store Options
  * Configuration
  * Mac Configuration
  * Shader Settings
  * Shader Variant Loading Settings
  * Script Compilation
  * Optimization
  * Stack Trace
  * Legacy

### Rendering

Use these settings to customize how Unity renders your game for desktop
platforms.

**Property** | **Description**  
---|---  
**Color Space** | Choose which color space to use for rendering. For more information, refer to [Linear rendering overview](LinearLighting).  
**Gamma** | Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.  
**Linear** | Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using [sRGB](https://en.wikipedia.org/wiki/SRGB) sampling. If your [Textures](Textures.html) are in linear color space, you need to work in linear color space and deactivate sRGB sampling for each Texture.  
**Auto Graphics API for Windows** | Enable this option to use the best Graphics API for the Windows machine the application runs on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Mac** | Enable this option to use the best Graphics API for the macOS machine the application runs on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Linux** | Enable this option to use the best Graphics API for the Linux machine the application runs on. Disable it to add and remove supported Graphics APIs.   
**Color Gamut** | You can add or remove [color gamuts](https://en.wikipedia.org/wiki/Gamut) to use for rendering. Click the plus (+) icon to see a list of available gamuts. A color gamut defines a possible range of colors available for a given device (such as a monitor or screen). The sRGB gamut is the default (and required) gamut.  
**Metal API Validation** | Enable this option to use in-Editor tool to debug Shader issues. On a draw call, the tool checks a shaders expected textures and buffers against the attached and confirms its compatibility. The results of the checks are available in the console.   
  
**Metal API Validation** doesn’t enable Apple’s [Metal API
validation](https://developer.apple.com/documentation/xcode/validating-your-
apps-metal-api-usage), but you can enable it by setting **Run in Xcode as** to
**Debug** in the Build Settings window for [macOS](PlayerSettings-macOS.html)
and [iOS](class-PlayerSettingsiOS.html).  
  
**Note** : This setting only appears when running the Editor on macOS.  
**Metal Write-Only Backbuffer** |  Allow improved performance in non-default device orientation. This sets the `frameBufferOnly` flag on the back buffer, which prevents readback from the back buffer and enables some driver optimization.   
**Force hard shadows on Metal** |  Enable this option to force Unity to use point sampling for shadows on Metal. This reduces shadow quality, which improves performance.   
**Memoryless Depth** |  Choose when to use [memoryless render textures](../ScriptReference/RenderTextureMemoryless.Depth.html). Memoryless render textures are temporarily stored in the on-tile memory when rendered, not in CPU or GPU memory. This reduces memory usage of your app but you can’t read or write to these render textures.  
  
**Note** : Memoryless render textures are only supported on iOS, tvOS 10.0+,
Metal, and Vulkan. Render textures are read/write protected and stored in CPU
or GPU memory on other platforms.  
**Unused** | Never use memoryless framebuffer depth.  
**Forced** | Always use memoryless framebuffer depth.  
**Automatic** | Let Unity decide when to use memoryless framebuffer depth.  
**Static Batching** | Enable this option to use [static batching](static-batching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching).  
**Dynamic Batching** | Use [Dynamic Batching](DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#DynamicBatching) on your build (enabled by
default).  
  
**Note:** Dynamic batching has no effect when a [Scriptable Render
Pipeline](ScriptableRenderPipeline) is active, so this setting is only visible
if the **Scriptable Render Pipeline Asset** [Graphics](class-
GraphicsSettings.html#SRLoop) setting is blank.  
**Sprite Batching Threshold** | Controls the maximum vertex threshold used when batching.  
**GPU Skinning** | Enable the use of shaders to calculate mesh skinning and blend shapes on the GPU.  
**Graphics Jobs** | Offload graphics tasks (render loops) to worker threads running on other CPU cores. This option reduces the time spent in `Camera.Render` on the main thread, which can be a bottleneck.  
**Lightmap Encoding** | Defines the encoding scheme and compression format of the lightmaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**  
**HDR Cubemap Encoding** | Defines the encoding scheme and compression format of the HDR Cubemaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High
Quality**. For more information, refer to [Lightmaps: Technical
information](Lightmaps-TechnicalInformation.html).  
**Lightmap Streaming** | Enable this option to use [Mipmap Streaming](TextureStreaming.html) for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
**Note:** To use this setting, you must enable the [Texture Mipmap Streaming
Quality](class-QualitySettings.html#texStream) setting.  
**Streaming Priority** | Set the priority for all lightmaps in the [Mipmap Streaming system](TextureStreaming.html). Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from `-128` to
`127`.  
**Frame Timing Stats** | Enable this option to gather CPU/GPU frame timing statistics.  
**OpenGL: Profiler GPU Recorders** | Enable profiler recorders when rendering with OpenGL.  
**Allow HDR Display Output** | Activate HDR mode output when the application runs. This only works on displays that support this feature. If the display doesn’t support HDR mode, the game runs in standard mode.  
**Swap Chain Bit Depth** | Selects the number of bits in each color channel for swap chain buffers. You can select **Bit Depth 10** or **Bit Depth 16**. The option to choose bit depth only becomes available when you enable HDR Mode.   
  
For more information on bit depth, refer to the Scripting API page for
[D3DHDRDisplayBitDepth](../ScriptReference/D3DHDRDisplayBitDepth.html).  
| **Bit Depth 10** | Unity will use the R10G10B10A2 buffer format and Rec2020 primaries with ST2084 PQ encoding.  
| **Bit Depth 16** | Unity will use the R16G16B16A16 buffer format and Rec709 primaries with linear color (no encoding).  
**Virtual Texturing** | Enable this option to reduce GPU memory usage and texture loading times if your Scene has many high resolution textures. For more information, refer to [Virtual Texturing](svt-streaming-virtual-texturing.html).   
  
**Note** : The Unity Editor requires a restart for this setting to take
effect.  
**360 Stereo Capture** | Indicate whether Unity can capture stereoscopic 360 images and videos. When enabled, Unity compiles additional shader variants to support 360 capture (currently only on Windows/OSX). The `enable_360_capture` keyword is added during the [`RenderToCubemap`](../ScriptReference/Camera.RenderToCubemap.html) call, but isn’t triggered outside of this function.  
**Load/Store Action Debug Mode** | Highlights undefined pixels that might cause rendering problems on mobile platforms. This affects the Unity Editor Game view, and your built application if you select **Development Build** in Build Settings. Refer to [LoadStoreActionDebugModeSettings](../ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html) for more information.  
  
### Vulkan Settings

**Property** | **Description**  
---|---  
**SRGB Write Mode** |  Enable this option to let the `Graphics.SetSRGBWrite()` renderer toggle the sRGB write mode during runtime. Use this to deactivate Linear-to-sRGB write color conversion.  
**Number of swapchain buffers** |  Set this option to 2 for double-buffering, or 3 for triple-buffering to use with the Vulkan renderer. This setting might help with latency on some platforms, but usually you shouldn’t change this from the default value of 3. Double-buffering might have a negative impact on performance.  
**Acquire swapchain image late as possible** |  Enable this to get the backbuffer after the frame renders to an offscreen staging image. Enabling this setting adds an extra blit when presenting the backbuffer. This setting, in combination with double-buffering, can improve performance. However, it also can cause performance issues as the additional blit uses extra bandwidth.  
**Recycle command buffers** | Enable this option to recycle [CommandBuffers](../ScriptReference/Rendering.CommandBuffer.html) after Unity executes them.  
  
### Mac App Store Options

**Property** | **Description**  
---|---  
**Override Default Bundle Identifier** | Indicates whether you can manually set the bundle identifier.  
  
**Note:** This setting affects macOS, iOS, tvOS, and Android.  
| **Bundle Identifier** | Enter the Bundle Identifier of your application. This appears as `CFBundleIdentifier` in the associated `info.plist` file. The Bundle Identifier must follow the convention `com.YourCompanyName.YourProductName` and must contain only alphanumeric and hyphen characters. For more information, refer to [CFBundleIdentifier](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#/apple_ref/doc/uid/20001431-102070).  
  
**Important** : Unity automatically replaces any invalid characters you type
with a hyphen.  
**Build** | Enter the build number for this version of your app. This appears as `CFBundleVersion` in the associated `info.plist` file. For more information, refer to [CFBundleVersion](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102364).  
**Category** | Enter the string corresponding to the app’s type. The App Store uses this string to select the appropriate categorization for the app. By default, this is `public.app-category.games`. For more information, refer to [LSApplicationCategoryType](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW8).  
**Mac App Store Validation** | Activate this so that your app only runs when it has a valid receipt from the Mac App Store. This prevents people from running the game on a different device. Only deactivate this setting if you have implemented your own receipt validation.  
  
### Publishing to the Mac App Store

The Use Player Log property creates a log file with debugging information,
helping to investigate any problems with your game. Deactivate this when
publishing games for Apple’s Mac App Store, as Apple can reject your
submission if activated. For more information, refer to [Log Files](log-
files.html). The **Use Mac App Store Validation** property activates receipt
validation for the Mac App Store. If activated, your game only runs when it
has a valid receipt from the Mac App Store. Use this when submitting games to
Apple for publishing on the App Store. This prevents people from running the
game on a different computer.

**Note** : This feature doesn’t implement any strong copy protection. In
particular, any potential crack for one Unity game can work for any other
Unity content. For this reason, it’s recommended that you implement your own
receipt validation code on top of this, using Unity’s **plug-in** A set of
code created outside of Unity that creates functionality in Unity. There are
two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) feature. Because Apple requires plug-
in validation to initially happen before showing the screen setup dialog, it’s
recommended to activate this property to avoid Apple rejecting your
submission.

### Configuration

**Property** | **Description**  
---|---  
**Scripting Backend** |  Choose the scripting backend you want to use. The scripting backend determines how Unity compiles and executes C# code in your Project.  
**Mono** | Compiles C# code into .NET Common Intermediate Language (CIL) and executes that CIL using a Common Language Runtime. For more information, refer to [Mono](Mono)A scripting backend used in Unity. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#Mono).  
**IL2CPP** | Compiles C# code into CIL, converts the CIL to C++ and then compiles that C++ into native machine code, which executes directly at runtime. For more information, refer to [IL2CPP](IL2CPP)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP).  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with third-party libraries. However, it has no effect on Editor-specific code (code in an Editor directory, or within an Editor-specific Assembly Definition).  
  
**Tip:** If you are having problems with a third-party assembly, you can try
the suggestion in the API Compatibility Level section below.  
**.Net Framework** | Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](dotnetProfileAssemblies).  
**.Net Standard 2.1** | Produces smaller builds and has full cross-platform support.  
**Editor Assemblies Compatibility Level** | Select which .NET APIs to use in your Editor assemblies.  
**.NET Framework** | Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.1 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.1. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](dotnetProfileAssemblies).  
**.NET Standard** | Compatible with [.NET Standard 2.1](https://docs.microsoft.com/en-us/dotnet/standard/net-standard). Produces smaller builds and has full cross-platform support.  
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation.  
  
**Note** : To use this, set **Scripting Backend** to **IL2CPP**.  
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
**Debug** | Debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.  
**Release** | Release configuration enables optimizations, so the compiled code runs faster and the binary size is smaller but it takes longer to compile.  
**Master** | Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. Unity recommends building the shipping version of your game using the Master configuration if the increase in build time is acceptable.  
**IL2CPP Stacktrace Information** | Choose the information to include in a stack trace. For further details on the information types, refer to [Managed stack traces with IL2CPP](il2cpp-managed-stack-traces.html).  
| **Method Name** | Include each managed method in the stack trace.  
| **Method Name, File Name, and Line Number** | Include each managed method with file and line number information in the stack trace.   
  
**Note** : Using this option can increase both the build time and final size
of the built program.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to [Automatic Memory Management](performance-managed-memory.html).  
**Allow downloads over HTTP** | Indicates whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
**Not Allowed** | Never allow downloads over HTTP.  
**Allowed in Development Builds** | Only allow downloads over HTTP in development builds.  
**Always Allowed** | Allow downloads over HTTP in development and release builds.  
**Target minimum macOS Version** | Enter the minimum version of macOS that the application will run on.  
**Active Input Handling** | Choose how to handle input from users.  
**Input Manager (Old)** | Uses the traditional [Input](class-InputManager.html) settings.  
**Input System Package (New)** | Uses the [Input](../ScriptReference/Input.html) system. This option requires you to install the [InputSystem package](https://github.com/Unity-Technologies/InputSystem).  
**Both** | Use both systems.  
  
#### API compatibility level

You can choose your mono API compatibility level for all targets. Sometimes a
third-party .NET library uses functionality that’s outside of your .NET
compatibility level. To understand what’s going on in such cases, and how to
best fix it, try following these suggestions:

  1. Install [ILSpy](https://www.microsoft.com/en-us/p/ilspy/9mxfbkfvsq13?cid=msft_web_chart&activetab=pivot:overviewtab) for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that’s not available in the .NET compatibility level of your choice in red.

### Mac Configuration

**Property** | **Description**  
---|---  
**Camera Usage Description** | Enter the reason for accessing the camera on the device.  
**Microphone Usage Description** | Enter the reason for accessing the microphone on the device.  
**Bluetooth Usage Description** | Enter the reason for accessing the device’s Bluetooth connection.   
**Supported URL schemes** | A list of [supported URL schemes](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app/). To add new schemes, increase the value of the **Size** property, then set a reference to the Asset to load in the new **Element** box that appears.  
  
### Shader Settings

**Property** | **Description**  
---|---  
**Shader Precision Model** | Select the default precision shaders use. For more information, refer to [Use 16-bit precision in shaders](SL-Use16BitPrecisionInShaders.html).  
**Platform default** | Use lower precision on mobile platforms, and full precision on other platforms.  
**Unified** | Use lower precision if the platform supports it.  
**Strict shader variant matching** | Use the error shader if a shader variant is missing and display an error in the console.  
**Keep Loaded Shaders Alive** | Keep all loaded shaders alive and prevent unloading.  
  
### Shader Variant Loading Settings

Use these settings to control how much memory **shaders** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) use at runtime.

**Property** | **Description**  
---|---  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is `16`. For more information, refer to [Shader loading](shader-loading.html#dynamicloading).  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is `0`, which means there’s no limit.  
**Override** | Enables overriding **Default chunk size** and **Default chunk count** for this build target.  
**Chunk size (MB)** | Overrides the value of **Default chunk size (MB)** on this build target.  
**Chunk count** | Overrides the value of **Default chunk count** on this build target.  
  
### Script compilation

**Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more information, refer to [Platform dependent compilation](platform-
dependent-compilation.html).  
**Additional Compiler Arguments** | Adds entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, click **Add** (**+**). To remove an entry, click
**Remove** (**-**).  
  
When you have added all desired arguments, click **Apply** to include your
additional arguments in future compilations. Click **Revert** to reset this
list to the most recent applied state.  
**Suppress Common Warnings** | Indicates whether to display the C# warnings [CS0169](https://docs.microsoft.com/en-us/dotnet/csharp/misc/cs0169) and [CS0649](https://docs.microsoft.com/en-us/dotnet/csharp/misc/CS0649).  
**Allow ‘unsafe’ Code** | Activate support for compiling [‘unsafe’ C# code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef`
files and activate the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Indicates whether to prevent compilation with the -deterministic C# flag. With this setting active, compiled assemblies are byte-for-byte the same each time they’re compiled.  
  
For more information, refer to Microsoft’s [deterministic compiler
option](https://docs.microsoft.com/en-us/dotnet/csharp/language-
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
  
### Stack Trace

Select your preferred logging type by enabling the option that corresponds to
each Log Type.

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).  
**Full** | Logs all the time.  
  
For more information, refer to [stack trace logging](stack-trace.html).

### Legacy

**Property** | **Description**  
---|---  
**Clamp BlendShapes (Deprecated)** | Activate the option to clamp the range of blend shape weights in [SkinnedMeshRenderers](class-SkinnedMeshRenderer.html).  
  
[](macos-requirements-and-compatibility.html)

macOS requirements and compatibility

[](macosdevelopment.html)

Developing for macOS

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

