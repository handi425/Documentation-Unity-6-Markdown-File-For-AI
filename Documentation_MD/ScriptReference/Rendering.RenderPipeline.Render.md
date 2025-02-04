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

#  [RenderPipeline](Rendering.RenderPipeline.html).Render

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
Render([Rendering.ScriptableRenderContext](Rendering.ScriptableRenderContext.html)
context, List<Camera> cameras);

### Description

Entry point method that defines custom rendering for this RenderPipeline.

This method is the entry point to the Scriptable Render Pipeline (SRP). This
functionality is not compatible with the Built-in Render Pipeline.  
  
Unity calls this method automatically. In a standalone application, Unity
calls this method once per frame to render the main view, and once per frame
for each manual call to [Camera.Render](Camera.Render.html). In the Unity
Editor, Unity calls this method once per frame for each Scene view or Game
view that is visible, once per frame if if the Scene camera preview is
visible, and once per frame for each manual call to
[Camera.Render](Camera.Render.html).  
  
If you are using the Universal Render Pipeline (URP) or the High Definition
Render Pipeline (HDRP), you can use the
[RenderPipelineManager.beginContextRendering](Rendering.RenderPipelineManager-
beginContextRendering.html),
[RenderPipelineManager.beginCameraRendering](Rendering.RenderPipelineManager-
beginCameraRendering.html),
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html) and
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) delegates to call your custom code at defined points
during this method.  
  
If you are writing a custom SRP, you can either add code directly to this
method body, or call the delegates yourself using
[RenderPipeline.BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html),
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html),
[RenderPipeline.EndCameraRendering](Rendering.RenderPipeline.EndCameraRendering.html)
and
[RenderPipeline.EndContextRendering](Rendering.RenderPipeline.EndContextRendering.html).  
  
The following example code shows how to implement this method in a custom SRP:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections.Generic;  
      
    public class ExampleRenderPipelineInstance : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipelineInstance()
        {
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, List<[Camera](Camera.html)> cameras)
        {
            // This is where you can write custom rendering code. Customize this method to customize your SRP.
            // Create and schedule a command to clear the current render target
            var cmd = new [CommandBuffer](Rendering.CommandBuffer.html)();
            cmd.ClearRenderTarget(true, true, [Color.red](Color-red.html));
            context.ExecuteCommandBuffer(cmd);
            cmd.Release();  
      
            // Tell the [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) to tell the graphics API to perform the scheduled commands
            context.Submit();
        }  
      
        // Older version of the Render function that can generate garbage, needed for backwards compatibility
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
        }
    }
    

Additional resources: [Unity Manual: Scriptable Render
Pipeline](../Manual/ScriptableRenderPipeline.html),
[RenderPipelineManager.beginContextRendering](Rendering.RenderPipelineManager-
beginContextRendering.html),
[RenderPipelineManager.beginCameraRendering](Rendering.RenderPipelineManager-
beginCameraRendering.html),
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html),
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html)

* * *

## Declaration

protected void
Render([Rendering.ScriptableRenderContext](Rendering.ScriptableRenderContext.html)
context, Camera[] cameras);

### Description

Entry point method that defines custom rendering for this RenderPipeline.

The functionality for this signature is exactly the same as for the version
that uses a List of Cameras, except that this version can cause heap
allocations due to array resizing.  
  
If you experience heap allocations, use the version that uses a List instead.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipeline()
        {
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            // This is where you can write custom rendering code. Customize this method to customize your SRP.
            // Create and schedule a command to clear the current render target
            var cmd = new [CommandBuffer](Rendering.CommandBuffer.html)();
            cmd.ClearRenderTarget(true, true, [Color.red](Color-red.html));
            context.ExecuteCommandBuffer(cmd);
            cmd.Release();  
      
            // Tell the [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) to tell the graphics API to perform the scheduled commands
            context.Submit();
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

