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
[ScriptCompilerOptions](Compilation.ScriptCompilerOptions.html).RoslynAdditionalFilePaths

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

public string[] RoslynAdditionalFilePaths;

### Description

Stores the paths to the Roslyn Analyzer additional files.

It is possible to add to the project a list of additional files that can be
used by your Roslyn Analyzer/SourceGenerator. The Unity Editor evaluates files
with the .additionalfile extension to test if they're suitable to pass into
the compilation pipeline. Files whose names match the Filename.[Analyzer
Name].additionalfile format are suitable and Unity passes them to the
compilation pipeline. If the file isn't named with the [Analyzer Name] suffix,
Unity still imports it but doesn't pass it to the compilation pipeline. Note:
For Unity to correctly recognize the format, the [Analyzer Name] must match
the name of the analyzer the file targets and the Filename prefix must not
contain a "." character. The [Analyzer Name] suffix is case-sensitive.  
  
Each compiled assembly receives a list of additional files based on the
analyzers running for that assembly definition, filtered by the [Analyzer
Name] suffix. The following example shows which additionalfiles Unity passes
on for three assemblies with either or both of two analyzers: Assembly1 uses
an analyzer named Analyzer1 Assembly2 uses an analyzer named Analyzer2
Assembly3 uses both Analyzer1 and Analyzer2  
  
If the project contains four additional files named
FileA.Analyzer1.additionalfile, FileB.Analyzer2.additionalfile,
FileC.additionalfile, and FileD.Analyzer3.additionalfile, then Unity passes
the following list of additional files with the respective assemblies:  
  
Assembly1: FileA.Analyzer1.additionalfile Assembly2:
FileB.Analyzer2.additionalfile Assembly3: FileA.Analyzer1.additionalfile,
FileB.Analyzer2.additionalfile  
  
Since FileC doesn't use an [Analyzer Name] suffix and FileD references an
analyzer that isn't present in the project, Unity doesn't pass either one to
the compilation pipeline.  
  
The full list of additional files added to the assembly compilation can then
be retrieved by the analyzers from the analyzer context. It is important to
note that this list comprises all the additional files added to the
compilation, not only the ones matching the name of the analyzers.  
  
For Assembly3 in the above example, Analyzer1 and Analyzer2 both retrieve the
correctly named additional files that references them. The analyzer is
responsible for checking if there is any data it can use.

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

