[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-optimization-player.html)
  * [中文](/cn/current/Manual/web-optimization-player.html)
  * [日本語](/ja/current/Manual/web-optimization-player.html)
  * [한국어](/kr/current/Manual/web-optimization-player.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-optimization-player.html)
  * [中文](/cn/current/Manual/web-optimization-player.html)
  * [日本語](/ja/current/Manual/web-optimization-player.html)
  * [한국어](/kr/current/Manual/web-optimization-player.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Optimize your Web build](web-optimization.html)
  * Recommended Player settings to optimize your Web build

[](web-optimization-graphics.html)

Recommended Graphics settings to optimize your Web build

[](web-optimization-quality.html)

Recommended Quality settings to optimize your Web build

# Recommended Player settings to optimize your Web build

Use the following recommended **Player** settings to optimize your builds for
the Unity Web platform.

## Player settings quick reference

Find these settings under **Edit** > **Project settings** > **Player**. For
more information on each setting, refer to the details in [Player
settings](class-PlayerSettingsWebGL.html)Settings that let you set various
player-specific options for the final game built by Unity. [More info](class-
PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).

**Setting** | **Recommended Setting** | **Description**  
---|---|---  
API Compatibility Level | .NET Standard 2.1 | Produces smaller builds.  
IL2CPP Code Generation | Faster (smaller) builds | Generates code optimized for build size and iteration.  
Managed Stripping Level | High | Unity does a high level of managed stripping to create a smaller build.  
  
Configure the following recommended settings in the **Publishing Settings**
section:

**Setting** | **Recommended Setting** | **Description**  
---|---|---  
Compression Format | Brotli | Files compressed by Brotli are smaller.  
Data Caching | Enabled | Runs faster because cached data doesn’t need to be downloaded again on subsequent runs (unless the contents have changed).  
Debug Symbols | Off | Debug symbols can slow down your application.  
Enable Exceptions | None | Enable **Target WebAssembly 2023** instead for exceptions without overhead.  
Target WebAssembly 2023 | Enable | The Web Assembly 2023 **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
See in [Glossary](Glossary.html#Featureset) contains features that help
optimize your project.  
Maximum Memory Size (MB) | Enter the amount of memory you need in MB. | Unity Web supports up to 4096 MB of memory for your build.  
  
## API Compatibility Level

Use the **API Compatibility Level** setting to choose which .NET APIs you can
use in your project. The recommended setting is **.Net Standard 2.1** because
this setting produces smaller builds and has cross-platform support. However,
you need to check if your platform fully supports .Net Standard 2.1. For other
options, refer to [Web player settings](class-PlayerSettingsWebGL.html).

### Change the API Compatibility Level

To change the **API Compatibility Level** via script instead, add this code to
one of your **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts):

    
    
    PlayerSettings.SetApiCompatibilityLevel(namedBuildTarget, ApiCompatibilityLevel.NET_2_0);
    

## IL2CPP Code generation

Use the ****IL2CPP** A Unity-developed scripting back-end which you can use as
an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) Code generation** setting to configure
how Unity manages IL2CPP code generation (if your project uses the IL2CPP
scripting back end).

The **Faster (smaller)** builds option is recommended because it creates a
smaller build and generates less code which results in faster build times.
Faster build times are vital in Web applications. However, this setting can
reduce runtime performance.

For more information, refer to [IL2CPP overview](./scripting-backends-
il2cpp.html).

### Change the IL2CPP Code generation via C

To enable this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.SetIl2CppCodeGeneration(namedBuildTarget,         
                                           Il2CppCodeGeneration.OptimizeSize);
    

## Managed stripping level

Use **Managed stripping level** to configure how much the Unity linker process
strips unused code from the managed DLLs your project uses. The recommended
setting is **High** because stripping code can make your executable
significantly smaller, which is important in Web applications. However,
possible side effects might include:

  * Managed code debugging of some methods might not work.

  * You might need to maintain a custom `link.xml` file.

  * Some reflection code paths might not behave the same.

