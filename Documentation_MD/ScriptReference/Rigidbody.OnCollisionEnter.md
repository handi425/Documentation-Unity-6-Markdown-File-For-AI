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

#  [Rigidbody](Rigidbody.html).OnCollisionEnter(Collision)

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

### Description

OnCollisionEnter is called when this collider/rigidbody has begun touching
another rigidbody/collider.

In contrast to OnTriggerEnter, OnCollisionEnter is passed the
[Collision](Collision.html) class and not a Collider. The
[Collision](Collision.html) class contains information about contact points,
impact velocity etc. If you don't use collisionInfo in the function, leave out
the collisionInfo parameter as this avoids unneccessary calculations. Notes:
Collision events are only sent if one of the colliders also has a non-
kinematic rigidbody attached. Collision events will be sent to disabled
MonoBehaviours, to allow enabling Behaviours in response to collisions.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [AudioSource](AudioSource.html) audioSource;  
      
        void Start()
        {
            audioSource = GetComponent<[AudioSource](AudioSource.html)>();
        }  
      
        void OnCollisionEnter([Collision](Collision.html) collision)
        {
            // [Debug](Debug.html)-draw all contact points and normals
            foreach ([ContactPoint](ContactPoint.html) contact in collision.contacts)
            {
                [Debug.DrawRay](Debug.DrawRay.html)(contact.point, contact.normal, [Color.white](Color-white.html));
            }  
      
            // Play a sound if the colliding objects had a big impact.
            if (collision.relativeVelocity.magnitude > 2)
                audioSource.Play();
        }
    }
    

Another example:

    
    
    // A grenade
    // instantiates a explosion Prefab when hitting a surface
    // then destroys itself
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) explosionPrefab;
        void OnCollisionEnter([Collision](Collision.html) collision)
        {
            [ContactPoint](ContactPoint.html) contact = collision.contacts[0];  
      
            // [Rotate](UIElements.Rotate.html) the object so that the y-axis faces along the normal of the surface
            [Quaternion](Quaternion.html) rot = [Quaternion.FromToRotation](Quaternion.FromToRotation.html)([Vector3.up](Vector3-up.html), contact.normal);
            [Vector3](Vector3.html) pos = contact.point;
            Instantiate(explosionPrefab, pos, rot);
            Destroy(gameObject);
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

