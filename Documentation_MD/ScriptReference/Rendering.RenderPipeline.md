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

# RenderPipeline

class in UnityEngine.Rendering

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

Defines a series of commands and settings that describes how Unity renders a
frame.

### Properties

[disposed](Rendering.RenderPipeline-disposed.html)| Returns true when the
RenderPipeline is invalid or destroyed.  
---|---  
  
### Public Methods

[ProcessRenderRequests](Rendering.RenderPipeline.ProcessRenderRequests.html)|
Executes RenderRequests submitted using Camera.SubmitRenderRequests.  
---|---  
  
### Protected Methods

[IsRenderRequestSupported](Rendering.RenderPipeline.IsRenderRequestSupported.html)|
Returns true when the active render pipeline supports the RenderRequest type.  
---|---  
[Render](Rendering.RenderPipeline.Render.html)| Entry point method that
defines custom rendering for this RenderPipeline.  
  
### Static Methods

[BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html)|
Calls the RenderPipelineManager.beginCameraRendering delegate.  
---|---  
[BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html)|
Calls the RenderPipelineManager.beginContextRendering and
RenderPipelineManager.beginFrameRendering delegates.  
[BeginFrameRendering](Rendering.RenderPipeline.BeginFrameRendering.html)|
Calls the RenderPipelineManager.beginFrameRendering delegate.  
[EndCameraRendering](Rendering.RenderPipeline.EndCameraRendering.html)| Calls
the RenderPipelineManager.endCameraRendering delegate.  
[EndContextRendering](Rendering.RenderPipeline.EndContextRendering.html)|
Calls the RenderPipelineManager.endContextRendering and
RenderPipelineManager.endFrameRendering delegates.  
[EndFrameRendering](Rendering.RenderPipeline.EndFrameRendering.html)| Calls
the RenderPipelineManager.endFrameRendering delegate.  
[SubmitRenderRequest](Rendering.RenderPipeline.SubmitRenderRequest.html)|
Submit a renderRequest.  
[SupportsRenderRequest](Rendering.RenderPipeline.SupportsRenderRequest.html)|
Query the active render pipeline to check support for the given RequestData
type.  
  
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

