[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/unity-linker.html)
  * [中文](/cn/current/Manual/unity-linker.html)
  * [日本語](/ja/current/Manual/unity-linker.html)
  * [한국어](/kr/current/Manual/unity-linker.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/unity-linker.html)
  * [中文](/cn/current/Manual/unity-linker.html)
  * [日本語](/ja/current/Manual/unity-linker.html)
  * [한국어](/kr/current/Manual/unity-linker.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Managed code stripping](managed-code-stripping.html)
  * Managed code stripping and the Unity linker

[](managed-code-stripping.html)

Managed code stripping

[](managed-code-stripping-configure.html)

Configure managed code stripping

# Managed code stripping and the Unity linker

The Unity build process uses a tool called the Unity linker to strip managed
code. The Unity linker is a version of the [IL
Linker](https://github.com/mono/linker) customized to work with Unity. Custom
parts of the Unity linker specific to the Unity engine aren’t publicly
available.

The Unity linker is responsible for both managed code stripping and part of
the process of engine code stripping, which is a separate process available
through the **IL2CPP** A Unity-developed scripting back-end which you can use
as an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) scripting back end that removes unused
engine code. For more information, refer to
[`PlayerSettings.StripEngineCode`](../ScriptReference/PlayerSettings-
stripEngineCode.html).

## How the Unity linker strips assemblies

When you build a Unity project, the build process compiles your C# code to a
.NET bytecode format called Common Intermediate Language (CIL). Unity packages
this CIL bytecode into files called assemblies. The .NET framework libraries
and any C# libraries in the **plug-ins** A set of code created outside of
Unity that creates functionality in Unity. There are two kinds of plug-ins you
can use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) you use in your project are also pre-
packaged as assemblies of CIL bytecode.

For the purpose of managed code stripping, assemblies are categorized as
follows:

  * **.NET Class Library assemblies** : Includes the Mono class libraries such as `mscorlib.dll` and `System.dll`, as well as .NET class library facade assemblies like `netstandard.dll`.
  * **Platform SDK assemblies** : Includes the managed assemblies specific to a platform SDK. For example, the `windows.winmd` assembly that’s part of the Universal Windows Platform SDK.
  * **Unity Engine Module assemblies** : Includes the managed assemblies that make up the Unity Engine, such as `UnityEngine.Core.dll`.
  * **Project assemblies** : Includes the assemblies specific to a project such as: 
    * Script assemblies such as `Assembly-CSharp.dll`.
    * Precompiled assemblies.
    * [Assembly Definition Assemblies](https://docs.unity3d.com/Manual/assembly-definition-files.html).
    * Package assemblies.

In general, any assemblies in your project that don’t fall under one of these
categories are not processed by the Unity linker and are excluded from the
Player build .

During a build, the Unity linker processes all applicable types of assemblies
and does the following:

  1. Marks root types, methods, properties, and fields according to the [root marking rules](managed-code-stripping-marking-rules.html#root-marking-rules) applicable for the assembly type and configured code stripping level.
  2. Analyzes the roots it has marked to identify, and marks any managed code that these roots depend upon according to the applicable [dependency marking rules](managed-code-stripping-marking-rules.html#dependency-marking-rules).
  3. Deletes any remaining unmarked code from the assembly as unreachable by any execution path through your application code.

## Editing of method bodies

At the **High** [stripping level](managed-code-stripping-configure.html), the
Unity linker edits method bodies to further reduce code size. The Unity linker
only edits method bodies in the .NET Class Library assemblies.

The Unity linker can edit a method body in the following ways:

  * Remove unreachable branches: `if` statement blocks that check `System.Environment.OSVersion.Platform` and aren’t reachable for the currently targeted platform.
  * Inline methods that only access fields: replaces calls to methods that get or set a field with direct access to the field. This often makes it possible to strip away the method entirely. When you use the Mono scripting back end, the Unity linker only makes this change when the caller of the method is allowed to directly access the field, based on the field’s visibility. For IL2CPP, visibility rules don’t apply, so the Unity linker makes this change where appropriate.
  * Inline methods that only return a `const` value.
  * Remove calls to methods that are empty and have a `void` return type.
  * Remove `try-finally` blocks when the `finally` block is empty. Removing empty calls can create empty `finally` blocks. When that happens during method editing, the Unity linker removes the entire `try-finally` block. One scenario where this can occur is when the compiler generates `try-finally` blocks as part of `foreach` loops in order to call `Dispose`.

**Note** : After editing method bodies, the source code of the assembly no
longer matches the compiled code in the assembly, which can make debugging
more difficult.

## Additional resources

  * [Preserving code using annotations](managed-code-stripping-preserving.html)
  * [Marking rules reference](managed-code-stripping-marking-rules.html)

[](managed-code-stripping.html)

Managed code stripping

[](managed-code-stripping-configure.html)

Configure managed code stripping

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

