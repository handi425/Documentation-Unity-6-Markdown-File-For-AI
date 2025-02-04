[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/TroubleShootingIPhone.html)
  * [中文](/cn/current/Manual/TroubleShootingIPhone.html)
  * [日本語](/ja/current/Manual/TroubleShootingIPhone.html)
  * [한국어](/kr/current/Manual/TroubleShootingIPhone.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/TroubleShootingIPhone.html)
  * [中文](/cn/current/Manual/TroubleShootingIPhone.html)
  * [日本語](/ja/current/Manual/TroubleShootingIPhone.html)
  * [한국어](/kr/current/Manual/TroubleShootingIPhone.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * [Test and debug an iOS application](ios-testing-and-debugging.html)
  * Troubleshooting on iOS devices

[](iOSManagedStackTraces.html)

Managed stack traces on iOS

[](iphone-bugreporting.html)

Report crash bugs for iOS

# Troubleshooting on iOS devices

Use the following information to help find solutions to common crashes and
other problems when running your Unity application on iOS devices.

**Note** : If your issue persists after troubleshooting, refer to [Report
crash bugs for iOS](iphone-bugreporting.html).

  * Application stops responding and Xcode displays interrupted in the status bar
  * Xcode console displays Program received signal: “SIGBUS” or EXC_BAD_ACCESS error
  * Xcode console shows WARNING -> applicationDidReceiveMemoryWarning() and then the application crashes
  * Application launches correctly from Xcode, but crashes loading the first scene on the device
  * Killed by SpringBoard appears in the Xcode Organizer console
  * Crashes occur on the device when using System.Security.Cryptography and managed code stripping
  * Application crashes when using System.Security.Cryptography.MD5 and managed code stripping
  * PlayerLoop called recursively! error message occurs when using Cocoa via a native function
  * The Profiler or Debugger is unable to access the application
  * Xcode displays error ARM64 branch out of range (<value> max is +/–128MB)
  * iOS simulators aren’t visible on ARM-based Macs running Xcode 14.3
  * Additional resources

## Application stops responding and Xcode displays interrupted in the status
bar

The following list provides some common reasons for this issue:

  * Scripting errors, such as using uninitialized variables.
  * Use of third party Thumb compiled native libraries. These libraries can trigger a known problem in the iOS SDK linker and might cause random crashes.
  * Use of generic types with value types as parameters. For example `List<int>`, `List<SomeStruct>`, `List<SomeEnum>` for serialized script properties.
  * Use of reflection when managed code stripping is enabled.
  * Errors in the native **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) interface where the managed code
method signature doesn’t match the native code function signature.

Information from the Xcode debugger console can often help detect these
problems. Access the debugger console from **View** > **Debug Area** >
**Activate Console**.

## Xcode console displays Program received signal: “SIGBUS” or EXC_BAD_ACCESS
error

This message typically appears on iOS devices when your application receives a
`NullReferenceException`. Use native stack traces to find out where the fault
occurred.

Native stack traces are a useful tool for fault investigation, but using them
requires some expertise. You generally can’t continue after these hardware
memory access faults happen. To access a native stack trace, type `bt all`
into the Xcode debugger console. Inspect the printed stack traces as they can
contain information about where the error occurred. For example, a typical
stack trace might look like this:

    
    
    ...
    Thread 1 (thread 11523): 
    
    1. 0 0x006267d0 in m_OptionsMenu_Start ()
    1. 1 0x002e4160 in wrapper_runtime_invoke_object_runtime_invoke_void__this___object_intptr_intptr_intptr ()
    1. 2 0x00a1dd64 in mono_jit_runtime_invoke (method=0x18b63bc, obj=0x5d10cb0, params=0x0, exc=0x2fffdd34) at /Users/mantasp/work/unity/unity-mono/External/Mono/mono/mono/mini/mini.c:4487
    1. 3 0x0088481c in MonoBehaviour::InvokeMethodOrCoroutineChecked ()
    ...
    

