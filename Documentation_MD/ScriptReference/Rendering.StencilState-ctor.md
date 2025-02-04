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

# StencilState Constructor

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

public StencilState(bool enabled, byte readMask, byte writeMask,
[Rendering.CompareFunction](Rendering.CompareFunction.html) compareFunction,
[Rendering.StencilOp](Rendering.StencilOp.html) passOperation,
[Rendering.StencilOp](Rendering.StencilOp.html) failOperation,
[Rendering.StencilOp](Rendering.StencilOp.html) zFailOperation);

## Declaration

public StencilState(bool enabled, byte readMask, byte writeMask,
[Rendering.CompareFunction](Rendering.CompareFunction.html)
compareFunctionFront, [Rendering.StencilOp](Rendering.StencilOp.html)
passOperationFront, [Rendering.StencilOp](Rendering.StencilOp.html)
failOperationFront, [Rendering.StencilOp](Rendering.StencilOp.html)
zFailOperationFront,
[Rendering.CompareFunction](Rendering.CompareFunction.html)
compareFunctionBack, [Rendering.StencilOp](Rendering.StencilOp.html)
passOperationBack, [Rendering.StencilOp](Rendering.StencilOp.html)
failOperationBack, [Rendering.StencilOp](Rendering.StencilOp.html)
zFailOperationBack);

### Parameters

readMask | An 8 bit mask as an 0–255 integer, used when comparing the reference value with the contents of the buffer.  
---|---  
writeMask | An 8 bit mask as an 0–255 integer, used when writing to the buffer.  
enabled | Controls whether the stencil buffer is enabled.  
compareFunctionFront | The function used to compare the reference value to the current contents of the buffer for front-facing geometry.  
passOperationFront | What to do with the contents of the buffer if the stencil test (and the depth test) passes for front-facing geometry.  
failOperationFront | What to do with the contents of the buffer if the stencil test fails for front-facing geometry.  
zFailOperationFront | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for front-facing geometry.  
compareFunctionBack | The function used to compare the reference value to the current contents of the buffer for back-facing geometry.  
passOperationBack | What to do with the contents of the buffer if the stencil test (and the depth test) passes for back-facing geometry.  
failOperationBack | What to do with the contents of the buffer if the stencil test fails for back-facing geometry.  
zFailOperationBack | What to do with the contents of the buffer if the stencil test passes, but the depth test fails for back-facing geometry.  
compareFunction | The function used to compare the reference value to the current contents of the buffer.  
passOperation | What to do with the contents of the buffer if the stencil test (and the depth test) passes.  
failOperation | What to do with the contents of the buffer if the stencil test fails.  
zFailOperation | What to do with the contents of the buffer if the stencil test passes, but the depth test.  
  
### Description

Creates a new stencil state with the given values.

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

