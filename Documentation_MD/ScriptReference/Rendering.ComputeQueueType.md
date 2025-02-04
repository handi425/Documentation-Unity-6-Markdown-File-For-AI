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

# ComputeQueueType

enumeration

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

Describes the desired characteristics with respect to prioritisation and load
balancing of the queue that a command buffer being submitted via
[Graphics.ExecuteCommandBufferAsync](Graphics.ExecuteCommandBufferAsync.html)
or [[ScriptableRenderContext.ExecuteCommandBufferAsync] should be sent to.

### Properties

[Default](Rendering.ComputeQueueType.Default.html)| This queue type would be
the choice for compute tasks supporting or as optimisations to graphics
processing. CommandBuffers sent to this queue would be expected to complete
within the scope of a single frame and likely be synchronised with the
graphics queue via GPUFences. Dispatches on default queue types would execute
at a lower priority than graphics queue tasks.  
---|---  
[Background](Rendering.ComputeQueueType.Background.html)| Background queue
types would be the choice for tasks intended to run for an extended period of
time, e.g for most of a frame or for several frames. Dispatches on background
queues would execute at a lower priority than gfx queue tasks.  
[Urgent](Rendering.ComputeQueueType.Urgent.html)| This queue type would be the
choice for compute tasks requiring processing as soon as possible and would be
prioritised over the graphics queue.  
  
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

