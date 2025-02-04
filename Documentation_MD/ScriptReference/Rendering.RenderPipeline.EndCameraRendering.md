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

#  [RenderPipeline](Rendering.RenderPipeline.html).EndCameraRendering

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

protected static void
EndCameraRendering([Rendering.ScriptableRenderContext](Rendering.ScriptableRenderContext.html)
context, [Camera](Camera.html) camera);

### Description

Calls the
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html) delegate.

In the Universal Render Pipeline (URP) and the High Definition Render Pipeline
(HDRP), Unity calls this method automatically after performing rendering
operations for an individual Camera. If you are writing a custom Scriptable
Render Pipeline, you can call this method manually to use the
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html) delegate.  
  
The following code example demonstrates where to call this method if you are
creating a custom Scriptable Render Pipeline:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipelineInstance : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipelineInstance()
        {
        }  
      
        override protected void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            for (var i = 0; i < cameras.Length; i++)
            {
                var camera = cameras[i];  
      
                // Put your code for rendering the [Camera](Camera.html) here  
      
                // Call the [RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-endCameraRendering.html) delegate
                EndCameraRendering(context, camera);
            }
        }
    }
    

Additional resources:
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html),
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html),
[RenderPipeline.BeginFrameRendering](Rendering.RenderPipeline.BeginFrameRendering.html),
[RenderPipeline.EndFrameRendering](Rendering.RenderPipeline.EndFrameRendering.html),
[Unity Manual: Scriptable Render
Pipeline](../Manual/ScriptableRenderPipeline.html)

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

