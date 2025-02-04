[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [中文](/cn/current/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [日本語](/ja/current/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [한국어](/kr/current/Manual/class-AssemblyDefinitionReferenceImporter.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [中文](/cn/current/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [日本語](/ja/current/Manual/class-AssemblyDefinitionReferenceImporter.html)
  * [한국어](/kr/current/Manual/class-AssemblyDefinitionReferenceImporter.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Assembly Definition Reference properties reference

[](class-AssemblyDefinitionImporter.html)

Assembly Definition properties reference

[](assembly-definition-file-format.html)

Assembly Definition File Format reference

# Assembly Definition Reference properties reference

An Assembly Definition Reference is an asset that defines a reference to an
Assembly Definition. Create an Assembly Definition Reference asset in a folder
to include the **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in that folder in the referenced
Assembly Definition (rather than creating a new assembly). Scripts in child
folders are also included, unless they have their own Assembly Definition or
Assembly Definition Reference asset.

![](../uploads/Main/asmdef-17.png) Property | Description  
---|---  
Use GUID | This setting controls how Unity serializes the reference to the Assembly Definition asset. When you enable this property, Unity saves the reference as the asset’s GUID, instead of the Assembly Definition name. It’s good practice to use the GUID instead of the name, because it means you can make changes to the name of an Assembly Definition asset without having to update other Assembly Definitions and References that reference it.  
Assembly Definition | The referenced Assembly Definition asset.  
  
See [Creating an Assembly Definition Reference asset](assembly-definitions-
creating.html)

AssemblyDefinitionReferenceImporter

[](class-AssemblyDefinitionImporter.html)

Assembly Definition properties reference

[](assembly-definition-file-format.html)

Assembly Definition File Format reference

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

