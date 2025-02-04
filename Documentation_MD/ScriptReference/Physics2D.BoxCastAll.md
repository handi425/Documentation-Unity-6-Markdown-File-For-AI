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

#  [Physics2D](Physics2D.html).BoxCastAll

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

public static RaycastHit2D[] BoxCastAll([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) size, float angle, [Vector2](Vector2.html) direction,
float distance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, float
minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity);

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

**RaycastHit2D[]** The cast results returned.

### Description

Casts a box against Colliders in the Scene, returning all Colliders that
contact with it.

A _BoxCast_ is conceptually like dragging a box through the Scene in a
particular direction. Any object making contact with the box can be detected
and reported.  
  
This function is similar to the [BoxCast](Physics2D.BoxCast.html) function but
instead of detecting just the first Collider that is hit, an array of all
Colliders along the path of the box is returned. The Colliders in the array
are sorted in order of distance from the origin point. The _layerMask_ can be
used to detect objects selectively only on certain layers (this allows you to
apply the detection only to enemy characters, for example).  
  
The returned [RaycastHit2D](RaycastHit2D.html) returns both the point and
normal of the contact where the box would touch the Collider. It also returns
the centroid where the box would be positioned for it to contact at that
point.  
  
Additional resources: [LayerMask](LayerMask.html) class,
[RaycastHit2D](RaycastHit2D.html) class, [BoxCast](Physics2D.BoxCast.html),
[BoxCastNonAlloc](Physics2D.BoxCastNonAlloc.html),
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

