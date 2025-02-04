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

#  [AnimatorStateTransition](Animations.AnimatorStateTransition.html).exitTime

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

public float exitTime;

### Description

If [AnimatorStateTransition.hasExitTime](Animations.AnimatorStateTransition-
hasExitTime.html) is true, **exitTime** represents the exact time at which the
transition can take effect.  
This is represented in normalized time, so for example an exit time of 0.75
means that on the first frame where 75% of the animation has played, the Exit
Time condition will be true. On the next frame, the condition will be false.  
For looped animations, transitions with exit times smaller than 1 will be
evaluated every loop, so you can use this to time your transition with the
proper timing in the animation, every loop.  
Transitions with exit times greater than one will be evaluated only once, so
they can be used to exit at a specific time, after a fixed number of loops.
For example, a transition with an exit time of 3.5 will be evaluated once,
after three and a half loops.

**Known limitation:** You need at least one evaluation of your state before
you can trigger an exitTime condition, meaning a transition with an exitTime
of 0 will never be fired on the first frame.

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

