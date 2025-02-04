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
[RenderPipelineManager](Rendering.RenderPipelineManager.html).activeRenderPipelineCreated

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

Delegate that you can use to invoke custom code right after
[RenderPipelineManager.currentPipeline](Rendering.RenderPipelineManager-
currentPipeline.html) is created.

Unity does not switch the render pipeline immediately when you set
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html) or
[QualitySettings.renderPipeline](QualitySettings-renderPipeline.html). Unity
only instantiate a new `RenderPipeline` instance the first time any
[Camera](Camera.html) renders after you set a new `RenderPipelineAsset`. You
can subscribe to this event to know that `RenderPipeline` is created. To
access the current pipeline object you can rely on
[RenderPipelineManager.currentPipeline](Rendering.RenderPipelineManager-
currentPipeline.html) which will point to the newly created `RenderPipeline`.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    
    public class CurrentRenderPipelineCreatedExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [RenderPipelineManager.activeRenderPipelineCreated](Rendering.RenderPipelineManager-activeRenderPipelineCreated.html) += RenderPipelineManager_activeRenderPipelineCreated;
        }  
      
        private void OnDestroy()
        {
            [RenderPipelineManager.activeRenderPipelineCreated](Rendering.RenderPipelineManager-activeRenderPipelineCreated.html) -= RenderPipelineManager_activeRenderPipelineCreated;
        }  
      
        private void RenderPipelineManager_activeRenderPipelineCreated()
        {
            [Debug.Log](Debug.Log.html)($"Render Pipeline {RenderPipelineManager.currentPipeline.GetType().Name} is created.");
        }
    }
    

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

