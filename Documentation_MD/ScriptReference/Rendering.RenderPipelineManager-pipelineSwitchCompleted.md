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
[RenderPipelineManager](Rendering.RenderPipelineManager.html).pipelineSwitchCompleted

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

public static bool pipelineSwitchCompleted;

### Description

Indicate when Render Pipeline switch is in progress.

The value is `false` if the render pipeline is in the process of being
switched. The value is `true` if the switch has completed and the render
pipeline is ready for use.  
  
Unity doesn't switch the render pipeline immediately when you set
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html) or
[QualitySettings.renderPipeline](QualitySettings-renderPipeline.html). Unity
only initializes a new [RenderPipeline](Rendering.RenderPipeline.html)
instance the first time any [Camera](Camera.html) renders after you set a new
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html). You can use this
property to check if this has happened and the switch has finished.  
  
You can also subscribe to the
[RenderPipelineManager.activeRenderPipelineAssetChanged](Rendering.RenderPipelineManager-
activeRenderPipelineAssetChanged.html) and
[RenderPipelineManager.activeRenderPipelineTypeChanged](Rendering.RenderPipelineManager-
activeRenderPipelineTypeChanged.html) callbacks on the
[RenderPipelineManager](Rendering.RenderPipelineManager.html) if you want to
receive a callback instead of using a property.

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

