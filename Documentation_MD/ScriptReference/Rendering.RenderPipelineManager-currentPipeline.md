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
[RenderPipelineManager](Rendering.RenderPipelineManager.html).currentPipeline

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

public static [Rendering.RenderPipeline](Rendering.RenderPipeline.html)
currentPipeline;

### Description

Returns the active [RenderPipeline](Rendering.RenderPipeline.html).

The active render pipeline is the render pipeline that Unity is currently
using to render your application and parts of the Editor such as the Scene
view and Game view. The active render pipeline can be a default value, or you
can set override values for different quality levels.  
  
Unity updates this property only after rendering at least one frame with the
active render pipeline, which can take up to four calls to
[Update](MonoBehaviour.Update.html). This means that this property is `null`
on startup, and does not immediately reflect changes to the active render
pipeline.  
  
You can access the [RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
that defines the active render pipeline with
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html). `GraphicsSettings.currentRenderPipeline` is
always up to date, which means that you can query it on startup or immediately
after changing the active render pipeline.  
  
Additional resources: [How to get, set, and configure the active render
pipeline](../Manual/srp-setting-render-pipeline-asset.html),
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html),
[GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-
defaultRenderPipeline.html), [QualitySettings.renderPipeline](QualitySettings-
renderPipeline.html),
[RenderPipelineManager.activeRenderPipelineTypeChanged](Rendering.RenderPipelineManager-
activeRenderPipelineTypeChanged.html).

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

