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

#  [ShaderData.Pass](ShaderData.Pass.html).PreprocessVariant

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

public [ShaderData.PreprocessedVariant](ShaderData.PreprocessedVariant.html)
PreprocessVariant([Rendering.ShaderType](Rendering.ShaderType.html)
shaderType, string[] keywords,
[Rendering.ShaderCompilerPlatform](Rendering.ShaderCompilerPlatform.html)
shaderCompilerPlatform, [BuildTarget](BuildTarget.html) buildTarget, bool
stripLineDirectives);

## Declaration

public [ShaderData.PreprocessedVariant](ShaderData.PreprocessedVariant.html)
PreprocessVariant([Rendering.ShaderType](Rendering.ShaderType.html)
shaderType, string[] keywords,
[Rendering.ShaderCompilerPlatform](Rendering.ShaderCompilerPlatform.html)
shaderCompilerPlatform, [BuildTarget](BuildTarget.html) buildTarget,
[Rendering.GraphicsTier](Rendering.GraphicsTier.html) tier, bool
stripLineDirectives);

## Declaration

public [ShaderData.PreprocessedVariant](ShaderData.PreprocessedVariant.html)
PreprocessVariant([Rendering.ShaderType](Rendering.ShaderType.html)
shaderType, string[] keywords,
[Rendering.ShaderCompilerPlatform](Rendering.ShaderCompilerPlatform.html)
shaderCompilerPlatform, [BuildTarget](BuildTarget.html) buildTarget,
BuiltinShaderDefine[] platformKeywords, bool stripLineDirectives);

## Declaration

public [ShaderData.PreprocessedVariant](ShaderData.PreprocessedVariant.html)
PreprocessVariant([Rendering.ShaderType](Rendering.ShaderType.html)
shaderType, string[] keywords,
[Rendering.ShaderCompilerPlatform](Rendering.ShaderCompilerPlatform.html)
shaderCompilerPlatform, [BuildTarget](BuildTarget.html) buildTarget,
BuiltinShaderDefine[] platformKeywords,
[Rendering.GraphicsTier](Rendering.GraphicsTier.html) tier, bool
stripLineDirectives);

### Parameters

shaderType | The shader type within this pass to preprocess. (e.g. Vertex, Fragment, etc.) Some platforms (OpenGLCore, GLES3x, Switch and Vulkan) include all stages within the Vertex shader type.  
---|---  
keywords | The keywords to use during the preprocessing.  
shaderCompilerPlatform | The shader compiler platform to preprocess for.  
buildTarget | The build target to preprocess for.  
tier | An optional graphics tier.  
platformKeywords | An optional set of platform keywords. If you do not provide any, Unity uses the default keywords for the given platform, target, and tier.  
stripLineDirectives | Whether to skip line number directives in the preprocessed output. When enabled, Unity produces more human-readable preprocessed source code and skips the line directives when the file name doesn't change. Otherwise, this method produces the exact preprocessed source that Unity passes to the compiler.  
  
### Returns

**PreprocessedVariant** The preprocessed variant result. If the pass doesn't
include the requested program, or if the pass is not the correct type, this
function still succeeds but returns empty preprocessed code.

### Description

Preprocesses a shader variant for this shader pass and returns the
preprocessed code.

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

