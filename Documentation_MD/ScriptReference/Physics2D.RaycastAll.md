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

#  [Physics2D](Physics2D.html).RaycastAll

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

public static RaycastHit2D[] RaycastAll([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) direction, float distance = Mathf.Infinity, int
layerMask = DefaultRaycastLayers, float minDepth = -Mathf.Infinity, float
maxDepth = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the ray originates.  
---|---  
direction | A vector representing the direction of the ray.  
distance | The maximum distance over which to cast the ray.  
layerMask | Filter to detect Colliders only on certain layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
  
### Returns

**RaycastHit2D[]** The cast results returned.

### Description

Casts a ray against Colliders in the Scene, returning all Colliders that
contact with it.

A _raycast_ is conceptually like a laser beam that is fired from a point in
space along a particular direction. Any object making contact with the beam
can be detected and reported.  
  
This function is similar to the Raycast function but instead of detecting just
the first Collider that is hit, an array of all Colliders along the path of
the ray is returned. The Colliders in the array are sorted in order of
distance from the origin point. The _layerMask_ can be used to detect objects
selectively only on certain layers (this allows you to apply the detection
only to enemy characters, for example).  
  
Raycasts are useful for determining lines of sight, targets hit by gunfire and
for many other purposes in gameplay.  
  
Additionally, this will also detect Collider(s) at the start of the ray. In
this case, the ray starts inside the Collider and doesn't intersect the
Collider surface. This means that the collision normal cannot be calculated,
in which case the returned collision normal is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
Additional resources: [LayerMask](LayerMask.html) class,
[RaycastHit2D](RaycastHit2D.html) class, [Raycast](Physics2D.Raycast.html),
[Linecast](Physics2D.Linecast.html),
[DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[raycastsHitTriggers](Physics2D-raycastsHitTriggers.html).

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

