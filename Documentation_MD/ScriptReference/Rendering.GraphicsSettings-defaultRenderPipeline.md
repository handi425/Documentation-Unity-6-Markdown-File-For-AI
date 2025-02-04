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

#  [GraphicsSettings](Rendering.GraphicsSettings.html).defaultRenderPipeline

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

public static
[Rendering.RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
defaultRenderPipeline;

### Description

The [RenderPipelineAsset](Rendering.RenderPipelineAsset.html) that defines the
default render pipeline.

If this value is `null`, the default render pipeline is the Built-in Render
Pipeline. Otherwise, the default render pipeline is the
[RenderPipeline](Rendering.RenderPipeline.html) defined in this
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html).  
  
Unity uses this value and the override value in
[QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) to
determine the active render pipeline for the current quality level. For more
information, see
[GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html).  
  
In the Unity Editor, this property corresponds to the **Render Pipeline
Setting** field in the **Graphics Settings** window.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ActiveRenderPipelineExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // In the Inspector, assign a Render Pipeline [Asset](VersionControl.Asset.html) to each of these fields
        public [RenderPipelineAsset](Rendering.RenderPipelineAsset.html) defaultRenderPipelineAsset;
        public [RenderPipelineAsset](Rendering.RenderPipelineAsset.html) overrideRenderPipelineAsset;  
      
        void Start()
        {
            [GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) = defaultRenderPipelineAsset;
            [QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) = overrideRenderPipelineAsset;  
      
            DisplayCurrentRenderPipeline();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // When the user presses the left shift key, switch the default render pipeline
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.LeftShift](KeyCode.LeftShift.html)))
            {
                SwitchDefaultRenderPipeline();
                DisplayCurrentRenderPipeline();
            }
            // When the user presses the right shift key, switch the override render pipeline
            else if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.RightShift](KeyCode.RightShift.html)))
            {
                SwitchOverrideRenderPipeline();
                DisplayCurrentRenderPipeline();
            }
        }  
      
        // [Switch](PlayerSettings.Switch.html) the default render pipeline between null,
        // and the render pipeline defined in defaultRenderPipelineAsset
        void SwitchDefaultRenderPipeline()
        {
            if ([GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) == defaultRenderPipelineAsset)
            {
                [GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) = null;
            }
            else
            {
                [GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) = defaultRenderPipelineAsset;
            }
        }  
      
        // [Switch](PlayerSettings.Switch.html) the override render pipeline between null,
        // and the render pipeline defined in overrideRenderPipelineAsset
        void SwitchOverrideRenderPipeline()
        {
            if ([QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) == overrideRenderPipelineAsset)
            {
                [QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) = null;
            }
            else
            {
                [QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) = overrideRenderPipelineAsset;
            }
        }  
      
        // Print the current render pipeline information to the console
        void DisplayCurrentRenderPipeline()
        {
            // [GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) determines the default render pipeline
            // If it is null, the default is the Built-in Render Pipeline
            if ([GraphicsSettings.defaultRenderPipeline](Rendering.GraphicsSettings-defaultRenderPipeline.html) != null)
            {
                [Debug.Log](Debug.Log.html)("The default render pipeline is defined by " + GraphicsSettings.defaultRenderPipeline.name);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("The default render pipeline is the Built-in Render Pipeline");
            }  
      
            // [QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) determines the override render pipeline for the current quality level
            // If it is null, no override exists for the current quality level
            if ([QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) != null)
            {
                [Debug.Log](Debug.Log.html)("The override render pipeline for the current quality level is defined by " + QualitySettings.renderPipeline.name);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("No override render pipeline exists for the current quality level");
            }  
      
            // If an override render pipeline is defined, Unity uses that
            // Otherwise, it falls back to the default value
            if ([QualitySettings.renderPipeline](QualitySettings-renderPipeline.html) != null)
            {
                [Debug.Log](Debug.Log.html)("The active render pipeline is the override render pipeline");
            }
            else
            {
                [Debug.Log](Debug.Log.html)("The active render pipeline is the default render pipeline");
            }  
      
            // To get a reference to the Render Pipeline [Asset](VersionControl.Asset.html) that defines the active render pipeline,
            // without knowing if it is the default or an override, use [GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-currentRenderPipeline.html)
            if ([GraphicsSettings.currentRenderPipeline](Rendering.GraphicsSettings-currentRenderPipeline.html) != null)
            {
                [Debug.Log](Debug.Log.html)("The active render pipeline is defined by " + GraphicsSettings.currentRenderPipeline.name);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("The active render pipeline is the Built-in Render Pipeline");
            }
        }
    }
    

Additional resources: [How to get, set, and configure the active render
pipeline](../Manual/srp-setting-render-pipeline-asset.html),
[currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html), [QualitySettings.renderPipeline](QualitySettings-
renderPipeline.html),
[RenderPipelineManager.activeRenderPipelineTypeChanged](Rendering.RenderPipelineManager-
activeRenderPipelineTypeChanged.html)

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

