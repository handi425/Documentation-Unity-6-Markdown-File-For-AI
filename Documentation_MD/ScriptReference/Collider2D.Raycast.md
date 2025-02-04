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

#  [Collider2D](Collider2D.html).Raycast

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

public int Raycast([Vector2](Vector2.html) direction, RaycastHit2D[] results,
float distance = Mathf.Infinity, int layerMask = Physics2D.AllLayers, float
minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity);

## Declaration

public int Raycast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, RaycastHit2D[] results,
float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction of the ray.  
---|---  
results | Array to receive results.  
distance | Maximum distance over which to cast the ray.  
layerMask | Filter to check objects only on specific layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than this value.  
contactFilter | Filter results defined by the contact filter.  
  
### Returns

**int** The number of results returned.

### Description

Casts a ray into the Scene that starts at the Collider position and ignores
the Collider itself.

This function is similar to the [[Physics2D::RaycastNonAlloc]] function and in
the same way, the results are returned in the supplied array. The integer
return value is the number of objects that intersect the ray (possibly zero)
but the results array will not be resized if it doesn't contain enough
elements to report all the results. The significance of this is that no memory
is allocated for the results and so garbage collection performance is improved
when raycasts are performed frequently.  
  
Overloads of this function that use `contactFilter` filters the results by the
options available in [ContactFilter2D](ContactFilter2D.html).  
  
Additionally, this will also detect other Collider(s) at the start of the ray.
In this case the ray is starting inside the Collider and doesn't intersect the
Collider surface. This means that the collision normal cannot be calculated in
which case the collision normal returned is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
Additional resources: [LayerMask](LayerMask.html) class,
[RaycastHit2D](RaycastHit2D.html) class, [[Physics2D::RaycastNonAlloc]],
[[Physics2D::AllLayers]], [[Physics2D::IgnoreRaycastLayer]],
[[Physics2D::raycastsHitTriggers]].

* * *

## Declaration

public int Raycast([Vector2](Vector2.html) direction,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<RaycastHit2D>
results, float distance = Mathf.Infinity);

### Parameters

direction | Vector representing the direction of the ray.  
---|---  
contactFilter | Filter results defined by the contact filter.  
results | List to receive results.  
distance | Maximum distance over which to cast the ray.  
  
### Returns

**int** The number of results returned.

### Description

Casts a ray into the Scene that starts at the Collider position and ignores
the Collider itself.

This function is similar to the [[Physics2D::RaycastNonAlloc]] function and in
the same way, the results are returned in the supplied list. The integer
return value is the number of Colliders that intersect the ray (possibly
zero). The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additionally, this will also detect other Collider(s) at the start of the ray.
In this case the ray is starting inside the Collider and doesn't intersect the
Collider surface. This means that the collision normal cannot be calculated in
which case the collision normal returned is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
Additional resources: [RaycastHit2D](RaycastHit2D.html) class.

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