Locate the stack trace for **“Thread 1”** , which is the main thread. The
initial lines of the stack trace will point to the place where the error
occurred. In this example, the trace indicates that the
`NullReferenceException` happened inside the `_OptionsMenu_` script’s
`_Start_` method. Inspecting this method implementation can help reveal the
cause of the problem. Typically, NullReferenceExceptions happen inside the
`_Start_` method when incorrect assumptions are made about initialization
order.

Sometimes only a partial stack trace is displayed in the debugger console. For
example:

    
    
    Thread 1 (thread 11523): 
    
    1. 0 0x0062564c in start ()
    

This message indicates that native symbols were stripped during the release
build of the application. To investigate further, access the full stack trace
using the following steps:

  1. Remove the application from the device.
  2. Clean all targets.
  3. Select **Product** > **Run**.
  4. Retrieve the stack traces as described previously.

## Xcode console shows WARNING -> applicationDidReceiveMemoryWarning() and
then the application crashes

You might encounter a warning message like `Program received signal: "0"`.
This warning message is often not fatal, and indicates that iOS is low on
memory. Typically, background processes like Mail will free some memory and
your application can continue to run. However, if your application continues
to use memory or ask for more, iOS will start terminating applications
including your own. Apple doesn’t document what memory usage is safe, but
observations have shown that applications using less than 50% of all device
RAM don’t have major memory usage problems.

The main metric to use is how much RAM your application uses. Your application
memory usage consists of the following components:

**Component** | **Description**  
---|---  
**Application code** | The OS needs to load and keep your application code in RAM, but some of it might be discarded if required.  
**Native heap** | Used by the engine to store its state and your assets in RAM.  
**Managed heap** | Used by your **il2cpp** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) runtime to store C# objects.  
**Metal memory pools** | Used to store Textures, framebuffers, and compiled **shaders** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).  
  
You can track application memory usage in Xcode. For more information, refer
to [Gathering information about memory
use](https://developer.apple.com/documentation/xcode/gathering-information-
about-memory-use) (Apple Developer).

To keep memory usage low, use the following suggestions:

  * Reduce the application binary size: Use the strongest iOS stripping options and avoid unnecessary dependencies on different .NET libraries. For more information, refer to [Player](class-PlayerSettings.html) settings and [Optimizing the size of the built iOS Player](iphone-playerSizeOptimization.html).
  * Reduce the size of your content: Use PVRTC **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) for textures and use low poly
models. For more information, refer to [reducing file
size](ReducingFilesize.html).

  * Don’t allocate more memory than necessary in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts): Track mono heap size and usage with
the [Profiler window](ProfilerWindow.html).

Querying the OS about the amount of free memory might seem to be the most
efficient way to evaluate how well your application is performing. However,
the free memory statistic is likely to be unreliable as the OS uses a lot of
dynamic buffers and caches. It’s recommended to keep track of memory
consumption for your application and use that as the main metric, combined
with the Xcode memory tools especially after loading new **scenes** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

## Application launches correctly from Xcode, but crashes loading the first
scene on the device

It’s recommended to inspect the device logs to get more details. To do this,
use the following steps:

  1. Connect the target device to your macOS device.
  2. From Xcode, select **Window** > **Devices and Simulators**.
  3. Select your target device in the window’s left **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar).

  4. Click **Show the device console** and review the latest messages.

You might also need to investigate crash reports. For more information, refer
to [Acquiring crash reports and diagnostic
logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-
and-diagnostic-logs/) (Apple Developer).

## Killed by SpringBoard appears in the Xcode Organizer console

There’s a set time limit to allow an iOS application to render the first
frames and process input. If your application exceeds this limit, it is
terminated by SpringBoard. For example, this can happen in an application
where the size of the first scene is too large. It’s recommended to create a
small initial scene with a splash screen, wait for a few frames, and then
proceed to load the larger scene. To achieve this, use the following example:

    
    
    IEnumerator Start() {
        yield return new WaitForEndOfFrame();
    // Do not forget using UnityEngine.SceneManagement directive
        SceneManager.LoadScene("Test");
    }
    

## Crashes occur on the device when using System.Security.Cryptography and
managed code stripping

