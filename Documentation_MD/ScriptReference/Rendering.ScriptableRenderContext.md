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

# ScriptableRenderContext

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

Defines state and drawing commands that custom render pipelines use.

When you define a custom [RenderPipeline](Rendering.RenderPipeline.html), you
use a ScriptableRenderContext to schedule and submit state updates and drawing
commands to the GPU.  
  
A [RenderPipeline.Render](Rendering.RenderPipeline.Render.html) method
implementation typically culls objects that the render pipeline doesn't need
to render for every Camera (see
[CullingResults](Rendering.CullingResults.html)), and then makes a series of
calls to ScriptableRenderContext.DrawRenderers intermixed with
[ScriptableRenderContext.ExecuteCommandBuffer](Rendering.ScriptableRenderContext.ExecuteCommandBuffer.html)
calls. These calls set up global Shader properties, change render targets,
dispatch compute shaders, and other rendering tasks. To actually execute the
render loop, call
[ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html).  
  
Additional resources: [RenderPipeline](Rendering.RenderPipeline.html).

### Public Methods

[BeginRenderPass](Rendering.ScriptableRenderContext.BeginRenderPass.html)|
Schedules the beginning of a new render pass. Only one render pass can be
active at any time.  
---|---  
[BeginScopedRenderPass](Rendering.ScriptableRenderContext.BeginScopedRenderPass.html)|
Schedules the beginning of a new render pass. If you call this a using-
statement, Unity calls EndRenderPass automatically when exiting the using-
block. Only one render pass can be active at any time.  
[BeginScopedSubPass](Rendering.ScriptableRenderContext.BeginScopedSubPass.html)|
Schedules the beginning of a new sub pass within a render pass. If you call
this in a using-statement, Unity executes EndSubPass automatically when
exiting the using-block. Render passes can never be standalone, they must
always contain at least one sub pass. Only one sub pass can be active at any
time.  
[BeginSubPass](Rendering.ScriptableRenderContext.BeginSubPass.html)| Schedules
the beginning of a new sub pass within a render pass. Render passes can never
be standalone, they must always contain at least one sub pass. Only one sub
pass can be active at any time.  
[CreateGizmoRendererList](Rendering.ScriptableRenderContext.CreateGizmoRendererList.html)|
Creates a new Gizmo RendererList.  
[CreateRendererList](Rendering.ScriptableRenderContext.CreateRendererList.html)|
Creates a new renderers RendererList.  
[CreateShadowRendererList](Rendering.ScriptableRenderContext.CreateShadowRendererList.html)|
Creates a new shadow RendererList.  
[CreateSkyboxRendererList](Rendering.ScriptableRenderContext.CreateSkyboxRendererList.html)|
Creates a new skybox RendererList.  
[CreateUIOverlayRendererList](Rendering.ScriptableRenderContext.CreateUIOverlayRendererList.html)|
Creates a new UIOverlay RendererList.  
[CreateWireOverlayRendererList](Rendering.ScriptableRenderContext.CreateWireOverlayRendererList.html)|
Creates a new WireOverlay RendererList.  
[Cull](Rendering.ScriptableRenderContext.Cull.html)| Performs culling based on
the ScriptableCullingParameters typically obtained from the Camera currently
being rendered.  
[CullShadowCasters](Rendering.ScriptableRenderContext.CullShadowCasters.html)|
Performs shadow casters culling for all the visible lights.  
[DrawGizmos](Rendering.ScriptableRenderContext.DrawGizmos.html)| Schedules the
drawing of a subset of Gizmos (before or after post-processing) for the given
Camera.  
[DrawUIOverlay](Rendering.ScriptableRenderContext.DrawUIOverlay.html)| Draw
the UI overlay.  
[DrawWireOverlay](Rendering.ScriptableRenderContext.DrawWireOverlay.html)|
Schedules the drawing of a wireframe overlay for a given Scene view Camera.  
[EndRenderPass](Rendering.ScriptableRenderContext.EndRenderPass.html)|
Schedules the end of a currently active render pass.  
[EndSubPass](Rendering.ScriptableRenderContext.EndSubPass.html)| Schedules the
end of the currently active sub pass.  
[ExecuteCommandBuffer](Rendering.ScriptableRenderContext.ExecuteCommandBuffer.html)|
Schedules the execution of a custom graphics Command Buffer.  
[ExecuteCommandBufferAsync](Rendering.ScriptableRenderContext.ExecuteCommandBufferAsync.html)|
Schedules the execution of a Command Buffer on an async compute queue. The
ComputeQueueType that you pass in determines the queue order.  
[HasInvokeOnRenderObjectCallbacks](Rendering.ScriptableRenderContext.HasInvokeOnRenderObjectCallbacks.html)|
Check if any objects in the scene have OnRenderObject callbacks registered.  
[InvokeOnRenderObjectCallback](Rendering.ScriptableRenderContext.InvokeOnRenderObjectCallback.html)|
Schedules an invocation of the OnRenderObject callback for MonoBehaviour
scripts.  
[PrepareRendererListsAsync](Rendering.ScriptableRenderContext.PrepareRendererListsAsync.html)|
Starts to process the provided RendererLists in the background.  
[QueryRendererListStatus](Rendering.ScriptableRenderContext.QueryRendererListStatus.html)|
Queries the status of a RendererList.  
[SetupCameraProperties](Rendering.ScriptableRenderContext.SetupCameraProperties.html)|
Schedules the setup of Camera specific global Shader variables.  
[StartMultiEye](Rendering.ScriptableRenderContext.StartMultiEye.html)|
Schedules a fine-grained beginning of stereo rendering on the
ScriptableRenderContext.  
[StereoEndRender](Rendering.ScriptableRenderContext.StereoEndRender.html)|
Schedule notification of completion of stereo rendering on a single frame.  
[StopMultiEye](Rendering.ScriptableRenderContext.StopMultiEye.html)| Schedules
a stop of stereo rendering on the ScriptableRenderContext.  
[Submit](Rendering.ScriptableRenderContext.Submit.html)| Submits all the
scheduled commands to the rendering loop for execution.  
[SubmitForRenderPassValidation](Rendering.ScriptableRenderContext.SubmitForRenderPassValidation.html)|
This method submits all the scheduled commands to the rendering loop for
validation. The validation checks whether render passes that were started with
the BeginRenderPass call can execute the scheduled commands.  
  
### Static Methods

[EmitGeometryForCamera](Rendering.ScriptableRenderContext.EmitGeometryForCamera.html)|
Emits UI geometry for rendering for the specified camera.  
---|---  
[EmitWorldGeometryForSceneView](Rendering.ScriptableRenderContext.EmitWorldGeometryForSceneView.html)|
Emits UI geometry into the Scene view for rendering.  
[PopDisableApiRenderers](Rendering.ScriptableRenderContext.PopDisableApiRenderers.html)|
Enable the immediate addition and removal of renderer scene nodes to the scene
arrays.  
[PushDisableApiRenderers](Rendering.ScriptableRenderContext.PushDisableApiRenderers.html)|
Prevent the immediate addition or removal of renderer scene nodes to the scene
arrays. This protects against the creation of invalid indices or dangling
pointers caused by changes to the scene arrays after the culling output has
been computed.  
  
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

