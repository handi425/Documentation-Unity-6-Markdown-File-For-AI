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

#  [PhysicsScene2D](PhysicsScene2D.html).Linecast

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

public [RaycastHit2D](RaycastHit2D.html) Linecast([Vector2](Vector2.html)
start, [Vector2](Vector2.html) end, int layerMask =
Physics2D.DefaultRaycastLayers);

## Declaration

public [RaycastHit2D](RaycastHit2D.html) Linecast([Vector2](Vector2.html)
start, [Vector2](Vector2.html) end, [ContactFilter2D](ContactFilter2D.html)
contactFilter);

### Parameters

start | The start point of the line in world space.  
---|---  
end | The end point of the line in world space.  
layerMask | The filter used to detect Colliders only on certain layers.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**RaycastHit2D** The cast results returned.

### Description

Casts a line segment against colliders in the PhysicsScene2D, returning the
first intersection only.

A _linecast_ is an imaginary line between two points in world space. Any
[Collider2D](Collider2D.html) making contact with this line can be detected
and reported. This differs from the similar _raycast_ in that raycasting
specifies the line using an origin, direction and distance. Linecasts are
useful for determining lines of sight, targets hit by gunfire and for many
other purposes in gameplay.  
  
This function returns a RaycastHit2D object when the line contacts a
[Collider2D](Collider2D.html) in the Scene. The direction of the line is
assumed to extend from the start point to the end point. Only the first
collider encountered in that direction will be reported.  
  
The _layerMask_ can be used to detect objects selectively only on certain
layers (this allows you to apply the detection only to enemy characters, for
example). Overloads of this method that use `contactFilter` can filter the
results by the options available in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect collider(s) at the start of the ray. In
this case, the ray starts inside the collider and doesn't intersect the
collider surface. This means that the collision normal cannot be calculated,
in which case the returned collision normal is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html),
[RaycastHit2D](RaycastHit2D.html), [LayerMask](LayerMask.html),
[Physics2D.DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[Physics2D.IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html).

* * *

## Declaration

public int Linecast([Vector2](Vector2.html) start, [Vector2](Vector2.html)
end, RaycastHit2D[] results, int layerMask = Physics2D.DefaultRaycastLayers);

## Declaration

public int Linecast([Vector2](Vector2.html) start, [Vector2](Vector2.html)
end, [ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[]
results);

### Parameters

start | The start point of the line in world space.  
---|---  
end | The end point of the line in world space.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
layerMask | The filter used to detect Colliders only on certain layers.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Casts a line segment against colliders in the PhysicsScene2D.

A _linecast_ is an imaginary line between two points in world space. Any
[Collider2D](Collider2D.html) making contact with this line can be detected
and reported. This differs from the similar _raycast_ in that raycasting
specifies the line using an origin, direction and distance. Linecasts are
useful for determining lines of sight, targets hit by gunfire and for many
other purposes in gameplay.  
  
This function returns any [Collider2D](Collider2D.html) that intersect the
line segment with the results returned in the supplied array. The integer
return value is the number of objects that intersect the line (possibly zero)
but the results array will not be resized if it doesn't contain enough
elements to report all the results. The significance of this is that no memory
is allocated for the results and so garbage collection performance is
improved. Note that you will always get zero results if you pass an empty
array.  
  
The _layerMask_ can be used to detect objects selectively only on certain
layers (this allows you to apply the detection only to enemy characters, for
example). Overloads of this method that use `contactFilter` can filter the
results by the options available in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect collider(s) at the start of the ray. In
this case, the ray starts inside the collider and doesn't intersect the
collider surface. This means that the collision normal cannot be calculated,
in which case the returned collision normal is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
All results are sorted by ascending distance order.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html),
[RaycastHit2D](RaycastHit2D.html), [LayerMask](LayerMask.html),
[Physics2D.DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[Physics2D.IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html).

* * *

## Declaration

public int Linecast([Vector2](Vector2.html) start, [Vector2](Vector2.html)
end, [ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results);

### Parameters

start | The start point of the line in world space.  
---|---  
end | The end point of the line in world space.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The listto receive results.  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

Casts a line segment against Colliders in the PhysicsScene2D.

A _linecast_ is an imaginary line between two points in world space. Any
[Collider2D](Collider2D.html) making contact with this line can be detected
and reported. This differs from the similar _raycast_ in that raycasting
specifies the line using an origin, direction and distance. Linecasts are
useful for determining lines of sight, targets hit by gunfire and for many
other purposes in gameplay.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`. All results are
sorted by ascending distance order.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html) and
[RaycastHit2D](RaycastHit2D.html).  
  
All results are sorted by ascending distance order.  
  
Additional resources: [PhysicsScene2D](PhysicsScene2D.html),
[RaycastHit2D](RaycastHit2D.html), [LayerMask](LayerMask.html),
[Physics2D.DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[Physics2D.IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[Physics2D.queriesHitTriggers](Physics2D-queriesHitTriggers.html).

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

