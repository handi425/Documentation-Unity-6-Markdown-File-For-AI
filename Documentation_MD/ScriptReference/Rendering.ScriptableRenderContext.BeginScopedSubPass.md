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
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).BeginScopedSubPass

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

public [Rendering.ScopedSubPass](Rendering.ScopedSubPass.html)
BeginScopedSubPass(NativeArray<int> colors, NativeArray<int> inputs, bool
isDepthReadOnly, bool isStencilReadOnly);

## Declaration

public [Rendering.ScopedSubPass](Rendering.ScopedSubPass.html)
BeginScopedSubPass(NativeArray<int> colors, NativeArray<int> inputs, bool
isDepthStencilReadOnly);

## Declaration

public [Rendering.ScopedSubPass](Rendering.ScopedSubPass.html)
BeginScopedSubPass(NativeArray<int> colors, bool isDepthReadOnly, bool
isStencilReadOnly);

## Declaration

public [Rendering.ScopedSubPass](Rendering.ScopedSubPass.html)
BeginScopedSubPass(NativeArray<int> colors, bool isDepthStencilReadOnly);

### Parameters

colors | Array of attachments to be used as the color render targets in this sub pass. These are specificed as indices into the array passed to [BeginRenderPass](Rendering.ScriptableRenderContext.BeginRenderPass.html). The values in the array are copied immediately.  
---|---  
inputs | Array of attachments to be used as input attachments in this sub pass. These are specificed as indices into the array passed to [BeginRenderPass](Rendering.ScriptableRenderContext.BeginRenderPass.html). The values in the array are copied immediately.  
isDepthStencilReadOnly | If true, both depth and stencil attachments are read-only in this sub pass. Some renderers require this in order to be able to use the depth and stencil attachments as inputs.  
isDepthReadOnly | If true, the depth attachment is read-only in this sub pass. Some renderers require this in order to be able to use the depth attachment as input.  
isStencilReadOnly | If true, the stencil attachment is read-only in this sub pass. Some renderers require this in order to be able to use the stencil attachment as input.  
  
### Description

Schedules the beginning of a new sub pass within a render pass. If you call
this in a using-statement, Unity executes EndSubPass automatically when
exiting the using-block. Render passes can never be standalone, they must
always contain at least one sub pass. Only one sub pass can be active at any
time.

This method does the same as
[BeginSubPass](Rendering.ScriptableRenderContext.BeginSubPass.html), but it
will return an _IDisposable_ that can be used in a _using_ -statement, and so
it is not necesssary to manually call
[EndSubPass](Rendering.ScriptableRenderContext.EndSubPass.html).  
  
Additional resources:
[BeginScopedRenderPass](Rendering.ScriptableRenderContext.BeginScopedRenderPass.html).

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

