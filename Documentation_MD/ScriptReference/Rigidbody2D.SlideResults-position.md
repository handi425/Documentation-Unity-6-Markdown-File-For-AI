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

#  [Rigidbody2D.SlideResults](Rigidbody2D.SlideResults.html).position

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

public [Vector2](Vector2.html) position;

### Description

The position that was calculate as a target position to move to when
performing a [Rigidbody2D.Slide](Rigidbody2D.Slide.html).

When a [Rigidbody2D.Slide](Rigidbody2D.Slide.html) command is complete, this
will be the position that both the
[Rigidbody2D.position](Rigidbody2D-position.html) and
[Transform.position](Transform-position.html) are set to however, if
[Rigidbody2D.SlideMovement.useSimulationMove](Rigidbody2D.SlideMovement-
useSimulationMove.html) is enabled, then neither the
[Rigidbody2D.position](Rigidbody2D-position.html) and
[Transform.position](Transform-position.html) will be changd upon return but a
[Rigidbody2D.MovePosition](Rigidbody2D.MovePosition.html) would have been
called using this position. If
[Rigidbody2D.SlideMovement.useNoMove](Rigidbody2D.SlideMovement-
useNoMove.html) is enabled then no move is processed at all but is simply
returned here.  
  
Additional resources:
[Rigidbody2D.SlideMovement.useNoMove](Rigidbody2D.SlideMovement-
useNoMove.html),
[Rigidbody2D.SlideMovement.useSimulationMove](Rigidbody2D.SlideMovement-
useSimulationMove.html), [Rigidbody2D.Slide](Rigidbody2D.Slide.html) and
[SlideMovement](Rigidbody2D.SlideMovement.html).

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

