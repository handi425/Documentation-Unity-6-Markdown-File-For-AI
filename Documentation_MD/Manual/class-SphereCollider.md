[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-SphereCollider.html)
  * [中文](/cn/current/Manual/class-SphereCollider.html)
  * [日本語](/ja/current/Manual/class-SphereCollider.html)
  * [한국어](/kr/current/Manual/class-SphereCollider.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-SphereCollider.html)
  * [中文](/cn/current/Manual/class-SphereCollider.html)
  * [日本語](/ja/current/Manual/class-SphereCollider.html)
  * [한국어](/kr/current/Manual/class-SphereCollider.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * [Primitive collider shapes](primitive-colliders.html)
  * Sphere collider component reference

[](class-BoxCollider.html)

Box collider component reference

[](class-CapsuleCollider.html)

Capsule collider component reference

# Sphere collider component reference

[Switch to Scripting](../ScriptReference/SphereCollider.html "Go to
SphereCollider page in the Scripting Reference")

The Sphere **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) is a built-in sphere-shaped
collider. It is useful for in-application items such as balls and marbles, or
as a simple collider shape that you can stretch and scale to make marbles,
projectiles, planets, and other spherical objects. **Sphere colliders** are
also useful for items that need to roll and tumble, such as falling boulders.

The Sphere collider has relatively low resource requirements.

**Property** | **Description**  
---|---  
**Edit Collider** | Enable the **Edit Collider** button to display the collider’s contact points in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. You can click and drag these
contact points to modify the size and shape of the collider. Alternatively,
use the **Center** and **Size** properties.  
**Is Trigger** | If enabled, this collider is used for triggering events, and is ignored by the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine).  
**Provides Contacts** | Enable **Provides Contacts** to generate contact information for this collider at all times. Usually, a collider only generates contact data if there is something to send it to; in this case, the messages [`OnCollisionEnter`](../ScriptReference/Collider.OnCollisionEnter.html), [`OnCollisionStay`](../ScriptReference/Collider.OnCollisionStay.html), or [`OnCollisionExit`](../ScriptReference/Collider.OnCollisionExit.html). When **Provides Contacts** is enabled, the collider generates contact data for the physics system at all times. Contact generation is resource-intensive, so **Provides Contacts** is disabled by default.  
**Material** | Reference to the [Physics Material](class-PhysicsMaterial.html)A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial) that determines how this
collider interacts with others.  
**Center** | The position of the collider in the object’s local space.  
**Radius** | The size of the collider. This is the only available property for resizing the collider; it is not possible to resize along a specific axis (for example, to flatten the sphere into a non-spherical shape).  
  
## Layer overrides

The Layer Overrides section provides properties that allow you to override the
project-wide [Layer-based collision detection](LayerBasedCollision.html)
settings for this collider.

**Property** | **Description**  
---|---  
**Layer Override Priority** | Define the priority of this collider override. When two colliders have conflicting overrides, the settings of the collider with the higher value priority are taken.   
For example, if a collider with a **Layer Override Priority** of 1 collides
with a Collider with a **Layer Override Priority** of 2, the physics system
uses the settings for the Collider with the **Layer Override Priority** of 2.  
**Include Layers** | Choose which Layers to include in **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) with this collider.  
**Exclude Layers** | Choose which Layers to exclude in collisions with this collider.  
  
[](class-BoxCollider.html)

Box collider component reference

[](class-CapsuleCollider.html)

Capsule collider component reference

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

