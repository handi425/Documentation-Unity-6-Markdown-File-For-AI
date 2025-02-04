[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dotnet-profile-support.html)
  * [中文](/cn/current/Manual/dotnet-profile-support.html)
  * [日本語](/ja/current/Manual/dotnet-profile-support.html)
  * [한국어](/kr/current/Manual/dotnet-profile-support.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dotnet-profile-support.html)
  * [中文](/cn/current/Manual/dotnet-profile-support.html)
  * [日本語](/ja/current/Manual/dotnet-profile-support.html)
  * [한국어](/kr/current/Manual/dotnet-profile-support.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * .NET profile support

[](overview-of-dot-net-in-unity.html)

Unity .NET features

[](dotnet-system-libraries.html)

.NET system libraries

# .NET profile support

Unity supports two .NET profiles: **.NET Standard** and **.NET Framework**.
Each profile provides a different set of APIs so that C# code can interact
with .NET class libraries. The **Api Compatibility Level** property has two
settings:

  * **.NET Standard 2.1** : .NET Standard 2.1, as published by the .NET Foundation.
  * **.NET Framework** : .NET Framework 4.8, as published by Microsoft, plus additional APIs in .NET Standard 2.1.

By default, the **Api compatibility Level** is set to **.NET Standard 2.1**.
To change the .NET profile, go to **Edit** > **Project Settings** > **Player**
>**Other settings**. Under the Configuration heading, set **Api Compatibility
Level** to the desired setting.

## Cross-platform compatibility

If you need broad cross-platform compatibility, then set the **Api
Compatibility Level** to **.NET Standard 2.1**. Where possible, Unity supports
the APIs in the **.NET Standard 2.1** profile on all platforms. Although some
platforms don’t fully support the **.NET Standard 2.1** profile, the **.NET
Framework** profile is less suitable for cross-platform compatibility. The
**.NET Framework** profile includes all APIs in the **.NET Standard 2.1**
profile and additional APIs, some of which might work on few or no platforms.

## Managed plug-ins

[Managed plug-ins](plug-ins-managed.html)A managed .NET assembly that is
created with tools like Visual Studio for use in Unity. [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Managedplug-in) are .NET assemblies that are
managed outside of Unity and compiled into dynamically linked libraries
(DLLs). You can use managed **plug-ins** A set of code created outside of
Unity that creates functionality in Unity. There are two kinds of plug-ins you
can use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) in Unity with either the **.NET
Standard 2.1** profile or the **.NET Framework** profile. The .NET profile of
your Unity project determines the level of support for managed plug-ins that
are compiled for different versions of .NET. The following table indicates the
configurations that Unity supports:

Managed plug-in compilation target | API Compatibility Level:  
---|---  
| **.NET Standard 2.1** | **.NET Framework 4.x**  
**.NET Standard (any version)** | Supported | Supported  
**.NET Framework (any version)** | Limited support | Supported  
**.NET Core (any version)** | Not Supported | Not Supported  
  
Support for managed plug-ins compiled for .NET Framework is limited when you
use the **.NET Standard 2.1** profile in Unity. Any .NET Framework APIs that
are also present in .NET Standard are supported. However, the **.NET
Framework** API contains types and methods that are not available in the
**.NET Standard 2.1** profile.

## Transport Layer Security (TLS) 1.2

The UnityWebRequest API and all .NET Framework Web APIs fully support TLS 1.2
on all platforms except Web. The Web platform uses the security settings from
the browser the application runs in and the web server instead. The platform-
specific local certificate store automatically verifies TLS certificates if
available. If access to the certificate store isn’t possible, Unity uses an
embedded root certificate store.

## Additional resources

  * [.NET System libraries](dotnet-system-libraries.html).
  * [Third-party .NET libraries](dotnet-third-party-libraries.html).

[](overview-of-dot-net-in-unity.html)

Unity .NET features

[](dotnet-system-libraries.html)

.NET system libraries

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

