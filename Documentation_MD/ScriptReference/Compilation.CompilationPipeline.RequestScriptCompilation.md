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
[CompilationPipeline](Compilation.CompilationPipeline.html).RequestScriptCompilation

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

## Declaration

public static void RequestScriptCompilation();

## Declaration

public static void
RequestScriptCompilation([Compilation.RequestScriptCompilationOptions](Compilation.RequestScriptCompilationOptions.html)
options);

### Parameters

options | Optional parameter to specify whether the Editor should clear the build cache before compilation.  
---|---  
  
### Description

Allows you to request that the Editor recompile scripts in the project.

When you call this method, the Unity Editor checks whether there have been any
changes to scripts, or to settings affecting script compilation, and
recompiles those scripts which require it. After the compilation, if the
compilation was successful, the Unity Editor reloads all assemblies. If you
want to force recompilation of all scripts, even if there are no changes, you
can pass
[RequestScriptCompilationOptions.CleanBuildCache](Compilation.RequestScriptCompilationOptions.CleanBuildCache.html)
for the options parameter. You may want to force recompilation of all scripts
in the following situations: \- If you have a successful compilation, but want
to see all compiler warnings again. \- If you have a setup where the
compilation pipeline takes input from files that Unity cannot track (this is
possible in rare circumstances when using response files). \- If there is a
bug or suspected bug in the compilation pipeline causing it to not pick up
changes.

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

