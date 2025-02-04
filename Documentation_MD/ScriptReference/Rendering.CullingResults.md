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

# CullingResults

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

A struct containing the results of a culling operation.

In the Scriptable Render Pipeline, when Unity performs a culling operation, it
stores the results in a `CullingResults` struct. This data includes
information about visible objects, lights, and reflection probes. Unity uses
this data to render objects and process lights. A `CullingResults` struct also
provides several functions to aid shadow rendering.  
  
To obtain a `CullingResults` struct, call
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html).  
  
A `CullingResults` struct is valid within the scope of a
[RenderPipeline.Render](Rendering.RenderPipeline.Render.html) function; its
data goes out of scope when the `Render` function returns. You can use the
same `CullingResults` struct multiple times within the same render loop, and
you can share a `CullingResults` struct between multiple
[Cameras](Camera.html) if you know that they can see the same objects. This
can save on wasted CPU operations, and therefore improve performance.  
  
This example demonstrates how to obtain a `CullingResults` struct, and then
pass it to ScriptableRenderContext.DrawRenderers.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipeline()
        {
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            foreach ([Camera](Camera.html) camera in cameras)
            {
                // Get the culling parameters from the current camera
                camera.TryGetCullingParameters(out var cullingParameters);  
      
                // Schedule the cull operation that populates the [CullingResults](Rendering.CullingResults.html) struct
                [CullingResults](Rendering.CullingResults.html) cullingResults = context.Cull(ref cullingParameters);  
      
                // Place code that schedules drawing operations using the [CullingResults](Rendering.CullingResults.html) struct here
                // See ScriptableRenderContext.DrawRenderers for details and examples
                // …  
      
                // Execute all of the scheduled operations, in order
                context.Submit();
            }
        }
    }
    

### Properties

[lightAndReflectionProbeIndexCount](Rendering.CullingResults-
lightAndReflectionProbeIndexCount.html)| Gets the number of per-object light
and reflection probe indices.  
---|---  
[lightIndexCount](Rendering.CullingResults-lightIndexCount.html)| Gets the
number of per-object light indices.  
[reflectionProbeIndexCount](Rendering.CullingResults-
reflectionProbeIndexCount.html)| Gets the number of per-object reflection
probe indices.  
[visibleLights](Rendering.CullingResults-visibleLights.html)| Array of visible
lights.  
[visibleOffscreenVertexLights](Rendering.CullingResults-
visibleOffscreenVertexLights.html)| Off-screen lights that still affect
visible vertices.  
[visibleReflectionProbes](Rendering.CullingResults-
visibleReflectionProbes.html)| Array of visible reflection probes.  
  
### Public Methods

[ComputeDirectionalShadowMatricesAndCullingPrimitives](Rendering.CullingResults.ComputeDirectionalShadowMatricesAndCullingPrimitives.html)|
Calculates the view and projection matrices and shadow split data for a
directional light.  
---|---  
[ComputePointShadowMatricesAndCullingPrimitives](Rendering.CullingResults.ComputePointShadowMatricesAndCullingPrimitives.html)|
Calculates the view and projection matrices and shadow split data for a point
light.  
[ComputeSpotShadowMatricesAndCullingPrimitives](Rendering.CullingResults.ComputeSpotShadowMatricesAndCullingPrimitives.html)|
Calculates the view and projection matrices and shadow split data for a spot
light.  
[FillLightAndReflectionProbeIndices](Rendering.CullingResults.FillLightAndReflectionProbeIndices.html)|
Fills a buffer with per-object light indices.  
[GetLightIndexMap](Rendering.CullingResults.GetLightIndexMap.html)| If a
RenderPipeline sorts or otherwise modifies the VisibleLight list, an index
remap will be necessary to properly make use of per-object light lists.  
[GetReflectionProbeIndexMap](Rendering.CullingResults.GetReflectionProbeIndexMap.html)|
If a RenderPipeline sorts or otherwise modifies the VisibleReflectionProbe
list, an index remap will be necessary to properly make use of per-object
reflection probe lists.  
[GetShadowCasterBounds](Rendering.CullingResults.GetShadowCasterBounds.html)|
Returns the bounding box that encapsulates the visible shadow casters. Can be
used to, for instance, dynamically adjust cascade ranges.  
[SetLightIndexMap](Rendering.CullingResults.SetLightIndexMap.html)| If a
RenderPipeline sorts or otherwise modifies the VisibleLight list, an index
remap will be necessary to properly make use of per-object light lists.  
[SetReflectionProbeIndexMap](Rendering.CullingResults.SetReflectionProbeIndexMap.html)|
If a RenderPipeline sorts or otherwise modifies the VisibleReflectionProbe
list, an index remap will be necessary to properly make use of per-object
reflection probe lists.  
  
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

