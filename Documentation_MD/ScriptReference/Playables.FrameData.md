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

# FrameData

struct in UnityEngine.Playables

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

This structure contains the frame information a
[Playable](Playables.Playable.html) receives in Playable.PrepareFrame.

### Properties

[deltaTime](Playables.FrameData-deltaTime.html)| The interval between this
frame and the preceding frame. The interval is unscaled and expressed in
seconds.  
---|---  
[effectiveParentSpeed](Playables.FrameData-effectiveParentSpeed.html)| The
accumulated speed of the parent Playable during the PlayableGraph traversal.  
[effectivePlayState](Playables.FrameData-effectivePlayState.html)| The
accumulated play state of this playable.  
[effectiveSpeed](Playables.FrameData-effectiveSpeed.html)| The accumulated
speed of the Playable during the PlayableGraph traversal.  
[effectiveWeight](Playables.FrameData-effectiveWeight.html)| The accumulated
weight of the Playable during the PlayableGraph traversal.  
[evaluationType](Playables.FrameData-evaluationType.html)| Indicates the type
of evaluation that caused PlayableGraph.PrepareFrame to be called.  
[frameId](Playables.FrameData-frameId.html)| The current frame identifier.  
[output](Playables.FrameData-output.html)| The PlayableOutput that initiated
this graph traversal.  
[seekOccurred](Playables.FrameData-seekOccurred.html)| Indicates that the
local time was explicitly set.  
[timeHeld](Playables.FrameData-timeHeld.html)| Indicates the local time did
not advance because it has reached the duration and the extrapolation mode is
set to Hold.  
[timeLooped](Playables.FrameData-timeLooped.html)| Indicates the local time
wrapped because it has reached the duration and the extrapolation mode is set
to Loop.  
[weight](Playables.FrameData-weight.html)| The weight of the current Playable.  
  
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

