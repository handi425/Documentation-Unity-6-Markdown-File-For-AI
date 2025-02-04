[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AssemblyDefinitionImporter.html)
  * [中文](/cn/current/Manual/class-AssemblyDefinitionImporter.html)
  * [日本語](/ja/current/Manual/class-AssemblyDefinitionImporter.html)
  * [한국어](/kr/current/Manual/class-AssemblyDefinitionImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AssemblyDefinitionImporter.html)
  * [中文](/cn/current/Manual/class-AssemblyDefinitionImporter.html)
  * [日本語](/ja/current/Manual/class-AssemblyDefinitionImporter.html)
  * [한국어](/kr/current/Manual/class-AssemblyDefinitionImporter.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Assembly Definition properties reference

[](assembly-definition-metadata.html)

Assembly metadata and compilation details

[](class-AssemblyDefinitionReferenceImporter.html)

Assembly Definition Reference properties reference

# Assembly Definition properties reference

Click on an Assembly Definition Asset to set the properties for an assembly in
the **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

Assembly Definition properties are divided into the following sections:

  * Name and General
  * Define Constraints
  * Assembly Definition References
  * Assembly References
  * Platforms
  * Version Defines

## Name and General

![](../uploads/Main/name-and-general.png) **Property:** | **Description:**  
---|---  
**Name** | The name for the assembly (without a file extension). Assembly names must be unique across the Project. Consider using a reverse-DNS naming style to reduce the chance of name conflicts, especially if you want to use the assembly in more than one Project.  
  
**Note** : Unity uses the name you assign to the Assembly Definition asset as
the default value of the Name field, but you can change the name as needed.
However, if you reference an Assembly Definition by its name rather than its
GUID, changing the name will break the reference.  
**Allow ‘unsafe’ Code** | Enable the Allow ‘unsafe’ Code option if you have used the C# `unsafe` keyword in a script within the assembly. When you enable this setting, Unity passes the /unsafe option to the C# compiler when it compiles the assembly.  
**Auto Referenced** | Specify whether the predefined assemblies should reference this Project assembly. When you disable the Auto Reference option, Unity does not automatically reference the assembly during compilation. This has no effect on whether Unity includes it in the build.  
**No Engine References** | When you enable this property, Unity does not add references to UnityEditor or UnityEngine when it compiles the assembly.  
**Override References** | Enable the Override References setting to manually specify which precompiled assemblies this assembly depends upon. When you enable Override References, the Inspector shows the Assembly References section, which you can use to specify the references.  
  
A precompiled assembly is a library compiled outside your Unity Project. By
default, assemblies you define in your Project reference all the precompiled
assemblies you add to the Project, which matches how the predefined assemblies
reference all precompiled assemblies. When you enable Override References,
this assembly only references the precompiled assemblies you add under
Assembly References.  
  
**Note** : To prevent Project assemblies from automatically referencing a
precompiled assembly, you can disable its Auto Referenced option. See Plugin
Inspector for more information.  
**Root Namespace** | The default namespace for ****scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts)** in this assembly definition. If you
use either [Rider] or [Visual Studio] as your code editor, they automatically
add this namespace to any new scripts you create in this assembly definition.  
  
