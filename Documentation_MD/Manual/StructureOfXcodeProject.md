[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StructureOfXcodeProject.html)
  * [中文](/cn/current/Manual/StructureOfXcodeProject.html)
  * [日本語](/ja/current/Manual/StructureOfXcodeProject.html)
  * [한국어](/kr/current/Manual/StructureOfXcodeProject.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StructureOfXcodeProject.html)
  * [中文](/cn/current/Manual/StructureOfXcodeProject.html)
  * [日本語](/ja/current/Manual/StructureOfXcodeProject.html)
  * [한국어](/kr/current/Manual/StructureOfXcodeProject.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Introducing iOS](ios-introducing.html)
  * Structure of a Unity Xcode project

[](how-unity-builds-ios-applications.html)

How Unity builds iOS applications

[](iphone-GettingStarted.html)

Getting started with iOS

# Structure of a Unity Xcode project

When you build a Unity project for the iOS platform, Unity creates a folder
that contains an Xcode project. You need to build and sign this project before
you deploy it on a device or distribute it on the App Store.

**Note** : You can modify a generated Xcode project using
[Xcode.PBXProject](../ScriptReference/iOS.Xcode.PBXProject.html).

Every generated Unity iOS Xcode project has the following structure and
targets:

![Unity iOS Xcode project structure](../uploads/Main/Unity-iPhone-Project-
Folder.png) Unity iOS Xcode project structure

The Xcode project includes the Xcode project file `xcodeproj`, and framework
links that only appear in the Xcode project navigator. Apart from the default
folders, you can create custom folders to add your custom files.

## Project targets

  * **Unity-iPhone** : A thin launcher part that runs the **UnityFramework**. It includes the `MainApp` folder and app representation data such as Launch Screens, `.xib` files, icons, data, and `Info.plist` files. The **Unity-iPhone** target has a single dependency on the **UnityFramework** target.
  * **UnityFramework** : The target that produces the `UnityFramework.framework` bundle. It includes the Unity runtime, `Classes`, `UnityFramework`, and `Libraries` folders, along with dependent frameworks. `UnityFramework` folder includes privacy manifest file (PrivacyInfo.xcprivacy), a consolidated privacy manifest file for Unity runtime, Unity **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in), packages, and your project.

  * **GameAssembly:** A container for your C# code translated as C++ code. To build it, Xcode uses the IL2CPP tool that Unity includes in every generated Xcode project. The build produces: 
    * `libGameAssembly.a`: A static library that contains all the project’s managed code, cross-compiled to C++, and built for iOS.
    * `il2cpp.a`: A static library that contains the [IL2CPP](./scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) runtime code to support your managed
code.

**Note** : Use
[PBXProject.GetUnityFrameworkTargetGuid()](../ScriptReference/iOS.Xcode.PBXProject.GetUnityFrameworkTargetGuid.html)
to get the **UnityFramework** target GUID and
[PBXProject.GetUnityMainTargetGuid()](../ScriptReference/iOS.Xcode.PBXProject.GetUnityMainTargetGuid.html)
to get the **Unity-iPhone** target GUID.

## Classes folder

The `Classes` folder contains code that integrates the Unity runtime and
Objective-C. Unity stores the entry points of the application in the `main.mm`
and `UnityAppController.mm/h` files inside this folder. You can create your
own `AppDelegate` derived from `UnityAppController`, or, if any of your plug-
ins include `AppController.h`, you can include `UnityAppController.h` instead.
If your `Plugins/iOS` folder includes `AppController.mm/h`, you can merge and
rename them.

The `InternalProfiler.h` file defines a compiler conditional to enable the
internal **profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler). The code in this folder doesn’t
change often, and you can place custom classes here. If you select the [Append
mode](iphone-BuildProcess.html#replace-and-append-mode), Xcode preserves
changes to this folder between builds. However, this function doesn’t support
multiple build targets and requires a fixed structure of the `Libraries`
folder.

Unity’s internal profiler is fast and unobtrusive, and feeds basic information
about:

  * Which subsystem is taking most of the frame time.
  * The .NET heap size.
  * GC event count and duration.

## Data folder

This folder contains your application’s serialized assets and .NET assemblies
(`.dll` or `.dat` files) as either full code or metadata, depending on code
stripping settings. The `machine.config` file sets up various .NET services
such as security and WebRequest. Xcode refreshes the contents of this folder
with every build. You shouldn’t make any changes to it.

By default, the `Data` folder’s **Target Membership** is the **Unity-iPhone**
target, and Unity runtime searches for it in the `mainBundle`. To change the
default bundle where Unity runtime looks for the `Data` folder, call
`setDataBundleId: "com.my.product"` on the UnityFramework instance before you
call one of the run functions. For example, if you want to have `Data`
together with the UnityFramework call, use `setDataBundleId:
"com.unity3d.framework"` and set the **Target Membership** to
**UnityFramework**.

![](../uploads/Main/Xcode-Data-Folder.png)

**Note:** On-Demand Resources are only supported when the `Data` folder is a
part of the Application target and not a part of the `UnityFramework` target.

## Libraries folder

The `Libraries` folder contains `libil2cpp.a` for IL2CPP. The `libiPhone-
lib.a` file is the Unity runtime static library, and `RegisterMonoModules.cpp`
binds Unity native code with .NET. Xcode refreshes the contents of this folder
with every build. You shouldn’t make any changes to it.

## Graphic files

Icons and splash screens (`.png` files) are located in asset catalogs in the
`Unity-iPhone` folder. Unity automatically manages these files. Launch
screens, their XML Interface Builders (`.xib` files), and Storyboard files are
stored in the project’s root folder. You can configure these files in the
**Player Settings** window (menu: **Edit** > **Project Settings** > **Player
Settings**). Make sure the custom launch images that you create adhere to
Apple’s [Human Interface Guidelines](https://developer.apple.com/ios/human-
interface-guidelines/).

## Property list (.plist) file

You can manage the `Info.plist` file within the **Unity-iPhone** target
(accessed via `mainBundle`) from Unity’s **Player Settings** window (menu:
**Edit** > **Project Settings** > **Player Settings** > **Other Settings** >
**Identification**). Unity updates this file rather than replacing it while
building the Player. Don’t make changes to it unless you need to.

The `/UnityFramework/Info.plist` file, accessed via
`bundleWithIdentifier:@"com.unity3d.framework"`, is a part of
`UnityFramework`. You can keep values in this file instead of the `Info.plist`
file of the `mainBundle`. This makes sure that you can still get these values
if `UnityFramework` is moved into another application, for example, when using
[Unity as a Library](UnityasaLibrary-iOS.html).

## Additional resources

  * [Built-in Profiler](iphone-InternalProfiler.html)
  * [iOS Player settings](class-PlayerSettingsiOS.html#Identification)

[](how-unity-builds-ios-applications.html)

How Unity builds iOS applications

[](iphone-GettingStarted.html)

Getting started with iOS

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

