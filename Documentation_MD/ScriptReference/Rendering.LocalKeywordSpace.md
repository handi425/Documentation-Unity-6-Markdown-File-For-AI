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

# LocalKeywordSpace

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

Represents the local keyword space of a [Shader](Shader.html) or
[ComputeShader](ComputeShader.html).

Shader keywords determine which shader variants Unity uses. For information on
working with local shader keywords and [global shader
keywords](Rendering.GlobalKeyword.html) and how they interact, see [Using
shader keywords with C# scripts](../Manual/shader-keywords-scripts.html).  
  
When you declare a [shader keyword](../Manual/shader-keywords.html) in the
source file for a [Shader](Shader.html) or
[ComputeShader](ComputeShader.html), Unity represents the keyword with a
[LocalKeyword](Rendering.LocalKeyword.html) and stores it in a
`LocalKeywordSpace`.  
  
For a [Shader](Shader.html), access the `LocalKeywordSpace` with
[Shader.keywordSpace](Shader-keywordSpace.html). It contains:

  * All keywords declared in the source file. For more information, see [Declaring shader keywords](../Manual/shader-keywords#declaring-keywords.html).
  * All keywords declared in dependencies of that source file. This comprises all Shaders that are included via the [Fallback command](../Manual/SL-Fallback.html), and all keywords declared in all Passes that are included via the [UsePass command](../Manual/SL-UsePass.html).
  * All keywords that Unity adds automatically. For more information, see [Unity's predefined shader keywords](../Manual/shader-keywords#predefined-shader-keywords.html).

For a [ComputeShader](ComputeShader.html), access the `LocalKeywordSpace` with
[ComputeShader.keywordSpace](ComputeShader-keywordSpace.html). It contains all
keywords declared in the source file. For more information, see [Declaring
shader keywords](../Manual/shader-keywords#declaring-keywords.html).  
  
Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[ComputeShader.keywordSpace](ComputeShader-keywordSpace.html),
[Shader.keywordSpace](Shader-keywordSpace.html).

### Properties

[keywordCount](Rendering.LocalKeywordSpace-keywordCount.html)| The number of
local shader keywords in this local keyword space. (Read Only)  
---|---  
[keywordNames](Rendering.LocalKeywordSpace-keywordNames.html)| An array
containing the names of all local shader keywords in this local keyword space.
(Read Only)  
[keywords](Rendering.LocalKeywordSpace-keywords.html)| An array containing all
LocalKeyword structs in this local keyword space. (Read Only)  
  
### Public Methods

[FindKeyword](Rendering.LocalKeywordSpace.FindKeyword.html)| Searches for a
local shader keyword with a given name in the keyword space.  
---|---  
  
### Operators

[operator !=](Rendering.LocalKeywordSpace-operator_ne.html)| Returns true if
the local shader keyword spaces are not the same. Otherwise, returns false.  
---|---  
[operator ==](Rendering.LocalKeywordSpace-operator_eq.html)| Returns true if
the local shader keyword spaces are the same. Otherwise, returns false.  
  
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

