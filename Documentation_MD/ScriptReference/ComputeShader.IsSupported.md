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

#  [ComputeShader](ComputeShader.html).IsSupported

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public bool IsSupported(int kernelIndex);

### Parameters

kernelIndex | Which kernel to query.  
---|---  
  
### Returns

**bool** True if the specified compute kernel is able to run on the current
end user device, false otherwise.

### Description

Allows you to check whether the current end user device supports the features
required to run the specified compute shader kernel.

The result of this call depends on which hardware requirements the compute
shader in question is expected to rely on (as defined by the `#pragma require
<requirement_a> <requirement_b> <requirement_c> ...` shader syntax). This
method implicitly refers to the compute shader variant defined by the set of
currently enabled shader keywords (the variant that would be run if
[ComputeShader.Dispatch](ComputeShader.Dispatch.html) were called instead).
This means that when the source code of the shader in question contains per-
keyword requirements defined using the '#pragma require KEYWORD_A KEYWORD_B
... : <requirement_a> <requirement_b> <requirement_c>...' syntax the result of
[IsSupported](ComputeShader.IsSupported.html) might depend on which shader
keywords are enabled.  
  
Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [Declaring and using shader keywords in
HLSL](../Manual/SL-MultipleProgramVariants.html), [Targeting shader models and
GPU features in HLSL](../Manual/SL-ShaderCompileTargets.html).

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

