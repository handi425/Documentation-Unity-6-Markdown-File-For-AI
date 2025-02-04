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

#  [Animation](Animation.html).CrossFadeQueued

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

[Switch to Manual](../Manual/class-Animation.html "Go to Animation Component
in the Manual")

## Declaration

public [AnimationState](AnimationState.html) CrossFadeQueued(string animation,
float fadeLength = 0.3F, [QueueMode](QueueMode.html) queue =
QueueMode.CompleteOthers, [PlayMode](PlayMode.html) mode =
PlayMode.StopSameLayer);

### Description

Cross fades an animation after previous animations has finished playing.

For example you might play a specific sequence of animations after each other.  
  
The animation duplicates itself before playing thus you can fade between the
same animation. This can be used to overlay two same animations. For example
you might have a sword swing animation. The player slashes two times quickly
after each other. You could rewind the animation and play from the beginning
but then you will get a jump in the animation.  
  
The following [queue modes](QueueMode.html) are available:  
If `queue` is [QueueMode.CompleteOthers](QueueMode.CompleteOthers.html) this
animation will only start once all other animations have stopped playing.  
If `queue` is [QueueMode.PlayNow](QueueMode.PlayNow.html) this animation will
start playing immediately on a duplicated animation state.  
  
After the animation has finished playing it will automatically clean itself
up. Using the duplicated animation state after it has finished will result in
an exception.  
  

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

