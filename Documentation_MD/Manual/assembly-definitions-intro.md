[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/assembly-definitions-intro.html)
  * [中文](/cn/current/Manual/assembly-definitions-intro.html)
  * [日本語](/ja/current/Manual/assembly-definitions-intro.html)
  * [한국어](/kr/current/Manual/assembly-definitions-intro.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/assembly-definitions-intro.html)
  * [中文](/cn/current/Manual/assembly-definitions-intro.html)
  * [日本語](/ja/current/Manual/assembly-definitions-intro.html)
  * [한국어](/kr/current/Manual/assembly-definitions-intro.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Introduction to assemblies in Unity

[](assembly-definition-files.html)

Organizing scripts into assemblies

[](assembly-definitions-creating.html)

Creating assembly assets

# Introduction to assemblies in Unity

Unity provides two special asset types, Assembly Definitions and Assembly
References, to help organize your **scripts** A piece of code that allows you
to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) into assemblies.

An assembly is a C# code library that contains the compiled classes and
structs that are defined by your scripts and which also define references to
other assemblies. Refer to [Assemblies in
.NET](https://learn.microsoft.com/en-us/dotnet/standard/assembly/) for more
information about assemblies in C#.

By default, Unity compiles almost all of your game scripts into a predefined
assembly called `Assembly-CSharp.dll`. Unity also creates a [few smaller,
specialized predefined assemblies](script-compile-order-folders.html).

This arrangement works acceptably for small projects, but has some drawbacks
as you add more code to your project:

  * Every time you change one script, Unity has to recompile all the other scripts, increasing overall compilation time for iterative code changes.
  * Any script can directly access types defined in any other script, which can make it more difficult to refactor and improve your code.
  * All scripts are compiled for all platforms.

By defining assemblies, you can organize your code to promote modularity and
reusability. Scripts in assemblies you define are no longer added to the
default assemblies and can only access scripts in your other custom
assemblies.

![](../uploads/Main/ScriptCompilation.png)

The above diagram illustrates how you might split up the code in your project
into multiple assemblies. Because _Main_ references _Stuff_ and not the other
way around, you know that any changes to the code in _Main_ cannot affect the
code in _Stuff_. Similarly, because _Library_ doesn’t depend on any other
assemblies, you can more easily reuse the code in _Library_ in another
project.

## Defining assemblies

To organize your project code into assemblies, create a folder for each
desired assembly and move the scripts that should belong to each assembly into
the relevant folder. Then [create Assembly Definition assets](assembly-
definitions-creating.html) to specify the assembly properties.

Unity compiles all the scripts in a folder that contains an Assembly
Definition into a single assembly, using the name and other settings defined
by the asset. The assembly includes any scripts in subfolders unless a
subfolder has its own Assembly Definition or Assembly Reference asset.

To include scripts from a non-child folder in an existing assembly, create an
Assembly Reference asset in the non-child folder and set it to reference the
Assembly Definition asset that defines the target assembly. For example, you
can combine the scripts from all the Editor folders in your project in their
own assembly, no matter where those folders are located.

Unity compiles assemblies in an order determined by their dependencies. You
can’t specify the order in which compilation takes place.

## Finding which assembly a script belongs to

To identify which assembly a script belongs to, select the script file in the
**Project** window to view its properties in the ****Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window. The assembly filename and
the Assembly Definition, if one exists, are shown in the **Assembly
Information** section of the **Inspector**.

## Editor folder

Unity normally compiles any scripts in folders named `Editor` into the
predefined `Assembly-CSharp-Editor` assembly no matter where those scripts are
located. However, if you create an Assembly Definition asset in a folder that
has an Editor folder underneath it, Unity no longer puts those Editor scripts
into the predefined Editor assembly. Instead, they go into the new assembly
created by your Assembly Definition — where they might not belong. To manage
`Editor` folders, you can create Assembly Definition or Reference assets in
each `Editor` folder to place those scripts in one or more Editor assemblies.
For more information, refer to [Creating an assembly for Editor
code](assembly-definitions-creating.html#create-editor-assembly).

## Additional resources

  * [Creating assembly definitions](assembly-definitions-creating.html)
  * [Referencing assemblies](assembly-definitions-referencing.html)
  * [Assembly metadata and compilation details](assembly-definition-metadata.html)
  * [Assembly Definition properties](class-AssemblyDefinitionImporter.html)
  * [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](assembly-definition-file-format.html)

[](assembly-definition-files.html)

Organizing scripts into assemblies

[](assembly-definitions-creating.html)

Creating assembly assets

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

