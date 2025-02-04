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

# ShaderPrecisionModel

enumeration

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

Options for the shader precision model.

This enumeration allows you to change two things: the default sampler
precision and the definition of `half`.  
  
The default sampler precision is only relevant to samplers that don't
explicitly declare a precision. For example, `sampler2D` uses the default
precision, but `sampler2D_float` uses full precision regardless of the default
precision.  
  
Regarding the shader type `half`, it is defined as either `float` or
`min16float` (see [SL-DataTypesAndPrecision](../Manual/SL-
DataTypesAndPrecision.html)). For the purpose of uploading data to buffers,
including constant buffers, the size and alignment is 4 bytes in both cases.

### Properties

[PlatformDefault](ShaderPrecisionModel.PlatformDefault.html)| Use the target
platform defaults. The default sampler precision is half precision on mobile
targets and full precision elsewhere. Also, shader type half is defined as
min16float on mobile targets and float elsewhere.  
---|---  
[Unified](ShaderPrecisionModel.Unified.html)| Use full sampler precision by
default, and explicitly declare when you want to use lower precision. Refer to
SL-DataTypesAndPrecision for more information. In addition, half is defined as
min16float on all platforms. This sets
BuiltinShaderDefine.UNITY_UNIFIED_SHADER_PRECISION_MODEL when Unity compiles
shaders.  
  
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

