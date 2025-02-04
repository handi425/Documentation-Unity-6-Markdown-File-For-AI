[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-build-settings.html)
  * [中文](/cn/current/Manual/web-build-settings.html)
  * [日本語](/ja/current/Manual/web-build-settings.html)
  * [한국어](/kr/current/Manual/web-build-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-build-settings.html)
  * [中文](/cn/current/Manual/web-build-settings.html)
  * [日本語](/ja/current/Manual/web-build-settings.html)
  * [한국어](/kr/current/Manual/web-build-settings.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * Web Build Settings

[](webgl-building-distribution.html)

Build and distribute a Web application

[](webgl-building.html)

Web Build folder

# Web Build Settings

Use the Web **Build Settings** to configure how Unity builds your application
for the Web platform.

## Access the Build Settings for Web

You can update your Web platform **Build Settings** from the [Build
Profiles](BuildSettings.html)A set of customizable configuration settings to
use when creating a build for your target platform. [More info](build-
profiles.html)  
See in [Glossary](Glossary.html#Buildprofile) window.

To access the **Build Settings** for Web:

  1. Go to **File** > **Build Profiles**. 

  2. Select **Web**. 

## Web Build Settings reference

The following table gives an overview of the Web **Build Settings**.

**Property** | **Description**  
---|---  
**Client Browser Type** | Select the browser client that you want your application to launch at runtime. For example, if you choose System Default, then your application launches the default browser, and removes the **Path to Client Browser** setting.  
**System Default** | This is the default setting. Select this option to launch the application in the default browser.  
**Microsoft Edge** | Select this option to launch the application in Edge browser.  
**Apple Safari** | Select this option to launch the application in Safari.  
**Mozilla Firefox** | Select this option to launch the application in Firefox.  
**Google Chrome** | Select this option to launch the application in Chrome.  
**Chromium** | Select this option to launch the application in a Chromium browser.  
**Path to Client Browser** | Specify the path to the browser client that you want your application to launch at runtime. **Note:** This option is only visible if the Client Browser Type isn’t set to the default browser.  
**Texture Compression** | The texture compression format to use for the build. For more information, refer to [Web texture compression](webgl-texture-compression.html).  
**Use Player Settings** | This is the default selection. It uses the texture compression format you set in the [Player settings](class-PlayerSettingsWebGL.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) window.  
**ETC2** | Uses ETC2 format, which is widely supported on mobile devices.  
**ASTC** | Uses ASTC format, which is widely supported on mobile devices.  
**DXT** | Uses DXT format, which is widely supported on desktop devices.  
**Development Build** | Include scripting debug symbols and the [Profiler](Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) in your build. Use this setting when
you want to test your application. When you select this option, Unity sets the
`DEVELOPMENT_BUILD` scripting define symbol. Your build then includes
preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  
  
For more information, refer to [Platform dependent
compilation](PlatformDependentCompilation).  
**Code Optimization** | Select the optimization mode to use for compiling the Web code.  
**Shorter Build Time** | This is the default setting. Select this option to generate WebGL code that takes the least amount of time to build.  
**Runtime Speed** | Select this option to generate WebGL code that’s optimized for runtime performance, at the expense of taking a longer time to build.  
**Runtime Speed with LTO** | This is the same as Runtime Speed, but with an additional Link Time Optimizations (LTO) stage (sometimes called Whole Program Optimization). Enable LTO when compiling shipping builds for deployment to end users.  
**Disk Size** | Select this option to favor optimizations that minimize build size, at the expense of taking a longer time to build. It’s recommended to select this option when targeting mobile web browsers that might have limits on the size of WebAssembly files that can be loaded. Smaller disk sizes generally result in shorter page startup times.  
**Disk Size with LTO** | This is the same as Disk Size but enables an additional Link Time Optimizations (LTO) stage. This is also known as Whole Program Optimization. Select this option when compiling shipping builds for deployment to end users.  
**Autoconnect Profiler** | Enable to make your next build a development build. Use development builds for the fastest iteration speed. Note that Development builds are larger than release builds and should not be published.   
**Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](Profiler.html).  
  
**Note** : This option is available only if you select **Development Build**.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](ProfilerWindow.html#deep-profiling).   
  
This property is available only if you enable **Development Build**.  
  
**Note** : Enabling **Deep Profiling** might slow down script execution.  
  
## Additional Resources

  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Build your Web application](webgl-building.html)
  * [Deploy a Web application](webgl-deploying.html)
  * [BuildOptions API reference](../ScriptReference/BuildOptions.html)

[](webgl-building-distribution.html)

Build and distribute a Web application

[](webgl-building.html)

Web Build folder

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

