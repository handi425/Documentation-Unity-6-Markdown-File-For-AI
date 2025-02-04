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

#  [Collider2D](Collider2D.html).Cast

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
float distance = Mathf.Infinity, bool ignoreSiblingColliders = true);

### Parameters

direction | Vector representing the direction to cast the shape.  
---|---  
results | List to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling Colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the Collider position
ignoring the Collider itself.

This function will take the Collider shape and cast it into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` list. The integer
return value is the number of results written into the `results` list. The
results list will be resized if it doesn't contain enough elements to report
all the results. This prevents memory from being allocated for results when
the `results` list does not need to be resized, and improves garbage
collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start
position if they are overlapping. In this case, the cast shape will start
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated, in which case the returned
collision normal is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results, float distance = Mathf.Infinity, bool ignoreSiblingColliders = true);

### Parameters

direction | Vector representing the direction to cast the shape.  
---|---  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling Colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the Collider position
ignoring the Collider itself.

This function will take the Collider shape and cast it into the Scene starting
at the Collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` list. The integer
return value is the number of results written into the `results` list. The
results list will be resized if it doesn't contain enough elements to report
all the results. This prevents memory from being allocated for results when
the `results` list does not need to be resized, and improves garbage
collection performance when casts are performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options
in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this also detects other Collider(s) at the Collider start
position if they are overlapping. In this case, the cast shape will start
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated, in which case the returned
collision normal is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction, RaycastHit2D[] results,
float distance = Mathf.Infinity, bool ignoreSiblingColliders = true);

### Parameters

direction | Vector representing the direction to cast the shape.  
---|---  
results | Array to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling Colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the Collider position
ignoring the Collider itself.

This function will take the collider shape and cast it into the Scene starting
at the collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` array. The integer
return value is the number of results written into the `results` array. The
results array will not be resized if it doesn't contain enough elements to
report all the results. The significance of this is that no memory is
allocated for the results and so garbage collection performance is improved
when casts are performed frequently.  
  
Additionally, this will also detect other Collider(s) at the collider start
position if they are overlapping. In this case the cast shape will be starting
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated in which case the collision
normal returned is set to the inverse of the `direction` vector being tested.  
  
**Note:** Use of Collider2D.Cast() requires the use of
[Rigidbody2D](Rigidbody2D.html). If no [Rigidbody2D](Rigidbody2D.html) is
declared [Cast](Collider2D.Cast.html)() does not work. However a
[Rigidbody2D](Rigidbody2D.html) can be static and attached to the
[Collider2D](Collider2D.html). This will make the
[Cast](Collider2D.Cast.html)() work as expected. Also, if the
[Collider2D](Collider2D.html) object has no [Rigidbody2D](Rigidbody2D.html)
object then it can collide with objects which have both
[Collider2D](Collider2D.html) and [Rigidbody2D](Rigidbody2D.html) objects.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[] results,
float distance = Mathf.Infinity, bool ignoreSiblingColliders = true);

### Parameters

direction | Vector representing the direction to cast the shape.  
---|---  
contactFilter | Filter results defined by the contact filter.  
results | Array to receive results.  
distance | Maximum distance over which to cast the shape.  
ignoreSiblingColliders | Determines whether the cast should ignore Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling Colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the Collider position
ignoring the Collider itself.

This function will take the collider shape and cast it into the Scene starting
at the collider position in the specified `direction` for an optional
`distance` and return the results in the provided `results` array. The integer
return value is the number of results written into the `results` array. The
results array will not be resized if it doesn't contain enough elements to
report all the results. The significance of this is that no memory is
allocated for the results and so garbage collection performance is improved
when casts are performed frequently.  
  
The `contactFilter` parameter can filter the returned results by the options
in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect other Collider(s) at the collider start
position if they are overlapping. In this case the cast shape will be starting
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated in which case the collision
normal returned is set to the inverse of the `direction` vector being tested.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) position, float angle,
[Vector2](Vector2.html) direction, List<RaycastHit2D> results, float distance
= Mathf.Infinity, bool ignoreSiblingColliders = true);

### Parameters

position | The position to start casting the Collider from.  
---|---  
angle | The rotation of the Collider.  
direction | Vector representing the direction to cast the Collider.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider.  
ignoreSiblingColliders | Determines whether the cast should ignore other Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the specified position and
rotation.

This function will take the Collider shape and cast it into the Scene starting
at the specified `position` and `angle` for an optional `distance` and return
the results in the provided `results` list.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start
position if they are overlapping. In this case, the cast shape will start
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated, in which case the returned
collision normal is set to the inverse of the `direction` vector being tested.  
  
**NOTE** : The `position` and `angle` used here represent the position of the
[Rigidbody2D](Rigidbody2D.html) the [Collider2D](Collider2D.html) is attached
to. If the [Collider2D](Collider2D.html) is offset from the center of mass
then the [Collider2D](Collider2D.html) will be overlapped at the same offset.
This can be confusing so it is recommened that only
[Collider2D](Collider2D.html) that align with the center of mass are used. If
not then you must take this into account. If the [Collider2D](Collider2D.html)
is not attached to a [Rigidbody2D](Rigidbody2D.html), this call cannot be used
and will result in a warning.

* * *

## Declaration

public int Cast([Vector2](Vector2.html) position, float angle,
[Vector2](Vector2.html) direction, [ContactFilter2D](ContactFilter2D.html)
contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity,
bool ignoreSiblingColliders = true);

### Parameters

position | The position to start casting the Collider from.  
---|---  
angle | The rotation of the Collider.  
direction | Vector representing the direction to cast the Collider.  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the Collider.  
ignoreSiblingColliders | Determines whether the cast should ignore other Colliders attached to the same [Rigidbody2D](Rigidbody2D.html) (known as sibling colliders).  
  
### Returns

**int** The number of results returned.

### Description

Casts the Collider shape into the Scene starting at the specified position and
rotation.

This function will take the Collider shape and cast it into the Scene starting
at the specified `position` and `angle` for an optional `distance` and return
the results in the provided `results` list.  
  
The `contactFilter` parameter can filter the returned results by the options
in [ContactFilter2D](ContactFilter2D.html).  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when casts are performed frequently.  
  
Additionally, this also detects other Collider(s) at the Collider start
position if they are overlapping. In this case, the cast shape will start
inside the Collider and may not intersect the Collider surface. This means
that the collision normal cannot be calculated, in which case the returned
collision normal is set to the inverse of the `direction` vector being tested.  
  
**NOTE** : The `position` and `angle` used here represent the position of the
[Rigidbody2D](Rigidbody2D.html) the [Collider2D](Collider2D.html) is attached
to. If the [Collider2D](Collider2D.html) is offset from the center of mass
then the [Collider2D](Collider2D.html) will be overlapped at the same offset.
This can be confusing so it is recommened that only
[Collider2D](Collider2D.html) that align with the center of mass are used. If
not then you must take this into account. If the [Collider2D](Collider2D.html)
is not attached to a [Rigidbody2D](Rigidbody2D.html), this call cannot be used
and will result in a warning.

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

