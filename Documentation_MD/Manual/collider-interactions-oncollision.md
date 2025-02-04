[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-interactions-oncollision.html)
  * [中文](/cn/current/Manual/collider-interactions-oncollision.html)
  * [日本語](/ja/current/Manual/collider-interactions-oncollision.html)
  * [한국어](/kr/current/Manual/collider-interactions-oncollision.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-interactions-oncollision.html)
  * [中文](/cn/current/Manual/collider-interactions-oncollision.html)
  * [日本語](/ja/current/Manual/collider-interactions-oncollision.html)
  * [한국어](/kr/current/Manual/collider-interactions-oncollision.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider interactions](collider-interactions.html)
  * OnCollision events

[](collider-types-interaction.html)

Interaction between collider types

[](collider-interactions-ontrigger.html)

OnTrigger events

# OnCollision events

Collision events occur when two non-trigger **colliders** An invisible shape
that is used to handle physical collisions for an object. A collider doesn’t
need to be exactly the same shape as the object’s mesh - a rough approximation
is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) make contact.

Example uses for **collision** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) events include:

  * When a projectile hits a target, destroy both the projectile and the enemy.
  * When a player character touches a door, trigger an animation to open the door.
  * When a player character touches a power-up, increase the player’s size.

Working with collision events primarily involves the following API functions:

  * [`Collider.OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html): Unity calls this function on each collider when two colliders first make contact.
  * [`Collider.OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html): Unity calls this function on each collider once per physics update while two colliders are in contact.
  * [`Collider.OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html): Unity calls this function on each collider when two colliders cease contact.

For collision events, at least one of the objects involved must have a dynamic
physics body (that is, a Rigidbody or ArticulationBody that has **Is
Kinematic** disabled). If both **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a collision are kinematic
physics bodies, the collision does not call `OnCollision` functions.

The following example prints a message to the console when Unity calls each
function.

    
    
    using UnityEngine;
    using System.Collections;
    
    public class DoorObject : MonoBehaviour
    {
        // “other” refers to the collider that is touching this collider
        void OnCollisionEnter (Collider other)
        {
            Debug.Log ("A collider has made contact with the DoorObject Collider");
        }
    
        void OnCollisionStay (Collider other)
        {
            Debug.Log ("A collider is in contact with the DoorObject Collider");
        }
        
        void OnCollisionExit (Collider other)
        {
            Debug.Log ("A collider has ceased contact with the DoorObject Collider");
        }
    }
    

For examples of practical applications for `OnCollision` events, refer to
[example scripts for collider events](collider-interactions-example-
scripts.html).

[](collider-types-interaction.html)

Interaction between collider types

[](collider-interactions-ontrigger.html)

OnTrigger events

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

