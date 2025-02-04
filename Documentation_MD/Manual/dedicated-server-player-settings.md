[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dedicated-server-player-settings.html)
  * [中文](/cn/current/Manual/dedicated-server-player-settings.html)
  * [日本語](/ja/current/Manual/dedicated-server-player-settings.html)
  * [한국어](/kr/current/Manual/dedicated-server-player-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dedicated-server-player-settings.html)
  * [中文](/cn/current/Manual/dedicated-server-player-settings.html)
  * [日本語](/ja/current/Manual/dedicated-server-player-settings.html)
  * [한국어](/kr/current/Manual/dedicated-server-player-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Dedicated Server](dedicated-server.html)
  * [Get started with Dedicated Server](dedicated-server-get-started.html)
  * Dedicated Server Player settings

[](dedicated-server-requirements.html)

Dedicated Server requirements

[](dedicated-server-optimizations.html)

Dedicated Server optimizations

# Dedicated Server Player settings

The Player settings for the Dedicated Server Player are a subset of the
Desktop target Player settings. For a description of the general Player
settings, refer to [Player Settings](class-PlayerSettings.html)Settings that
let you set various player-specific options for the final game built by Unity.
[More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

![Dedicated Server Player settings](../uploads/Main/dedicated-server-player-
settings.png) Dedicated Server Player settings

Due to the headless and server application nature of the Dedicated Server,
only the options in the **Other Settings** section are applicable. You can
find documentation for the same in the Other Settings section:

The following options don’t apply:

  * Icon
  * Resolution and Presentation
  * Splash Image
  * Publishing Settings

## Other Settings

This section allows you to customize a range of options organized into the
following groups:

  * Configuration
  * Shader Settings
  * Shader Variant Loading Settings
  * Script Compilation
  * Optimization
  * Stack Trace
  * Legacy
  * Capture Logs

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
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation. This option is only available if you use the IL2CPP scripting backend.  
**Faster runtime** | Generates code optimized for runtime performance. This setting is activated by default.  
**Faster (smaller) builds** | Generates code optimized for build size and iteration. This setting generates less code and produces a smaller build, but can reduce runtime performance for generic code. Use this option when faster build times are important, such as when iterating on changes.  
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
**Debug** | Debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.  
**Release** | Release configuration enables optimizations, so the compiled code runs faster and the binary size is smaller but it takes longer to compile.  
**Master** | Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. Unity recommends building the shipping version of your game using the Master configuration if the increase in build time is acceptable.  
**IL2CPP Stacktrace Information** | Select the information to be included in a stack trace. For further details on the information types, refer to [Managed stack traces with IL2CPP](il2cpp-managed-stack-traces.html).  
**Method Name** | Include each managed method in the stack trace.  
**Method Name, File Name, and Line Number** | Include each managed method with file and line number information in the stack trace. Note: Using this option can increase both the build time and final size of the built program.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to [Automatic Memory Management](performance-managed-memory.html).  
**Allow downloads over HTTP** | Indicates whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
**Not Allowed** | Never allow downloads over HTTP.  
**Allowed in Development Builds** | Only allow downloads over HTTP in development builds.  
**Always Allowed** | Allow downloads over HTTP in development and release builds.  
**Target minimum macOS version** | Specifies the minimum supported macOS version which is 10.13.0  
  
#### API Compatibility Level

You can choose your mono API compatibility level for all targets. Sometimes a
third-party .NET library uses functionality that’s outside of your .NET
compatibility level. To understand what’s going on in such cases, and how to
best fix it, try following these suggestions:

  1. Install [ILSpy](https://www.microsoft.com/en-us/p/ilspy/9mxfbkfvsq13?cid=msft_web_chart&activetab=pivot:overviewtab) for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that’s not available in the .NET compatibility level of your choice in red.

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
  
### Script Compilation

**Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more details, refer to [Platform dependent compilation](platform-
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
**Enable Dedicated Server optimizations** | Activate this option to perform additional optimizations on the Dedicated Server build.  
**Prebake Collision Meshes** | Adds collision data to [Meshes](class-Mesh.html) at build time.   
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a
reference to the Asset to load in the new **Element** box that appears.  
**Managed Stripping Level** | Chooses how aggressively Unity strips unused managed (C#) code. The options are **Minimal** , **Low** , **Medium** , and **High**.   
When Unity builds your app, the Unity Linker process can strip unused code
from the managed DLLs your Project uses. Stripping code can make the resulting
executable significantly smaller, but can sometimes accidentally remove code
that’s in use.  
  
For more information about these options and bytecode stripping with IL2CPP,
refer to
[ManagedStrippingLevel](../ScriptReference/ManagedStrippingLevel.html).  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in
memory, reduce file size, and improve GPU performance.  
  
For more information on how to configure vertex compression and limitations of
this setting, refe to [Compressing mesh data](mesh-compression).  
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, you should remember to not
change material or shader settings at runtime.  
  
Refer to
[PlayerSettings.stripUnusedMeshComponents](../ScriptReference/PlayerSettings-
stripUnusedMeshComponents.html) for more information.  
**Texture MipMap Stripping** | Enables mipmap stripping for all platforms. This strips unused mipmaps from Textures at build time. Unity determines unused mipmaps by comparing the value of the mipmap against the **Quality Settings** for the current platform. If a mipmap value is excluded from every **Quality Setting** for the current platform, then Unity strips those mipmaps from the build at build time. If [QualitySettings.masterTextureLimit](../ScriptReference/QualitySettings-masterTextureLimit.html) is set to a mipmap value that has been stripped, Unity will set the value to the closest mipmap value that has not been stripped.  
  
### Stack Trace

Select your preferred logging type by enabling the option that corresponds to
each Log Type.

**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).  
**Full** | Logs all the time.  
  
Refer to [stack trace logging](stack-trace.html) for more information.

### Legacy

Activate the **Clamp BlendShapes (Deprecated)** option to clamp the range of
blend shape weights in [SkinnedMeshRenderers](class-SkinnedMeshRenderer.html).

### Capture Logs

Activate the **Capture Startup Logs** option to capture the startup logs for
later processing.

## Additional resources

  * [Build your application for Dedicated Server](dedicated-server-build.html)
  * [Dedicated Server AssetBundles](dedicated-server-assetbundles.html)

[](dedicated-server-requirements.html)

Dedicated Server requirements

[](dedicated-server-optimizations.html)

Dedicated Server optimizations

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

