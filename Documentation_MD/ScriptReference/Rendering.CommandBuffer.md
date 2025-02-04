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

# CommandBuffer

class in UnityEngine.Rendering

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

List of graphics commands to execute.

Command buffers hold list of rendering commands ("set render target, draw
mesh, ..."). They can be set to execute at various points during camera
rendering (see [Camera.AddCommandBuffer](Camera.AddCommandBuffer.html)), light
rendering (see [Light.AddCommandBuffer](Light.AddCommandBuffer.html)) or be
executed immediately (see
[Graphics.ExecuteCommandBuffer](Graphics.ExecuteCommandBuffer.html)).  
  
Typically they would be used to extend Unity's render pipelines in a custom
way. For example, you could render some additional objects into deferred
rendering G-buffer after all regular objects are done, or do custom processing
of light shadow maps. See [command buffers
overview](../Manual/GraphicsCommandBuffers.html) page for more details.  
  
Command buffers can be created and then executed many times if needed.  
  
Additional resources: [Camera.AddCommandBuffer](Camera.AddCommandBuffer.html),
[Light.AddCommandBuffer](Light.AddCommandBuffer.html),
[CameraEvent](Rendering.CameraEvent.html),
[LightEvent](Rendering.LightEvent.html),
[Graphics.ExecuteCommandBuffer](Graphics.ExecuteCommandBuffer.html), [command
buffers overview](../Manual/GraphicsCommandBuffers.html).

### Static Properties

[ThrowOnSetRenderTarget](Rendering.CommandBuffer.ThrowOnSetRenderTarget.html)|
Throw an exception when SetRenderTarget is recorded on a command buffer. This
is mainly usefull when using native renderpasses to avoid inadvertently
recording SetRenderTarget commands on the command buffer.  
---|---  
  
### Properties

[name](Rendering.CommandBuffer-name.html)| Name of this command buffer.  
---|---  
[sizeInBytes](Rendering.CommandBuffer-sizeInBytes.html)| Size of this command
buffer in bytes (Read Only).  
  
### Constructors

[CommandBuffer](Rendering.CommandBuffer-ctor.html)| Create a new empty command
buffer.  
---|---  
  
### Public Methods

[BeginRenderPass](Rendering.CommandBuffer.BeginRenderPass.html)| Begin a new
native render pass.  
---|---  
[BeginSample](Rendering.CommandBuffer.BeginSample.html)| Adds a command to
begin profile sampling.  
[Blit](Rendering.CommandBuffer.Blit.html)| Adds a command to use a shader to
copy the pixel data from a texture into a render texture.  
[BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)|
Adds a command to build the RayTracingAccelerationStructure to be used in a
ray tracing dispatch or when using inline ray tracing (ray queries).  
[Clear](Rendering.CommandBuffer.Clear.html)| Clear all commands in the buffer.  
[ClearRandomWriteTargets](Rendering.CommandBuffer.ClearRandomWriteTargets.html)|
Unset random write targets for Shader Model 4.5 level pixel shaders.  
[ClearRenderTarget](Rendering.CommandBuffer.ClearRenderTarget.html)| Adds a
"clear render target" command.  
[ConfigureFoveatedRendering](Rendering.CommandBuffer.ConfigureFoveatedRendering.html)|
Adds a command to configure foveated rendering.  
[ConvertTexture](Rendering.CommandBuffer.ConvertTexture.html)| Adds a command
to copy the pixel data from one texture, convert the data into a different
format, and copy it into another texture.  
[CopyBuffer](Rendering.CommandBuffer.CopyBuffer.html)| Adds a command to copy
the contents of one GraphicsBuffer into another.  
[CopyCounterValue](Rendering.CommandBuffer.CopyCounterValue.html)| Adds a
command to copy ComputeBuffer or GraphicsBuffer counter value.  
[CopyTexture](Rendering.CommandBuffer.CopyTexture.html)| Adds a command to
copy pixel data from one texture to another.  
[CreateAsyncGraphicsFence](Rendering.CommandBuffer.CreateAsyncGraphicsFence.html)|
Shortcut for calling CommandBuffer.CreateGraphicsFence with
GraphicsFenceType.AsyncQueueSynchronisation as the first parameter.  
[CreateGraphicsFence](Rendering.CommandBuffer.CreateGraphicsFence.html)|
Creates a GraphicsFence.  
[DisableKeyword](Rendering.CommandBuffer.DisableKeyword.html)| Adds a command
to disable a global or local shader keyword.  
[DisableScissorRect](Rendering.CommandBuffer.DisableScissorRect.html)| Add a
command to disable the hardware scissor rectangle.  
[DisableShaderKeyword](Rendering.CommandBuffer.DisableShaderKeyword.html)|
Adds a command to disable a global shader keyword with a given name.  
[DispatchCompute](Rendering.CommandBuffer.DispatchCompute.html)| Add a command
to execute a ComputeShader.  
[DispatchRays](Rendering.CommandBuffer.DispatchRays.html)| Adds a command to
execute a RayTracingShader.  
[DrawMesh](Rendering.CommandBuffer.DrawMesh.html)| Add a "draw mesh" command.  
[DrawMeshInstanced](Rendering.CommandBuffer.DrawMeshInstanced.html)| Adds a
"draw mesh with instancing" command.The mesh will be just drawn once, it won't
be per-pixel lit and will not cast or receive realtime shadows.The command
will not immediately fail and throw an exception if Material.enableInstancing
is false, but it will log an error and skips rendering each time the command
is being executed if such a condition is detected.InvalidOperationException
will be thrown if the current platform doesn't support this API (i.e. if GPU
instancing is not available). See SystemInfo.supportsInstancing.  
[DrawMeshInstancedIndirect](Rendering.CommandBuffer.DrawMeshInstancedIndirect.html)|
Add a "draw mesh with indirect instancing" command.  
[DrawMeshInstancedProcedural](Rendering.CommandBuffer.DrawMeshInstancedProcedural.html)|
Add a "draw mesh with instancing" command.Draw a mesh using Procedural
Instancing. This is similar to Graphics.DrawMeshInstancedIndirect, except that
when the instance count is known from script, it can be supplied directly
using this method, rather than via a ComputeBuffer. If
Material.enableInstancing is false, the command logs an error and skips
rendering each time the command is executed; the command does not immediately
fail and throw an exception.InvalidOperationException will be thrown if the
current platform doesn't support this API (for example, if GPU instancing is
not available). See SystemInfo.supportsInstancing.  
[DrawOcclusionMesh](Rendering.CommandBuffer.DrawOcclusionMesh.html)| Adds a
command onto the commandbuffer to draw the VR Device's occlusion mesh to the
current render target.  
[DrawProcedural](Rendering.CommandBuffer.DrawProcedural.html)| Add a "draw
procedural geometry" command.  
[DrawProceduralIndirect](Rendering.CommandBuffer.DrawProceduralIndirect.html)|
Add a "draw procedural geometry" command.  
[DrawRenderer](Rendering.CommandBuffer.DrawRenderer.html)| Add a "draw
renderer" command.  
[DrawRendererList](Rendering.CommandBuffer.DrawRendererList.html)| Adds a
"draw renderer list" command.  
[EnableKeyword](Rendering.CommandBuffer.EnableKeyword.html)| Adds a command to
enable a global or local shader keyword.  
[EnableScissorRect](Rendering.CommandBuffer.EnableScissorRect.html)| Add a
command to enable the hardware scissor rectangle.  
[EnableShaderKeyword](Rendering.CommandBuffer.EnableShaderKeyword.html)| Adds
a command to enable a global keyword with a given name.  
[EndRenderPass](Rendering.CommandBuffer.EndRenderPass.html)| Terminate the
active native renderpass.  
[EndSample](Rendering.CommandBuffer.EndSample.html)| Adds a command to end
profile sampling.  
[GenerateMips](Rendering.CommandBuffer.GenerateMips.html)| Generate mipmap
levels of a render texture.  
[GetTemporaryRT](Rendering.CommandBuffer.GetTemporaryRT.html)| Add a "get a
temporary render texture" command.  
[GetTemporaryRTArray](Rendering.CommandBuffer.GetTemporaryRTArray.html)| Add a
"get a temporary render texture array" command.  
[IncrementUpdateCount](Rendering.CommandBuffer.IncrementUpdateCount.html)|
Increments the updateCount property of a Texture.  
[InvokeOnRenderObjectCallbacks](Rendering.CommandBuffer.InvokeOnRenderObjectCallbacks.html)|
Schedules an invocation of the OnRenderObject callback for MonoBehaviour
scripts.  
[IssuePluginCustomBlit](Rendering.CommandBuffer.IssuePluginCustomBlit.html)|
Send a user-defined blit event to a native code plugin.  
[IssuePluginCustomTextureUpdateV2](Rendering.CommandBuffer.IssuePluginCustomTextureUpdateV2.html)|
Send a texture update event to a native code plugin.  
[IssuePluginEvent](Rendering.CommandBuffer.IssuePluginEvent.html)| Send a
user-defined event to a native code plugin.  
[IssuePluginEventAndData](Rendering.CommandBuffer.IssuePluginEventAndData.html)|
Send a user-defined event to a native code plugin with custom data.  
[IssuePluginEventAndDataWithFlags](Rendering.CommandBuffer.IssuePluginEventAndDataWithFlags.html)|
Send a user-defined event to a native code plugin with custom data and
callback flags.  
[MarkLateLatchMatrixShaderPropertyID](Rendering.CommandBuffer.MarkLateLatchMatrixShaderPropertyID.html)|
Mark a global shader property id to be late latched. Possible shader
properties include view, inverseView, viewProjection, and
inverseViewProjection matrices. The Universal Render Pipeline (URP) uses this
function to support late latching of shader properties. If you call this
function when using built-in Unity rendering or the High-Definition Rendering
Pipeline (HDRP), the results are ignored.  
[NextSubPass](Rendering.CommandBuffer.NextSubPass.html)| Start the next native
subpass as discribed by CommandBuffer.BeginRenderPass.  
[ReleaseTemporaryRT](Rendering.CommandBuffer.ReleaseTemporaryRT.html)| Add a
"release a temporary render texture" command.  
[RequestAsyncReadback](Rendering.CommandBuffer.RequestAsyncReadback.html)|
Adds an asynchonous GPU readback request command to the command buffer.  
[RequestAsyncReadbackIntoNativeArray](Rendering.CommandBuffer.RequestAsyncReadbackIntoNativeArray.html)|
Adds an asynchonous GPU readback request command to the command buffer.  
[RequestAsyncReadbackIntoNativeSlice](Rendering.CommandBuffer.RequestAsyncReadbackIntoNativeSlice.html)|
Adds an asynchonous GPU readback request command to the command buffer.  
[ResolveAntiAliasedSurface](Rendering.CommandBuffer.ResolveAntiAliasedSurface.html)|
Force an antialiased render texture to be resolved.  
[SetBufferCounterValue](Rendering.CommandBuffer.SetBufferCounterValue.html)|
Adds a command to set the counter value of append/consume buffer.  
[SetBufferData](Rendering.CommandBuffer.SetBufferData.html)| Adds a command to
set the buffer with values from an array.  
[SetComputeBufferParam](Rendering.CommandBuffer.SetComputeBufferParam.html)|
Adds a command to set an input or output buffer parameter on a ComputeShader.  
[SetComputeConstantBufferParam](Rendering.CommandBuffer.SetComputeConstantBufferParam.html)|
Adds a command to set a constant buffer on a ComputeShader.  
[SetComputeFloatParam](Rendering.CommandBuffer.SetComputeFloatParam.html)|
Adds a command to set a float parameter on a ComputeShader.  
[SetComputeFloatParams](Rendering.CommandBuffer.SetComputeFloatParams.html)|
Adds a command to set multiple consecutive float parameters on a
ComputeShader.  
[SetComputeIntParam](Rendering.CommandBuffer.SetComputeIntParam.html)| Adds a
command to set an integer parameter on a ComputeShader.  
[SetComputeIntParams](Rendering.CommandBuffer.SetComputeIntParams.html)| Adds
a command to set multiple consecutive integer parameters on a ComputeShader.  
[SetComputeMatrixArrayParam](Rendering.CommandBuffer.SetComputeMatrixArrayParam.html)|
Adds a command to set a matrix array parameter on a ComputeShader.  
[SetComputeMatrixParam](Rendering.CommandBuffer.SetComputeMatrixParam.html)|
Adds a command to set a matrix parameter on a ComputeShader.  
[SetComputeParamsFromMaterial](Rendering.CommandBuffer.SetComputeParamsFromMaterial.html)|
Sets the parameters for a compute shader kernel from a Material.  
[SetComputeTextureParam](Rendering.CommandBuffer.SetComputeTextureParam.html)|
Adds a command to set a texture parameter on a ComputeShader.  
[SetComputeVectorArrayParam](Rendering.CommandBuffer.SetComputeVectorArrayParam.html)|
Adds a command to set a vector array parameter on a ComputeShader.  
[SetComputeVectorParam](Rendering.CommandBuffer.SetComputeVectorParam.html)|
Adds a command to set a vector parameter on a ComputeShader.  
[SetExecutionFlags](Rendering.CommandBuffer.SetExecutionFlags.html)| Set flags
describing the intention for how the command buffer will be executed.  
[SetFoveatedRenderingMode](Rendering.CommandBuffer.SetFoveatedRenderingMode.html)|
Adds a command to set the mode to use for foveated rendering.  
[SetGlobalBuffer](Rendering.CommandBuffer.SetGlobalBuffer.html)| Add a "set
global shader buffer property" command.  
[SetGlobalColor](Rendering.CommandBuffer.SetGlobalColor.html)| Add a "set
global shader color property" command.  
[SetGlobalConstantBuffer](Rendering.CommandBuffer.SetGlobalConstantBuffer.html)|
Add a command to bind a global constant buffer.  
[SetGlobalDepthBias](Rendering.CommandBuffer.SetGlobalDepthBias.html)| Adds a
command to set the global depth bias.  
[SetGlobalFloat](Rendering.CommandBuffer.SetGlobalFloat.html)| Add a "set
global shader float property" command.  
[SetGlobalFloatArray](Rendering.CommandBuffer.SetGlobalFloatArray.html)| Add a
"set global shader float array property" command.  
[SetGlobalInt](Rendering.CommandBuffer.SetGlobalInt.html)| Adds a command to
set the value of a given property for all Shaders, where the property has a
type of Int in ShaderLab code.  
[SetGlobalInteger](Rendering.CommandBuffer.SetGlobalInteger.html)| Adds a
command to set the value of a given property for all Shaders, where the
property is an integer.  
[SetGlobalMatrix](Rendering.CommandBuffer.SetGlobalMatrix.html)| Add a "set
global shader matrix property" command.  
[SetGlobalMatrixArray](Rendering.CommandBuffer.SetGlobalMatrixArray.html)| Add
a "set global shader matrix array property" command.  
[SetGlobalRayTracingAccelerationStructure](Rendering.CommandBuffer.SetGlobalRayTracingAccelerationStructure.html)|
Adds a command to bind the RayTracingAccelerationStructure object to all
shader stages.  
[SetGlobalTexture](Rendering.CommandBuffer.SetGlobalTexture.html)| Add a "set
global shader texture property" command, referencing a RenderTexture.  
[SetGlobalVector](Rendering.CommandBuffer.SetGlobalVector.html)| Add a "set
global shader vector property" command.  
[SetGlobalVectorArray](Rendering.CommandBuffer.SetGlobalVectorArray.html)| Add
a "set global shader vector array property" command.  
[SetInstanceMultiplier](Rendering.CommandBuffer.SetInstanceMultiplier.html)|
Adds a command to multiply the instance count of every draw call by a specific
multiplier.  
[SetInvertCulling](Rendering.CommandBuffer.SetInvertCulling.html)| Add a "set
invert culling" command to the buffer.  
[SetKeyword](Rendering.CommandBuffer.SetKeyword.html)| Adds a command to set
the state of a global or local shader keyword.  
[SetLateLatchProjectionMatrices](Rendering.CommandBuffer.SetLateLatchProjectionMatrices.html)|
Set the current stereo projection matrices for late latching. Stereo matrices
is passed in as an array of two matrices.  
[SetProjectionMatrix](Rendering.CommandBuffer.SetProjectionMatrix.html)| Add a
command to set the projection matrix.  
[SetRandomWriteTarget](Rendering.CommandBuffer.SetRandomWriteTarget.html)| Set
random write target for Shader Model 4.5 level pixel shaders.  
[SetRayTracingAccelerationStructure](Rendering.CommandBuffer.SetRayTracingAccelerationStructure.html)|
Adds a command to set the RayTracingAccelerationStructure to be used in a
RayTracingShader or a ComputeShader.  
[SetRayTracingBufferParam](Rendering.CommandBuffer.SetRayTracingBufferParam.html)|
Adds a command to set an input or output buffer parameter on a
RayTracingShader.  
[SetRayTracingConstantBufferParam](Rendering.CommandBuffer.SetRayTracingConstantBufferParam.html)|
Adds a command to set a constant buffer on a RayTracingShader.  
[SetRayTracingFloatParam](Rendering.CommandBuffer.SetRayTracingFloatParam.html)|
Adds a command to set a float parameter on a RayTracingShader.  
[SetRayTracingFloatParams](Rendering.CommandBuffer.SetRayTracingFloatParams.html)|
Adds a command to set multiple consecutive float parameters on a
RayTracingShader.  
[SetRayTracingIntParam](Rendering.CommandBuffer.SetRayTracingIntParam.html)|
Adds a command to set an integer parameter on a RayTracingShader.  
[SetRayTracingIntParams](Rendering.CommandBuffer.SetRayTracingIntParams.html)|
Adds a command to set multiple consecutive integer parameters on a
RayTracingShader.  
[SetRayTracingMatrixArrayParam](Rendering.CommandBuffer.SetRayTracingMatrixArrayParam.html)|
Adds a command to set a matrix array parameter on a RayTracingShader.  
[SetRayTracingMatrixParam](Rendering.CommandBuffer.SetRayTracingMatrixParam.html)|
Adds a command to set a matrix parameter on a RayTracingShader.  
[SetRayTracingShaderPass](Rendering.CommandBuffer.SetRayTracingShaderPass.html)|
Adds a command to select which Shader Pass to use when executing ray/geometry
intersection shaders.  
[SetRayTracingTextureParam](Rendering.CommandBuffer.SetRayTracingTextureParam.html)|
Adds a command to set a texture parameter on a RayTracingShader.  
[SetRayTracingVectorArrayParam](Rendering.CommandBuffer.SetRayTracingVectorArrayParam.html)|
Adds a command to set a vector array parameter on a RayTracingShader.  
[SetRayTracingVectorParam](Rendering.CommandBuffer.SetRayTracingVectorParam.html)|
Adds a command to set a vector parameter on a RayTracingShader.  
[SetRenderTarget](Rendering.CommandBuffer.SetRenderTarget.html)| Add a "set
active render target" command.  
[SetShadowSamplingMode](Rendering.CommandBuffer.SetShadowSamplingMode.html)|
Add a "set shadow sampling mode" command.  
[SetSinglePassStereo](Rendering.CommandBuffer.SetSinglePassStereo.html)| Add a
command to set single-pass stereo mode for the camera.  
[SetupCameraProperties](Rendering.CommandBuffer.SetupCameraProperties.html)|
Schedules the setup of Camera specific global Shader variables.  
[SetViewMatrix](Rendering.CommandBuffer.SetViewMatrix.html)| Add a command to
set the view matrix.  
[SetViewport](Rendering.CommandBuffer.SetViewport.html)| Add a command to set
the rendering viewport.  
[SetViewProjectionMatrices](Rendering.CommandBuffer.SetViewProjectionMatrices.html)|
Add a command to set the view and projection matrices.  
[SetWireframe](Rendering.CommandBuffer.SetWireframe.html)| Add a "set
wireframe" command to the buffer.  
[UnmarkLateLatchMatrix](Rendering.CommandBuffer.UnmarkLateLatchMatrix.html)|
Unmark a global shader property for late latching. After unmarking, the shader
property will no longer be late latched. This function is intended for the
Universal Render Pipeline (URP) to specify late latched shader properties.  
[WaitAllAsyncReadbackRequests](Rendering.CommandBuffer.WaitAllAsyncReadbackRequests.html)|
Adds an "AsyncGPUReadback.WaitAllRequests" command to the CommandBuffer.  
[WaitOnAsyncGraphicsFence](Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html)|
Instructs the GPU to pause processing of the queue until it passes through the
GraphicsFence fence.  
  
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

