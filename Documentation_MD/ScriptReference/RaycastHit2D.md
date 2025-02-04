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

# RaycastHit2D

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

Returns information about 2D Colliders detected by a 2D physics query in the
scene.

The RaycastHit2D struct is used to return results from many 2D physics
queries. It contains many pieces of information about a detection result
including the [Collider2D](Collider2D.html) detected along with extra detail
such as the contact point, the distance traversed to that contact point, the
contact normal at that contact point etc.  
  
When using any physics query that returns a RaycastHit2D, you should always
first check to see if it contains a valid result which indicates that a hit
(intersection) was detected. You can do this by checking if the RaycastHit2D
is `true` or `false` (see code examples). Also, when the result is invalid,
all the RaycastHit2D fields will be at their default.  
  
**NOTE** : This type is also used by the following physics queries:  
  
Additional resources: [Physics2D.Raycast](Physics2D.Raycast.html),
[Physics2D.Linecast](Physics2D.Linecast.html),
[Physics2D.BoxCast](Physics2D.BoxCast.html),
[Physics2D.CapsuleCast](Physics2D.CapsuleCast.html),
[Physics2D.CircleCast](Physics2D.CircleCast.html),
[Physics2D.GetRayIntersection](Physics2D.GetRayIntersection.html),
[Collider2D.Cast](Collider2D.Cast.html),
[Rigidbody2D.Cast](Rigidbody2D.Cast.html),
[PhysicsScene2D.Raycast](PhysicsScene2D.Raycast.html),
[PhysicsScene2D.Linecast](PhysicsScene2D.Linecast.html),
[PhysicsScene2D.BoxCast](PhysicsScene2D.BoxCast.html),
[PhysicsScene2D.CapsuleCast](PhysicsScene2D.CapsuleCast.html),
[PhysicsScene2D.CircleCast](PhysicsScene2D.CircleCast.html) and
[PhysicsScene2D.GetRayIntersection](PhysicsScene2D.GetRayIntersection.html).

### Properties

[centroid](RaycastHit2D-centroid.html)| The world space centroid (center) of
the physics query shape when it intersects.  
---|---  
[collider](RaycastHit2D-collider.html)| The Collider2D detected by the physics
query.  
[distance](RaycastHit2D-distance.html)| The distance the physics query
traversed before it detected a Collider2D.  
[fraction](RaycastHit2D-fraction.html)| The fraction of the distance specified
to the physics query before it detected a Collider2D.  
[normal](RaycastHit2D-normal.html)| The surface normal of the detected
Collider2D.  
[point](RaycastHit2D-point.html)| The world space position where the physics
query shape intersected with the detected Collider2D surface.  
[rigidbody](RaycastHit2D-rigidbody.html)| The Rigidbody2D that the Collider2D
detected by the physics query is attached to.  
[transform](RaycastHit2D-transform.html)| The Transform on the GameObject that
the Collider2D is attached to.  
  
### Operators

[bool](RaycastHit2D-operator_RaycastHit2D.html)| Implicit operator used to
return a true or false result indicating if the result is valid or not.  
---|---  
  
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

