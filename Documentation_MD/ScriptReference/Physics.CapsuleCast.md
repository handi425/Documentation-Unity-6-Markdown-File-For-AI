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

#  [Physics](Physics.html).CapsuleCast

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

public static bool CapsuleCast([Vector3](Vector3.html) point1,
[Vector3](Vector3.html) point2, float radius, [Vector3](Vector3.html)
direction, float maxDistance = Mathf.Infinity, int layerMask =
DefaultRaycastLayers, [QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

point1 | The center of the sphere at the `start` of the capsule.  
---|---  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
maxDistance | The max length of the sweep.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True when the capsule sweep intersects any collider, otherwise false.

### Description

Casts a capsule against all colliders in the Scene and returns detailed
information on what was hit.

The capsule is defined by the two spheres with `radius` around `point1` and
`point2`, which form the two ends of the capsule. Hits are returned for the
first collider which would collide against this capsule if the capsule was
moved along `direction`. This is useful when a Raycast does not give enough
precision, because you want to find out if an object of a specific size, such
as a character, will be able to move somewhere without colliding with anything
on the way.  
  
**Notes:** CapsuleCast will not detect colliders for which the capsule
overlaps the collider. Passing a zero radius results in undefined output and
doesn't always behave the same as [Physics.Raycast](Physics.Raycast.html).  
  
Additional resources: [Physics.SphereCast](Physics.SphereCast.html),
[Physics.CapsuleCastAll](Physics.CapsuleCastAll.html),
[Physics.Raycast](Physics.Raycast.html),
[Rigidbody.SweepTest](Rigidbody.SweepTest.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            [RaycastHit](RaycastHit.html) hit;
            [CharacterController](CharacterController.html) charContr = GetComponent<[CharacterController](CharacterController.html)>();
            [Vector3](Vector3.html) p1 = transform.position + charContr.center + [Vector3.up](Vector3-up.html) * -charContr.height * 0.5F;
            [Vector3](Vector3.html) p2 = p1 + [Vector3.up](Vector3-up.html) * charContr.height;
            float distanceToObstacle = 0;  
      
            // Cast character controller shape 10 meters forward to see if it is about to hit anything.
            if ([Physics.CapsuleCast](Physics.CapsuleCast.html)(p1, p2, charContr.radius, transform.forward, out hit, 10))
                distanceToObstacle = hit.distance;
        }
    }
    

* * *

## Declaration

public static bool CapsuleCast([Vector3](Vector3.html) point1,
[Vector3](Vector3.html) point2, float radius, [Vector3](Vector3.html)
direction, out [RaycastHit](RaycastHit.html) hitInfo, float maxDistance =
Mathf.Infinity, int layerMask = DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

point1 | The center of the sphere at the `start` of the capsule.  
---|---  
point2 | The center of the sphere at the `end` of the capsule.  
radius | The radius of the capsule.  
direction | The direction into which to sweep the capsule.  
maxDistance | The max length of the sweep.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](RaycastHit.html)).  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a capsule.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Description

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

