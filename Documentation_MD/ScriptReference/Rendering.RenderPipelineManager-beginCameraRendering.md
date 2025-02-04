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
[RenderPipelineManager](Rendering.RenderPipelineManager.html).beginCameraRendering

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

Delegate that you can use to invoke custom code before Unity renders an
individual Camera.

When Unity calls
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html),
it executes the methods in this delegate's invocation list.  
  
In the Universal Render Pipeline (URP) and the High Definition Render Pipeline
(HDRP), Unity calls
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html)
automatically. If you are writing a custom Scriptable Render Pipeline and you
want to use this delegate, you must add a call to
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html).  
  
The following code example demonstrates how to add a method to this delegate's
invocation list, and later remove it.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [RenderPipelineManager.beginCameraRendering](Rendering.RenderPipelineManager-beginCameraRendering.html) += OnBeginCameraRendering;
        }  
      
        void OnBeginCameraRendering([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html) camera)
        {
            // Put the code that you want to execute before the camera renders here
            // If you are using URP or HDRP, Unity calls this method automatically
            // If you are writing a custom SRP, you must call [RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html)
        }  
      
        void OnDestroy()
        {
            [RenderPipelineManager.beginCameraRendering](Rendering.RenderPipelineManager-beginCameraRendering.html) -= OnBeginCameraRendering;
        }
    }
    

Additional resources:
[RenderPipeline.BeginCameraRendering](Rendering.RenderPipeline.BeginCameraRendering.html),
[RenderPipeline.EndCameraRendering](Rendering.RenderPipeline.EndCameraRendering.html),
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