.NET Cryptography services aren’t compatible with managed code stripping.
These services rely on reflection, whereas managed code stripping involves
static code analysis. The stripping process can be customized by adding a
custom `link.xml` file to the `Assets` folder of your Unity project. This
specifies the types and namespaces to exclude from stripping. Exclude the
`System.Security.Crypography` namespace from the stripping process to help
resolve this issue. For example, add the following to the `link.xml` file:

    
    
    <linker>
           <assembly fullname="mscorlib">
                   <namespace fullname="System.Security.Cryptography" preserve="all"/>
           </assembly>
    </linker>
    

## Application crashes when using System.Security.Cryptography.MD5 and managed
code stripping

You can resolve this issue in the same way as outlined in the previous
section, or you can add extra references to specific classes to your script
code. To do this, use the following example:

    
    
    object obj = new MD5CryptoServiceProvider();
    

## PlayerLoop called recursively! error message occurs when using Cocoa via a
native function

Some operations within the **UI**(User Interface) Allows a user to interact
with your application. Unity currently supports three UI systems. [More
info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) will result in iOS redrawing the window
immediately. The most common example is adding a UIView with a
UIViewController to the main UIWindow. If calling a native function from a
script, it will happen inside Unity’s PlayerLoop, resulting in the PlayerLoop
being called recursively. When this occurs, you will receive the error message
`PlayerLoop called recursively!`. In such cases, consider using the
[performSelectorOnMainThread](https://developer.apple.com/documentation/objectivec/nsobject/1414900-performselector)
(Apple Developer) method with `waitUntilDone` set to **false**. It will inform
iOS to schedule the operation to run between Unity’s PlayerLoop calls.

## The Profiler or Debugger is unable to access the application

To diagnose this issue, use the following suggestions:

  * Check that you have built a ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)**, enabled **Script
Debugging** , and enabled **Autoconnect**Profiler** A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler)**. For more information on these
properties, refer to [iOS Build Settings reference](BuildSettingsiOS.html).

  * The application running on the device will make a multicast broadcast to `225.0.0.222` on UDP port `54997`. Check that your network settings allow this traffic. The profiler will also make a connection to the remote device on a port in the range `55000 - 55511` to fetch profiler data from the device. These ports will need to be open for TCP access.

## Xcode displays error ARM64 branch out of range (<value> max is +/–128MB)

This issue is caused when the built machine code is too large and has hit
Xcode limitations. This can occur if you have lots of script code, or are
using large external .NET assemblies in a build. Using the **Script
Debugging** build setting can also add to this issue, as it creates additional
instructions for each function.

To assist with this issue, in the Unity Editor navigate to **Edit** >
**Project Settings** > **Player** > **iOS** and try one or more of the
following options:

  * Enable **Strip Engine Code**.
  * Use a higher **Managed Stripping Level**.
  * Set **IL2CPP Code Generation** to **Faster (smaller) Builds**.

If the issue persists, it’s recommended to split user script code into
multiple assemblies. For example, the `Plugins` folder can be used to place
any split code as code at this location is added to a different assembly. It’s
also recommended to refer to [Special folders and script compilation
order](script-compile-order-folders.html) for information on how special
folder names affect script compilation.

## iOS simulators aren’t visible on ARM-based Macs running Xcode 14.3

Starting with Xcode version 14.3, Apple introduced the **Destination
Architecture** option. With **Destination Architecture** , you can use iOS
simulators on ARM-based Macs without the need to run Xcode in Rosetta
simulator mode.

To view the iOS simulators, use the following steps:

  1. In the Xcode menu bar, select **Product** > **Destination** > **Destination Architectures**.
  2. Select **Show Rosetta Destinations** , or **Show Both** to view the iOS simulators for both Apple Silicon and Rosetta architectures.

## Additional resources

  * [Scripting Restrictions](scripting-restrictions.html)
  * [Report crash bugs for iOS](iphone-bugreporting.html)

[](iOSManagedStackTraces.html)

Managed stack traces on iOS

[](iphone-bugreporting.html)

Report crash bugs for iOS

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