For more information, refer to [Creating an Assembly Definition
asset](assembly-definitions-creating.html#create-asmdef).

## Define Constraints

![](../uploads/Main/define-constraints.png)

Define constraints specify the compiler #define directives that must be
defined for Unity to compile or reference an assembly.

Unity only compiles and references a Project assembly if all of the Define
Constraints are satisfied. Constraints work like the #if preprocessor
directive in C#, but on the assembly level instead of the script level. Define
all the symbols in the Define Constraints setting for the constraints to be
satisfied.

To specify that a symbol must be undefined, prefix it with a negating ! (bang)
symbol. For example, if you specify the following symbols as the Define
Constraints:

  * `!ENABLE_IL2CPP`
  * `UNITY_2018_3_OR_NEWER`

The constraints are satisfied when the symbol `ENABLE_IL2CPP` is not defined
and the symbol `UNITY_2018_3_OR_NEWER` is defined. The result is that Unity
only compiles and references this assembly on non-IL2CPP scripting runtimes
for Unity 2018.3 or newer.

You can use the || (OR) operator to specify that at least one of the
constraints must be present in order for the constraints to be satisfied. For
example:

  * `UNITY_IOS || UNITY_EDITOR_OSX`
  * `UNITY_2019_3_OR_NEWER`
  * `!UNITY_ANDROID`

The constraints are satisfied when either `UNITY_IOS` or `UNITY_EDITOR_OSX`
and `UNITY_2019_3_OR_NEWER` are defined and `UNITY_ANDROID` is not defined.
Individual lines are analogous to performing a logical AND operation between
the constraints in them. The above example is equivalent to:

`(UNITY_IOS OR UNITY_EDITOR_OSX) AND (UNITY_2019_3_OR_NEWER) AND (NOT
UNITY_ANDROID)`

You can use any of Unity’s built-in #define directives, symbols defined in a
global compiler response (.rsp) file, and any symbols defined in the Project’s
Scripting Define Symbols Player setting. For more information, refer to
[Platform dependent compilation](platform-dependent-compilation.html),
including a list of the built-in symbols.

**Note** : The Scripting Define Symbols settings are platform-specific. If you
use this setting to define whether Unity should use an assembly, make sure
that you define the necessary symbols on all the relevant platforms.

For more information, refer to [Conditionally including an assembly](assembly-
definition-includes.html).

### Invalid or incompatible constraints

Unity marks each constraint with an indicator based on the currently defined
settings (for example, the following set of three constraints indicates that
the first symbol is currently defined while the other two are not). Since each
individual constraint must be true for the overall constraint to be satisfied,
the Editor marks the entire Define Constraints section as currently
incompatible or invalid.

![Invalid or incompatible constraints are flagged.](../uploads/Main/invalid-
constraints.png) Invalid or incompatible constraints are flagged.

To satisfy the constraints in this example, you could change the ****Scripting
Backend** A framework that powers scripting in Unity. Unity supports three
different scripting backends depending on target platform: Mono, .NET and
IL2CPP. Universal Windows Platform, however, supports only two: .NET and
IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend)** to ****IL2CPP** A Unity-
developed scripting back-end which you can use as an alternative to Mono when
building projects for some platforms. [More info](./scripting-backends-
il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP)** for the second constraint (in
**Player Settings**) and remove the invalid characters from the third
constraint. However, what often matters is how the constraints are evaluated
when you build the project, not how the constraints appear in the Unity Editor
(for example, you might have an assembly that you only want to include in
builds that use the IL2CPP backend, but not on other builds that use the Mono
backend).

## Assembly Definition References

![](../uploads/Main/assembly-definition-ref.png) **Property:** | **Description:**  
---|---  
**Assembly Definition References** | Specify references to other assemblies that you have created using Assembly Definition assets. Unity uses these references to compile the assembly and also define the **dependencies** between assemblies.  
**Use GUIDs** | This setting controls how Unity serializes references to other Assembly Definition assets. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definition files that reference it.  
  
For more information, refer to [Creating an Assembly Definition
asset](assembly-definitions-creating.html#create-asmdef).

## Assembly References

![](../uploads/Main/assembly-ref.png)

The Assembly References section only appears when you enable the **Override
References** property (in the [General] section). Use this area to specify any
references to precompiled assemblies on which this assembly depends.

For more information, refer to [Referencing a precompiled, plugin
assembly](assembly-definitions-referencing.html#reference-precompiled-
assembly).

## Platforms

![](../uploads/Main/platforms.png)

Set the platform compatibility of the assembly. Unity only compiles or
references this assembly on the included (or not excluded) platforms.

For more information, refer to [Creating a platform-specific
assembly](assembly-definitions-creating.html#create-platform-specific).

## Version Defines

![](../uploads/Main/version-defines.png)

Specify which symbols to define according to the versions of the packages and
modules in a project.

**Property:** | **Description:**  
---|---  
**Resource** | A package or module  
**Define** | The symbol to define when an applicable version of the Resource is also present in this Unity Project.  
**Expression** | An expression defining a version or range of versions. For more information, refer to Version Defines.  
**Expression outcome** | The Expression evaluated as a logical statement, where “x” is the version checked. If the Expression outcome says, Invalid, then the Expression is malformed.  
  
For more information, refer to [Defining symbols based on project
packages](assembly-definition-includes.html#define-symbols).

## Additional resources

  * [Creating assembly definitions](assembly-definitions-creating.html)
  * [Referencing assemblies](assembly-definitions-referencing.html)
  * [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](assembly-definition-file-format.html)

[](assembly-definition-metadata.html)

Assembly metadata and compilation details

[](class-AssemblyDefinitionReferenceImporter.html)

Assembly Definition Reference properties reference

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

