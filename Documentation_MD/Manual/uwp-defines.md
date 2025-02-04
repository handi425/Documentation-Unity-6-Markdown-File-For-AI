[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-defines.html)
  * [中文](/cn/current/Manual/uwp-defines.html)
  * [日本語](/ja/current/Manual/uwp-defines.html)
  * [한국어](/kr/current/Manual/uwp-defines.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-defines.html)
  * [中文](/cn/current/Manual/uwp-defines.html)
  * [日本語](/ja/current/Manual/uwp-defines.html)
  * [한국어](/kr/current/Manual/uwp-defines.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * UWP scripting symbols

[](windowsstore-profiler.html)

Connect the profiler to UWP

[](uwp-il2cpp-scripting.html)

IL2CPP scripting backend for UWP

# UWP scripting symbols

Unity has a range of built-in scripting symbols which represent options that
you can use in your **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) to selectively include or exclude
portions of code from compilation. For more information on conditional
compilation, refer to [Conditional compilation](platform-dependent-
compilation.html).

**Note:** You can also refer to scripting symbols can as define symbols,
preprocessor defines, or defines.

Unity automatically defines these scripting symbols for Universal Windows
Platform (UWP):

**Scripting symbol** | **Description**  
---|---  
`UNITY_WINRT` | Defined on all scripts.  
`UNITY_WSA` | Defined on all scripts.  
`UNITY_WINRT_10_0` | Defined on all scripts.  
`UNITY_WSA_10_0` | Defined on all scripts.  
`ENABLE_IL2CPP` | Defined on all scripts when using **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) **scripting backend** A framework that
powers scripting in Unity. Unity supports three different scripting backends
depending on target platform: Mono, .NET and IL2CPP. Universal Windows
Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-
backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend).  
`WINDOWS_UWP` | Defined on all scripts when building for UWP.  
`ENABLE_WINMD_SUPPORT` | Defined on all scripts when building for UWP.  
  
## Additional resources

  * [Conditional compilation](platform-dependent-compilation.html)
  * [Custom scripting symbols](custom-scripting-symbols.html)
  * [Microsoft documentation on C# preprocessor directives](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives)

[](windowsstore-profiler.html)

Connect the profiler to UWP

[](uwp-il2cpp-scripting.html)

IL2CPP scripting backend for UWP

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

