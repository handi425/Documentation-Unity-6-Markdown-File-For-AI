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
[ShaderUtil](ShaderUtil.html).GetPassKeywords(Shader,Rendering.PassIdentifier)

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
  
### Returns

**void** Returns an array of LocalKeywords that are valid for the Pass you
identify. If the [PassIdentifier](Rendering.PassIdentifier.html) you use is
invalid, this function returns an empty array and Unity displays an error in
the Console window.

### Description

Gets the local shader keywords that are valid for a Pass within a particular
shader.

Additional resources: [Pass](../Manual/SL-Pass.html).

* * *

### Parameters

s | The shader the Pass belongs to.  
---|---  
passIdentifier | The identifier of a Pass within the given shader.  
shaderType | The shader stage of the given Pass.  
  
### Returns

**void** Returns an array of LocalKeywords that are valid for the given
[shader stage](Rendering.ShaderType.html) of the Pass you identify. If the
[PassIdentifier](Rendering.PassIdentifier.html) you use is invalid, this
function returns an empty array and Unity displays an error in the Console
window. If the shader stage doesn't exist in the pass, this function returns
an empty array.

### Description

Gets the local shader keywords that are valid for a specified shader stage of
a Pass within a particular shader.

Additional resources: [Pass](../Manual/SL-Pass.html),
[ShaderType](Rendering.ShaderType.html).

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

