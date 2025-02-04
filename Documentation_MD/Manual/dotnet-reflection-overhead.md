[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dotnet-reflection-overhead.html)
  * [中文](/cn/current/Manual/dotnet-reflection-overhead.html)
  * [日本語](/ja/current/Manual/dotnet-reflection-overhead.html)
  * [한국어](/kr/current/Manual/dotnet-reflection-overhead.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dotnet-reflection-overhead.html)
  * [中文](/cn/current/Manual/dotnet-reflection-overhead.html)
  * [日本語](/ja/current/Manual/dotnet-reflection-overhead.html)
  * [한국어](/kr/current/Manual/dotnet-reflection-overhead.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * C# reflection overhead

[](csharp-compiler.html)

C# compiler

[](dotnet-garbage-collection.html)

Garbage collection

# C# reflection overhead

Mono and **IL2CPP** A Unity-developed scripting back-end which you can use as
an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) internally cache all C# reflection
(`System.Reflection`) objects and by design, Unity doesn’t garbage collect
them. The result of this behavior is that the garbage collector continuously
scans the cached C# reflection objects during the lifetime of your
application, which causes unnecessary and potentially significant garbage
collector overhead.

To minimize the garbage collector overhead, avoid methods such as
[Assembly.GetTypes](https://docs.microsoft.com/en-
us/dotnet/api/system.reflection.assembly.gettypes) and
[Type.GetMethods()](https://docs.microsoft.com/en-
us/dotnet/api/system.type.getmethods) in your application, which create a lot
of C# reflection objects at runtime. Instead, you should scan assemblies in
the Unity Editor for the required data and serialize and/or codegen it for use
at runtime.

## Additional resources

  * [.NET Profile Support](dotnet-profile-support.html).
  * [C# compiler](csharp-compiler.html).
  * [Garbage collector overview](performance-garbage-collector.html).

[](csharp-compiler.html)

C# compiler

[](dotnet-garbage-collection.html)

Garbage collection

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

