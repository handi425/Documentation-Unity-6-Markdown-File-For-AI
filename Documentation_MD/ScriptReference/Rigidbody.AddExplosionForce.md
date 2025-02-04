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

#  [Rigidbody](Rigidbody.html).AddExplosionForce

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

public void AddExplosionForce(float explosionForce, [Vector3](Vector3.html)
explosionPosition, float explosionRadius, float upwardsModifier = 0.0f,
[ForceMode](ForceMode.html) mode = ForceMode.Force));

### Parameters

explosionForce | The force of the explosion (which may be modified by distance).  
---|---  
explosionPosition | The centre of the sphere within which the explosion has its effect.  
explosionRadius | The radius of the sphere within which the explosion has its effect.  
upwardsModifier | Adjustment to the apparent position of the explosion to make it seem to lift objects.  
mode | The method used to apply the force to its targets.  
  
### Description

Applies a force to a rigidbody that simulates explosion effects.

The explosion is modelled as a sphere with a certain centre position and
radius in world space; normally, anything outside the sphere is not affected
by the explosion and the force decreases in proportion to distance from the
centre. However, if a value of zero is passed for the radius then the full
force will be applied regardless of how far the centre is from the rigidbody.  
  
This function applies a force to the object at the point on the surface of the
rigidbody that is closest to `explosionPosition`. The force acts along the
direction from `explosionPosition` to the surface point on the rigidbody. If
`explosionPosition` is inside the rigidbody, or the rigidbody has no active
colliders, then the center of mass is used instead of the closest point on the
surface.  
  
The magnitude of the force depends on the distance between `explosionPosition`
and the point where the force was applied. As the distance between
`explosionPosition` and the force point increases, the actual applied force
decreases.  
  
The vertical direction of the force can be modified using `upwardsModifier`.
If this parameter is greater than zero, the force is applied at the point on
the surface of the Rigidbody that is closest to `explosionPosition` but
shifted along the y-axis by negative `upwardsModifier`. Using this parameter,
you can make the explosion appear to throw objects up into the air, which can
give a more dramatic effect rather than a simple outward force. Force can be
applied only to an active rigidbody. If a GameObject is inactive,
AddExplosionForce has no effect.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Applies an explosion force to all nearby rigidbodies
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float radius = 5.0F;
        public float power = 10.0F;  
      
        void Start()
        {
            [Vector3](Vector3.html) explosionPos = transform.position;
            [Collider](Collider.html)[] colliders = [Physics.OverlapSphere](Physics.OverlapSphere.html)(explosionPos, radius);
            foreach ([Collider](Collider.html) hit in colliders)
            {
                [Rigidbody](Rigidbody.html) rb = hit.GetComponent<[Rigidbody](Rigidbody.html)>();  
      
                if (rb != null)
                    rb.AddExplosionForce(power, explosionPos, radius, 3.0F);
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

