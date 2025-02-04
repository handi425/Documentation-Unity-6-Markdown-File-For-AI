[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dotnet-profile-assemblies.html)
  * [中文](/cn/current/Manual/dotnet-profile-assemblies.html)
  * [日本語](/ja/current/Manual/dotnet-profile-assemblies.html)
  * [한국어](/kr/current/Manual/dotnet-profile-assemblies.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dotnet-profile-assemblies.html)
  * [中文](/cn/current/Manual/dotnet-profile-assemblies.html)
  * [日本語](/ja/current/Manual/dotnet-profile-assemblies.html)
  * [한국어](/kr/current/Manual/dotnet-profile-assemblies.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * Referencing additional class library assemblies

[](dotnet-third-party-libraries.html)

Third-party .NET libraries

[](csharp-compiler.html)

C# compiler

# Referencing additional class library assemblies

If your Unity project uses a part of the .NET class library API that Unity
doesn’t compile by default, you can provide the C# compiler with a list of
additional assemblies to reference during compilation. The behavior depends on
which .NET profile the project uses. For more information, see [.NET Profile
support](dotnet-profile-support.html).

## .NET Standard profile

If your project uses the .NET Standard profile, all parts of the .NET class
library API are referenced by default. You can’t reference additional
assemblies. If part of the API seems to be missing, it might not be included
with .NET Standard. Try using the .NET Framework profile instead. To avoid
compilation problems when you change profiles, see Switching between profiles.

## .NET Framework profile

By default, Unity references the following assemblies when you use the .NET
Framework profile:

  * mscorlib.dll
  * System.dll
  * System.Core.dll
  * System.Runtime.Serialization.dll
  * System.Xml.dll
  * System.Xml.Linq.dll

To reference any other class library assemblies, use a csc.rsp file: a
response file that contains a list of command line arguments that you can pass
to the C# compiler. To use a csc.rsp file, follow the below instructions:

  1. Create a file named csc.rsp in the `Assets` folder of your Unity project.
  2. Move any assembly files you want to reference into the `Assets` folder of your project, if they aren’t already in this folder.
  3. Populate the csc.rsp file with command line arguments for the assemblies you want to reference.

For example, if your project uses the `HttpClient` class, which is defined in
the `System.Net.Http.dll` assembly, the C# compiler might produce this initial
error message if the assembly isn’t present:

    
    
    The type `HttpClient` is defined in an assembly that is not referenced. You must add a reference to assembly 'System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a'.
    
    

To resolve this error, add a csc.rsp file that contains the following command
line argument to the project:

    
    
    -r:System.Net.Http.dll
    
    

Add a new line with the appropriate command line argument for each assembly
you want to reference.

## Switching between profiles

When you use a csc.rsp file to reference class library assemblies and you
change the .NET profile, you might experience compilation problems.

If you change the .NET profile from .NET Framework to .NET Standard and your
csc.rsp file references an assembly that doesn’t exist in the .NET Standard
profile, then compilation fails. To solve the issue, edit the csc.rsp file to
remove any references to assemblies that are exclusive to the .NET Framework
profile before you change the .NET profile to .NET Standard.

## Additional resources

  * [.NET Profile Support](dotnet-profile-support.html).
  * [.NET System libraries](dotnet-system-libraries.html).
  * [Third-party .NET libraries](dotnet-third-party-libraries.html).

[](dotnet-third-party-libraries.html)

Third-party .NET libraries

[](csharp-compiler.html)

C# compiler

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

