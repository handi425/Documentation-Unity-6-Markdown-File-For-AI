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

#  [Physics](Physics.html).SphereCastNonAlloc

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

public static int SphereCastNonAlloc([Vector3](Vector3.html) origin, float
radius, [Vector3](Vector3.html) direction, RaycastHit[] results, float
maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The center of the sphere at the start of the sweep.  
---|---  
radius | The radius of the sphere.  
direction | The direction in which to sweep the sphere.  
results | The buffer to save the hits into.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**int** The amount of hits stored into the `results` buffer.

### Description

Cast sphere along the direction and store the results into buffer.

This is variant of [Physics.SphereCastAll](Physics.SphereCastAll.html), but
instead of allocating the array with the results of the query, it stores the
results into the user-provided array. It will only compute as many hits as fit
into the buffer, and store them in no particular order. It's not guaranteed
that it will store only the closest hits. Generates no garbage.

* * *

## Declaration

public static int SphereCastNonAlloc([Ray](Ray.html) ray, float radius,
RaycastHit[] results, float maxDistance = Mathf.Infinity, int layerMask =
DefaultRaycastLayers, [QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

ray | The starting point and direction of the ray into which the sphere sweep is cast.  
---|---  
radius | The radius of the sphere.  
results | The buffer to save the results to.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a sphere.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**int** The amount of hits stored into the `results` buffer.

### Description

Cast sphere along the direction and store the results into buffer.

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

