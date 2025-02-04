[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-surface-friction.html)
  * [中文](/cn/current/Manual/collider-surface-friction.html)
  * [日本語](/ja/current/Manual/collider-surface-friction.html)
  * [한국어](/kr/current/Manual/collider-surface-friction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-surface-friction.html)
  * [中文](/cn/current/Manual/collider-surface-friction.html)
  * [日本語](/ja/current/Manual/collider-surface-friction.html)
  * [한국어](/kr/current/Manual/collider-surface-friction.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider surfaces](collider-surfaces.html)
  * Collider surface friction

[](collider-surfaces.html)

Collider surfaces

[](collider-surface-bounce.html)

Collider surface bounciness

# Collider surface friction

In real-world physics, friction is a force that impedes motion between two
surfaces that are in contact with each other. For example, ice has a low-
friction surface, which allows objects to slide easily across its surface.
Rubber has a high-friction surface, which prevents objects from sliding across
its surface.

In the PhysX system, there are two types of friction that you can control:

**Static friction** applies when the **collider** An invisible shape that is
used to handle physical collisions for an object. A collider doesn’t need to
be exactly the same shape as the object’s mesh - a rough approximation is
often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) is stationary. A high amount of
static friction impedes the collider from starting to move while it is in
contact with another collider. ****Dynamic friction** A Physics Material
property that defines the friction for a Rigidbody when it’s in motion. Lower
values mean less friction, so a setting of zero represents slipping on ice.
[More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#DynamicFriction)** applies when the collider
is moving. A high amount of dynamic friction impedes the collider’s movement
speed while it is in contact with another collider.

Static friction is particularly relevant in physics simulation when you need
to stack objects. For example, if you put one low-friction object on top of
another (such as a cube of ice on top of another cube of ice), the low
friction between them might cause the top object to move, even if the bottom
object is stationary.

PhysX calculates contact surfaces which are larger than a single point (such
as two boxes resting on each other) as having multiple contact points. This in
turn multiples the friction forces. If this happens, you need to adjust your
friction values to correctly scale the results - for example, if there are two
contact points, you should halve your friction values.

The default friction in Unity is 0.6. This value simulates real-world friction
in most projects.

## Friction calculation

You can choose the type of calculation that PhysX uses to simulate friction
between colliders. To do this, go to the Physics Settings (**Edit** >
**Project Settings** > **Physics**) and use the **Friction Type** property.
See the [Physics Settings](class-PhysicsManager.html) documentation for more
information on each friction type.

The choice of friction type is always to balance accuracy and performance;
more accuracy always requires more processing time. Some projects require
extremely accurate friction, while others are more focused on performance
optimization. Choose the friction type that best suits your project’s focus.
The default friction type is **Patch Friction**.

  * **Patch Friction** : Patch friction calculates friction forces in multiple directions based on the distribution of forces across the colliders’ surfaces. Patch friction is very accurate, but it is the most computationally intensive option.
  * **One-directional Friction** : One-directional friction is a simpler friction calculation method that considers friction along a single perpendicular direction. One-directional friction is the least accurate option, and the least computationally intensive.
  * **Two-directional Friction** : Two-directional friction is a variation of one-directional friction that takes into account two perpendicular directions. It is more accurate than **One-directional friction** , but less accurate than **Patch friction**.

[](collider-surfaces.html)

Collider surfaces

[](collider-surface-bounce.html)

Collider surface bounciness

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

