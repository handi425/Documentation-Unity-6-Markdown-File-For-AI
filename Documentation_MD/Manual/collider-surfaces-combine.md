[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-surfaces-combine.html)
  * [中文](/cn/current/Manual/collider-surfaces-combine.html)
  * [日本語](/ja/current/Manual/collider-surfaces-combine.html)
  * [한국어](/kr/current/Manual/collider-surfaces-combine.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-surfaces-combine.html)
  * [中文](/cn/current/Manual/collider-surfaces-combine.html)
  * [日本語](/ja/current/Manual/collider-surfaces-combine.html)
  * [한국어](/kr/current/Manual/collider-surfaces-combine.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider surfaces](collider-surfaces.html)
  * How collider surface values combine

[](collider-surface-bounce.html)

Collider surface bounciness

[](create-apply-physics-material.html)

Create and apply a custom Physics Material

# How collider surface values combine

When two colliders are in contact, the physics system uses the surface
properties of each **collider** An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) to calculate the total friction and
bounce between the two surfaces.

In Unity, you use the [Physic Material](class-PhysicsMaterial.html) asset to
control these parameters. The Physic Material asset is represented in the API
by the [`PhysicsMaterial`](../ScriptReference/PhysicsMaterial.html) class.

The Physic Material asset provides two properties: **Friction Combine**
([`PhysicsMaterial.frictionCombine`](../ScriptReference/PhysicsMaterial-
frictionCombine.html)) and **Bounce Combine**
([`PhysicsMaterial.bounceCombine`](../ScriptReference/PhysicsMaterial-
bounceCombine.html)). These properties each provide four options to control
how the physics system calculates the total friction and bounce between two
colliders:

**Priority** | **Property** | **Description**  
---|---|---  
1 | **Maximum** | Use the largest of the two values.  
2 | **Multiply** | Use the sum of one value multiplied by the other.  
3 | **Minimum** | Use the smallest of the two values.  
4 | **Average** | Use the mean average of the two values; that is, the sum of both values, divided by two.  
  
**Friction Combine** applies to both ****Dynamic Friction** A Physics Material
property that defines the friction for a Rigidbody when it’s in motion. Lower
values mean less friction, so a setting of zero represents slipping on ice.
[More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#DynamicFriction)** and **Static Friction**.

The properties in the table are in priority order. Unity takes priority into
consideration when the colliders in a collider pair have Physic Material
assets with different combine settings. For example, if one Physic Material
asset’s **Friction Combine** is set to **Average** , and the other Physic
Material asset’s **Friction Combine** is set to **Maximum** , Unity uses the
**Maximum** calculation.

[](collider-surface-bounce.html)

Collider surface bounciness

[](create-apply-physics-material.html)

Create and apply a custom Physics Material

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

