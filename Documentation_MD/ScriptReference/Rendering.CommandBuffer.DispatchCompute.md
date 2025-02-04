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

#  [CommandBuffer](Rendering.CommandBuffer.html).DispatchCompute

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

public void DispatchCompute([ComputeShader](ComputeShader.html) computeShader,
int kernelIndex, int threadGroupsX, int threadGroupsY, int threadGroupsZ);

## Declaration

public void DispatchCompute([ComputeShader](ComputeShader.html) computeShader,
int kernelIndex, [ComputeBuffer](ComputeBuffer.html) indirectBuffer, uint
argsOffset);

## Declaration

public void DispatchCompute([ComputeShader](ComputeShader.html) computeShader,
int kernelIndex, [GraphicsBuffer](GraphicsBuffer.html) indirectBuffer, uint
argsOffset);

### Parameters

computeShader |  [ComputeShader](ComputeShader.html) to execute.  
---|---  
kernelIndex | Kernel index to execute, see [ComputeShader.FindKernel](ComputeShader.FindKernel.html).  
threadGroupsX | Number of work groups in the X dimension.  
threadGroupsY | Number of work groups in the Y dimension.  
threadGroupsZ | Number of work groups in the Z dimension.  
indirectBuffer |  [ComputeBuffer](ComputeBuffer.html) with dispatch arguments.  
argsOffset | Byte offset indicating the location of the dispatch arguments in the buffer.  
  
### Description

Add a command to execute a [ComputeShader](ComputeShader.html).

When the command buffer executes, a compute shader kernel is dispatched, with
work group size either specified directly (see
[ComputeShader.Dispatch](ComputeShader.Dispatch.html)) or read from the GPU
buffer (see
[ComputeShader.DispatchIndirect](ComputeShader.DispatchIndirect.html)).

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

