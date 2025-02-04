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

#  [Camera](Camera.html).AddCommandBufferAsync

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

## Declaration

public void
AddCommandBufferAsync([Rendering.CameraEvent](Rendering.CameraEvent.html) evt,
[Rendering.CommandBuffer](Rendering.CommandBuffer.html) buffer,
[Rendering.ComputeQueueType](Rendering.ComputeQueueType.html) queueType);

### Parameters

evt | The point during the graphics processing at which this command buffer should commence on the GPU.  
---|---  
buffer | The buffer to execute.  
queueType | The desired async compute queue type to execute the buffer on.  
  
### Description

Adds a command buffer to the GPU's async compute queues and executes that
command buffer when graphics processing reaches a given point.

Executes an async compute command buffer on the GPU when the graphics queues
processing reaches a point described by the evt parameter.  
  
Multiple command buffers can be set to execute at the same camera event (or
even the same buffer can be added multiple times). To remove a command buffer
from execution, use [RemoveCommandBuffer](Camera.RemoveCommandBuffer.html).  
  
The command buffer can only call the following commands for execution on the
async compute queues, otherwise an error will be logged and displayed in the
Editor window:  
  
[CommandBuffer.BeginSample](Rendering.CommandBuffer.BeginSample.html)  
  
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)  
  
[CommandBuffer.CopyCounterValue](Rendering.CommandBuffer.CopyCounterValue.html)  
  
[CommandBuffer.CopyTexture](Rendering.CommandBuffer.CopyTexture.html)  
  
CommandBuffer.CreateGPUFence  
  
[CommandBuffer.DispatchCompute](Rendering.CommandBuffer.DispatchCompute.html)  
  
[CommandBuffer.EndSample](Rendering.CommandBuffer.EndSample.html)  
  
[CommandBuffer.IssuePluginEvent](Rendering.CommandBuffer.IssuePluginEvent.html)  
  
[CommandBuffer.SetComputeBufferParam](Rendering.CommandBuffer.SetComputeBufferParam.html)  
  
[CommandBuffer.SetComputeFloatParam](Rendering.CommandBuffer.SetComputeFloatParam.html)  
  
[CommandBuffer.SetComputeFloatParams](Rendering.CommandBuffer.SetComputeFloatParams.html)  
  
[CommandBuffer.SetComputeTextureParam](Rendering.CommandBuffer.SetComputeTextureParam.html)  
  
[CommandBuffer.SetComputeVectorParam](Rendering.CommandBuffer.SetComputeVectorParam.html)  
  
CommandBuffer.WaitOnGPUFence  
  
All of the commands within the buffer are guaranteed to be executed on the
same queue. If the target platform does not support async compute queues then
the work is dispatched on the graphics queue. This API is only available with
the Built-in renderer.  
  
Additional resources:GPUFence, [SystemInfo.supportsAsyncCompute](SystemInfo-
supportsAsyncCompute.html), [CommandBuffer](Rendering.CommandBuffer.html),
[RemoveCommandBuffer](Camera.RemoveCommandBuffer.html),
[GetCommandBuffers](Camera.GetCommandBuffers.html).

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

