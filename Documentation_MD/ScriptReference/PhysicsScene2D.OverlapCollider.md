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

#  [PhysicsScene2D](PhysicsScene2D.html).OverlapCollider

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

public static int OverlapCollider([Vector2](Vector2.html) position, float
angle, [Collider2D](Collider2D.html) collider, List<Collider2D> results);

### Parameters

position | The position at which to overlap the Collider.  
---|---  
angle | The angle of at which to overlap the Collider.  
collider | The Collider that defines the area used to query for other Collider overlaps.  
results | The list to receive results.  
  
### Returns

**int** The list to receive results.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
**NOTE** : The `position` and `angle` used here represent the position of the
[Rigidbody2D](Rigidbody2D.html) the [Collider2D](Collider2D.html) is attached
to. If the [Collider2D](Collider2D.html) is offset from the center of mass
then the [Collider2D](Collider2D.html) will be overlapped at the same offset.
This can be confusing so it is recommened that only
[Collider2D](Collider2D.html) that align with the center of mass are used. If
not then you must take this into account. If the [Collider2D](Collider2D.html)
is not attached to a [Rigidbody2D](Rigidbody2D.html), this call cannot be used
and will result in a warning.  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html) and
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html).

* * *

## Declaration

public static int OverlapCollider([Vector2](Vector2.html) position, float
angle, [Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<Collider2D>
results);

### Parameters

position | The position at which to overlap the Collider.  
---|---  
angle | The angle of at which to overlap the Collider.  
collider | The Collider that defines the area used to query for other Collider overlaps.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask and Z depth. Note that the normal angle is not used for overlap testing.  
results | The list to receive results.  
  
### Returns

**int** The list to receive results.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
**NOTE** : The `position` and `angle` used here represent the position of the
[Rigidbody2D](Rigidbody2D.html) the [Collider2D](Collider2D.html) is attached
to. If the [Collider2D](Collider2D.html) is offset from the center of mass
then the [Collider2D](Collider2D.html) will be overlapped at the same offset.
This can be confusing so it is recommened that only
[Collider2D](Collider2D.html) that align with the center of mass are used. If
not then you must take this into account. If the [Collider2D](Collider2D.html)
is not attached to a [Rigidbody2D](Rigidbody2D.html), this call cannot be used
and will result in a warning.  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html) and
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html).

* * *

## Declaration

public static int OverlapCollider([Collider2D](Collider2D.html) collider,
List<Collider2D> results);

### Parameters

collider | The Collider that defines the area used to query for other Collider overlaps.  
---|---  
results | The list to receive results.  
  
### Returns

**int** The list to receive results.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html) and
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html).

* * *

## Declaration

public static int OverlapCollider([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<Collider2D>
results);

### Parameters

collider | The Collider that defines the area used to query for other Collider overlaps.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask and Z depth. Note that the normal angle is not used for overlap testing.  
results | The list to receive results.  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html) and
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html).

* * *

## Declaration

public static int OverlapCollider([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, Collider2D[] results);

### Parameters

collider | The Collider that defines the area used to query for other Collider overlaps.  
---|---  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask and Z depth. Note that the normal angle is not used for overlap testing.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of objects that intersect the box
(possibly zero) but the results array will not be resized if it doesn't
contain enough elements to report all the results. The significance of this is
that no memory is allocated for the results and so garbage collection
performance is improved. Note that you will always get zero results if you
pass an empty array.  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html) and
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html).

* * *

## Declaration

public static int OverlapCollider([Collider2D](Collider2D.html) collider,
Collider2D[] results, int layerMask = Physics2D.DefaultRaycastLayers);

### Parameters

collider | The Collider that defines the area used to query for other Collider overlaps.  
---|---  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
layerMask | Filter to check objects only on specific layers.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Checks a Collider against Colliders in the PhysicsScene2D, returning all
intersections.

An "OverlapCollider" is conceptually like looking at the Scene through a
Collider shape to determine what can be seen. Any
[Collider2D](Collider2D.html) seen can be detected and reported.  
  
The integer return value is the number of objects that intersect the box
(possibly zero) but the results array will not be resized if it doesn't
contain enough elements to report all the results. The significance of this is
that no memory is allocated for the results and so garbage collection
performance is improved. Note that you will always get zero results if you
pass an empty array.  
  
The _layerMask_ can be used to detect objects selectively only on certain
layers (this allows you to apply the detection only to enemy characters, for
example). Overloads of this method that use `contactFilter` can filter the
results by the options available in [ContactFilter2D](ContactFilter2D.html).  
  
Additional resources: [Collider2D.Overlap](Collider2D.Overlap.html),
[Rigidbody2D.Overlap](Rigidbody2D.Overlap.html) and
[LayerMask](LayerMask.html).

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

