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

#  [Physics2D](Physics2D.html).reuseCollisionCallbacks

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

public static bool reuseCollisionCallbacks;

### Description

Determines whether the garbage collector should reuse only a single instance
of a Collision2D type for all collision callbacks.

When an
[MonoBehaviour.OnCollisionEnter2D](MonoBehaviour.OnCollisionEnter2D.html),
[MonoBehaviour.OnCollisionStay2D](MonoBehaviour.OnCollisionStay2D.html) or
[MonoBehaviour.OnCollisionExit2D](MonoBehaviour.OnCollisionExit2D.html)
collision callback occurs, the [Collision2D](Collision2D.html) object passed
to it is created for each individual callback. This means the garbage
collector has to remove each object, which reduces performance.  
  
When this option is true, only a single instance of the
[Collision2D](Collision2D.html) type is created and reused for each individual
callback. This reduces waste for the garbage collector to handle and improves
performance.  
  
You would only set this option to false if the [Collision2D](Collision2D.html)
object is referenced outside of the collision callback for processing later,
so recycling the [Collision2D](Collision2D.html) object is not required.

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

