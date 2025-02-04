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
[CommandBufferExtensions](Rendering.CommandBufferExtensions.html).SwitchIntoFastMemory

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
SwitchIntoFastMemory([Rendering.CommandBuffer](Rendering.CommandBuffer.html)
cmd, [Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rid, [Rendering.FastMemoryFlags](Rendering.FastMemoryFlags.html)
fastMemoryFlags, float residency, bool copyContents);

### Parameters

rid | The render target to put into fast GPU memory.  
---|---  
fastMemoryFlags | The memory layout to use if only part of the render target is put into fast GPU memory, either because of the residency parameter or because of fast GPU memory availability.  
residency | The amount of the render target to put into fast GPU memory. Valid values are 0.0f - 1.0f inclusive. A value of 0.0f is equal to none of the render target, and a value of 1.0f is equal to the whole render target.   
copyContents | When this value is true, Unity copies the existing contents of the render target into fast memory. When this value is false, Unity does not copy the existing contents of the render target into fast memory. Set this value to true if you plan to add to the existing contents, and set it to false if you plan to overwrite or clear the existing contents. Where possible, set this value to false for better performance.   
  
### Description

Adds a command to put a given render target into fast GPU memory.

On certain console platforms, you can put render targets in fast GPU memory
for improved rendering performance.  
  
On platforms that do not support fast GPU memory, this function does nothing.  
  
On platforms that support fast GPU memory, the results of this function depend
on the state of the render target and the amount of fast GPU memory available
at the time that the graphics API executes this command. If the render target
is not already in fast GPU memory, Unity puts as much of the render target as
possible into fast GPU memory, up to the amount specified in the `residency`
parameter. If Unity cannot put the render target into fast GPU memory, either
because it is already in fast GPU memory or because no fast GPU memory is
available, Unity does nothing. There is no performance cost in this case.  
  
Note that it is not possible to determine in advance whether a render target
is already in fast GPU memory, or how much fast GPU memory is available.  
  
Additional resources:
[CommandBufferExtensions.SwitchOutOfFastMemory](Rendering.CommandBufferExtensions.SwitchOutOfFastMemory.html)

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

