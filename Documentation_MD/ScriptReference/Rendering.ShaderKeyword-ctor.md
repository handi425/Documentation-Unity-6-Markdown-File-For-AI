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

# ShaderKeyword Constructor

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

public ShaderKeyword(string keywordName);

### Parameters

keywordName | The name of the keyword.  
---|---  
  
### Description

Initializes a new instance of the ShaderKeyword class from a shader global
keyword name.

If you call this function and a keyword with the name you pass in does not
exist, Unity creates one with that name. To get all the global keywords that
already exist, use [Shader.globalKeywords](Shader-globalKeywords.html).  
  
Additional resources:
[IPreprocessShaders.OnProcessShader](Build.IPreprocessShaders.OnProcessShader.html),
[IPreprocessComputeShaders.OnProcessComputeShader](Build.IPreprocessComputeShaders.OnProcessComputeShader.html).

* * *

## Declaration

public ShaderKeyword([Shader](Shader.html) shader, string keywordName);

### Parameters

shader | The shader that declares the keyword.  
---|---  
keywordName | The name of the keyword.  
  
### Description

Initializes a new instance of the ShaderKeyword class from a local shader
keyword name.

If the shader defines a local keyword with the given name, Unity creates a
valid ShaderKeyword instance that represents the local keyword. Otherwise,
Unity creates an invalid ShaderKeyword instance.  
  
Additional resources: Build.IPreprocessComputeShaders.OnProcessShader,
[ShaderKeyword.IsValid](Rendering.ShaderKeyword.IsValid.html).

* * *

## Declaration

public ShaderKeyword([ComputeShader](ComputeShader.html) shader, string
keywordName);

### Parameters

shader | The compute shader that declares the local keyword.  
---|---  
keywordName | The name of the keyword.  
  
### Description

Initializes a new instance of the ShaderKeyword class from a local shader
keyword name, and the compute shader that defines that local keyword.

If the compute shader defines a local keyword with the given name, Unity
creates a valid ShaderKeyword instance that represents the local keyword.
Otherwise, Unity creates an invalid ShaderKeyword instance.  
  
Additional resources:
[IPreprocessComputeShaders.OnProcessComputeShader](Build.IPreprocessComputeShaders.OnProcessComputeShader.html),
[ShaderKeyword.IsValid](Rendering.ShaderKeyword.IsValid.html).

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

