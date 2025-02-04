[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [中文](/cn/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [日本語](/ja/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [한국어](/kr/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [中文](/cn/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [日本語](/ja/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
  * [한국어](/kr/current/Manual/WindowsPlayerIL2CPPScriptingBackend.html)

  * [Platform development ](PlatformSpecific.html)
  * [Windows](Windows.html)
  * [Develop for Windows](windows-develop.html)
  * Windows Player: IL2CPP Scripting Backend

[](WindowsLowIntegrity.html)

Windows integrity control

[](WindowsStandaloneBinaries.html)

Windows Build Settings reference

# Windows Player: IL2CPP Scripting Backend

You can use IL2CPP as an alternative to Mono for **scripting backend** A
framework that powers scripting in Unity. Unity supports three different
scripting backends depending on target platform: Mono, .NET and IL2CPP.
Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More
info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) when building projects for
Windows Player.

When you build a Project using IL2CPP, Unity converts IL code from **scripts**
A piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and assemblies to C++ before creating
a native binary. See [IL2CPP](./scripting-backends-il2cpp.html)A Unity-
developed scripting back-end which you can use as an alternative to Mono when
building projects for some platforms. [More info](./scripting-backends-
il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) for more information.

## C++ source code plugins for IL2CPP

You can add C++ (.cpp) code files directly into a Unity Project when using the
[IL2CPP](./scripting-backends-il2cpp.html) scripting backend. The C++ files
act as plugins within the Plugin **Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). If you configure the C++ files to
be compatible with Windows Player, Unity compiles them together with C++ code
that gets generated from managed assemblies.

To view the plugin importer settings for C++ files, click a .cpp file and
select the appropriate **Windows** option in the Platform settings section of
the Inspector:

![Plugin importer settings for C++
files](../uploads/Main/PlatformIL2CPPPlatformSettings.png) Plugin importer
settings for C++ files

Because the functions are linked together with generated C++ code, there is no
separate DLL to `_P/Invoke` into. Due to this, you can use the `“__Internal”`
keyword in place of the DLL name, which makes it the C++ linker’s
responsibility to resolve the functions, rather than loading them at run time,
as the following example shows:

    
    
    [DllImport("__Internal")]
    private static extern int
    CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);
    

You can define this kind of function in `NativeFunctions.cpp` as follows:

    
    
    extern "C" __declspec(dllexport) int __stdcall CountLettersInString(wchar_t* str)
    {
        int length = 0;
        while (*str++ != L'\0')
            length++;
        return length;
    }
    

Because the linker resolves the function call, any error made in the function
declaration on the managed side (C# code that executes under managed run time)
produces a linker error instead of a run-time error. This means, no dynamic
loading can take place during run time, and the function is called directly
from C#, which significantly decreases the performance overhead of a
`P/Invoke` call.

Unity compiles source code plug-ins with the same C++ compiler arguments as
the generated C++ code, which can’t be modified. If some **plug-in** A set of
code created outside of Unity that creates functionality in Unity. There are
two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) source code requires control over C++
compiler arguments, you must build a native plug-in instead. For more
information, see [Native plug-in](plug-ins-native.html)A platform-specific
native code library that is created outside of Unity for use in Unity. Allows
you can access features like OS calls and third-party code libraries that
would otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in).

## IL2CPP build files

A project using the IL2CPP scripting backend typically produces these files:

![IL2CPP files produced during
build](../uploads/Main/IL2CPPBuildProducedFiles.png) IL2CPP files produced
during build

The following files are common to projects that use IL2CPP:

**File:** | **Description:**  
---|---  
**a_Data** | Folder with game data.  
**a.exe** | Main game executable.  
**UnityCrashHandler64.exe** | Crash handler executable.  
**UnityPlayer.dll** | Unity Player library containing all native code.  
**WinPixEventRuntime.dll** | PIX for Windows runtime. This file is present only in **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild).  
**a_BackUpThisFolder_ButDontShipItWithYourGame** | Folder containing data required to debug your game, including PDB (debug info) files and C++ code generated from your scripts. You should back up this folder for every build you ship, but don’t redistribute it.  
**GameAssembly.dll** | Library that contains the IL2CPP runtime and all your script code.  
**SymbolMap** | File containing a list of all managed function addresses and their lengths. IL2CPP needs this to resolve managed stack traces. If you delete it, you can still run your game but there’s no gurantee that exceptions will generate sensible call stacks.  
  
## Additional resources:

  * [Plugin Inspector](plug-in-inspector.html)
  * [IL2CPP](./scripting-backends-il2cpp.html)
  * [Use P/Invoke](https://docs.unity3d.com/Manual/uwp-pinvoke.html)

[](WindowsLowIntegrity.html)

Windows integrity control

[](WindowsStandaloneBinaries.html)

Windows Build Settings reference

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

