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

#  [MonoBehaviour](MonoBehaviour.html).OnParticleCollision(GameObject)

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

OnParticleCollision is called when a particle hits a Collider.

This can be used to apply damage to a GameObject when hit by particles.  
  
This message is sent to scripts attached to Particle Systems and to the
[Collider](Collider.html) that was hit.  
  
When [OnParticleCollision](MonoBehaviour.OnParticleCollision.html) is invoked
from a script attached to a [GameObject](GameObject.html) with a
[Collider](Collider.html), the [GameObject](GameObject.html) parameter
represents the [ParticleSystem](ParticleSystem.html). The
[Collider](Collider.html) receives at most one message per Particle System
that collided with it in any given frame even when the Particle System struck
the [Collider](Collider.html) with multiple particles in the current frame. To
retrieve detailed information about all the collisions caused by the
[ParticleSystem](ParticleSystem.html), the
[ParticlePhysicsExtensions.GetCollisionEvents](ParticlePhysicsExtensions.GetCollisionEvents.html)
must be used to retrieve the array of ParticleSystem.CollisionEvent.  
  
When OnParticleCollision is invoked from a script attached to a
[ParticleSystem](ParticleSystem.html), the [GameObject](GameObject.html)
parameter represents a [GameObject](GameObject.html) with an attached
[Collider](Collider.html) struck by the [ParticleSystem](ParticleSystem.html).
The [ParticleSystem](ParticleSystem.html) receives at most one message per
[Collider](Collider.html) that is struck. As above,
[ParticlePhysicsExtensions.GetCollisionEvents](ParticlePhysicsExtensions.GetCollisionEvents.html)
must be used to retrieve all the collision incidents on the
[GameObject](GameObject.html).  
  
Messages are only sent if you enable `Send Collision Messages` in the
Inspector of the Particle System Collision module.  
  
The OnParticleCollision can be a co-routine. Simply use the yield statement in
the function.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) part;
        public List<[ParticleCollisionEvent](ParticleCollisionEvent.html)> collisionEvents;  
      
        void Start()
        {
            part = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            collisionEvents = new List<[ParticleCollisionEvent](ParticleCollisionEvent.html)>();
        }  
      
        void OnParticleCollision([GameObject](GameObject.html) other)
        {
            int numCollisionEvents = part.GetCollisionEvents(other, collisionEvents);  
      
            [Rigidbody](Rigidbody.html) rb = other.GetComponent<[Rigidbody](Rigidbody.html)>();
            int i = 0;  
      
            while (i < numCollisionEvents)
            {
                if (rb)
                {
                    [Vector3](Vector3.html) pos = collisionEvents[i].intersection;
                    [Vector3](Vector3.html) force = collisionEvents[i].velocity * 10;
                    rb.AddForce(force);
                }
                i++;
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

