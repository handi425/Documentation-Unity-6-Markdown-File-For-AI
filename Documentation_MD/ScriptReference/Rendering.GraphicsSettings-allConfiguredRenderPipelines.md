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
[GraphicsSettings](Rendering.GraphicsSettings.html).allConfiguredRenderPipelines

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

public static RenderPipelineAsset[] allConfiguredRenderPipelines;

### Description

An array containing the
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html) instances that
describe the default render pipeline and any quality level overrides.

The default render pipeline is defined in
[GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-
defaultRenderPipeline.html). The override render pipeline for the current
quality level is defined in [QualitySettings.renderPipeline](QualitySettings-
renderPipeline.html), or you can request the override value for a given
quality level with
[QualitySettings.GetRenderPipelineAssetAt](QualitySettings.GetRenderPipelineAssetAt.html).  
  
This property returns all instances of
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html) that are assigned to
these fields. The same
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html) can appear in this
array more than once, if it is assigned to more than one field.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class AllConfiguredRenderPipelinesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)("All Render Pipeline Assets that define the default render pipeline, or an override: ");
            foreach (var asset in [GraphicsSettings.allConfiguredRenderPipelines](Rendering.GraphicsSettings-allConfiguredRenderPipelines.html))
            {
                [Debug.Log](Debug.Log.html)(asset.name);
            }
        }
    }
    

Additional resources: [How to get, set, and configure the active render
pipeline](../Manual/srp-setting-render-pipeline-asset.html),
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html),
[GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-
defaultRenderPipeline.html), [QualitySettings.renderPipeline](QualitySettings-
renderPipeline.html).

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

