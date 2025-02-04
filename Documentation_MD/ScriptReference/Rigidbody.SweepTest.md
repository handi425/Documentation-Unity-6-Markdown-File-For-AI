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

#  [Rigidbody](Rigidbody.html).SweepTest

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

## Declaration

public bool SweepTest([Vector3](Vector3.html) direction, out
[RaycastHit](RaycastHit.html) hitInfo, float maxDistance = Mathf.Infinity,
[QueryTriggerInteraction](QueryTriggerInteraction.html)
queryTriggerInteraction = QueryTriggerInteraction.UseGlobal);

### Parameters

direction | The direction into which to sweep the rigidbody.  
---|---  
hitInfo | If true is returned, `hitInfo` will contain more information about where the collider was hit (Additional resources: [RaycastHit](RaycastHit.html)).  
maxDistance | The length of the sweep.  
queryTriggerInteraction | Specifies whether this query should hit Triggers.  
  
### Returns

**bool** True when the rigidbody sweep intersects any collider, otherwise
false.

### Description

Tests if a rigidbody would collide with anything, if it was moved through the
Scene.

Tests if a rigidbody would collide with anything, if it was moved through the
Scene. This is similar to doing a [Physics.Raycast](Physics.Raycast.html) for
all points contained in any of a Rigidbody's colliders and returning the
closest of all hits (if any) reported. This is useful for AI code, say if you
need to know that an object would fit through a gap without colliding with
anything.  
  
Note that this function only works when a primitive collider type (sphere,
cube or capsule) or a convex mesh is attached to the rigidbody object -
concave mesh colliders will not work, although they can be detected in the
Scene by the sweep.  
  
Additional resources: [Physics.SphereCast](Physics.SphereCast.html),
[Physics.CapsuleCast](Physics.CapsuleCast.html),
[Rigidbody.SweepTestAll](Rigidbody.SweepTestAll.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float collisionCheckDistance;
        public bool aboutToCollide;
        public float distanceToCollision;
        public [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [RaycastHit](RaycastHit.html) hit;
            if (rb.SweepTest(transform.forward, out hit, collisionCheckDistance))
            {
                aboutToCollide = true;
                distanceToCollision = hit.distance;
            }
        }
    }
    

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

