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

# PhysicsMaterialCombine2D

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

Describes how [PhysicsMaterial2D](PhysicsMaterial2D.html) friction and
bounciness are combined when two [Collider2D](Collider2D.html) come into
contact.

When two [Collider2D](Collider2D.html) come into contact, each might has its
own [PhysicsMaterial2D](PhysicsMaterial2D.html) assigned, and each with its
own [PhysicsMaterial2D.friction](PhysicsMaterial2D-friction.html) and
[PhysicsMaterial2D.bounciness](PhysicsMaterial2D-bounciness.html). To
calculate the collision response, both friction and bounciness values must be
combined using the [PhysicsMaterialCombine2D](PhysicsMaterialCombine2D.html)
provides multiple algorithms.  
  
**Note:** Each [Collider2D](Collider2D.html) can have a unique
[PhysicsMaterial2D](PhysicsMaterial2D.html) with different combine modes for
friction and bounciness. When different modes are set, the mode with the
highest priority is used in this order:
[Maximum](PhysicsMaterialCombine2D.Maximum.html),
[Minimum](PhysicsMaterialCombine2D.Minimum.html),
[Multiply](PhysicsMaterialCombine2D.Multiply.html),
[Mean](PhysicsMaterialCombine2D.Mean.html), and
[Average](PhysicsMaterialCombine2D.Average.html). For example, if one
[PhysicsMaterial2D](PhysicsMaterial2D.html) uses
[Average](PhysicsMaterialCombine2D.Average.html) while the other uses
[Maximum](PhysicsMaterialCombine2D.Maximum.html), the
[Maximum](PhysicsMaterialCombine2D.Maximum.html) combine function is used
because it has higher priority.  
  
Additional resources:
[PhysicsMaterial2D.frictionCombine](PhysicsMaterial2D-frictionCombine.html),
[PhysicsMaterial2D.bounceCombine](PhysicsMaterial2D-bounceCombine.html)

### Properties

[Average](PhysicsMaterialCombine2D.Average.html)| Uses an Average algorithm
when combining friction or bounciness.  
---|---  
[Mean](PhysicsMaterialCombine2D.Mean.html)| Uses a Geomtric Mean algorithm
when combining friction or bounciness.  
[Multiply](PhysicsMaterialCombine2D.Multiply.html)| Uses a Multiply algorithm
when combining friction or bounciness i.e. the product of the two values is
used.  
[Minimum](PhysicsMaterialCombine2D.Minimum.html)| Uses a Minimum algorithm
when combining friction or bounciness i.e. the minimum of the two values is
used.  
[Maximum](PhysicsMaterialCombine2D.Maximum.html)| Uses a Maximum algorithm
when combining friction or bounciness i.e. the maximum of the two values is
used.  
  
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

