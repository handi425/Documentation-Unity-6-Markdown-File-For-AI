[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/windowsstore-generatedproject-il2cpp.html)
  * [中文](/cn/current/Manual/windowsstore-generatedproject-il2cpp.html)
  * [日本語](/ja/current/Manual/windowsstore-generatedproject-il2cpp.html)
  * [한국어](/kr/current/Manual/windowsstore-generatedproject-il2cpp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/windowsstore-generatedproject-il2cpp.html)
  * [中文](/cn/current/Manual/windowsstore-generatedproject-il2cpp.html)
  * [日本語](/ja/current/Manual/windowsstore-generatedproject-il2cpp.html)
  * [한국어](/kr/current/Manual/windowsstore-generatedproject-il2cpp.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Build and deliver for Universal Windows Platform](uwp-building-and-delivering.html)
  * Generate your Visual Studio C++ solution

[](windowsstore-buildsettings.html)

UWP Build Settings reference

[](uwp-package-app-vs.html)

Package a UWP app in Visual Studio

# Generate your Visual Studio C++ solution

When you [build a project from Unity for Universal Windows
Platform](windowsstore-buildsettings.html) (UWP), Unity automatically
generates a Visual Studio solution.

## Create your Visual Studio C++ solution

Unity generates a Visual Studio solution containing the following projects:

**Project** | **Description**  
---|---  
**projectName** | Contains your main project code. Visual Studio builds this project into an application package, which you can deploy to a device or uploaded to the Microsoft Store.   
  
**Note:** Unity doesn’t overwrite this project when you build on top of it.  
**Unity Data** | Contains all the Unity-specific files you need to build your project, such as assets.  
**Il2CppOutputProject** | Contains the generated C++ code which Unity converts from managed assemblies.   
  
**Note:** This project is overwritten every time you build over it.  
  
## Visual Studio build configurations

Unity provides the following [build configuration options in Visual
Studio](https://learn.microsoft.com/en-us/visualstudio/ide/understanding-
build-configurations):

**Configuration** | **Description**  
---|---  
**Debug** | Use **Debug** to debug your code. This configuration:   
\- Disables all optimization.  
\- Preserves all debugging information in the code.  
\- Results in code that runs slowly.  
\- Results in the fastest build time.  
**Release** | Use **Release** to profile your game. This configuration:   
\- Enables code optimizations.  
**Master** | Use **Master** for game submission and final testing. This configuration:   
\- Disables the profiler.  
\- Results in the same build time as the Release configuration.  
\- Results in the same build time as the **Release** configuration.  
**MasterWithLTCG** | Use **MasterWithLTCG** for game submission and final testing. This configuration:   
\- Enables link time code generation for generated C++ code, IL2CPP runtime,
and IL2CPP garbage collection.  
\- Results in much longer build times compared to the **Master**
configuration.  
\- Results in an application that executes faster than the **Master**
configuration.  
  
[](windowsstore-buildsettings.html)

UWP Build Settings reference

[](uwp-package-app-vs.html)

Package a UWP app in Visual Studio

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

