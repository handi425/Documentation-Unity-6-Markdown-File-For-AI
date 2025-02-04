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

#  [RenderPipeline](Rendering.RenderPipeline.html).ProcessRenderRequests

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

protected void
ProcessRenderRequests([Rendering.ScriptableRenderContext](Rendering.ScriptableRenderContext.html)
context, [Camera](Camera.html) camera, RequestData renderRequest);

### Parameters

renderRequests | The list of `RenderRequests` to execute.  
---|---  
  
### Description

Executes `RenderRequests` submitted using Camera.SubmitRenderRequests.

Unity calls this method when the user calls Camera.SubmitRenderRequests.  
  
If the active `RenderPipeline` implements this method, Unity updates the
[RenderTexture](RenderTexture.html) assigned to the `results` property of each
[RenderRequest](Camera.RenderRequest.html) with the requested data.  
  
If the active `RenderPipeline` does not implement this method, Unity does
nothing; it performs a no-op, and every
[RenderRequests](Camera.RenderRequest.html) remains in the same state.  
  
If you are creating a custom Scriptable Render Pipeline you must ensure that
you implement this method as described, or do not implement it.  
  
Additional resources:
[RenderPipeline.SupportsRenderRequest](Rendering.RenderPipeline.SupportsRenderRequest.html),
[RenderPipeline.SubmitRenderRequest](Rendering.RenderPipeline.SubmitRenderRequest.html).

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

