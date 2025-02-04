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

#  [Physics2D](Physics2D.html).BoxCast

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

public static [RaycastHit2D](RaycastHit2D.html)
BoxCast([Vector2](Vector2.html) origin, [Vector2](Vector2.html) size, float
angle, [Vector2](Vector2.html) direction, float distance = Mathf.Infinity, int
layerMask = Physics2D.AllLayers, float minDepth = -Mathf.Infinity, float
maxDepth = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the box originates.  
---|---  
size | The size of the box.  
angle | The angle of the box (in degrees).  
direction | A vector representing the direction of the box.  
distance | The maximum distance over which to cast the box.  
layerMask | Filter to detect Colliders only on certain layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
  
### Returns

**RaycastHit2D** The cast results returned.

### Description

Casts a box against Colliders in the Scene, returning the first Collider to
contact with it.

A _BoxCast_ is conceptually like dragging a box through the Scene in a
particular direction. Any object making contact with the box can be detected
and reported.  
  
This function returns a [RaycastHit2D](RaycastHit2D.html) object with a
reference to the Collider that is hit by the box (the Collider property of the
result will be NULL if nothing was hit). The _layerMask_ can be used to detect
objects selectively only on certain layers (this allows you to apply the
detection only to enemy characters, for example).  
  
The returned [RaycastHit2D](RaycastHit2D.html) returns both the point and
normal of the contact where the box would touch the Collider. It also returns
the centroid where the box would be positioned for it to contact at that
point.  
  
[BoxCast](Physics2D.BoxCast.html) has a `size` option. This defines how large
the box is. The box is fired through the world. The larger the box is the more
GameObjects will be hit.  
  
[BoxCast](Physics2D.BoxCast.html) also has a `angle` option. The box which is
fired through the elements in the game can be rotated. This means that the
collision between the BoxCast and a GameObject can be more hard to observe.  
  
The [BoxCast](Physics2D.BoxCast.html).direction variable determines how the
Box moves in the Game. This is a 2D variable controlling the horizontal and
vertical directions.  
  
[Distance](Physics2D.Distance.html) controls how far from the `origin` the Box
travels. It may interact with many `Colliders` or none. In these cases the
closest [Collider2D](Collider2D.html) provides the values set in the
[RaycastHit2D](RaycastHit2D.html) variable. If no `Collider2D` is hit then
NULL is returned.  
  
Additional resources: [LayerMask](LayerMask.html) class,
[RaycastHit2D](RaycastHit2D.html) class,
[BoxCastAll](Physics2D.BoxCastAll.html),
[BoxCastNonAlloc](Physics2D.BoxCastNonAlloc.html),
[DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[raycastsHitTriggers](Physics2D-raycastsHitTriggers.html).

* * *

## Declaration

public static int BoxCast([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) size, float angle, [Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[] results,
float distance = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the box originates.  
---|---  
size | The size of the box.  
angle | The angle of the box (in degrees).  
direction | A vector representing the direction of the box.  
distance | The maximum distance over which to cast the box.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Casts a box against the Colliders in the Scene and returns all Colliders that
are in contact with it.

This function returns the number of contacts found and places those contacts
in the `results` array. The results can also be filtered by the
`contactFilter`.  
  
Additional resources: [ContactFilter2D](ContactFilter2D.html) and
[RaycastHit2D](RaycastHit2D.html).

* * *

## Declaration

public static int BoxCast([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) size, float angle, [Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results, float distance = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the box originates.  
---|---  
size | The size of the box.  
angle | The angle of the box (in degrees).  
direction | A vector representing the direction of the box.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The list to receive results.  
distance | The maximum distance over which to cast the box.  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

Casts a box against the Colliders in the Scene and returns all Colliders that
are in contact with it.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [ContactFilter2D](ContactFilter2D.html) and
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

