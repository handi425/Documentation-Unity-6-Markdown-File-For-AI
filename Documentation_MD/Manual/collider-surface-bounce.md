[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-surface-bounce.html)
  * [中文](/cn/current/Manual/collider-surface-bounce.html)
  * [日本語](/ja/current/Manual/collider-surface-bounce.html)
  * [한국어](/kr/current/Manual/collider-surface-bounce.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-surface-bounce.html)
  * [中文](/cn/current/Manual/collider-surface-bounce.html)
  * [日本語](/ja/current/Manual/collider-surface-bounce.html)
  * [한국어](/kr/current/Manual/collider-surface-bounce.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider surfaces](collider-surfaces.html)
  * Collider surface bounciness

[](collider-surface-friction.html)

Collider surface friction

[](collider-surfaces-combine.html)

How collider surface values combine

# Collider surface bounciness

In physics, the bounciness of a surface is called the “coefficient of
restitution”. The coefficient of restitution is represented as a number
between 0 and 1, which defines how much speed an object retains in the
opposite direction along the line of impact after a **collision** A collision
occurs when the physics engine detects that the colliders of two GameObjects
make contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision).

In PhysX, the Physic Material asset’s **Bounce** property has a value of 0–1,
which represents the coefficient of restitution.

0 represents a completely inelastic collision (no bounce) 1 represents a
perfectly elastic collision (full bounce) A value between 0 and 1 indicates a
partially elastic collision with varying degrees of bounciness.

The default **Bounce** value in Unity is 0.

## Velocity threshold for bounce behavior

In physics simulation, you can also define a threshold at which colliders no
longer bounce off each other. If two colliding objects have a relative
velocity below the defined value, they do not bounce off each other. To
configure the bounce threshold, go to the Physics Settings (**Edit** >
**Project Settings** > **Physics**) and set the **Bounce Threshold** to the
minimum velocity at which colliders should bounce. This value is set to 2 by
default.

[](collider-surface-friction.html)

Collider surface friction

[](collider-surfaces-combine.html)

How collider surface values combine

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

