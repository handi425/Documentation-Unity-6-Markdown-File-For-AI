[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/assembly-definition-metadata.html)
  * [中文](/cn/current/Manual/assembly-definition-metadata.html)
  * [日本語](/ja/current/Manual/assembly-definition-metadata.html)
  * [한국어](/kr/current/Manual/assembly-definition-metadata.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/assembly-definition-metadata.html)
  * [中文](/cn/current/Manual/assembly-definition-metadata.html)
  * [日本語](/ja/current/Manual/assembly-definition-metadata.html)
  * [한국어](/kr/current/Manual/assembly-definition-metadata.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Organizing scripts into assemblies](assembly-definition-files.html)
  * Assembly metadata and compilation details

[](assembly-definition-includes.html)

Conditionally including assemblies

[](class-AssemblyDefinitionImporter.html)

Assembly Definition properties reference

# Assembly metadata and compilation details

You can define additional metadata for your assemblies and retrieve
information on the assemblies included in a project build.

## Setting assembly attributes

You can use assembly attributes to set metadata properties for your
assemblies. By convention, assembly attribute statements are typically put in
a file named `AssemblyInfo.cs`.

For example, the following assembly attributes specify a few [.NET assembly
metadata values], an `[InternalsVisibleTo]` attribute, which can be useful for
testing, and the Unity-defined [Preserve
attribute](../ScriptReference/PreserveAttribute.html) that affects how unused
code is removed from an assembly when you build your project:

    
    
    [assembly: System.Reflection.AssemblyCompany("Bee Corp.")]
    [assembly: System.Reflection.AssemblyTitle("Bee's Assembly")]
    [assembly: System.Reflection.AssemblyCopyright("Copyright 2020.")]
    [assembly: System.Runtime.CompilerServices.InternalsVisibleTo("UnitTestAssembly")]
    [assembly: UnityEngine.Scripting.Preserve]
    

## Getting assembly information in build scripts

Use the
[CompilationPipeline](../ScriptReference/Compilation.CompilationPipeline.html)
class to retrieve information about all assemblies built by Unity for a
project, including those created based on Assembly Definition assets.

For example, the following script uses the `CompilationPipeline` class to list
all the current Player assemblies in a project:

    
    
    using UnityEditor;
    using UnityEditor.Compilation;
    public static class AssemblyLister
    {
        [MenuItem("Tools/List Player Assemblies in Console")]
        public static void PrintAssemblyNames()
        {
            UnityEngine.Debug.Log("== Player Assemblies ==");
            Assembly[] playerAssemblies =
                CompilationPipeline.GetAssemblies(AssembliesType.Player);
    
            foreach (var assembly in playerAssemblies)
            {
                UnityEngine.Debug.Log(assembly.name);
            }
        }
    }
    

## Additional resources

  * [Creating assembly definitions](assembly-definitions-creating.html)
  * [Referencing assemblies](assembly-definitions-referencing.html)
  * [Assembly Definition properties](class-AssemblyDefinitionImporter.html)
  * [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
  * [Assembly Definition File Format](assembly-definition-file-format.html)

[](assembly-definition-includes.html)

Conditionally including assemblies

[](class-AssemblyDefinitionImporter.html)

Assembly Definition properties reference

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

