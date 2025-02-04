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

# ContactPoint2D

struct in UnityEngine

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

Details about a specific point of contact involved in a 2D physics collision.

A contact point describes a point of intersection between two
[Collider2D](Collider2D.html). [ContactPoint2D](ContactPoint2D.html) can only
exist on [Collider2D](Collider2D.html) that are not set to be triggers as
triggers do not define contact points.  
  
Additional resources: [Collider2D.isTrigger](Collider2D-isTrigger.html),
[Physics2D.GetContacts](Physics2D.GetContacts.html),
[Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html),
[Collider2D.GetContacts](Collider2D.GetContacts.html) and
[Collision2D](Collision2D.html).

### Properties

[bounciness](ContactPoint2D-bounciness.html)| The effective bounciness used
for the ContactPoint2D.  
---|---  
[collider](ContactPoint2D-collider.html)| The incoming Collider2D involved in
the collision with the otherCollider.  
[enabled](ContactPoint2D-enabled.html)| Indicates whether the collision
response or reaction is enabled or disabled.  
[friction](ContactPoint2D-friction.html)| The effective friction used for the
ContactPoint2D.  
[normal](ContactPoint2D-normal.html)| Surface normal at the contact point.  
[normalImpulse](ContactPoint2D-normalImpulse.html)| Gets the impulse applied
at the contact point along the ContactPoint2D.normal.  
[otherCollider](ContactPoint2D-otherCollider.html)| The other Collider2D
involved in the collision with the collider.  
[otherRigidbody](ContactPoint2D-otherRigidbody.html)| The other Rigidbody2D
involved in the collision with the rigidbody.  
[point](ContactPoint2D-point.html)| The point of contact between the two
colliders in world space.  
[relativeVelocity](ContactPoint2D-relativeVelocity.html)| Gets the relative
velocity of the two colliders at the contact point (Read Only).  
[rigidbody](ContactPoint2D-rigidbody.html)| The incoming Rigidbody2D involved
in the collision with the otherRigidbody.  
[separation](ContactPoint2D-separation.html)| Gets the distance between the
colliders at the contact point.  
[tangentImpulse](ContactPoint2D-tangentImpulse.html)| Gets the impulse applied
at the contact point which is perpendicular to the ContactPoint2D.normal.  
  
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

