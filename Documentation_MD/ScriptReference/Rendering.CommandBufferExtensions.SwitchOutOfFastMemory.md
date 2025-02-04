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
[CommandBufferExtensions](Rendering.CommandBufferExtensions.html).SwitchOutOfFastMemory

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
SwitchOutOfFastMemory([Rendering.CommandBuffer](Rendering.CommandBuffer.html)
cmd, [Rendering.RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)
rid, bool copyContents);

### Parameters

rid | The render target to remove from fast GPU memory.  
---|---  
copyContents | When this value is true, Unity copies the existing contents of the render target when it removes it from fast GPU memory. When this value is false, Unity does not copy the existing contents of the render target when it removes it from fast GPU memory. Set this value to true if you plan to add to the existing contents, and set it to false if you plan to overwrite or clear the existing contents. Where possible, set this value to false for better performance.  
  
### Description

Adds a command to remove a given render target from fast GPU memory.

On certain console platforms, you can put render targets in fast GPU memory
for improved rendering performance.  
  
On platforms that do not support fast GPU memory, this function does nothing.  
  
On platforms that support fast GPU memory, the results of this function depend
on the state of the render target at the time that the graphics API executes
this command. If the render target is in fast GPU memory, Unity removes the
render target from fast GPU memory. If the render target is not in fast GPU
memory, Unity does nothing. There is no performance cost in this case.  
  
Additional resources:
[CommandBufferExtensions.SwitchIntoFastMemory](Rendering.CommandBufferExtensions.SwitchIntoFastMemory.html)

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

