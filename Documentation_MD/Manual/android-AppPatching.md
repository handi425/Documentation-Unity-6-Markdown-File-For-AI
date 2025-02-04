[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/android-AppPatching.html)
  * [中文](/cn/current/Manual/android-AppPatching.html)
  * [日本語](/ja/current/Manual/android-AppPatching.html)
  * [한국어](/kr/current/Manual/android-AppPatching.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/android-AppPatching.html)
  * [中文](/cn/current/Manual/android-AppPatching.html)
  * [日本語](/ja/current/Manual/android-AppPatching.html)
  * [한국어](/kr/current/Manual/android-AppPatching.html)

  * [Platform development ](PlatformSpecific.html)
  * [Android](android.html)
  * [Developing for Android](android-developing.html)
  * [Testing and debugging](android-testing-and-debugging.html)
  * Application patching

[](android-profile-on-an-android-device.html)

Collecting performance data on an Android device

[](android-optimization.html)

Optimization for Android

# Application patching

Building an application for Android can take a significant amount of time. For
faster iterations during development, you can patch the application package
instead of rebuilding it. When you patch an application package, Unity only
processes files you made changes to since the last patch and sends them to the
connected Android device.

## Patching an application

To patch an application, you can use the Unity Editor or, if you implement
your own build pipeline, the scripting API.

The first time you patch an application, Unity sets up the patch application
environment on the device. This means that the first patch takes longer than
future patches.

### From the Editor

To patch an application from the Unity Editor:

  1. Open the Build Settings window (menu: **File** > **Build Settings**).
  2. Select the **Android** platform from the **Platform** list.
  3. Enable ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild)**.

  4. Select **Patch** or, if you want to run the patch after Unity finishes building it, **Patch And Run**.

![The Android Build Settings window.](../uploads/Main/android-app-
patching.png) The Android Build Settings window.

### Using the scripting API

If you implement your own build pipeline, you can use the scripting API to
patch your application. To do this, pass the
[BuildOptions.BuildScriptsOnly](../ScriptReference/BuildOptions.BuildScriptsOnly.html)
and
[BuildOptions.PatchPackage](../ScriptReference/BuildOptions.PatchPackage.html)
options to the
[BuildPipeline.BuildPlayer](../ScriptReference/BuildPipeline.BuildPlayer.html)
method.

For example:

    
    
    BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
    buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity"};
    buildPlayerOptions.target = BuildTarget.Android;
    // Use Patch & Run for all builds for optimal turn-around times.
    // (In prior versions, an initial regular Build & Run was necessary.)
    buildPlayerOptions.options = BuildOptions.PatchPackage | BuildOptions.AutoRunPlayer | BuildOptions.Development;
    BuildPipeline.BuildPlayer(buildPlayerOptions);
    

## How application patching works

When you patch an application, Unity:

  * Creates a minimal **APK** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) that contains all compiled Java sources.

  * Takes files that have changed since the last patch and stores them in a directory inside the application’s cache folder at: `/storage/emulated/0/Android/data/<PackageName>/pram-shadow-files/`.
  * Stores native library files, including scripts compiled using [Il2cpp](./scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP), in the application’s data directory
at: `/data/data/<PackageName>/pram-shadow-files/lib/`.

When the application starts, it checks for a marker file inside the APK. If
the marker exists, the application redirects its file reads to the `pram-
shadow-files` directory.

A **Build & Run** doesn’t clear any of the patch files. Instead, it replaces
the APK install. This disables the redirect to the `pram-shadow-files`
directory. This means that subsequent patch builds can re-use unchanged files.

## Clearing patch files

You can use the Android storage settings to clear the application’s cache.
Clearing the cache removes the patch files installed by the application
patching build process.

The steps to clear an application’s cache are different depending on the
Android device. To find the steps for your device:

  1. Go to [Get help from your device manufacturer](https://support.google.com/android/answer/3094742).
  2. Find your device manufacturer and follow the link to its support website.
  3. Search the support website for steps on clearing an application’s cache.

[](android-profile-on-an-android-device.html)

Collecting performance data on an Android device

[](android-optimization.html)

Optimization for Android

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

