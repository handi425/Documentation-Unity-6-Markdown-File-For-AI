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

# StencilState

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

Values for the stencil state.

Use this with [RenderStateBlock](Rendering.RenderStateBlock.html) and
ScriptableRenderContext.DrawRenderers to override the GPU's render state.  
  
Corresponds to the `Stencil` command in [ShaderLab](../Manual/SL-
Reference.html).  
  
Additional resources: [RenderStateBlock](Rendering.RenderStateBlock.html),
[[ScriptableRenderContext.DrawRenderers], [ShaderLab command:
Stencil](../Manual/SL-Stencil.html).

### Static Properties

[defaultValue](Rendering.StencilState-defaultValue.html)| Default values for
the stencil state.  
---|---  
  
### Properties

[compareFunctionBack](Rendering.StencilState-compareFunctionBack.html)| The
function used to compare the reference value to the current contents of the
buffer for back-facing geometry.  
---|---  
[compareFunctionFront](Rendering.StencilState-compareFunctionFront.html)| The
function used to compare the reference value to the current contents of the
buffer for front-facing geometry.  
[enabled](Rendering.StencilState-enabled.html)| Controls whether the stencil
buffer is enabled.  
[failOperationBack](Rendering.StencilState-failOperationBack.html)| What to do
with the contents of the buffer if the stencil test fails for back-facing
geometry.  
[failOperationFront](Rendering.StencilState-failOperationFront.html)| What to
do with the contents of the buffer if the stencil test fails for front-facing
geometry.  
[passOperationBack](Rendering.StencilState-passOperationBack.html)| What to do
with the contents of the buffer if the stencil test (and the depth test)
passes for back-facing geometry.  
[passOperationFront](Rendering.StencilState-passOperationFront.html)| What to
do with the contents of the buffer if the stencil test (and the depth test)
passes for front-facing geometry.  
[readMask](Rendering.StencilState-readMask.html)| An 8 bit mask as an 0–255
integer, used when comparing the reference value with the contents of the
buffer.  
[writeMask](Rendering.StencilState-writeMask.html)| An 8 bit mask as an 0–255
integer, used when writing to the buffer.  
[zFailOperationBack](Rendering.StencilState-zFailOperationBack.html)| What to
do with the contents of the buffer if the stencil test passes, but the depth
test fails for back-facing geometry.  
[zFailOperationFront](Rendering.StencilState-zFailOperationFront.html)| What
to do with the contents of the buffer if the stencil test passes, but the
depth test fails for front-facing geometry.  
  
### Constructors

[StencilState](Rendering.StencilState-ctor.html)| Creates a new stencil state
with the given values.  
---|---  
  
### Public Methods

[SetCompareFunction](Rendering.StencilState.SetCompareFunction.html)| The
function used to compare the reference value to the current contents of the
buffer.  
---|---  
[SetFailOperation](Rendering.StencilState.SetFailOperation.html)| What to do
with the contents of the buffer if the stencil test fails.  
[SetPassOperation](Rendering.StencilState.SetPassOperation.html)| What to do
with the contents of the buffer if the stencil test (and the depth test)
passes.  
[SetZFailOperation](Rendering.StencilState.SetZFailOperation.html)| What to do
with the contents of the buffer if the stencil test passes, but the depth test
fails.  
  
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