For more information, refer to [Managed code stripping](managed-code-
stripping.html).

### Change the Managed stripping level via C

To change this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.SetManagedStrippingLevel(namedBuildTarget,     
                                            ManagedStrippingLevel.High);    
    

## Compression Format

Choose what **compression** A method of storing data that reduces the amount
of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) format to use for release build
files. **Brotli** is the recommended setting because it has the best
compression ratios and Brotli-compressed files are smaller than gzip. Smaller
files are best for Web applications. However, Chrome and Firefox only support
Brotli if the user accesses the website over HTTPS. Also, although most modern
servers support Brotli, some servers don’t support it. Make sure that your
server supports Brotli.

For more information on compression formats, refer to [Deploy a Web
application](webgl-deploying.html).

### Change Compression Format via C# script

To enable this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.WebGL.compressionFormat = WebGLCompressionFormat.Brotli;
    

## Data caching

Enable **Data caching** so that Unity caches your contents asset data on the
user’s machine. Data caching can make the application run faster. For more
information, refer to [Cache behavior in Web](webgl-caching.html).

### Enable data caching via C# script

To enable this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.WebGL.dataCaching = true;
    

## Debug symbols

The **Debug symbols** setting preserves debug symbols and displays original
function names of the stack trace when an error occurs, so it’s easier to
identify the source of an error. The recommended best practice is to disable
**Debug symbols** on your final release build because it can make your build
unnecessarily large and slow down your application. Enable this setting during
development and testing to make it easier to identify the source of an error.

### Deactivate Debug symbols via C# script

To deactivate this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.WebGL.debugSymbolMode = WebGLDebugSymbolMode.Off;
    

## Enable exceptions

The **Enable exceptions** setting lets you choose how to handle errors at
runtime. The recommended best practice is to choose the **None** option in
your final release build because this setting gives the best performance and
smallest builds.

However, with this option, any exception thrown causes your content to stop
with an error, so it’s best to enable exceptions during development and
testing. For more information, refer to [Web Player settings](class-
PlayerSettingsWebGL.html#wasm-language-features).

### Deactivate exceptions via C# script

To deactivate exceptions via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.WebGL.exceptionSupport = WebGLExceptionSupport.None;
    

## Target WebAssembly 2023

WebAssembly 2023 is a selection of WebAssembly language features that can
improve performance and reduce code size. Therefore, it is recommended that
you enable this setting.

### Enable WebAssembly 2023 via C# script

To enable this setting via script instead, add this code to one of your
scripts:

    
    
    PlayerSettings.WebGL.wasm2023 = true;
    // PlayerSettings.WebGL.webAssemblyTable = true;
    // PlayerSettings.WebGL.webAssemblyBigInt = true;
    

To enable the `WebAssembly.Table` or `BigInt` features without WebAssembly
2023, remove the first line of code and remove the comment lines.

## Maximum Memory Size (MB)

Unity supports up to 4096 MB of memory for your build. For most applications,
2048 MB of memory is enough. But for more complex real-time 3D experiences,
especially for desktop browsers, it’s better to have more memory. With more
memory, you can load in richer, larger **scenes** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) more dynamically.

However, there are known bugs for builds over 2048 MB in Firefox and Chrome
browsers before version 119.

### Change the maximum memory via C# script

To change the maximum memory via script instead, add this code to your script
and change the number to your preferred memory size:

    
    
    PlayerSettings.WebGL.maximumMemorySize = 4096; 
    

## Additional resources

  * [Optimize your Web build](web-optimization.html)

  * [Recommended Graphics settings to optimize your Web build](web-optimization-graphics.html)

  * [Recommended Quality settings to optimize your Web build](web-optimization-quality.html)

  * [Remove unused resources from your Web build](web-optimization-remove-resources.html)

  * [Optimize Web platform for mobile](web-optimization-mobile.html)

[](web-optimization-graphics.html)

Recommended Graphics settings to optimize your Web build

[](web-optimization-quality.html)

Recommended Quality settings to optimize your Web build

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

