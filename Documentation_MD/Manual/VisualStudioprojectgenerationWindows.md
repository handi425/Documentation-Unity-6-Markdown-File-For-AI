[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VisualStudioprojectgenerationWindows.html)
  * [中文](/cn/current/Manual/VisualStudioprojectgenerationWindows.html)
  * [日本語](/ja/current/Manual/VisualStudioprojectgenerationWindows.html)
  * [한국어](/kr/current/Manual/VisualStudioprojectgenerationWindows.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VisualStudioprojectgenerationWindows.html)
  * [中文](/cn/current/Manual/VisualStudioprojectgenerationWindows.html)
  * [日本語](/ja/current/Manual/VisualStudioprojectgenerationWindows.html)
  * [한국어](/kr/current/Manual/VisualStudioprojectgenerationWindows.html)

  * [Platform development ](PlatformSpecific.html)
  * [Windows](Windows.html)
  * [Develop for Windows](windows-develop.html)
  * Visual Studio project generation for Windows 

[](windows-develop.html)

Develop for Windows

[](WindowsDebugging.html)

Windows debugging

# Visual Studio project generation for Windows

The **Create Visual Studio Solution** Build Setting makes Unity generate a
Visual Studio [Solution](https://docs.microsoft.com/en-
us/visualstudio/ide/solutions-and-projects-in-visual-
studio?view=vs-2019#solutions) instead of build a Player. Generating a Visual
Studio Solution enables you to change your build process. For example, you
can:

  * Modify your application’s manifest.
  * Add C++ code.
  * Modify embedded resources.
  * Launch your application with the debugger attached.

**Note** : This option is only available when you are using the Windows build
target.

## Create a Visual Studio Solution

**Warning:** Make sure you save and back up any changes you make in Visual
Studio before rebuilding your Unity project. If you do not back up your
changes, Unity overwrites them during the build process.

  1. Go to **File** > **Build Settings** > **Target Platform**.
  2. Select the **Windows** build target.
  3. Enable the **Create Visual Studio Solution** build setting.
  4. Select **Build** to generate the solution.

![Build Settings Panel with Create Visual Studio Solution
selected](../uploads/Main/buildsettingsVSsolution.png) Build Settings Panel
with Create Visual Studio Solution selected

By default, Unity stores the Visual Studio Solution you generate in the same
directory as your built project.

### Scripting backends

Depending on which [scripting backend](scripting-backends.html)A framework
that powers scripting in Unity. Unity supports three different scripting
backends depending on target platform: Mono, .NET and IL2CPP. Universal
Windows Platform, however, supports only two: .NET and IL2CPP. [More
info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) your Unity project uses, the
Visual Studio Solution that Unity generates includes a different number of
projects. For the [Mono](./scripting-backends-mono.html)A scripting backend
used in Unity. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#Mono) scripting backend, the solution includes
three projects. For the [IL2CPP](./scripting-backends-il2cpp.html)A Unity-
developed scripting back-end which you can use as an alternative to Mono when
building projects for some platforms. [More info](./scripting-backends-
il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) scripting backend, the solution
includes four projects.

**Note** : You can only build Windows IL2CPP on a Windows machine.

## Project retarget wizard

Unity generates a Visual Studio Solution that targets Visual Studio 2015. If
you are using a newer version of Visual Studio, you might see the **Retarget
Projects** dialog box when you open your Visual Studio Solution.

The **Retarget Projects** dialog prompts you to upgrade your Visual Studio
Solution to match the Visual Studio version you have installed. Select **OK**
to accept this suggestion.

## Solution contents

Below is a list of the projects Unity generates for your Visual Studio
Solution.

**Project** | **Description**  
---|---  
**projectName**  
(represents your project name) | This is your main project. Visual Studio builds this project into the final application executable. You are most likely to make changes here.  
**UnityData**  
(stored inside the projectName project) | This project contains all the Unity-specific files you need to build your project, such as assets.  
**UnityPlayerStub** | This is a stub library for `UnityPlayer.dll`. Unity uses this to link your executable to the `UnityPlayer.dll` and expose the available `UnityPlayer.dll` API.  
**Il2CppOutputProject**  
(IL2CPP scripting backend only) | This project contains:   
• The generated C++ code which Unity converts from managed assemblies.  
• The source code for IL2CPP runtime.  
• The IL2CPP garbage collector.  
You can debug this code from inside Visual Studio.  
  
## Build configuration options in Visual Studio

Visual Studio provides a variety of build configuration options. All
optimization and debug references in this section refer to the Visual Studio
Solution only. To select your options, click on **Release** and choose from
the drop-down menu.

### Types of build configurations

**Configuration** | **Use** | **Description**  
---|---|---  
**Debug** | Use the **Debug** configuration when debugging C++ code. |    
• Disables all optimization.  
• Preserves all debugging information in the code.  
• Results in code that runs slowly.  
**Release** | Use the **Release** configuration to profile your game. | • Enables code optimizations.  
**Master** | Use the **Master** configuration for game submission and final testing. | • Disables the profiler.  
• Results in the same build time as the **Release** configuration.  
**MasterWithLTCG** .Only available with the IL2CPP scripting backend is enabled. | If you are using the IL2CPP scripting backend, you can choose either **Master** or **MasterWithLTCG** for game submission and final testing. | • Enables link time code generation for generated C++ code, IL2CPP runtime and IL2CPP garbage collection.  
• Results in much longer build times compared to the **Master** configuration.  
• Resulting application executes faster.  
  
[](windows-develop.html)

Develop for Windows

[](WindowsDebugging.html)

Windows debugging

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

