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

# LocalKeyword

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Represents a shader keyword declared in a shader source file.

Shader keywords determine which shader variants Unity uses. You can use a
`LocalKeyword` to enable, disable, or check the state of a **local** shader
keyword. For information on working with local shader keywords and [global
shader keywords](Rendering.GlobalKeyword.html) and how they interact, see
[Using shader keywords with C# scripts](../Manual/shader-keywords-
scripts.html).  
  
When you declare a shader keyword in the source file for a
[Shader](Shader.html) or [ComputeShader](ComputeShader.html), Unity represents
the keyword with a `LocalKeyword` and stores it in a
[LocalKeywordSpace](Rendering.LocalKeywordSpace.html).  
  
For a [Shader](Shader.html):

  * To set the state of a local shader keyword, use [Material.SetKeyword](Material.SetKeyword.html), [Material.EnableKeyword](Material.EnableKeyword.html), or [Material.DisableKeyword](Material.DisableKeyword.html).
  * To check the state of a local shader keyword, use [Material.IsKeywordEnabled](Material.IsKeywordEnabled.html) or [Material.enabledKeywords](Material-enabledKeywords.html).
  * To access the `LocalKeywordSpace`, use [Material.shader](Material-shader.html) to access the [Shader](Shader.html) that the material uses, and then use [Shader.keywordSpace](Shader-keywordSpace.html).

For a [ComputeShader](ComputeShader.html):

  * To set the state of a local shader keyword, use [ComputeShader.SetKeyword](ComputeShader.SetKeyword.html), [ComputeShader.EnableKeyword](ComputeShader.EnableKeyword.html), or [ComputeShader.DisableKeyword](ComputeShader.DisableKeyword.html).
  * To check the state of a local shader keyword, use [ComputeShader.IsKeywordEnabled](ComputeShader.IsKeywordEnabled.html) or [ComputeShader.enabledKeywords](ComputeShader-enabledKeywords.html).
  * To access the `LocalKeywordSpace`, use [ComputeShader.keywordSpace](ComputeShader-keywordSpace.html).

In addition to this, you can also enable or disable a local or global keyword
with a `CommandBuffer`. To do this, use
[CommandBuffer.SetKeyword](Rendering.CommandBuffer.SetKeyword.html),
[CommandBuffer.EnableKeyword](Rendering.CommandBuffer.EnableKeyword.html), or
[CommandBuffer.DisableKeyword](Rendering.CommandBuffer.DisableKeyword.html).  
  
**Note:** A `LocalKeyword` is specific to a single [Shader](Shader.html) or
[ComputeShader](ComputeShader.html) instance. You cannot use it with other
[Shader](Shader.html) or [ComputeShader](ComputeShader.html) instances, even
if they declare keywords with the same `name`.  
  
Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [GlobalKeyword](Rendering.GlobalKeyword.html).

### Properties

[isDynamic](Rendering.LocalKeyword-isDynamic.html)| Specifies whether this
local shader keyword is used for dynamic branching (Read Only).  
---|---  
[isOverridable](Rendering.LocalKeyword-isOverridable.html)| Whether this local
shader keyword can be overridden by a global shader keyword. (Read Only).  
[isValid](Rendering.LocalKeyword-isValid.html)| Specifies whether this local
shader keyword is valid (Read Only).  
[name](Rendering.LocalKeyword-name.html)| The name of the shader keyword (Read
Only).  
[type](Rendering.LocalKeyword-type.html)| The type of the shader keyword (Read
Only).  
  
### Constructors

[LocalKeyword](Rendering.LocalKeyword-ctor.html)| Initializes and returns a
LocalKeyword struct that represents an existing local shader keyword for a
given Shader.  
---|---  
  
### Operators

[operator !=](Rendering.LocalKeyword-operator_ne.html)| Returns true if the
shader keywords are not the same. Otherwise, returns false.  
---|---  
[operator ==](Rendering.LocalKeyword-operator_eq.html)| Returns true if the
shader keywords are the same. Otherwise, returns false.  
  
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

