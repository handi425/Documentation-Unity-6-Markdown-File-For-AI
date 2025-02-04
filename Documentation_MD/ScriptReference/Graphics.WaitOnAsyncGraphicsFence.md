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

#  [Graphics](Graphics.html).WaitOnAsyncGraphicsFence

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
WaitOnAsyncGraphicsFence([Rendering.GraphicsFence](Rendering.GraphicsFence.html)
fence);

## Declaration

public static void
WaitOnAsyncGraphicsFence([Rendering.GraphicsFence](Rendering.GraphicsFence.html)
fence, [Rendering.SynchronisationStage](Rendering.SynchronisationStage.html)
stage = SynchronisationStage.PixelProcessing);

### Parameters

fence | The [GraphicsFence](Rendering.GraphicsFence.html) the GPU waits for. The `fenceType` of the graphics fence must be [GraphicsFenceType.AsyncQueueSynchronisation](Rendering.GraphicsFenceType.AsyncQueueSynchronisation.html).  
---|---  
stage | Which [SynchronisationStage](Rendering.SynchronisationStage.html) to wait for.  
  
### Description

Instructs the GPU to pause processing of the queue until it passes through the
[GraphicsFence](Rendering.GraphicsFence.html) fence.

This method returns immediately on the CPU. Only GPU processing is affected by
the graphics fence.  
  
You can use the `stage` parameter to wait until the start of the next item's
vertex or pixel processing. On some platforms, there's a gap between the end
of vertex processing and the start of pixel processing in a draw call. If the
last command was a compute shader dispatch, Unity ignores `stage`.  
  
This method only works on platforms that support fences. Use
[SystemInfo.supportsGraphicsFence](SystemInfo-supportsGraphicsFence.html) to
check if a platform supports fences.  
  
It's possible to create circular dependencies with this function that deadlock
the GPU. See [GraphicsFence](Rendering.GraphicsFence.html) for more
information.  
  
Additional resources: [GraphicsFence](Rendering.GraphicsFence.html),
[Graphics.CreateGraphicsFence](Graphics.CreateGraphicsFence.html).

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

