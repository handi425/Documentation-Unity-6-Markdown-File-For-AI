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

#  [PlayerSettings](PlayerSettings.html).SetIl2CppCodeGeneration

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

## Declaration

public static void
SetIl2CppCodeGeneration([Build.NamedBuildTarget](Build.NamedBuildTarget.html)
buildTarget, [Build.Il2CppCodeGeneration](Build.Il2CppCodeGeneration.html)
value);

### Parameters

buildTarget | The [NamedBuildTarget](Build.NamedBuildTarget.html).  
---|---  
value | Code generation option.  
  
### Description

Sets the code generation option for IL2CPP for the specified build target.

There are two options for IL2CPP code generation.
[Il2CppCodeGeneration.OptimizeSpeed](Build.Il2CppCodeGeneration.OptimizeSpeed.html)
generates code that is optimized for runtime performance. This is the default
and the behavior in previous versions of Unity.
[Il2CppCodeGeneration.OptimizeSize](Build.Il2CppCodeGeneration.OptimizeSize.html)
generates code that is optimized for build size and iteration. It generates
less code and produces a smaller build but may have an impact on runtime
performance, especially for generic code. You should consider this option when
faster build times are important, such as when iterating on changes.  
  
Additionally,
[Il2CppCodeGeneration.OptimizeSize](Build.Il2CppCodeGeneration.OptimizeSize.html)
generates a universal version of each generic type and method. This avoids
some restrictions
[Il2CppCodeGeneration.OptimizeSpeed](Build.Il2CppCodeGeneration.OptimizeSpeed.html)
has when executing generic code.

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

