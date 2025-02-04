[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dotnet-third-party-libraries.html)
  * [中文](/cn/current/Manual/dotnet-third-party-libraries.html)
  * [日本語](/ja/current/Manual/dotnet-third-party-libraries.html)
  * [한국어](/kr/current/Manual/dotnet-third-party-libraries.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dotnet-third-party-libraries.html)
  * [中文](/cn/current/Manual/dotnet-third-party-libraries.html)
  * [日本語](/ja/current/Manual/dotnet-third-party-libraries.html)
  * [한국어](/kr/current/Manual/dotnet-third-party-libraries.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * Third-party .NET libraries

[](dotnet-system-libraries.html)

.NET system libraries

[](dotnet-profile-assemblies.html)

Referencing additional class library assemblies

## Third-party .NET libraries

You should only use third-party .NET libraries that have been extensively
tested on a wide range of Unity configurations and platforms.

The performance characteristics of just-in-time (JIT) and ahead-of-time (AOT)
code paths in third-party libraries might be significantly different. AOT
generally reduces startup times and is suited to larger applications for this
reason but increases the binary file size to accommodate the compiled code.
AOT also takes longer to build during development.

JIT adjusts at runtime based on the platform it’s running on, which can
increase running performance at the cost of a potentially longer application
startup time. As such, you should profile your application in both the Editor,
and on your target platform. For more information, see [Profiler
overview](Profiler.html).

You should profile the usage of your .NET system libraries on all target
platforms because their performance characteristics might vary depending on
the **scripting backends** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend), .NET versions, and profiles
you use.

When you review a third-party library, consider the following areas:

  * Compatibility: Third-party libraries might not be compatible with some Unity platforms and scripting backends.
  * Performance: Third-party libraries might have vastly different performance characteristics in Unity compared to other .NET runtimes.
  * AOT binary size: Third-party libraries might increase AOT binary size significantly because of the number of dependencies the library uses.

## Additional resources

  * [.NET Profile Support](dotnet-profile-support.html).
  * [.NET System libraries](dotnet-system-libraries.html).
  * [Referencing additional class library assemblies](dotnet-profile-assemblies.html).

[](dotnet-system-libraries.html)

.NET system libraries

[](dotnet-profile-assemblies.html)

Referencing additional class library assemblies

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

