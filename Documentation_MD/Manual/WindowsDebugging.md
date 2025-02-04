[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/WindowsDebugging.html)
  * [中文](/cn/current/Manual/WindowsDebugging.html)
  * [日本語](/ja/current/Manual/WindowsDebugging.html)
  * [한국어](/kr/current/Manual/WindowsDebugging.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/WindowsDebugging.html)
  * [中文](/cn/current/Manual/WindowsDebugging.html)
  * [日本語](/ja/current/Manual/WindowsDebugging.html)
  * [한국어](/kr/current/Manual/WindowsDebugging.html)

  * [Platform development ](PlatformSpecific.html)
  * [Windows](Windows.html)
  * [Develop for Windows](windows-develop.html)
  * Windows debugging

[](VisualStudioprojectgenerationWindows.html)

Visual Studio project generation for Windows

[](WindowsLowIntegrity.html)

Windows integrity control

# Windows debugging

Unity provides several options for debugging on Windows for forensic or live
debugging of game and Editor processes. Unity allows two types of debugging:
native C++ debugging and C# managed debugging.

  * Native Debugging stores symbols in Program Database (PDB) for the associated binary files, such as exe and dll.
  * On Windows, the standard .NET managed symbols are stored in PDB files with a .pdb extension.

## Symbols

You can use Unity’s [Symbol Store](http://symbolserver.unity3d.com/) for
accessing the Unity server URL in Windows Debugger (WinDbg), or Visual Studio
2019 and later for automatic symbol resolution and downloading.

### Windows Debugger (WinDbg)setup

To add a symbol store on WinDbg, use the `.sympath` command:

> `.sympath+ SRV*c:\symbols-cache*http://symbolserver.unity3d.com/`

Where:

> `.sympath+`  
>  The + addition, leaves the existing symbol path alone, and appends this
> symbol store lookup.
>
> `SRV*c:\symbols-cache`  
>  The SRV indicates a remote server to fetch from, while the `c:\symbols` is
> a local path to cache the downloaded symbols and to look there first before
> downloading again.
>
> `*http://symbolserver.unity3d.com/`  
>  The path to the symbol store to fetch from.

### Visual Studio setup

To configure Visual Studio for debugging, follow these steps: 1\. Go to
**Tools > Options**. 2\. Expand the **Debugging** section and then select
**Symbols**. 3\. Specify a cache directory if not already specified. 4\. Add a
**Symbol file (.pdb) location** , such as Unity’s [Symbol
Store](http://symbolserver.unity3d.com/).

## Live debugging

Live debugging is the scenario of attaching a debugger to a process that’s
already running, or to a process where an exception has been caught. For the
debugger to spot the issue, you must include the symbols in the build using
the steps described in the Visual Studio setup section. In addtion, if the
game executable has the same name as your game name, the debugger might have
issues finding the correct `.pdb` file, espectially if it doesn’t have access
to the renamed executable.

#### Setting up automatic exception debugging

On Windows, Microsoft automatically sets up application crashes to send to Dr
Watson/Error Reporting to Microsoft. However, if you have Visual Studio or
WinDbg installed, Microsoft provides an option to instead opt to [debug the
crashes](https://msdn.microsoft.com/en-
us/library/windows/desktop/bb204634\(v=vs.85\).aspx).

Follow this registry file contents to install:  
` Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug]
"Auto"="1" [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows
NT\CurrentVersion\AeDebug] "Auto"="1" `

Additional content for Editor debugging:

> `Unity.exe -dbgbreak`  
>  Will launch Unity and promptly offer a debugger to connect if the automatic
> crash handling is set up.

### Post-Mortem/Forensic debugging

Windows provides facilities to investigate crash dump files (.dmp or .mdmp).
Depending on the crash dump, you might either see stack information or the
entire process memory. The contents of the dump file determine the cause of
the crash, which typically has at least a stack to investigate (as long as
it’s a valid stack).

To investigate a dump file, you can load it up via Visual Studio or WinDbg.
While Visual Studio is easy to use, WinDbg provids additional features, which
makes it a preferred debugging tool.

### Debugging hints and tricks

When running Visual Studio, you can use the
[UnityMixedCallstack](https://github.com/Unity-
Technologies/UnityMixedCallstack) extension for VS Code by Unity that makes
debugging even easier.

#### Managed exceptions in native land

A `NullReferenceException` typically looks like this:

    
    
        1b45558c()  
    >   mono-2.0-bdwgc.dll!malloc(unsigned int size=12)  Line 163 + 0x5f bytes  C  
        mono-2.0-bdwgc.dll!g_hash_table_insert_replace(_GHashTable * hash=0x065c3960, void * key=0x0018cba4, void * value=0x0018cb8c, int replace=457528232)  Line 204 + 0x7 bytes  C  
        mono-2.0-bdwgc.dll!mono_jit_runtime_invoke(_MonoMethod * method=0x242bf8b0, void * obj=0x065c3960, void ** params=0x0018cba4, MonoObject * * exc=0x0018cb8c)  Line 4889 + 0xc bytes C  
    

#### Managed stack frames

Managed stack frames typically resemble this:

    
    
        1b45558c()  
    >   mono-2.0-bdwgc.dll!malloc(unsigned int size=12)  Line 163 + 0x5f bytes  C  
        mono-2.0-bdwgc.dll!g_hash_table_insert_replace(_GHashTable * hash=0x065c3960, void * key=0x0018cba4, void * value=0x0018cb8c, int replace=457528232)  Line 204 + 0x7 bytes  C  
        mono-2.0-bdwgc.dll!mono_jit_runtime_invoke(_MonoMethod * method=0x242bf8b0, void * obj=0x065c3960, void ** params=0x0018cba4, MonoObject * * exc=0x0018cb8c)  Line 4889 + 0xc bytes C  
    

The lines without any information are managed frames. You can get the managed
stack information in mono using its built-in function called `mono_pmip`,
which accepts the address of a stack frame and returns a char* with
information. You can invoke `mono_pmip` in the Visual Studio Immediate window
for debugging.

> `?(char*){,,mono-2.0-bdwgc.dll}mono_pmip((void*)0x1b45558c)`  
>  0x26a296c0 “ Tiles:OnPostRender () + 0x1e4 (1B4553A8 1B4555DC) [065C6BD0 -
> Unity Child Domain]”`

**Note:** This only works where `mono-2.0-bdwgc.dll` symbols are loaded
properly.

#### Force Applications to Create Dumps

Ocassionally, an application doesn’t crash despite having the debugger
attached, or it crashes on a remote device where the debugger isn’t available.
In such cases, you can get useful information from the dump file using the
following steps:

**Note:** These instructions apply to both **Windows Standalone** and
**Universal Windows** platforms when running on desktop.

  1. Open the Windows registry.
  2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting`.
  3. Create `LocalDumps` folder if it’s not there.
  4. Add following keys: 
     * `“DumpFolder”=&lt;FolderPath goes here> , e.g., C:\Temp`
     * `“DumpCount”=dword:00000010`
     * `“DumpType”=dword:00000002`
  5. Launch the application via the Universal Windows Platform or Windows Standalone executable.
  6. Reproduce the crash. The dump file is created in the folder you specified earlier. You can open the dump file with your preferred debugging tool, such as Visual Studio or WinDbg.

[](VisualStudioprojectgenerationWindows.html)

Visual Studio project generation for Windows

[](WindowsLowIntegrity.html)

Windows integrity control

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

