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

#  [Physics](Physics.html).BoxCastAll

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

public static RaycastHit[] BoxCastAll([Vector3](Vector3.html) center,
[Vector3](Vector3.html) halfExtents, [Vector3](Vector3.html) direction,
[Quaternion](Quaternion.html) orientation = Quaternion.identity, float
maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

center | Center of the box.  
---|---  
halfExtents | Half the size of the box in each dimension.  
direction | The direction in which to cast the box.  
orientation | Rotation of the box.  
maxDistance | The max length of the cast.  
layermask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**RaycastHit[]** All colliders that were hit.

### Description

Like [Physics.BoxCast](Physics.BoxCast.html), but returns all hits.

**Notes:** For colliders that overlap the box at the start of the sweep,
[RaycastHit.normal](RaycastHit-normal.html) is set opposite to the direction
of the sweep, [RaycastHit.distance](RaycastHit-distance.html) is set to zero,
and the zero vector gets returned in [RaycastHit.point](RaycastHit-
point.html). You might want to check whether this is the case in your
particular query and perform additional queries to refine the result.

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

