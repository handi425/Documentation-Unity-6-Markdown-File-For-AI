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

#  [Graphics](Graphics.html).CreateGraphicsFence

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

public static [Rendering.GraphicsFence](Rendering.GraphicsFence.html)
CreateGraphicsFence([Rendering.GraphicsFenceType](Rendering.GraphicsFenceType.html)
fenceType,
[Rendering.SynchronisationStageFlags](Rendering.SynchronisationStageFlags.html)
stage = SynchronisationStage.PixelProcessing);

### Parameters

fenceType | The [GraphicsFenceType](Rendering.GraphicsFenceType.html) to create. Currently the only supported value is [GraphicsFenceType.AsyncQueueSynchronisation](Rendering.GraphicsFenceType.AsyncQueueSynchronisation.html).  
---|---  
stage | Which [SynchronisationStage](Rendering.SynchronisationStage.html) to insert the fence after.  
  
### Returns

**GraphicsFence** Returns a new [GraphicsFence](Rendering.GraphicsFence.html).

### Description

Creates a [GraphicsFence](Rendering.GraphicsFence.html).

The GPU passes through the `GraphicsFence` fence after it completes the
`Blit`, `Clear`, `Draw`, `Dispatch` or texture copy command you sent before
this call. This includes commands from [command
buffers](Rendering.CommandBuffer.html) that the GPU executes immediately
before you create the fence.  
  
You can use the `stage` parameter to insert the
[GraphicsFence](Rendering.GraphicsFence.html) fence after the end of either
vertex or pixel processing. On some platforms, there's a gap between the end
of vertex processing and the start of pixel processing in a draw call.  
  
If the previous command was a compute shader dispatch, Unity ignores `stage`.  
  
Some platforms cannot differentiate between the end of vertex processing and
the end of pixel processing. On these platforms, you'll get the same results
regardless of whether you use
[SynchronisationStage.PixelProcessing](Rendering.SynchronisationStage.PixelProcessing.html)
or
[SynchronisationStage.VertexProcessing](Rendering.SynchronisationStage.VertexProcessing.html)
as the value for `stage`.  
  
If you call `CreateGraphicsFence` on a platform that doesn't support fences,
the fence has no function, and the methods
[Graphics.WaitOnAsyncGraphicsFence](Graphics.WaitOnAsyncGraphicsFence.html)
and
[CommandBuffer.WaitOnAsyncGraphicsFence](Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html)
do nothing. Use [SystemInfo.supportsGraphicsFence](SystemInfo-
supportsGraphicsFence.html) to check if a platform supports fences.  
  
Additional resources: [GraphicsFence](Rendering.GraphicsFence.html),
[Graphics.WaitOnAsyncGraphicsFence](Graphics.WaitOnAsyncGraphicsFence.html),
[CommandBuffer.WaitOnAsyncGraphicsFence](Rendering.CommandBuffer.WaitOnAsyncGraphicsFence.html).

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

