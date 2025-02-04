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

#  [ComputeShader](ComputeShader.html).DispatchIndirect

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

## Declaration

public void DispatchIndirect(int kernelIndex,
[ComputeBuffer](ComputeBuffer.html) argsBuffer, uint argsOffset = 0);

## Declaration

public void DispatchIndirect(int kernelIndex,
[GraphicsBuffer](GraphicsBuffer.html) argsBuffer, uint argsOffset = 0);

### Parameters

kernelIndex | Which kernel to execute. A single compute shader asset can have multiple kernel entry points.  
---|---  
argsBuffer | Buffer with dispatch arguments.  
argsOffset | The byte offset into the buffer, where the draw arguments start.  
  
### Description

Execute a compute shader.

This function "runs" the compute shader, with the given work size read
directly from the GPU. Typical use case is generating arbitrary amount of data
from a [ComputeShader](ComputeShader.html) and then dispatching that, without
requiring a readback to the CPU.  
  
Buffer with arguments, `argsBuffer`, has to have three integer numbers at
given `argsOffset` offset: number of work groups in X dimension, number of
work groups in Y dimension, number of work groups in Z dimension.  
  
Within each work group, a number of shader invocations ("threads") are done.
The work group size is specified in the compute shader itself (using
"numthreads" HLSL attribute), and the total amount of compute shader
invocations is thus group count multiplied by the thread group size. Work
group size can be queried using
[GetKernelThreadGroupSizes](ComputeShader.GetKernelThreadGroupSizes.html)
function.  
  
This very much maps to Direct3D11 DispatchIndirect, OpenGL
glDispatchComputeIndirect and equivalent functions on other graphics APIs.  
  
Additional resources: [Dispatch](ComputeShader.Dispatch.html),
[Graphics.DrawProceduralIndirect](Graphics.DrawProceduralIndirect.html),
[ComputeBuffer.CopyCount](ComputeBuffer.CopyCount.html), [Compute
Shaders](../Manual/class-ComputeShader.html).

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

