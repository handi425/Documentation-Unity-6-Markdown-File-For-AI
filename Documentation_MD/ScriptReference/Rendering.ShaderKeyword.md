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

# ShaderKeyword

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

Represents an identifier for a specific code path in a shader.

Unity now provides the [LocalKeyword](Rendering.LocalKeyword.html) and
[GlobalKeyword](Rendering.GlobalKeyword.html) APIs which are more performant
than ShaderKeyword. It is best practice to use these APIs instead.  
  
Additional resources: [LocalKeyword](Rendering.LocalKeyword.html),
[GlobalKeyword](Rendering.GlobalKeyword.html),
[ShaderKeywordSet](Rendering.ShaderKeywordSet.html),
[Shader.EnableKeyword](Shader.EnableKeyword.html), [Shader variants and
keywords](../Manual/shader-variants-and-keywords.html), [Declaring and using
shader keywords in HLSL](../Manual/SL-MultipleProgramVariants.html).

### Properties

[index](Rendering.ShaderKeyword-index.html)| The index of the shader keyword.  
---|---  
[name](Rendering.ShaderKeyword-name.html)| The name of the shader keyword.
(Read Only)  
  
### Constructors

[ShaderKeyword](Rendering.ShaderKeyword-ctor.html)| Initializes a new instance
of the ShaderKeyword class from a shader global keyword name.  
---|---  
  
### Public Methods

[IsValid](Rendering.ShaderKeyword.IsValid.html)| Checks whether the global
shader keyword exists.  
---|---  
  
### Static Methods

[GetGlobalKeywordType](Rendering.ShaderKeyword.GetGlobalKeywordType.html)|
Returns the type of global keyword: built-in or user defined.  
---|---  
[IsKeywordLocal](Rendering.ShaderKeyword.IsKeywordLocal.html)| Returns true if
the keyword is local.  
  
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

