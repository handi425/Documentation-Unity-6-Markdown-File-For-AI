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
[ShaderUtil](ShaderUtil.html).PassHasKeyword(Shader,Rendering.PassIdentifier,Rendering.LocalKeyword)

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

### Parameters

s | The shader the Pass belongs to.  
---|---  
passIdentifier | The identifier of a Pass within the given shader.  
keyword | The local shader keyword to check.  
  
### Returns

**void** Returns true if the keyword is valid for the given Pass. Otherwise,
returns false. If the [PassIdentifier](Rendering.PassIdentifier.html) you use
is invalid, this function returns false and Unity displays an error in the
Console window.

### Description

Checks whether a local shader keyword is valid for a Pass within a particular
shader.

Additional resources: [Pass](../Manual/SL-Pass.html).

* * *

### Parameters

s | The shader the Pass belongs to.  
---|---  
passIdentifier | The identifier of a Pass within the given shader.  
keyword | The local shader keyword to check.  
shaderType | The shader stage of the given pass.  
  
### Returns

**void** Returns true if the keyword is valid for the given shader stage of
the Pass. Otherwise, returns false. If the
[PassIdentifier](Rendering.PassIdentifier.html) you use is invalid, this
function returns false and Unity displays an error in the Console window.

### Description

Checks whether a local shader keyword is valid for a particular shader stage
of a Pass within a particular shader.

Additional resources: [Pass](../Manual/SL-Pass.html).

* * *

### Parameters

s | The shader the Pass belongs to.  
---|---  
passIdentifier | The identifier of a Pass within the given shader.  
keyword | The local shader keyword to check.  
shaderType | The shader stage of the given pass.  
shaderCompilerPlatform | The shader compiler platform to check against.  
  
### Returns

**void** Returns true if the keyword is valid for the given shader stage of
the Pass for the given ShaderCompilerPlatform. Otherwise, returns false. If
the [PassIdentifier](Rendering.PassIdentifier.html) you use is invalid, this
function returns false and Unity displays an error in the Console window.

### Description

Checks whether a local shader keyword is valid for a particular shader stage
of a Pass within a particular shader for the given shader compiler platform.

Some shader compiler platforms combine several shader stages in one. This
method overload ensures that correct data is returned for all shader compiler
platforms.  
  
Additional resources: [Pass](../Manual/SL-Pass.html).

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

