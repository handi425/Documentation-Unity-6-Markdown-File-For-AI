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

#  [Rigidbody2D](Rigidbody2D.html).Cast

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

public int Cast([Vector2](Vector2.html) direction, List<RaycastHit2D> results,
float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
---|---  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

All the [Collider2D](Collider2D.html) shapes attached to the
[Rigidbody2D](Rigidbody2D.html) are cast into the Scene starting at each
Collider position ignoring the Colliders attached to the same
[Rigidbody2D](Rigidbody2D.html).

This function will take all the [Collider2D](Collider2D.html) shapes attached
to the [Rigidbody2D](Rigidbody2D.html) and cast them into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` list.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additionally, this will also detect other Collider(s) overlapping the collider
start position. In this case the cast shape will be starting inside the
Collider and may not intersect the Collider surface. This means that the
collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results, float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
---|---  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

All the [Collider2D](Collider2D.html) shapes attached to the
[Rigidbody2D](Rigidbody2D.html) are cast into the Scene starting at each
Collider position ignoring the Colliders attached to the same
[Rigidbody2D](Rigidbody2D.html).

This function will take all the [Collider2D](Collider2D.html) shapes attached
to the [Rigidbody2D](Rigidbody2D.html) and cast them into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` list.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options
in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect other Collider(s) overlapping the collider
start position. In this case the cast shape will be starting inside the
Collider and may not intersect the Collider surface. This means that the
collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction, RaycastHit2D[] results,
float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
---|---  
results | Array to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

All the [Collider2D](Collider2D.html) shapes attached to the
[Rigidbody2D](Rigidbody2D.html) are cast into the Scene starting at each
Collider position ignoring the Colliders attached to the same
[Rigidbody2D](Rigidbody2D.html).

This function will take all the [Collider2D](Collider2D.html) shapes attached
to the [Rigidbody2D](Rigidbody2D.html) and cast them into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` array.  
  
The integer return value is the number of results written into the `results`
array. The results array will not be resized if it doesn't contain enough
elements to report all the results. The significance of this is that no memory
is allocated for the results and so garbage collection performance is improved
when casts are performed frequently.  
  
Additionally, this will also detect other Collider(s) overlapping the collider
start position. In this case the cast shape will be starting inside the
Collider and may not intersect the Collider surface. This means that the
collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[] results,
float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
---|---  
contactFilter | Filter results defined by the contact filter.  
results | Array to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

All the [Collider2D](Collider2D.html) shapes attached to the
[Rigidbody2D](Rigidbody2D.html) are cast into the Scene starting at each
Collider position ignoring the Colliders attached to the same
[Rigidbody2D](Rigidbody2D.html).

This function will take all the [Collider2D](Collider2D.html) shapes attached
to the [Rigidbody2D](Rigidbody2D.html) and cast them into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` array.  
  
The integer return value is the number of results written into the `results`
array. The results array will not be resized if it doesn't contain enough
elements to report all the results. The significance of this is that no memory
is allocated for the results and so garbage collection performance is improved
when casts are performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options
in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect other Collider(s) overlapping the collider
start position. In this case the cast shape will be starting inside the
Collider and may not intersect the Collider surface. This means that the
collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) position, float angle,
[Vector2](Vector2.html) direction, List<RaycastHit2D> results, float distance
= Mathf.Infinity);

### Parameters

position | The position to start casting the rigidbody from.  
---|---  
angle | The rotation of the rigidbody.  
direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

The [Rigidbody2D](Rigidbody2D.html) is cast into the Scene starting at the
specified position and rotation. All the [Collider2D](Collider2D.html) shapes
attached to the [Rigidbody2D](Rigidbody2D.html) are cast along with it
ignoring the Colliders attached to the same [Rigidbody2D](Rigidbody2D.html).

This function, unlike [Rigidbody2D.Cast](Rigidbody2D.Cast.html) allows you to
cast the [Rigidbody2D](Rigidbody2D.html) and all its attached
[Collider2D](Collider2D.html) through the scene but also allows the starting
`position` and `angle` of the [Rigidbody2D](Rigidbody2D.html) to be specified.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
**NOTE** : Additionally, this will also detect other Collider(s) overlapping
the start position. In this case the cast shape will be starting inside
another Collider and may not intersect the Collider surface. This means that
the collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.  
  
Additional resources: [Rigidbody2D.Cast](Rigidbody2D.Cast.html) and
[ContactFilter2D](ContactFilter2D.html).

* * *

## Declaration

public int Cast([Vector2](Vector2.html) position, float angle,
[Vector2](Vector2.html) direction, [ContactFilter2D](ContactFilter2D.html)
contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity);

### Parameters

position | The position to start casting the rigidbody from.  
---|---  
angle | The rotation of the rigidbody.  
direction | Vector representing the direction to cast each [Collider2D](Collider2D.html) shape.  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider(s).  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

The [Rigidbody2D](Rigidbody2D.html) is cast into the Scene starting at the
specified position and rotation. All the [Collider2D](Collider2D.html) shapes
attached to the [Rigidbody2D](Rigidbody2D.html) are cast along with it
ignoring the Colliders attached to the same [Rigidbody2D](Rigidbody2D.html).

This function, unlike [Rigidbody2D.Cast](Rigidbody2D.Cast.html) allows you to
cast the [Rigidbody2D](Rigidbody2D.html) and all its attached
[Collider2D](Collider2D.html) through the scene but also allows the starting
`position` and `angle` of the [Rigidbody2D](Rigidbody2D.html) to be specified.  
  
This function also uses the specified `contactFilter` therefore the specific
[LayerMask](LayerMask.html) of each [Collider2D](Collider2D.html) attached to
this [Rigidbody2D](Rigidbody2D.html) is not used to detect contacts. If this
isn't desired then the CastFrom overload without the
[ContactFilter2D](ContactFilter2D.html) argument should be used.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
**NOTE** : Additionally, this will also detect other Collider(s) overlapping
the start position. In this case the cast shape will be starting inside
another Collider and may not intersect the Collider surface. This means that
the collision normal cannot be calculated in which case the collision normal
returned is set to the inverse of the `direction` vector being tested.  
  
Additional resources: [Rigidbody2D.Cast](Rigidbody2D.Cast.html) and
[ContactFilter2D](ContactFilter2D.html).

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

