[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/assembly-definitions-creating.html)
  * [中文](/cn/current/Manual/assembly-definitions-creating.html)
  * [日本語](/ja/current/Manual/assembly-definitions-creating.html)
  * [한국어](/kr/current/Manual/assembly-definitions-creating.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/assembly-definitions-creating.html)
  * [中文](/cn/current/Manual/assembly-definitions-creating.html)
  * [日本語](/ja/current/Manual/assembly-definitions-creating.html)
  * [한국어](/kr/current/Manual/assembly-definitions-creating.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Creating assembly assets

[](assembly-definitions-intro.html)

Introduction to assemblies in Unity

[](assembly-definitions-referencing.html)

Referencing assemblies

# Creating assembly assets

The Assembly Definition (`.asmdef`) asset allows you to define a new assembly
by placing it in the root of a folder containing **scripts** A piece of code
that allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

The Assembly Definition Reference (`.asmref`) asset allows you to explicitly
include a set of script files into a preexisting assembly.

## Creating an Assembly Definition asset

To create an Assembly Definition asset:

  1. In the **Project** window, locate the folder containing the scripts you want to include in the assembly.
  2. Create an Assembly Definition asset in the folder (menu: **Assets** > **Create** > **Scripting** > **Assembly Definition**).
  3. Assign a name to the asset. By default, the assembly file uses the name you assign to the asset, but you can change the name in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window.

Unity recompiles the scripts in the project to create the new assembly. You
can then edit the [properties](class-AssemblyDefinitionImporter.html) of the
new Assembly Definition.

The new assembly includes all scripts in the same folder as the Assembly
Definition plus those in any subfolders that don’t have their own Assembly
Definition or Reference file. Unity removes scripts from their previous
assembly where applicable.

## Creating an Assembly Definition Reference asset

To create an Assembly Definition Reference asset:

  1. In the **Project** window, locate the folder containing the scripts you want to include in the referenced assembly.

  2. Create an Assembly Reference asset in the folder (menu: **Assets** > **Create** > **Scripting** > **Assembly Definition Reference**).

  3. Assign a name to the asset.

Unity recompiles the scripts in the project to create the new assembly. Once
it has finished, you can edit the [properties](class-
AssemblyDefinitionReferenceImporter.html) of the new Assembly Definition
Reference.

  4. Select the new Assembly Definition Reference asset to view its properties in the **Inspector**.

![](../uploads/Main/asmdef-2.png)

  5. Set the Assembly Definition property to reference the target Assembly Definition asset.

  6. Click **Apply**.

The referenced assembly now includes all scripts in the same folder as the
Assembly Definition Reference, plus those in any subfolders that don’t have
their own Assembly Definition or Reference file. Unity removes scripts from
their previous assembly where applicable.

## Creating a platform-specific assembly

To create an assembly for a specific platform:

  1. Create an Assembly Definition asset.

  2. Select the new Assembly Definition Reference asset to view its properties in the **Inspector**.

![](../uploads/Main/asmdef-3.png)

  3. Check the **Any Platform** option and choose specific platforms to exclude. Alternately, you can uncheck Any Platform and choose specific platforms to include.

  4. Click **Apply**.

The assembly will be included (or excluded) according to the selected
platforms when you build your project for a platform.

## Creating an assembly for Editor code

Editor assemblies allow you to put your Editor scripts anywhere in the
project, not just in top-level folders named `Editor`.

To create an assembly that contains the Editor code in your project:

  1. Create a platform-specific assembly in a folder containing your Editor scripts.
  2. Include ONLY the Editor platform.
  3. If you have additional folders containing Editor scripts, create Assembly Definition Reference assets in those folders and set them to reference this Assembly Definition.

## Creating a test assembly

Test assemblies are assemblies which Unity expects to contain tests. Putting
your tests in test assemblies has the following benefits:

  * They keep your test code separate from the application code you’ll ship to users, so the test code can be compiled only when needed.
  * Any tests in a test assembly are automatically visible to the [Test Framework package](testing-editortestsrunner.html), which makes them available to run from the ****Test Runner** The Test Framework package (formerly called the Test Runner) is a Unity tool that tests your code in both Edit mode and Play mode, and also on target platforms such as Standalone, Android, or iOS. [More info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)  
See in [Glossary](Glossary.html#TestRunner)** window.

Unity automatically identifies any assembly as a test assembly if it has an
[assembly reference](class-AssemblyDefinitionImporter.html#assembly-
references) to **nunit.framework.dll** and [assembly definition
references](class-AssemblyDefinitionImporter.html#asmdef-references) to
**UnityEngine.TestRunner** and **UnityEditor.TestRunner**.

Refer to the Unity [Test Framework
documentation](https://docs.unity3d.com/Packages/com.unity.test-
framework@latest?subfolder=/manual/workflow-create-test-assembly.html) for
instructions on installing the Test Framework package and creating test
assemblies. You can use the Editor **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) to create an assembly definition file with
the relevant references predefined, or you can configure the references
manually [through the Inspector window](class-AssemblyDefinitionImporter.html)
or by [editing the JSON file directly](assembly-definition-file-format.html).

**Note** : Test assemblies are not compiled as part of the regular build
pipeline, so any code placed in a test assembly will be excluded from a
standard [project build](BuildSettings.html). Your test assembly code will
only be included in a Player when you [run Play Mode tests in a
Player](https://docs.unity3d.com/Packages/com.unity.test-
framework@latest?subfolder=/manual/workflow-run-playmode-test-standalone.html)
through the **Test Runner** window. If you have production code that
unexpectedly doesn’t compile into your project build, double-check to make
sure it’s not in a test assembly.

# Additional resources

  * [Special folders and script compilation order](script-compile-order-folders.html)

[](assembly-definitions-intro.html)

Introduction to assemblies in Unity

[](assembly-definitions-referencing.html)

Referencing assemblies

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

