[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scripting-symbol-reference.html)
  * [中文](/cn/current/Manual/scripting-symbol-reference.html)
  * [日本語](/ja/current/Manual/scripting-symbol-reference.html)
  * [한국어](/kr/current/Manual/scripting-symbol-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scripting-symbol-reference.html)
  * [中文](/cn/current/Manual/scripting-symbol-reference.html)
  * [日本語](/ja/current/Manual/scripting-symbol-reference.html)
  * [한국어](/kr/current/Manual/scripting-symbol-reference.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Conditional compilation](conditional-compilation.html)
  * Unity scripting symbol reference

[](platform-dependent-compilation.html)

Conditional compilation in Unity

[](custom-scripting-symbols.html)

Custom scripting symbols

# Unity scripting symbol reference

## Platform symbols

Unity automatically defines certain symbols based on the authoring and build
target platform. These are as follows:

**Define** | **Function**  
---|---  
**UNITY_EDITOR** | Scripting symbol to call Unity Editor **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) from your game code.  
**UNITY_EDITOR_WIN** | Scripting symbol for Editor code on Windows.  
**UNITY_EDITOR_OSX** | Scripting symbol for Editor code in macOS.  
**UNITY_EDITOR_LINUX** | Scripting symbol for Editor code on Linux.  
**UNITY_EMBEDDED_LINUX** | Scripting symbol for embedded Linux.  
**UNITY_QNX** | Scripting symbol for QNX.  
**UNITY_STANDALONE_OSX** | Scripting symbol to compile or execute code specifically for macOS (including Universal, PPC and Intel architectures).  
**UNITY_STANDALONE_WIN** | Scripting symbol for compiling/executing code specifically for Windows standalone applications.  
**UNITY_STANDALONE_LINUX** | Scripting symbol for compiling/executing code specifically for Linux standalone applications.  
**UNITY_STANDALONE** | Scripting symbol for compiling/executing code for any standalone platform (Mac OS X, Windows or Linux).  
**UNITY_SERVER** | Scripting symbol for compiling/executing code for a [dedicated server](dedicated-server.html) (macOS, Windows or Linux).  
**UNITY_IOS** | Scripting symbol for compiling/executing code for the iOS platform.  
**UNITY_ANDROID** | Scripting symbol for the Android platform.  
**UNITY_TVOS** | Scripting symbol for the Apple TV platform.  
**UNITY_VISIONOS** | Scripting symbol for the VisionOS platform.  
**UNITY_WSA** | Scripting symbol for Universal Windows Platform.  
**UNITY_WSA_10_0** | Scripting symbol for Universal Windows Platform.  
**UNITY_WEBGL** | Scripting symbol for Web.  
**UNITY_ANALYTICS** | Scripting symbol for calling Unity **Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) methods from your game code.  
**UNITY_ASSERTIONS** | Scripting symbol for assertions control process.  
**UNITY_64** | Scripting symbol for 64-bit platforms. In practice this **should not be used** because it does not work on all 64-bit architectures and different CPU architectures on a given platform can share the same compiled assemblies. To execute code conditionally based on architecture, use a standard `if` statement that checks [IntPtr.Size](https://learn.microsoft.com/en-us/dotnet/api/system.intptr.size?view=net-8.0), which is `4` in a 32-bit process and `8` in a 64-bit process. For an example, refer to [Alternatives to directives](platform-dependent-compilation.html#ConditionalExecution).  
  
## Unity Editor version symbols

Unity automatically defines certain scripting symbols based on the version of
the Unity Editor that you’re currently using.

Given a version number **X.Y.Z** (for example, 2019.4.14), Unity exposes three
global scripting symbols in the following formats: **UNITY_X** , **UNITY_X_Y**
and **UNITY_X_Y_Z**.

Here is an example of scripting symbols exposed in Unity 2019.4.14:

**Define** | **Function**  
---|---  
**UNITY_2019** | Scripting symbol for the release version of Unity 2019, exposed in every 2019.Y.Z release.  
**UNITY_2019_4** | Scripting symbol for the major version of Unity 2019.4, exposed in every 2019.4.Z release.  
**UNITY_2019_4_14** | Scripting symbol for the minor version of Unity 2019.4.14.  
  
You can also compile code selectively based on the earliest version of Unity
required to compile or execute a section of code snippet. Following the same
version format as above (**X.Y**), Unity exposes one global `#define` in the
format **UNITY_X_Y_OR_NEWER** , that you can use for this purpose.

## Other symbols

The other symbols Unity defines are:

**Define** | **Function**  
---|---  
**CSHARP_7_3_OR_NEWER** | Defined when building scripts with support for C# 7.3 or newer.  
**ENABLE_MONO** | Scripting back end #define for Mono.  
**ENABLE_IL2CPP** | Scripting back end #define for **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP).  
**ENABLE_VR** | Defined when the target build platform supports **VR** Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR). Doesn’t imply that VR is currently
enabled or that the necessary **plug-ins** A set of code created outside of
Unity that creates functionality in Unity. There are two kinds of plug-ins you
can use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) and packages needed to support VR are
installed.  
**NET_2_0** | Defined when building scripts against .NET 2.0 API compatibility level on Mono and IL2CPP.  
**NET_2_0_SUBSET** | Defined when building scripts against .NET 2.0 Subset API compatibility level on Mono and IL2CPP.  
**NET_LEGACY** | Defined when building scripts against .NET 2.0 or .NET 2.0 Subset API compatibility level on Mono and IL2CPP.  
**NET_4_6** | Defined when building scripts against .NET 4.x API compatibility level on Mono and IL2CPP.  
**NET_STANDARD_2_0** | Defined when building scripts against .NET Standard 2.0 API compatibility level on Mono and IL2CPP.  
**NET_STANDARD_2_1** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NET_STANDARD** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NETSTANDARD2_1** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**NETSTANDARD** | Defined when building scripts against .NET Standard 2.1 API compatibility level on Mono and IL2CPP.  
**ENABLE_WINMD_SUPPORT** | Defined when Windows Runtime support is enabled on IL2CPP. For more information, refer to [Windows Runtime Support](il2cpp-windows-runtime-support.html).  
**ENABLE_INPUT_SYSTEM** | Defined when the Input System package is enabled in **Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings).  
**ENABLE_LEGACY_INPUT_MANAGER** | Defined when the legacy **Input Manager** Settings where you can define all the different input axes, buttons and controls for your project. [More info](class-InputManager.html)  
See in [Glossary](Glossary.html#InputManager) is enabled in Player Settings.  
**DEVELOPMENT_BUILD** | Defined when your script is running in a Player which was built with the **Development Build** option enabled.  
  
This define only reflects whether the development build option was enabled at
the time of the build. To know whether your script is running in the
development build mode, use [Debug.isDebugBuild](../ScriptReference/Debug-
isDebugBuild.html). `__DEVELOPMENT\_BUILD__` isn’t sufficient to determine
whether you’re currently running in a development build because most platforms
allow changing between development and non-development build without
rebuilding the project. However, on some platforms, Unity doesn’t support
switching between development and non-development builds in the Editor and
requires you to switch after the build is complete. For example, on Windows,
you can choose the **Create Visual Studio solution** option to choose whether
you want a development or non-development build in Visual Studio. Switching in
Visual Studio doesn’t recompile your scripts and therefore, it will not
reevaluate scripting defines. You can also switch from the final game build to
a development build by swapping `UnityPlayer.dll` in the game build with the
one from a development build for debugging live game builds.  
**UNITY_CLOUD_BUILD** | Defined when the project is built with [Unity Build Automation](https://docs.unity.com/ugs/en-us/manual/devops/manual/unity-build-automation)A continuous integration service for Unity projects that automates the process of creating builds on Unity’s servers. [More info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
See in [Glossary](Glossary.html#UnityBuildAutomation).  
  
**Note** : The `DEBUG` symbol is predefined in C# and in Unity using the
directive `#if DEBUG` is equivalent to `#if UNITY_EDITOR || DEVELOPMENT_BUILD`

## Additional resources

  * [Test your conditionally compiled code](test-conditional-compilation.html)
  * [Custom scripting symbols](custom-scripting-symbols.html)

[](platform-dependent-compilation.html)

Conditional compilation in Unity

[](custom-scripting-symbols.html)

Custom scripting symbols

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

