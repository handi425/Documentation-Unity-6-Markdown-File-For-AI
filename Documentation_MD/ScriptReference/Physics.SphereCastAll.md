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

#  [Physics](Physics.html).SphereCastAll

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

## Declaration

public static RaycastHit[] SphereCastAll([Vector3](Vector3.html) origin, float
radius, [Vector3](Vector3.html) direction, float maxDistance = Mathf.Infinity,
int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The center of the sphere at the start of the sweep.  
---|---  
radius | The radius of the sphere.  
direction | The direction in which to sweep the sphere.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**RaycastHit[]** An array of all colliders hit in the sweep.

### Description

Like [Physics.SphereCast](Physics.SphereCast.html), but this function will
return all hits the sphere sweep intersects.

Casts a sphere against all colliders in the Scene and returns detailed
information on each collider which was hit. This is useful when a Raycast does
not give enough precision, because you want to find out if an object of a
specific size, such as a character, will be able to move somewhere without
colliding with anything on the way.  
  
**Notes:** For colliders that overlap the sphere at the start of the sweep,
[RaycastHit.normal](RaycastHit-normal.html) is set opposite to the direction
of the sweep, [RaycastHit.distance](RaycastHit-distance.html) is set to zero,
and the zero vector gets returned in [RaycastHit.point](RaycastHit-
point.html). You might want to check whether this is the case in your
particular query and perform additional queries to refine the result. Passing
a zero radius results in undefined output and doesn't always behave the same
as [Physics.Raycast](Physics.Raycast.html).  
  
Additional resources: [Physics.SphereCast](Physics.SphereCast.html),
[Physics.CapsuleCast](Physics.CapsuleCast.html),
[Physics.Raycast](Physics.Raycast.html),
[Rigidbody.SweepTest](Rigidbody.SweepTest.html).

* * *

## Declaration

public static RaycastHit[] SphereCastAll([Ray](Ray.html) ray, float radius,
float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

ray | The starting point and direction of the ray into which the sphere sweep is cast.  
---|---  
radius | The radius of the sphere.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Description

Like [Physics.SphereCast](Physics.SphereCast.html), but this function will
return all hits the sphere sweep intersects.

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

