[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/il2cpp-windows-runtime-support.html)
  * [中文](/cn/current/Manual/il2cpp-windows-runtime-support.html)
  * [日本語](/ja/current/Manual/il2cpp-windows-runtime-support.html)
  * [한국어](/kr/current/Manual/il2cpp-windows-runtime-support.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/il2cpp-windows-runtime-support.html)
  * [中文](/cn/current/Manual/il2cpp-windows-runtime-support.html)
  * [日本語](/ja/current/Manual/il2cpp-windows-runtime-support.html)
  * [한국어](/kr/current/Manual/il2cpp-windows-runtime-support.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Scripting backends](scripting-backends.html)
  * [IL2CPP Overview](scripting-backends-il2cpp.html)
  * Windows Runtime support

[](linux-il2cpp-crosscompiler.html)

Linux IL2CPP cross-compiler

[](il2cpp-managed-stack-traces.html)

Managed stack traces with IL2CPP

# Windows Runtime support

Unity includes Windows Runtime support for [IL2CPP](./scripting-backends-
il2cpp.html)A Unity-developed scripting back-end which you can use as an
alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) on Universal Windows Platform
platform. Use Windows Runtime support to call into both native system Windows
Runtime APIs as well as custom .winmd files directly from managed code
(scripts and DLLs).

To automatically enable Windows Runtime support in IL2CPP, go to the
[Player](class-PlayerSettings.html) settings (**Edit** > **Project Settings**
A broad collection of settings which allow you to configure how Physics,
Audio, Networking, Graphics, Input and many other areas of your project
behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings), then select the **Player**
category), navigate to the **Configuration** section, and set the **Api
Compatibility Level** to **.NET 4.6** or **.NET Standard 2.0**.

![The Configuration section of the Player settings. The options shown above
change depending on your chosen build platform.](../uploads/Main/IL2CPP-4.png)
The Configuration section of the **Player** settings. The options shown above
change depending on your chosen build platform.

Unity automatically references Windows Runtime APIs (such as _Windows.winmd_
on Universal Windows Platform) when it has Windows Runtime support enabled. To
use custom .winmd files, import them (together with any accompanying DLLs)
into your Unity project folder. Then use the [Plugin Inspector](plug-in-
inspector.html) to configure the files for your target platform.

![Use the Plugin Inspector to configure custom .winmd files for specific
platforms ](../uploads/Main/IL2CPP-5.png) Use the Plugin Inspector to
configure custom .winmd files for specific platforms

In your Unity project’s [scripts](scripting.html)A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) you can use the
`ENABLE_WINMD_SUPPORT` #define directive to check that your project has
Windows Runtime support enabled. Use this before a call to .winmd Windows APIs
or custom .winmd scripts to ensure they can run and to ensure any scripts not
relevant to Windows ignore them. Note, this is only supported in C# scripts.
See the examples below.

**Examples**

**`C#`**

    
    
    void Start() {
      #if ENABLE_WINMD_SUPPORT
        Debug.Log("Windows Runtime Support enabled");
        // Put calls to your custom .winmd API here
      #endif
    }
    

## Additional resources

  * [Windows build settings reference](WindowsStandaloneBinaries.html)

[](linux-il2cpp-crosscompiler.html)

Linux IL2CPP cross-compiler

[](il2cpp-managed-stack-traces.html)

Managed stack traces with IL2CPP

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

