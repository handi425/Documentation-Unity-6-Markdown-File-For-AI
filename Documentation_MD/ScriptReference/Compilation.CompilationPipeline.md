[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# CompilationPipeline

class in UnityEditor.Compilation

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Methods and properties for script compilation pipeline.

### Static Properties

[codeOptimization](Compilation.CompilationPipeline-codeOptimization.html)|
Current code optimization mode.  
---|---  
  
### Static Methods

[AssemblyDefinitionReferenceGUIDToGUID](Compilation.CompilationPipeline.AssemblyDefinitionReferenceGUIDToGUID.html)|
Converts an assembly definition file GUID reference to a GUID string.  
---|---  
[GetAssemblies](Compilation.CompilationPipeline.GetAssemblies.html)| Get all
script assemblies compiled by Unity filtered by AssembliesType.  
[GetAssemblyDefinitionFilePathFromAssemblyName](Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromAssemblyName.html)|
Returns the assembly definition file path from an assembly name. Returns null
if there is no assembly definition file for the given assembly name.  
[GetAssemblyDefinitionFilePathFromAssemblyReference](Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromAssemblyReference.html)|
Returns the assembly definition file path for an Assembly Definition File GUID
or assembly name reference. Returns null if there is no assembly definition
file for the given assembly reference.  
[GetAssemblyDefinitionFilePathFromScriptPath](Compilation.CompilationPipeline.GetAssemblyDefinitionFilePathFromScriptPath.html)|
Returns the assembly definition file path for a source (script) path. Returns
null if there is no assembly definition file for the given script path.  
[GetAssemblyDefinitionPlatforms](Compilation.CompilationPipeline.GetAssemblyDefinitionPlatforms.html)|
Returns all the platforms supported by assembly definition files.Additional
resources: AssemblyDefinitionPlatform.  
[GetAssemblyDefinitionReferenceType](Compilation.CompilationPipeline.GetAssemblyDefinitionReferenceType.html)|
Utility method to determine whether an Assembly Definition File reference is a
GUID reference or an assembly name reference.  
[GetAssemblyNameFromScriptPath](Compilation.CompilationPipeline.GetAssemblyNameFromScriptPath.html)|
Returns the assembly name for a source (script) path. Returns null if there is
no assembly name for the given script path.  
[GetAssemblyRootNamespaceFromScriptPath](Compilation.CompilationPipeline.GetAssemblyRootNamespaceFromScriptPath.html)|
Gets the root namespace associated with the given script path.  
[GetDefinesFromAssemblyName](Compilation.CompilationPipeline.GetDefinesFromAssemblyName.html)|
Lists all the #define directives used to compile the specified assembly.  
[GetPrecompiledAssemblyNames](Compilation.CompilationPipeline.GetPrecompiledAssemblyNames.html)|
Get all precompiled assembly names.  
[GetPrecompiledAssemblyPathFromAssemblyName](Compilation.CompilationPipeline.GetPrecompiledAssemblyPathFromAssemblyName.html)|
Returns the Assembly file path from an assembly name. Returns null if there is
no Precompiled Assembly name match.  
[GetPrecompiledAssemblyPaths](Compilation.CompilationPipeline.GetPrecompiledAssemblyPaths.html)|
Returns the paths to the precompiled assemblies which are included when
building editor assemblies and match any of the given
PrecompiledAssemblySources.  
[GetResponseFileDefinesFromAssemblyName](Compilation.CompilationPipeline.GetResponseFileDefinesFromAssemblyName.html)|
Lists all the #define directives used to compile the specified assembly, that
is from a Response File.  
[GetSystemAssemblyDirectories](Compilation.CompilationPipeline.GetSystemAssemblyDirectories.html)|
Use this to get a list of directories containing system references for the
specific ApiCompatibilityLevel.  
[GUIDToAssemblyDefinitionReferenceGUID](Compilation.CompilationPipeline.GUIDToAssemblyDefinitionReferenceGUID.html)|
Converts the given GUID to an assembly definition file GUID reference.  
[IsDefineConstraintsCompatible](Compilation.CompilationPipeline.IsDefineConstraintsCompatible.html)|
Allows you to test whether the specified #define constraints are satisfied by
the specified list of #define directives.  
[ParseResponseFile](Compilation.CompilationPipeline.ParseResponseFile.html)|
Retrieves the ResponseFileData describing the content of the response file.  
[RequestScriptCompilation](Compilation.CompilationPipeline.RequestScriptCompilation.html)|
Allows you to request that the Editor recompile scripts in the project.  
  
### Events

[assemblyCompilationFinished](Compilation.CompilationPipeline-
assemblyCompilationFinished.html)| An event that is invoked on the main thread
when compilation of an assembly finishes.  
---|---  
[assemblyCompilationNotRequired](Compilation.CompilationPipeline-
assemblyCompilationNotRequired.html)| An event that is invoked on the main
thread when an assembly does not require compilation.  
[assemblyCompilationStarted](Compilation.CompilationPipeline-
assemblyCompilationStarted.html)| An event that is invoked on the main thread
when the assembly build starts.  
[codeOptimizationChanged](Compilation.CompilationPipeline-
codeOptimizationChanged.html)| This event triggers whenever the
codeOptimization property changes between Debug and Release modes.  
[compilationFinished](Compilation.CompilationPipeline-
compilationFinished.html)| An event that is invoked on the main thread when
the compilation of assemblies finishes.  
[compilationStarted](Compilation.CompilationPipeline-compilationStarted.html)|
An event that is invoked on the main thread when the compilation of assemblies
starts.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

