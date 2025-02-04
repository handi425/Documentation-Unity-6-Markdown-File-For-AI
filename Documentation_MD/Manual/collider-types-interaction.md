[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-types-interaction.html)
  * [中文](/cn/current/Manual/collider-types-interaction.html)
  * [日本語](/ja/current/Manual/collider-types-interaction.html)
  * [한국어](/kr/current/Manual/collider-types-interaction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-types-interaction.html)
  * [中文](/cn/current/Manual/collider-types-interaction.html)
  * [日本語](/ja/current/Manual/collider-types-interaction.html)
  * [한국어](/kr/current/Manual/collider-types-interaction.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider interactions](collider-interactions.html)
  * Interaction between collider types

[](collider-interactions-other-events.html)

Use collisions to trigger other events

[](collider-interactions-oncollision.html)

OnCollision events

# Interaction between collider types

The **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) matrix tables on this page describe
which event messages Unity generates based on the configuration of each
**collider** An invisible shape that is used to handle physical collisions for
an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) in a collision pair.

## Collision generates collision detection messages

When a pair of colliders make contact, they generate **collision detection**
An automatic process performed by Unity which determines whether a moving
GameObject with a Rigidbody and collider component has come into contact with
any other colliders. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) messages if the following
are both true:

  * There is at least one dynamic collider.
  * The other collider is a static collider, a kinematic collider, or another dynamic collider.

The following table describes each combination of collider types. A “Y”
indicates a combination that can generate collision detection and collision
messages.

**Collision detection occurs and messages are sent upon collision**  
---  
| Static collider | Dynamic collider | Kinematic collider | Static trigger collider | Dynamic trigger collider | Kinematic trigger collider  
Static collider |  | Y |  |  |  |   
Dynamic collider | Y | Y | Y |  |  |   
Kinematic collider |  | Y |  |  |  |   
Static trigger collider |  |  |  |  |  |   
Dynamic trigger collider |  |  |  |  |  |   
Kinematic trigger collider |  |  |  |  |  |   
  
Remember that Unity only applies physics forces to collider **GameObjects**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that have a physics body (a
Rigidbody or ArticulationBody). When a physics body collider collides with a
static collider, only the physics body collider behavior changes as a result
of the collision (for example, it might bounce or slow down as a result of the
collision).

## Collision generates trigger messages

Trigger messages occur in the following circumstances:

  * A dynamic or kinematic trigger collider collides with any collider type.
  * A static trigger collider collides with any dynamic or Kinematic collider.

The following table describes each combination of collider types. A “Y”
indicates a combination that can generate trigger messages from any trigger
collider in the pair.

**Trigger messages are sent upon collision**  
---  
| Static collider | Dynamic collider | Kinematic collider | Static trigger collider | Dynamic trigger collider | Kinematic trigger collider  
Static collider |  |  |  |  | Y | Y  
Dynamic collider |  |  |  | Y | Y | Y  
Kinematic collider |  |  |  | Y | Y | Y  
Static trigger collider |  | Y | Y |  | Y | Y  
Dynamic trigger collider | Y | Y | Y | Y | Y | Y  
Kinematic trigger collider | Y | Y | Y | Y | Y | Y  
  
Unity collision matrix Unity collision interaction

[](collider-interactions-other-events.html)

Use collisions to trigger other events

[](collider-interactions-oncollision.html)

OnCollision events

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

