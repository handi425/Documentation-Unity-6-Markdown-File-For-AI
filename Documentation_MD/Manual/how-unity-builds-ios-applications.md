[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/how-unity-builds-ios-applications.html)
  * [中文](/cn/current/Manual/how-unity-builds-ios-applications.html)
  * [日本語](/ja/current/Manual/how-unity-builds-ios-applications.html)
  * [한국어](/kr/current/Manual/how-unity-builds-ios-applications.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/how-unity-builds-ios-applications.html)
  * [中文](/cn/current/Manual/how-unity-builds-ios-applications.html)
  * [日本語](/ja/current/Manual/how-unity-builds-ios-applications.html)
  * [한국어](/kr/current/Manual/how-unity-builds-ios-applications.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Introducing iOS](ios-introducing.html)
  * How Unity builds iOS applications

[](ios-requirements-and-compatibility.html)

iOS requirements and compatibility

[](StructureOfXcodeProject.html)

Structure of a Unity Xcode project

# How Unity builds iOS applications

Unity uses [Xcode](https://developer.apple.com/xcode/) to build iOS
applications. You can use [iOS Player settings](class-PlayerSettingsiOS.html)
to configure most aspects of the final build. However, for more granular
control, building an Xcode project allows you to directly modify Xcode project
files.

## The build process

  1. Unity collects project resources, code libraries, and **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) from your Unity project and uses them
to create a valid [Xcode project](StructureOfXcodeProject.html).

  2. Unity updates the Xcode project based on the Unity project’s **Player settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) and Build settings. Depending
on whether you use [replace or append mode](iphone-BuildProcess.html#replace-
and-append-mode), Unity replaces or preserves previous changes you made.
Append mode preserves changes you previously made and only overwrites certain
values. Replace mode creates a new project which overwrites any changes you
previously made.

  3. Unity generates C++ source files based on your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and places them in the generated
Xcode project. Xcode then invokes the [IL2CPP](./scripting-backends-
il2cpp.html)A Unity-developed scripting back-end which you can use as an
alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) program which compiles the C++ source
files into libraries called `libGameAssembly.a` and `il2cpp.a`.

  4. Xcode builds the project into a standalone application and deploys and launches it on a connected device or the [Xcode simulator](https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device).

## Incremental build pipeline

Unity uses the [incremental build
pipeline](https://docs.unity3d.com/Manual/incremental-build-pipeline.html)
when it generates the Xcode project for iOS. This means that Unity
incrementally builds and generates files such as [Information Property
List](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html)
(plist) files and
[Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements)
files. If you implement callbacks that modify or move any iOS file or asset
that the incremental build pipeline uses, refer to [Creating non-incremental
builds](https://docs.unity3d.com/Manual/incremental-build-
pipeline.html#creating-non-incremental-builds).

## Additional resources

  * [Build an iOS application](iphone-BuildProcess.html)
  * [iOS Build Settings](BuildSettingsiOS.html)

[](ios-requirements-and-compatibility.html)

iOS requirements and compatibility

[](StructureOfXcodeProject.html)

Structure of a Unity Xcode project

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

