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

#
[ScriptCompilerOptions](Compilation.ScriptCompilerOptions.html).AnalyzerConfigPath

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

public string AnalyzerConfigPath;

### Description

Stores the path to the Roslyn global config file.

You can define a project-wide analyzer configuration in a file with the
.globalconfig file extension. Use key-value pairs to configure the default
behavior of all files in your project. If a file with this extension is
present, Unity automatically detects it and stores the path in this property.
Use this global config file in the same way as a ruleset file. Create a file
named "Default.globalconfig" in your root asset folder to apply the
configuration to all predefined assemblies and any assemblies that Unity
builds with .asmdef files.  
  
You can override the options for some predefined Unity assemblies by creating
a .globalconfig file in the root asset folder with the name
[PredefinedAssemblyName].globalconfig. If a
[PredefinedAssemblyName].globalconfig is present, the options specified in
that file are used instead of the ones in the Default.globalconfig (if
present).  
  
Only these .globalconfig files are permitted inside the root asset folder: \-
Default.globalconfig \- Assembly-CSharp.globalconfig \- Assembly-CSharp-
firstpass.globalconfig \- Assembly-CSharp-Editor.globalconfig \- Assembly-
CSharp-Editor-firstpass.globalconfig  
  
It is also possible to override the options for each assembly definition, by
creating a .globalconfig file in the same folder as its .asmdef file. There
are no name restrictions in this case, but it is a good practice to follow the
rule [AssemblyDefinitionName].globalconfig. If a globalconfig file is present
for assembly definition, the options specified in that file are used instead
the ones in the Default.globalconfig (if present).  
  
If multiple keys with the same name are present in the same config file, Unity
uses the last entry in the file for that key. Config files are not additive:
you can't have a Default.globalconfig that sets some common value and has a
subset for a specific assembly. If you add a global config override for
PredefinedAssemblyName or an assembly definition, that file should contain all
the keys-value pairs.

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

