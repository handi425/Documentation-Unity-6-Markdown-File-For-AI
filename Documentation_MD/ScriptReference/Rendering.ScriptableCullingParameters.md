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

# ScriptableCullingParameters

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

Parameters that configure a culling operation in the Scriptable Render
Pipeline.

Obtain a ScriptableCullingParameters struct by calling
[Camera.TryGetCullingParameters](Camera.TryGetCullingParameters.html).  
  
Note that you can obtain and view a ScriptableCullingParameters struct from a
Camera in the Built-in Render Pipeline; however, changing the values has no
effect.  
  
The following Scriptable Render Pipeline code demonstrates how to obtain a
ScriptableCullingParameters struct from a Camera using
[Camera.TryGetCullingParameters](Camera.TryGetCullingParameters.html),
configure the struct, and then pass the struct to
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html) to
obtain a [CullingResults](Rendering.CullingResults.html) struct. You can then
use the [CullingResults](Rendering.CullingResults.html) struct in a call to
ScriptableRenderContext.DrawRenderers.

    
    
    using UnityEngine;
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
                // Change culling parameters to configure the culling operation
                cullingParameters.cullingOptions &= ~[CullingOptions.OcclusionCull](Rendering.CullingOptions.OcclusionCull.html);
                cullingParameters.isOrthographic = false;  
      
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
[Camera.TryGetCullingParameters](Camera.TryGetCullingParameters.html),
[ScriptableRenderContext.Cull](Rendering.ScriptableRenderContext.Cull.html),
[CullingResults](Rendering.CullingResults.html),
ScriptableRenderContext.DrawRenderers.

### Static Properties

[cullingJobsLowerLimit](Rendering.ScriptableCullingParameters-
cullingJobsLowerLimit.html)| The lower limit to the value
ScriptableCullingParameters.maximumPortalCullingJobs.  
---|---  
[cullingJobsUpperLimit](Rendering.ScriptableCullingParameters-
cullingJobsUpperLimit.html)| The upper limit to the value
ScriptableCullingParameters.maximumPortalCullingJobs.  
[layerCount](Rendering.ScriptableCullingParameters-layerCount.html)| The
amount of layers available.  
[maximumCullingPlaneCount](Rendering.ScriptableCullingParameters-
maximumCullingPlaneCount.html)| Maximum amount of culling planes that can be
specified.  
  
### Properties

[accurateOcclusionThreshold](Rendering.ScriptableCullingParameters-
accurateOcclusionThreshold.html)| This parameter determines query distance for
occlusion culling.  
---|---  
[cameraProperties](Rendering.ScriptableCullingParameters-
cameraProperties.html)| Camera Properties used for culling.  
[conservativeEnclosingSphere](Rendering.ScriptableCullingParameters-
conservativeEnclosingSphere.html)| This property enables a conservative method
for calculating the size and position of the minimal enclosing sphere around
the frustum cascade corner points for shadow culling.  
[cullingMask](Rendering.ScriptableCullingParameters-cullingMask.html)| The
mask for the culling operation.  
[cullingMatrix](Rendering.ScriptableCullingParameters-cullingMatrix.html)| The
matrix for the culling operation.  
[cullingOptions](Rendering.ScriptableCullingParameters-cullingOptions.html)|
Flags to configure a culling operation in the Scriptable Render Pipeline.  
[cullingPlaneCount](Rendering.ScriptableCullingParameters-
cullingPlaneCount.html)| Number of culling planes to use.  
[isOrthographic](Rendering.ScriptableCullingParameters-isOrthographic.html)|
Is the cull orthographic.  
[lodParameters](Rendering.ScriptableCullingParameters-lodParameters.html)|
LODParameters for culling.  
[maximumPortalCullingJobs](Rendering.ScriptableCullingParameters-
maximumPortalCullingJobs.html)| This parameter controls how many active jobs
contribute to occlusion culling.  
[maximumVisibleLights](Rendering.ScriptableCullingParameters-
maximumVisibleLights.html)| This parameter controls how many visible lights
are allowed.  
[numIterationsEnclosingSphere](Rendering.ScriptableCullingParameters-
numIterationsEnclosingSphere.html)|  
[origin](Rendering.ScriptableCullingParameters-origin.html)| Position for the
origin of the cull.  
[reflectionProbeSortingCriteria](Rendering.ScriptableCullingParameters-
reflectionProbeSortingCriteria.html)| Reflection Probe Sort options for the
cull.  
[shadowDistance](Rendering.ScriptableCullingParameters-shadowDistance.html)|
Shadow distance to use for the cull.  
[shadowNearPlaneOffset](Rendering.ScriptableCullingParameters-
shadowNearPlaneOffset.html)| Offset to apply to the near camera plane when
performing shadow map rendering.  
[stereoProjectionMatrix](Rendering.ScriptableCullingParameters-
stereoProjectionMatrix.html)| The projection matrix generated for single-pass
stereo culling.  
[stereoSeparationDistance](Rendering.ScriptableCullingParameters-
stereoSeparationDistance.html)| Distance between the virtual eyes.  
[stereoViewMatrix](Rendering.ScriptableCullingParameters-
stereoViewMatrix.html)| The view matrix generated for single-pass stereo
culling.  
  
### Public Methods

[GetCullingPlane](Rendering.ScriptableCullingParameters.GetCullingPlane.html)|
Fetch the culling plane at the given index.  
---|---  
[GetLayerCullingDistance](Rendering.ScriptableCullingParameters.GetLayerCullingDistance.html)|
Get the distance for the culling of a specific layer.  
[SetCullingPlane](Rendering.ScriptableCullingParameters.SetCullingPlane.html)|
Set the culling plane at a given index.  
[SetLayerCullingDistance](Rendering.ScriptableCullingParameters.SetLayerCullingDistance.html)|
Set the distance for the culling of a specific layer.  
  
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

