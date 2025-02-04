[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/dotnet-garbage-collection.html)
  * [中文](/cn/current/Manual/dotnet-garbage-collection.html)
  * [日本語](/ja/current/Manual/dotnet-garbage-collection.html)
  * [한국어](/kr/current/Manual/dotnet-garbage-collection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/dotnet-garbage-collection.html)
  * [中文](/cn/current/Manual/dotnet-garbage-collection.html)
  * [日本語](/ja/current/Manual/dotnet-garbage-collection.html)
  * [한국어](/kr/current/Manual/dotnet-garbage-collection.html)

  * [Scripting](scripting.html)
  * [Environment and tools](environment-and-tools.html)
  * [Unity .NET features](overview-of-dot-net-in-unity.html)
  * Garbage collection

[](dotnet-reflection-overhead.html)

C# reflection overhead

[](object-oriented-development.html)

Object-oriented development

# Garbage collection

Unity uses the [Boehm garbage
collector](https://en.wikipedia.org/wiki/Boehm_garbage_collector) for both the
Mono and **IL2CPP** A Unity-developed scripting back-end which you can use as
an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) backends. Unity uses the
**Incremental** mode by default. You can disable the **Incremental** mode to
use stop-the-world garbage collection but the recommended best practice is to
use **Incremental** mode.

To toggle between Incremental mode and stop-the-world, go to **Edit** >
**Project Settings** > **Player** , open the **Other Settings** panel and
click on the **Use incremental GC** checkbox. In **Incremental** mode, Unity’s
garbage collector only runs for a limited period of time and doesn’t
necessarily collect all objects in one pass. This spreads the time it takes to
collect objects over multiple frames and reduces stuttering and CPU spikes.
For more information, refer to [Managed memory](performance-managed-
memory.html).

To check the number of allocations and possible CPU spikes in your
application, use the [Unity Profiler](Profiler.html). You can also use the
[GarbageCollector](../ScriptReference/Scripting.GarbageCollector.html) API to
completely disable garbage collection in Players. When the collector is
disabled, be careful to avoid allocating excess memory.

## Additional resources

  * [.NET Profile Support](dotnet-profile-support.html).
  * [Garbage collector overview](performance-garbage-collector.html).

[](dotnet-reflection-overhead.html)

C# reflection overhead

[](object-oriented-development.html)

Object-oriented development

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

