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

#  [Graphics](Graphics.html).ExecuteCommandBufferAsync

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

public static void
ExecuteCommandBufferAsync([Rendering.CommandBuffer](Rendering.CommandBuffer.html)
buffer, [Rendering.ComputeQueueType](Rendering.ComputeQueueType.html)
queueType);

### Parameters

buffer | The [CommandBuffer](Rendering.CommandBuffer.html) to be executed.  
---|---  
queueType | Describes the desired async compute queue the supplied [CommandBuffer](Rendering.CommandBuffer.html) should be executed on.  
  
### Description

Executes a command buffer on an async compute queue with the queue selected
based on the [ComputeQueueType](Rendering.ComputeQueueType.html) parameter
passed.

It is required that all of the commands within the command buffer be of a type
suitable for execution on the async compute queues. If the buffer contains any
commands that are not appropriate then an error will be logged and displayed
in the editor window. Specifically the following commands are permitted in a
[CommandBuffer](Rendering.CommandBuffer.html) intended for async execution:  
  
[CommandBuffer.BeginSample](Rendering.CommandBuffer.BeginSample.html)  
  
[CommandBuffer.BuildRayTracingAccelerationStructure](Rendering.CommandBuffer.BuildRayTracingAccelerationStructure.html)  
  
[CommandBuffer.CopyCounterValue](Rendering.CommandBuffer.CopyCounterValue.html)  
  
[CommandBuffer.CopyTexture](Rendering.CommandBuffer.CopyTexture.html)  
  
[CommandBuffer.CreateGraphicsFence](Rendering.CommandBuffer.CreateGraphicsFence.html)  
  
[CommandBuffer.DisableShaderKeyword](Rendering.CommandBuffer.DisableShaderKeyword.html)  
  
[CommandBuffer.DispatchCompute](Rendering.CommandBuffer.DispatchCompute.html)  
  
[CommandBuffer.EnableShaderKeyword](Rendering.CommandBuffer.EnableShaderKeyword.html)  
  
[CommandBuffer.EndSample](Rendering.CommandBuffer.EndSample.html)  
  
[CommandBuffer.GetTemporaryRT](Rendering.CommandBuffer.GetTemporaryRT.html)  
  
[CommandBuffer.GetTemporaryRTArray](Rendering.CommandBuffer.GetTemporaryRTArray.html)  
  
[CommandBuffer.IssuePluginEvent](Rendering.CommandBuffer.IssuePluginEvent.html)  
  
[CommandBuffer.ReleaseTemporaryRT](Rendering.CommandBuffer.ReleaseTemporaryRT.html)  
  
CommandBuffer.SetComputeBufferData  
  
[CommandBuffer.SetComputeBufferParam](Rendering.CommandBuffer.SetComputeBufferParam.html)  
  
[CommandBuffer.SetComputeFloatParam](Rendering.CommandBuffer.SetComputeFloatParam.html)  
  
[CommandBuffer.SetComputeFloatParams](Rendering.CommandBuffer.SetComputeFloatParams.html)  
  
[CommandBuffer.SetComputeIntParam](Rendering.CommandBuffer.SetComputeIntParam.html)  
  
[CommandBuffer.SetComputeIntParams](Rendering.CommandBuffer.SetComputeIntParams.html)  
  
[CommandBuffer.SetComputeMatrixArrayParam](Rendering.CommandBuffer.SetComputeMatrixArrayParam.html)  
  
[CommandBuffer.SetComputeMatrixParam](Rendering.CommandBuffer.SetComputeMatrixParam.html)  
  
[CommandBuffer.SetComputeTextureParam](Rendering.CommandBuffer.SetComputeTextureParam.html)  
  
[CommandBuffer.SetComputeVectorParam](Rendering.CommandBuffer.SetComputeVectorParam.html)  
  
[CommandBuffer.SetComputeVectorArrayParam](Rendering.CommandBuffer.SetComputeVectorArrayParam.html)  
  
[CommandBuffer.SetGlobalBuffer](Rendering.CommandBuffer.SetGlobalBuffer.html)  
  
[CommandBuffer.SetGlobalColor](Rendering.CommandBuffer.SetGlobalColor.html)  
  
[CommandBuffer.SetGlobalFloat](Rendering.CommandBuffer.SetGlobalFloat.html)  
  
[CommandBuffer.SetGlobalFloatArray](Rendering.CommandBuffer.SetGlobalFloatArray.html)  
  
[CommandBuffer.SetGlobalInt](Rendering.CommandBuffer.SetGlobalInt.html)  
  
[CommandBuffer.SetGlobalMatrix](Rendering.CommandBuffer.SetGlobalMatrix.html)  
  
[CommandBuffer.SetGlobalMatrixArray](Rendering.CommandBuffer.SetGlobalMatrixArray.html)  
  
[CommandBuffer.SetGlobalTexture](Rendering.CommandBuffer.SetGlobalTexture.html)  
  
[CommandBuffer.SetGlobalVector](Rendering.CommandBuffer.SetGlobalVector.html)  
  
[CommandBuffer.SetGlobalVectorArray](Rendering.CommandBuffer.SetGlobalVectorArray.html)  
  
CommandBuffer.WaitOnGraphicsFence  
  
All of the commands within the buffer are guaranteed to be executed on the
same queue. If the target platform does not support async compute queues then
the work is dispatched on the graphics queue.

Additional resources: [SystemInfo.supportsAsyncCompute](SystemInfo-
supportsAsyncCompute.html) , GPUFence,
[CommandBuffer](Rendering.CommandBuffer.html).

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

