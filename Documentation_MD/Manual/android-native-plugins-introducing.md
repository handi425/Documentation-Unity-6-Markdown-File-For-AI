[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-native-plugins-introducing.html)
  * [中文](/cn/current/Manual/android-native-plugins-introducing.html)
  * [日本語](/ja/current/Manual/android-native-plugins-introducing.html)
  * [한국어](/kr/current/Manual/android-native-plugins-introducing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-native-plugins-introducing.html)
  * [中文](/cn/current/Manual/android-native-plugins-introducing.html)
  * [日本語](/ja/current/Manual/android-native-plugins-introducing.html)
  * [한국어](/kr/current/Manual/android-native-plugins-introducing.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Create and use plug-ins in Android](PluginsForAndroid.html)
  * [Android plug-in types](android-plugin-types.html)
  * [Native plug-ins for Android](AndroidNativePlugins.html)
  * Introducing native plug-ins for Android

[](AndroidNativePlugins.html)

Native plug-ins for Android

[](android-native-plugins-create.html)

Create a native plug-in for Android

# Introducing native plug-ins for Android

You can use [native plug-ins](plug-ins-native.html)A platform-specific native
code library that is created outside of Unity for use in Unity. Allows you can
access features like OS calls and third-party code libraries that would
otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in) in Android applications. There
are different types of native **plug-in** A set of code created outside of
Unity that creates functionality in Unity. There are two kinds of plug-ins you
can use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in), and the project’s [scripting
backend](scripting-backends.html)A framework that powers scripting in Unity.
Unity supports three different scripting backends depending on target
platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports
only two: .NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) determines which plug-in
types Unity supports. The possible plug-in types are:

  * **Shared library** : Plug-ins packaged in a shared library (`.so`).
  * **Static library** : Plug-ins packaged in a static library (`.a`).
  * **C/C++ source files** : C/C++ source files that Unity compiles along with [IL2CPP](./scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) generated files. This includes all
C/C++ source files with extensions `.c`, `.cc`, `.cpp` and `.h`.

## Scripting backend compatibility

The following table shows which scripting backends support the different types
of native plug-ins.

**Scripting backend** | **Shared library** | **Static library** | **C/C++ source files**  
---|---|---|---  
**IL2CPP** | Yes | Yes | Yes  
**Mono** | Yes | No | No  
  
**Notes** :

  * IL2CPP scripting backend doesn’t support direct use of .NET dynamic linked libraries (.dll) at runtime. These libraries must be converted to C++ code during the build process.
  * Integration with other .NET runtime platforms, such as Xamarin isn’t supported.

## Additional resources

  * [Create a native plug-in for Android](android-native-plugins-create.html)

[](AndroidNativePlugins.html)

Native plug-ins for Android

[](android-native-plugins-create.html)

Create a native plug-in for Android

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

