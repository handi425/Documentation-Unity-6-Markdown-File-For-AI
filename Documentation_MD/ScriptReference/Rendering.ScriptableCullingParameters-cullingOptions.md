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
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html).cullingOptions

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

public [Rendering.CullingOptions](Rendering.CullingOptions.html)
cullingOptions;

### Description

Flags to configure a culling operation in the Scriptable Render Pipeline.

Unity sets some of the [CullingOptions](Rendering.CullingOptions.html) flags
with default values, and others depending on the properties of the
[Camera](Camera.html) from which you obtained the
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html)
struct. You can override these values before performing the culling operation.  
  
The following example demonstrates how to retrieve a
ScriptableCullingParameters object from a Camera, disable occlusion culling on
the ScriptableCullingParameters object by unsetting the
CullingOptions.OcclusionCull flag, and then use the
ScriptableCullingParameters object in a culling operation.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipelineInstance : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipelineInstance()
        {
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            // Get the culling parameters from the desired [Camera](Camera.html)
            if (cameras[0].TryGetCullingParameters(out var cullingParameters))
            {
                // Disable occlusion culling
                cullingParameters.cullingOptions &= ~[CullingOptions.OcclusionCull](Rendering.CullingOptions.OcclusionCull.html);  
      
                // Schedule the cull operation
                [CullingResults](Rendering.CullingResults.html) cullingResults = context.Cull(ref cullingParameters);  
      
                // Place code that schedules drawing operations using the [CullingResults](Rendering.CullingResults.html) struct here
                // See ScriptableRenderContext.DrawRenderers for details and examples
                // …  
      
                // Execute all of the scheduled operations, in order
                context.Submit();
            }
        }
    }
    

Additional resources:
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html),
[Camera](Camera.html).

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

