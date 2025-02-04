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
[Rigidbody2D.SlideMovement](Rigidbody2D.SlideMovement.html).surfaceSlideAngle

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

public float surfaceSlideAngle;

### Description

When the velocity movement causes a contact with a
[Collider2D](Collider2D.html), a slide maybe occur if the surface angle is
less than this angle.

Use this angle threshold to control whether slippage will occur on surface
slopes above the threshold.  
  
The angle is in degrees and is relative to the
[Rigidbody2D.SlideMovement.surfaceUp](Rigidbody2D.SlideMovement-
surfaceUp.html) vector.  
  
**NOTE:** Slide will only occur if some initial `velocity` is passed to the
[Rigidbody2D.Slide](Rigidbody2D.Slide.html) method.  
  
Additional resources:
[Rigidbody2D.SlideMovement.gravitySlipAngle](Rigidbody2D.SlideMovement-
gravitySlipAngle.html), [Rigidbody2D.Slide](Rigidbody2D.Slide.html) and
[SlideResults](Rigidbody2D.SlideResults.html).

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

