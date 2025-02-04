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
[RenderPipelineManager](Rendering.RenderPipelineManager.html).endContextRendering

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

Delegate that you can use to invoke custom code at the end of
[RenderPipeline.Render](Rendering.RenderPipeline.Render.html).

When Unity calls
[RenderPipeline.BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html)
at the end of [RenderPipeline.Render](Rendering.RenderPipeline.Render.html),
it executes the methods in this delegate's invocation list.  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline
(HDRP), Unity calls
[RenderPipeline.BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html)
automatically. If you are writing a custom Scriptable Render Pipeline, you
must call the method yourself. This functionality is not compatible with the
Built-in Render Pipeline.  
  
This delegate works in the same way as
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html), except that this version does not cause heap
allocations.  
  
The following code example demonstrates how to add a method to this delegate's
invocation list, and later remove it.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections.Generic;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-endContextRendering.html) += OnEndContextRendering;
        }  
      
        void OnEndContextRendering([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, List<[Camera](Camera.html)> cameras)
        {
            // Put the code that you want to execute at the end of [RenderPipeline.Render](Rendering.RenderPipeline.Render.html) here
        }  
      
        void OnDestroy()
        {
            [RenderPipelineManager.endContextRendering](Rendering.RenderPipelineManager-endContextRendering.html) -= OnEndContextRendering;
        }
    }
    

Additional resources:
[RenderPipeline.EndContextRendering](Rendering.RenderPipeline.EndContextRendering.html),
[RenderPipelineManager.beginContextRendering](Rendering.RenderPipelineManager-
beginContextRendering.html),
[RenderPipeline.BeginContextRendering](Rendering.RenderPipeline.BeginContextRendering.html),
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

