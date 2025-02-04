[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/static/static-body-type-fundamentals.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [2D Physics](../../../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](../../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * [Static Body Type](../../../../2d-physics/rigidbody/body-types/static/static-body-type-landing.html)
  * Static Body Type fundamentals

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
landing.html)

Static Body Type

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
reference.html)

Static Body Type reference

# Static Body Type fundamentals

A Static **Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../../../class-
Rigidbody.html)  
See in [Glossary](../../../../Glossary.html#Rigidbody) 2D is designed to not
move under simulation at all. If anything collides with it, a Static Rigidbody
2D behaves like an immovable object (as though it has infinite mass). It is
also the least resource intensive ****Body Type** Defines a fixed behavior for
a 2D Rigidbody. Can be Dynamic (the body moves under simulation and is
affected by forces like gravity), Kinematic (the body moves under simulation,
but and isn’t affected by forces like gravity) or Static (the body doesn’t
move under simulation). [More
info](../../../../2d-physics/rigidbody/introduction-to-rigidbody-2d.html)  
See in [Glossary](../../../../Glossary.html#BodyType)**. A Static body only
collides with Dynamic Rigidbody 2Ds.

**Note** : Having two Static Rigidbody 2Ds collide is not supported, since
they are not designed to move.

## Use a large number of Static Collider 2D

Aside from setting the Rigidbody 2D to the **Static** Body Type, there is
another scenario where a Static Rigidbody 2D is created. This is when a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../../../class-GameObject.html)  
See in [Glossary](../../../../Glossary.html#GameObject) with a **Collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collider) 2D component does not
have a Rigidbody 2D component at all. All Collider 2Ds without a Rigidbody 2D
component are internally considered to be attached to a single hidden
**Static** Rigidbody 2D component.

This means that you are able to create a large number of Static Collider 2Ds
as you do not have to add a Rigidbody 2D component for each individual
GameObject. Both methods of creating Static Collider 2Ds have their
advantages, depending on the scenario.

If an individual Static Collider 2D needs to be moved or reconfigured at
runtime, then add a Rigidbody 2D component and set it to the **Static** Body
Type, as it is faster to simulate the Collider 2D when it has its own
Rigidbody 2D. If a group of Collider 2Ds needs to be moved or reconfigured at
runtime, it is faster to have them all be children of the single hidden parent
Rigidbody 2D than to move each GameObject individually.

**Note** : As stated above, Static Rigidbody 2Ds are designed not to move, and
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More
info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collision) between two Static
Rigidbody **2D objects** A 2D GameObject such as a tilemap or sprite. [More
info](../../../../Unity2D.html)  
See in [Glossary](../../../../Glossary.html#2DObject) that intersect are not
registered. However, Static Rigidbody 2Ds and Kinematic Rigidbody 2Ds will
interact with each other if one of their Collider 2Ds is set to be a
**trigger**. There is also a feature that changes what a Kinematic body will
interact with (see [Use Full Kinematic Contacts](../kinematic/kinematic-body-
type-reference.html) for more information).

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
landing.html)

Static Body Type

[](../../../../2d-physics/rigidbody/body-types/static/static-body-type-
reference.html)

Static Body Type reference

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

