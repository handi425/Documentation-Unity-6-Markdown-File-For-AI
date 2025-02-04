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

#  [Physics2D](Physics2D.html).Raycast

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

public static [RaycastHit2D](RaycastHit2D.html)
Raycast([Vector2](Vector2.html) origin, [Vector2](Vector2.html) direction,
float distance = Mathf.Infinity, int layerMask = DefaultRaycastLayers, float
minDepth = -Mathf.Infinity, float maxDepth = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the ray originates.  
---|---  
direction | A vector representing the direction of the ray.  
distance | The maximum distance over which to cast the ray.  
layerMask | Filter to detect Colliders only on certain layers.  
minDepth | Only include objects with a Z coordinate (depth) greater than or equal to this value.  
maxDepth | Only include objects with a Z coordinate (depth) less than or equal to this value.  
  
### Returns

**RaycastHit2D** The cast results returned.

### Description

Casts a ray against Colliders in the Scene.

A _raycast_ is conceptually like a laser beam that is fired from a point in
space along a particular direction. Any object making contact with the beam
can be detected and reported.  
  
This function returns a RaycastHit2D object with a reference to the Collider
that is hit by the ray (the Collider property of the result will be NULL if
nothing was hit). The _layerMask_ can be used to detect objects selectively
only on certain layers (this allows you to apply the detection only to enemy
characters, for example).  
  
Overloads of this method that use `contactFilter` can filter the results by
the options available in [ContactFilter2D](ContactFilter2D.html).  
  
Raycasts are useful for determining lines of sight, targets hit by gunfire and
for many other purposes in gameplay.  
  
Additionally, this will also detect Collider(s) at the start of the ray. In
this case, the ray starts inside the Collider and doesn't intersect the
Collider surface. This means that the collision normal cannot be calculated,
in which case the returned collision normal is set to the inverse of the ray
vector being tested. This can easily be detected because such results are
always at a RaycastHit2D fraction of zero.  
  
Additional resources: [LayerMask](LayerMask.html) class,
[RaycastHit2D](RaycastHit2D.html) class,
[RaycastAll](Physics2D.RaycastAll.html), [Linecast](Physics2D.Linecast.html),
[DefaultRaycastLayers](Physics2D.DefaultRaycastLayers.html),
[IgnoreRaycastLayer](Physics2D.IgnoreRaycastLayer.html),
[raycastsHitTriggers](Physics2D-raycastsHitTriggers.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Float a rigidbody object a set distance above a surface.  
      
        public float floatHeight;     // Desired floating height.
        public float liftForce;       // Force to apply when lifting the rigidbody.
        public float damping;         // Force reduction proportional to speed (reduces bouncing).  
      
        [Rigidbody2D](Rigidbody2D.html) rb2D;  
      
    
        void Start()
        {
            rb2D = GetComponent<[Rigidbody2D](Rigidbody2D.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            // Cast a ray straight down.
            [RaycastHit2D](RaycastHit2D.html) hit = [Physics2D.Raycast](Physics2D.Raycast.html)(transform.position, -[Vector2.up](Vector2-up.html));  
      
            // If it hits something...
            if (hit)
            {
                // Calculate the distance from the surface and the "error" relative
                // to the floating height.
                float distance = [Mathf.Abs](Mathf.Abs.html)(hit.point.y - transform.position.y);
                float heightError = floatHeight - distance;  
      
                // The force is proportional to the height error, but we remove a part of it
                // according to the object's speed.
                float force = liftForce * heightError - rb2D.velocity.y * damping;  
      
                // Apply the force to the rigidbody.
                rb2D.AddForce([Vector3.up](Vector3-up.html) * force);
            }
        }
    }
    

* * *

## Declaration

public static int Raycast([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) direction, [ContactFilter2D](ContactFilter2D.html)
contactFilter, RaycastHit2D[] results, float distance = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the ray originates.  
---|---  
direction | A vector representing the direction of the ray.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The array to receive results. The size of the array determines the maximum number of results that can be returned.  
distance | The maximum distance over which to cast the ray.  
  
### Returns

**int** Returns the number of results placed in the `results` array.

### Description

Casts a ray against Colliders in the Scene.

This function returns the number of contacts found and places those contacts
in the `results` array. The results can also be filtered by the
`contactFilter`.  
  
Additional resources: [ContactFilter2D](ContactFilter2D.html) and
[RaycastHit2D](RaycastHit2D.html).

* * *

## Declaration

public static int Raycast([Vector2](Vector2.html) origin,
[Vector2](Vector2.html) direction, [ContactFilter2D](ContactFilter2D.html)
contactFilter, List<RaycastHit2D> results, float distance = Mathf.Infinity);

### Parameters

origin | The point in 2D space where the ray originates.  
---|---  
direction | A vector representing the direction of the ray.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
results | The list to receive results.  
distance | The maximum distance over which to cast the ray.  
  
### Returns

**int** Returns the number of results placed in the `results` list.

### Description

Casts a ray against Colliders in the Scene.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [ContactFilter2D](ContactFilter2D.html) and
[RaycastHit2D](RaycastHit2D.html).

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

