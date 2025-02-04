[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/csharp-compiler.html)
  * [中文](/cn/current/Manual/csharp-compiler.html)
  * [日本語](/ja/current/Manual/csharp-compiler.html)
  * [한국어](/kr/current/Manual/csharp-compiler.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/csharp-compiler.html)
  * [中文](/cn/current/Manual/csharp-compiler.html)
  * [日本語](/ja/current/Manual/csharp-compiler.html)
  * [한국어](/kr/current/Manual/csharp-compiler.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * C# compiler

[](dotnet-profile-assemblies.html)

Referencing additional class library assemblies

[](dotnet-reflection-overhead.html)

C# reflection overhead

# C# compiler

To compile C# source code in a Unity Project, the Unity Editor uses a C#
compiler.

**C# compiler** | **C# language version**  
---|---  
[Roslyn](https://github.com/dotnet/roslyn) | [C# 9.0](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9)  
  
The Editor passes a default set of options to the C# compiler. To pass
additional options in your project, see the documentation on [Platform
Dependent Compilation](platform-dependent-compilation.html).

## Unsupported features

### C# 9.0

  * Suppress emitting localsinit flag
  * Covariant return types
  * Module Initializers
  * Extensible calling conventions for unmanaged function pointers
  * Init only setters

If you try to use unsupported features in your project, compilation generates
errors.

### Record support

C# 9 init and record support comes with a few caveats.

  * The type `System.Runtime.CompilerServices.IsExternalInit` is required for full record support as it uses init only setters, but is only available in .NET 5 and later (which Unity doesn’t support). Users can work around this issue by declaring the `System.Runtime.CompilerServices.IsExternalInit` type in their own projects.
  * You shouldn’t use C# records in serialized types because Unity’s serialization system doesn’t support C# records.

### Unmanaged function pointer support

Unity supports unmanaged functions pointers as introduced in C# 9, but it
doesn’t support extensible calling conventions. The following example code
provides more detailed information about how to correctly use unmanaged
function pointers.

The following example targets Windows platforms and requires the **Allow
‘unsafe’ code** to be enabled in the [Player Settings](class-
PlayerSettings.html)Settings that let you set various player-specific options
for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings) menu. For more information
about C#’s `unsafe` context, see [Microsoft’s unsafe (C# Reference)
documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-
reference/keywords/unsafe) or [Microsoft’s Unsafe code, pointer types, and
function pointers documentation](https://docs.microsoft.com/en-
us/dotnet/csharp/language-reference/unsafe-code).

    
    
    using System;
    using System.Runtime.InteropServices;
    using UnityEngine;
    
    public class UnmanagedFunctionPointers : MonoBehaviour
    {
      [DllImport("kernel32.dll")]
      static extern IntPtr LoadLibrary(string lpLibFileName);
      
      [DllImport("kernel32.dll")]
      static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);
      
      // You must enable "Allow 'unsafe' code" in the Player Settings
      unsafe void Start()
      {
    #if UNITY_EDITOR_WIN || UNITY_STANDALONE_WIN
        // This example is only valid on Windows
        
        // Get a pointer to an unmanaged function
        IntPtr kernel32 = LoadLibrary("kernel32.dll");
        IntPtr getCurrentThreadId = GetProcAddress(kernel32, "GetCurrentThreadId");
    
        // The unmanaged calling convention
        delegate* unmanaged[Stdcall]<UInt32> getCurrentThreadIdUnmanagedStdcall = (delegate* unmanaged[Stdcall]<UInt32>)getCurrentThreadId;
        Debug.Log(getCurrentThreadIdUnmanagedStdcall());
    #endif
      }
    }
    
    
    

## Additional resources

  * [.NET Profile Support](dotnet-profile-support.html).
  * [Platform dependent compilation](platform-dependent-compilation.html).

[](dotnet-profile-assemblies.html)

Referencing additional class library assemblies

[](dotnet-reflection-overhead.html)

C# reflection overhead

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

