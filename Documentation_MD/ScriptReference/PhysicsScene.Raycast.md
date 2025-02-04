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

#  [PhysicsScene](PhysicsScene.html).Raycast

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

public bool Raycast([Vector3](Vector3.html) origin, [Vector3](Vector3.html)
direction, float maxDistance = Mathf.Infinity, int layerMask =
Physics.DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The starting point of the ray in world coordinates.  
---|---  
direction | The direction of the ray.  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore Colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True if the ray intersects with a Collider, otherwise false.

### Description

Casts a ray, from point `origin`, in direction `direction`, of length
`maxDistance`, against all colliders in the Scene.

You may optionally provide a [LayerMask](LayerMask.html), to filter out any
Colliders you aren't interested in generating collisions with. Specifying
`queryTriggerInteraction` allows you to control whether or not Trigger
colliders generate a hit, or whether to use the global
[Physics.queriesHitTriggers](Physics-queriesHitTriggers.html) setting.  
  
This example creates a simple Raycast, projecting forwards from the position
of the object's current position, extending for 10 units.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            [Vector3](Vector3.html) fwd = transform.TransformDirection([Vector3.forward](Vector3-forward.html));  
      
            if ([Physics.Raycast](Physics.Raycast.html)(transform.position, fwd, 10))
                print("There is something in front of the object!");
        }
    }
    

* * *

## Declaration

public bool Raycast([Vector3](Vector3.html) origin, [Vector3](Vector3.html)
direction, out [RaycastHit](RaycastHit.html) hitInfo, float maxDistance =
Mathf.Infinity, int layerMask = Physics.DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The starting point of the ray in world coordinates.  
---|---  
direction | The direction of the ray.  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit. (Additional resources: [RaycastHit](RaycastHit.html)).  
maxDistance | The max distance the ray should check for collisions.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore Colliders when casting a ray.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True if the ray intersects with a Collider, otherwise false.

### Description

Casts a ray, from point `origin`, in direction `direction`, of length
`maxDistance`, against all colliders in the Scene.

This method generates no garbage.

    
    
    using UnityEngine;
    public class RaycastExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            [RaycastHit](RaycastHit.html) hit;  
      
            if ([Physics.Raycast](Physics.Raycast.html)(transform.position, -[Vector3.up](Vector3-up.html), out hit))
                print("Found an object - distance: " + hit.distance);
        }
    }
    

* * *

## Declaration

public int Raycast([Vector3](Vector3.html) origin, [Vector3](Vector3.html)
direction, RaycastHit[] raycastHits, float maxDistance = Mathf.Infinity, int
layerMask = Physics.DefaultRaycastLayers,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

origin | The starting point and direction of the ray.  
---|---  
direction | The direction of the ray.  
raycastHits | The buffer to store the hits into.  
maxDistance | The max distance the rayhit is allowed to be from the start of the ray.  
layerMask | A [Layer mask](../Manual/Layers.html) that is used to selectively ignore colliders when casting a ray.  
queryTriggerInteraction | The amount of hits stored into the `results` buffer.  
  
### Returns

**int** True if the ray intersects with a Collider, otherwise false.

### Description

Casts a ray, from point `origin`, in direction `direction`, of length
`maxDistance`, against all colliders in the Scene.

This method generates no garbage.

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

