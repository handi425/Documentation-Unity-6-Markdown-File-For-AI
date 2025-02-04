[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/assembly-definitions-referencing.html)
  * [中文](/cn/current/Manual/assembly-definitions-referencing.html)
  * [日本語](/ja/current/Manual/assembly-definitions-referencing.html)
  * [한국어](/kr/current/Manual/assembly-definitions-referencing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/assembly-definitions-referencing.html)
  * [中文](/cn/current/Manual/assembly-definitions-referencing.html)
  * [日本語](/ja/current/Manual/assembly-definitions-referencing.html)
  * [한국어](/kr/current/Manual/assembly-definitions-referencing.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Referencing assemblies

[](assembly-definitions-creating.html)

Creating assembly assets

[](assembly-definition-includes.html)

Conditionally including assemblies

# Referencing assemblies

Any assembly that contains types (such as classes or structs) that depend on
types in another assembly must have a reference to the other assembly. You can
control the references between assemblies by configuring Assembly Definition
properties in the Inspector window. For more information, refer to [Assembly
definition properties reference](class-AssemblyDefinitionImporter.html).

## Automatic references

By default, the predefined assemblies reference all other assemblies,
including those created with Assembly Definitions (1) and precompiled
assemblies added to the project as plugins (2). Custom assemblies you create
with an Assembly Definition asset automatically reference all precompiled
assemblies (3):

![](../uploads/Main/AssemblyDependencies.png)

In the default setup, classes in the predefined assemblies can use all types
defined by any other assemblies in the project. Likewise, assemblies you
create with an Assembly Definition asset can use all types defined in any
precompiled (plug-in) assemblies.

### Turn off automatic references

To prevent a custom assembly being automatically referenced by the predefined
assemblies, deselect the Assembly Definition’s **Auto Referenced**
[property](class-AssemblyDefinitionImporter.html) in the Inspector. This means
the predefined assemblies don’t recompile when you change code in the assembly
but also means the predefined assemblies can’t use code in this assembly
directly.

To prevent a plugin assembly from being automatically referenced by either
predefined or custom assemblies, deselect the **Auto Referenced** property in
the [Plugin Inspector](plug-in-inspector.html) for a plugin asset. You can
still add an explicit reference to the **plug-in** A set of code created
outside of Unity that creates functionality in Unity. There are two kinds of
plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies
created with tools like Visual Studio) and Native plug-ins (platform-specific
native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) from a custom assembly, refer to
Referencing a precompiled plug-in assembly.

## Referencing rules and limitations

Unity doesn’t allow the following types of references:

  * References from custom assemblies created with an Assembly Definition to the predefined assemblies.
  * Explicit references from the predefined assemblies. The predefined assemblies can only use code in auto-referenced assemblies.
  * Cyclical references, which is when two assemblies reference each other. If you encounter a cyclical reference error, you must refactor your code to remove the cyclical reference or put the mutually referencing classes in the same assembly.

## Adding a reference to another assembly

To use code from another assembly, you must add a reference to the other
assembly in the Assembly Definition asset.

To add a reference to another assembly:

  1. Select the Assembly Definition for the assembly that requires the reference to view its properties in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

  2. In the **Assembly Definition References** section, click the **+** button to add a new reference.

![](../uploads/Main/asmdef-4.png)

  3. Assign the Assembly Definition asset to the newly created slot in the list of references.

Enabling the **Use GUIDs** option allows you to change the filename of the
referenced Assembly Definition asset without updating references in other
Assembly Definitions to reflect the new name.

**Note:** GUIDs must be reset if the metadata files for the asset files are
deleted or you move the files outside the Unity Editor without also moving the
metadata files along with them.

## Adding a reference to a precompiled plug-in assembly

By default, all custom assemblies you create with Assembly Definitions
automatically reference all precompiled assemblies. This means Unity
recompiles all your assemblies when you update any one of the precompiled
assemblies, even if the code in the assembly is not used.

To avoid this extra overhead, you can override the automatic references and
specify references to only those precompiled libraries the assembly actually
uses:

  1. Select the Assembly Definition for the assembly that requires the reference to view its properties in the **Inspector**.

  2. In the **General** section, enable the **Override References** option.

![](../uploads/Main/asmdef-5.png)

The **Assembly References** section of the **Inspector** becomes available
when **Override References** is checked.

  3. In the **Assembly References** section, click the **+** button to add a new reference.

  4. Use the drop-down list in the empty slot to assign a reference to a precompiled assembly. The list shows all the precompiled assemblies in the project for the currently active platform in [Build Profiles](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
See in [Glossary](Glossary.html#Buildprofile). (Set the platform compatibility
for a precompiled assembly in the [Plugin Inspector].)

![](../uploads/Main/asmdef-6.png)

  5. Click **Apply**.

  6. Repeat for each platform for which you build your project.

## Additional resources

  * [Creating assembly definitions](assembly-definitions-creating.html)
  * [Conditionally including assemblies](assembly-definition-includes.html)

[](assembly-definitions-creating.html)

Creating assembly assets

[](assembly-definition-includes.html)

Conditionally including assemblies

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

