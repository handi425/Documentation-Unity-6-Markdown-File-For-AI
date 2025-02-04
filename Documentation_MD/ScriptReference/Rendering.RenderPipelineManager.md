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

# RenderPipelineManager

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

Render Pipeline manager.

### Static Properties

[currentPipeline](Rendering.RenderPipelineManager-currentPipeline.html)|
Returns the active RenderPipeline.  
---|---  
[pipelineSwitchCompleted](Rendering.RenderPipelineManager-
pipelineSwitchCompleted.html)| Indicate when Render Pipeline switch is in
progress.  
  
### Events

[activeRenderPipelineAssetChanged](Rendering.RenderPipelineManager-
activeRenderPipelineAssetChanged.html)| Delegate that you can use to invoke
custom code when the current RenderPipelineAsset between frames has changed.  
---|---  
[activeRenderPipelineCreated](Rendering.RenderPipelineManager-
activeRenderPipelineCreated.html)| Delegate that you can use to invoke custom
code right after RenderPipelineManager.currentPipeline is created.  
[activeRenderPipelineDisposed](Rendering.RenderPipelineManager-
activeRenderPipelineDisposed.html)| Delegate that you can use to invoke custom
code right before RenderPipelineManager.currentPipeline is disposed.  
[activeRenderPipelineTypeChanged](Rendering.RenderPipelineManager-
activeRenderPipelineTypeChanged.html)| Delegate that you can use to invoke
custom code when Unity changes the active render pipeline, and the new
RenderPipeline has a different type to the old one.  
[beginCameraRendering](Rendering.RenderPipelineManager-
beginCameraRendering.html)| Delegate that you can use to invoke custom code
before Unity renders an individual Camera.  
[beginContextRendering](Rendering.RenderPipelineManager-
beginContextRendering.html)| Delegate that you can use to invoke custom code
at the start of RenderPipeline.Render.  
[beginFrameRendering](Rendering.RenderPipelineManager-
beginFrameRendering.html)| Delegate that you can use to invoke custom code at
the start of RenderPipeline.Render.  
[endCameraRendering](Rendering.RenderPipelineManager-endCameraRendering.html)|
Delegate that you can use to invoke custom code after Unity renders an
individual Camera.  
[endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html)| Delegate that you can use to invoke custom code at
the end of RenderPipeline.Render.  
[endFrameRendering](Rendering.RenderPipelineManager-endFrameRendering.html)|
Delegate that you can use to invoke custom code at the end of
RenderPipeline.Render.  
  
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

