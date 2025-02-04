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

#  [PhysicsScene2D](PhysicsScene2D.html).CapsuleCast

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

public [RaycastHit2D](RaycastHit2D.html) CapsuleCast([Vector2](Vector2.html)
origin, [Vector2](Vector2.html) size,
[CapsuleDirection2D](CapsuleDirection2D.html) capsuleDirection, float angle,
[Vector2](Vector2.html) direction, float distance, int layerMask =
Physics2D.DefaultRaycastLayers);

## Declaration

public [RaycastHit2D](RaycastHit2D.html) CapsuleCast([Vector2](Vector2.html)
origin, [Vector2](Vector2.html) size,
[CapsuleDirection2D](CapsuleDirection2D.html) capsuleDirection, float angle,
[Vector2](Vector2.html) direction, float distance,
[ContactFilter2D](ContactFilter2D.html) contactFilter);

### Parameters

origin | The point in 2D space where the capsule originates.  
---|---  
size | The size of the capsule.  
capsuleDirection | The direction of the capsule.  
angle | The angle of the capsule (in degrees).  
direction | Vector representing the direction to cast the capsule.  
distance | Maximum distance over which to cast the capsule.  
layerMask | The filter used to detect Colliders only on certain layers.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**RaycastHit2D** The cast results returned.

### Description

Casts a capsule against colliders in the PhysicsScene2D, returning the first
intersection only.

A _CapsuleCast_ is conceptually like dragging a capsule shape through the
Scene in a particular direction. Any [Collider2D](Collider2D.html) making
contact with the capsule can be detected and reported.  
  
This function returns a [RaycastHit2D](RaycastHit2D.html) object with a
reference to the collider that is hit by the capsule (the collider property of
the result will be NULL if nothing was hit) and contains both the point and
normal of the contact where the capsule would touch the collider. It also
returns the centroid where the capsule would be positioned for it to contact
the collider at that point.  
  
The _layerMask_ can be used to detect objects selectively only on certain
layers (this allows you to apply the detection only to enemy characters, for
example). Overloads of this method that use `contactFilter` can filter the
results by the options available in [ContactFilter2D](ContactFilter2D.html).  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html),
[RaycastHit2D](RaycastHit2D.html), [LayerMask](LayerMask.html),
[Physics2D.DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[Physics2D.IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html).

* * *

## Declaration

public int CapsuleCast([Vector2](Vector2.html) origin, [Vector2](Vector2.html)
size, [CapsuleDirection2D](CapsuleDirection2D.html) capsuleDirection, float
angle, [Vector2](Vector2.html) direction, float distance, RaycastHit2D[]
results, int layerMask = Physics2D.DefaultRaycastLayers);

## Declaration

public int CapsuleCast([Vector2](Vector2.html) origin, [Vector2](Vector2.html)
size, [CapsuleDirection2D](CapsuleDirection2D.html) capsuleDirection, float
angle, [Vector2](Vector2.html) direction, float distance,
[ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[]
results);

### Parameters

origin | The point in 2D space where the capsule originates.  
---|---  
size | The size of the capsule.  
capsuleDirection | The direction of the capsule.  
angle | The angle of the capsule (in degrees).  
direction | Vector representing the direction to cast the capsule.  
distance | Maximum distance over which to cast the capsule.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
layerMask | The filter used to detect Colliders only on certain layers.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Casts a capsule against the Colliders in the PhysicsScene2D, returning all
intersections.

A _CapsuleCast_ is conceptually like dragging a capsule shape through the
Scene in a particular direction. Any [Collider2D](Collider2D.html) making
contact with the capsule can be detected and reported.  
  
This function returns an array of [RaycastHit2D](RaycastHit2D.html) object(s)
with a reference to the collider that is hit by the capsule (the collider
property of the result will be NULL if nothing was hit) and contains both the
point and normal of the contact where the capsule would touch the collider. It
also returns the centroid where the capsule would be positioned for it to
contact the collider at that point.  
  
The integer return value is the number of objects that intersect the capsule
(possibly zero) but the results array will not be resized if it doesn't
contain enough elements to report all the results. The significance of this is
that no memory is allocated for the results and so garbage collection
performance is improved. Note that you will always get zero results if you
pass an empty array.  
  
The _layerMask_ can be used to detect objects selectively only on certain
layers (this allows you to apply the detection only to enemy characters, for
example). Overloads of this method that use `contactFilter` can filter the
results by the options available in [ContactFilter2D](ContactFilter2D.html).  
  
All results are sorted by ascending distance order.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html),
[RaycastHit2D](RaycastHit2D.html), [LayerMask](LayerMask.html),
[Physics2D.DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[Physics2D.IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html).

* * *

## Declaration

public int CapsuleCast([Vector2](Vector2.html) origin, [Vector2](Vector2.html)
size, [CapsuleDirection2D](CapsuleDirection2D.html) capsuleDirection, float
angle, [Vector2](Vector2.html) direction, float distance,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results);

### Parameters

origin | The point in 2D space where the capsule originates.  
---|---  
size | The size of the capsule.  
capsuleDirection | The direction of the capsule.  
angle | The angle of the capsule (in degrees).  
direction | Vector representing the direction to cast the capsule.  
distance | Maximum distance over which to cast the capsule.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The list to receive results.  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

Casts a capsule against the Colliders in the PhysicsScene2D, returning all
intersections.

A _CapsuleCast_ is conceptually like dragging a capsule shape through the
Scene in a particular direction. Any Collider making contact with the capsule
can be detected and reported.  
  
The integer return value is the number of objects that intersect the capsule
(possibly zero) but the results array will not be resized if it doesn't
contain enough elements to report all the results. This prevents memory from
being allocated for results when the `results` list does not need to be
resized, and improves garbage collection performance when the query is
performed frequently.  
  
The results can also be filtered by the `contactFilter`. All results are
sorted by ascending distance order.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html) and
[RaycastHit2D](RaycastHit2D.html).

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

