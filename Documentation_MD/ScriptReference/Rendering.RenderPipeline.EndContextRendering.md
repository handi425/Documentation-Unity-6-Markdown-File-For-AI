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

#  [RenderPipeline](Rendering.RenderPipeline.html).EndContextRendering

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
EndContextRendering([Rendering.ScriptableRenderContext](Rendering.ScriptableRenderContext.html)
context, List<Camera> cameras);

### Description

Calls the
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) and
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html) delegates.

Use the delegates that this method calls to implement functionality at the end
of [RenderPipeline.Render](Rendering.RenderPipeline.Render.html).  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline
(HDRP), Unity calls this method automatically at the end of
[RenderPipeline.Render](Rendering.RenderPipeline.Render.html). If you are
writing a custom Scriptable Render Pipeline, you can call this method yourself
in the same place. This functionality is not compatible with the Built-in
Render Pipeline.  
  
The delegates that this method calls work in the same way as one another,
except that
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html) causes heap allocations and
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) does not. You should therefore use
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) to avoid unnecessary heap allocations and garbage
collection.  
  
This method replaces
[RenderPipeline.EndFrameRendering](Rendering.RenderPipeline.EndFrameRendering.html).
It does everything that method does, and in addition it calls the
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html) delegate. If you are writing a custom Scriptable
Render Pipeline, use this method instead of
[RenderPipeline.EndFrameRendering](Rendering.RenderPipeline.EndFrameRendering.html).  
  
The following code example demonstrates where to call this method if you are
creating a custom Scriptable Render Pipeline:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections.Generic;  
      
    public class ExampleRenderPipelineInstance : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipelineInstance()
        {
        }  
      
        override protected void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, List<[Camera](Camera.html)> cameras)
        {
            // Put the rest of your Render method code here  
      
            // Call the [RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-endContextRendering.html) and [RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-endFrameRendering.html) delegates
            EndContextRendering(context, cameras);
        }  
      
        // Older version of the Render function that can generate garbage, needed for backwards compatibility
        override protected void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
        }
    }
    

Additional resources:
[RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-
endContextRendering.html),
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html),
[RenderPipeline.BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html),
[RenderPipelineManager.beginContextRendering](Rendering.RenderPipelineManager-
beginContextRendering.html),
[RenderPipelineManager.beginFrameRendering](Rendering.RenderPipelineManager-
beginFrameRendering.html), [Unity Manual: Scriptable Render
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

