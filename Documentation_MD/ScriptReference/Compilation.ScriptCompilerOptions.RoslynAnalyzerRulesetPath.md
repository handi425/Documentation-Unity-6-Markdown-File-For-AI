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
[ScriptCompilerOptions](Compilation.ScriptCompilerOptions.html).RoslynAnalyzerRulesetPath

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

public string RoslynAnalyzerRulesetPath;

### Description

Stores the path to the Roslyn ruleset file.

You can define your own rules on how to handle the various warnings and errors
that Roslyn analyzers raise. You must put these rules inside a file with the
.ruleset extension. Unity detects this .ruleset file, and stores its path
inside RoslynAnalyzerRulesetPath.  
  
In the root folder, you can store a ruleset file named "Default.ruleset". The
rules defined in Default.ruleset apply to all predefined assemblies, as well
as all assemblies that are built using .asmdef files.  
  
To override the rules in Default.ruleset for a predefined assembly, create a
.ruleset file in the root folder with the name
[PredefinedAssemblyName].ruleset. For example, the rules in Assembly-
CSharp.ruleset apply to Assembly-CSharp.dll.  
  
Only these .ruleset files are permitted inside the root folder: \-
Default.ruleset \- Assembly-CSharp.ruleset \- Assembly-CSharp-
firstpass.ruleset \- Assembly-CSharp-Editor.ruleset \- Assembly-CSharp-Editor-
firstpass.ruleset  
  
To override the rules in Default.ruleset for an assembly built using an
.asmdef file, create a .ruleset file in the same folder as its .asmdef file.
You can give it any name you like. The name of this ruleset file does not
necessarily have to match the name of the assembly.

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

