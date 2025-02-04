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

#  [CommandBuffer](Rendering.CommandBuffer.html).EnableKeyword

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

public void EnableKeyword(ref
[Rendering.GlobalKeyword](Rendering.GlobalKeyword.html) keyword);

## Declaration

public void EnableKeyword([Material](Material.html) material, ref
[Rendering.LocalKeyword](Rendering.LocalKeyword.html) keyword);

## Declaration

public void EnableKeyword([ComputeShader](ComputeShader.html) computeShader,
ref [Rendering.LocalKeyword](Rendering.LocalKeyword.html) keyword);

### Parameters

keyword | The global or local shader keyword to enable.  
---|---  
material | The material on which to enable the local shader keyword.  
computeShader | The compute shader for which to enable the local shader keyword.  
  
### Description

Adds a command to enable a global or local shader keyword.

Shader keywords determine which shader variants Unity uses. For information on
working with [local shader keywords](Rendering.LocalKeyword.html) and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html),
[SetKeyword](Rendering.CommandBuffer.SetKeyword.html),
[DisableKeyword](Rendering.CommandBuffer.DisableKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[LocalKeyword](Rendering.LocalKeyword.html),
[Shader.DisableKeyword](Shader.DisableKeyword.html),
[Material.DisableKeyword](Material.DisableKeyword.html),
[ComputeShader.DisableKeyword](ComputeShader.DisableKeyword.html).

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

