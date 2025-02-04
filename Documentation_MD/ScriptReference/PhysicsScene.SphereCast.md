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

#  [PhysicsScene](PhysicsScene.html).SphereCast

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

public bool SphereCast([Vector3](Vector3.html) origin, float radius,
[Vector3](Vector3.html) direction, out [RaycastHit](RaycastHit.html) hitInfo,
float maxDistance = Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The center of the sphere at the start of the sweep.  
---|---  
radius | The radius of the sphere.  
direction | The direction into which to sweep the sphere.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](RaycastHit.html)).  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True when the sphere sweep intersects any collider, otherwise false.

### Description

Casts a sphere along a ray and returns detailed information on what was hit.

Additional resources: [Physics.SphereCast](Physics.SphereCast.html).

* * *

## Declaration

public int SphereCast([Vector3](Vector3.html) origin, float radius,
[Vector3](Vector3.html) direction, RaycastHit[] results, float maxDistance =
Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The center of the sphere at the start of the sweep.  
---|---  
radius | The radius of the sphere.  
direction | The direction into which to sweep the sphere.  
results | The buffer to save the results to.  
maxDistance | The max length of the cast.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
  
### Returns

**int** The amount of hits stored into the `results` buffer.

### Description

Cast sphere along the direction and store the results into buffer.

Additional resources: Physics.SphereCastNonAllloc.

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

