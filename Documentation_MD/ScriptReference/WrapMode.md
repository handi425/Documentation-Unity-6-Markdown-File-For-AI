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

# WrapMode

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

Determines how time is treated outside of the keyframed range of an
[AnimationClip](AnimationClip.html) or [AnimationCurve](AnimationCurve.html).

The WrapMode that the animation system uses for a specific animation is
determined this way:  
You can set the WrapMode of an [AnimationClip](AnimationClip.html) in the
import settings of the clip. This is the recommended way to control the
WrapMode.  
When an [AnimationState](AnimationState.html) is created, it inherits its
WrapMode from the [AnimationClip](AnimationClip.html) it is created from, but
you can also change it from code.  
If the WrapMode of an [AnimationState](AnimationState.html) is set to Default,
the animation system will use the WrapMode from the
[Animation](Animation.html) component.

### Properties

[Once](WrapMode.Once.html)| When time reaches the end of the animation clip,
the clip will automatically stop playing and time will be reset to beginning
of the clip.  
---|---  
[Loop](WrapMode.Loop.html)| When time reaches the end of the animation clip,
time will continue at the beginning.  
[PingPong](WrapMode.PingPong.html)| When time reaches the end of the animation
clip, time will ping pong back between beginning and end.  
[Default](WrapMode.Default.html)| Reads the default repeat mode set higher up.  
[ClampForever](WrapMode.ClampForever.html)| Plays back the animation. When it
reaches the end, it will keep playing the last frame and never stop playing.  
  
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

