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

#  [RaycastHit](RaycastHit.html).distance

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

public float distance;

### Description

The distance from the ray's origin to the impact point.

In the case of a ray, the distance represents the magnitude of the vector from
the ray's origin to the impact point.  
  
In the case of a swept volume or sphere cast, the distance represents the
magnitude of the vector from the origin point to the translated point at which
the volume contacts the other collider.  
  
Note that [RaycastHit.point](RaycastHit-point.html) represents the point in
space where the collision occurs.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Movable, levitating object.  
      
        // This works by measuring the distance to ground with a
        // raycast then applying a force that decreases as the object
        // reaches the desired levitation height.  
      
        // Vary the parameters below to
        // get different control effects. For example, reducing the
        // hover damping will tend to make the object bounce if it
        // passes over an object underneath.  
      
        // Forward movement force.
        float moveForce = 1.0f;  
      
        // Torque for left/right rotation.
        float rotateTorque = 1.0f;  
      
        // Desired hovering height.
        float hoverHeight = 4.0f;  
      
        // The force applied per unit of distance below the desired height.
        float hoverForce = 5.0f;  
      
        // The amount that the lifting force is reduced per unit of upward speed.
        // This damping tends to stop the object from bouncing after passing over
        // something.
        float hoverDamp = 0.5f;  
      
        // [Rigidbody](Rigidbody.html) component.
        [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();  
      
            // Fairly high drag makes the object easier to control.
            rb.drag = 0.5f;
            rb.angularDrag = 0.5f;
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            // Push/turn the object based on arrow key input.
            rb.AddForce([Input.GetAxis](Input.GetAxis.html)("Vertical") * moveForce * transform.forward);
            rb.AddTorque([Input.GetAxis](Input.GetAxis.html)("Horizontal") * rotateTorque * [Vector3.up](Vector3-up.html));  
      
            [RaycastHit](RaycastHit.html) hit;
            [Ray](Ray.html) downRay = new [Ray](Ray.html)(transform.position, -[Vector3.up](Vector3-up.html));  
      
            // Cast a ray straight downwards.
            if ([Physics.Raycast](Physics.Raycast.html)(downRay, out hit))
            {
                // The "error" in height is the difference between the desired height
                // and the height measured by the raycast distance.
                float hoverError = hoverHeight - hit.distance;  
      
                // Only apply a lifting force if the object is too low (ie, let
                // gravity pull it downward if it is too high).
                if (hoverError > 0)
                {
                    // Subtract the damping from the lifting force and apply it to
                    // the rigidbody.
                    float upwardSpeed = rb.velocity.y;
                    float lift = hoverError * hoverForce - upwardSpeed * hoverDamp;
                    rb.AddForce(lift * [Vector3.up](Vector3-up.html));
                }
            }
        }
    }
    

Additional resources: [Physics.Raycast](Physics.Raycast.html),
[Physics.Linecast](Physics.Linecast.html),
[Physics.RaycastAll](Physics.RaycastAll.html).

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

