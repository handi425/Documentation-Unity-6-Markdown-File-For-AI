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

# ColliderDistance2D

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

Represents the separation or overlap of two [Collider2D](Collider2D.html).

The [ColliderDistance2D](ColliderDistance2D.html) primarily defines a point on
the exterior of each [Collider2D](Collider2D.html) along with the
[distance](ColliderDistance2D-distance.html) between those two points. The
[distance](ColliderDistance2D-distance.html) between them can be positive
indicating that the [Collider2D](Collider2D.html) are separated (not
overlapped), zero indicating that they are touching (but not overlapped) or
negative indicating that they are overlapped.  
  
A [normal](ColliderDistance2D-normal.html) is provided that is a normalized
vector that points from [pointB](ColliderDistance2D-pointB.html) to
[pointA](ColliderDistance2D-pointA.html). This vector, when scaled with the
[distance](ColliderDistance2D-distance.html), provide a vector that can be
used to move the [Collider2D](Collider2D.html) so that they are no longer
overlapped (if the [distance](ColliderDistance2D-distance.html) is negative)
or so they are touching (if the [distance](ColliderDistance2D-distance.html)
is positive).  
  
A common use-case for this is solving overlaps between two
[Collider2D](Collider2D.html), particularly when attached to a
[Rigidbody2D](Rigidbody2D.html) set to be
[RigidbodyType2D.Kinematic](RigidbodyType2D.Kinematic.html).  
  
Additional resources: [Physics2D.Distance](Physics2D.Distance.html),
[Collider2D.Distance](Collider2D.Distance.html) and
[Rigidbody2D.Distance](Rigidbody2D.Distance.html).

### Properties

[distance](ColliderDistance2D-distance.html)| Gets the distance between two
colliders.  
---|---  
[isOverlapped](ColliderDistance2D-isOverlapped.html)| Gets whether the
distance represents an overlap or not.  
[isValid](ColliderDistance2D-isValid.html)| Gets whether the distance is valid
or not.  
[normal](ColliderDistance2D-normal.html)| A normalized vector that points from
pointB to pointA.  
[pointA](ColliderDistance2D-pointA.html)| A point on a Collider2D that is a
specific distance away from pointB.  
[pointB](ColliderDistance2D-pointB.html)| A point on a Collider2D that is a
specific distance away from pointA.  
  
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

