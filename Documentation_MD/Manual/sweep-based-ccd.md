[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sweep-based-ccd.html)
  * [中文](/cn/current/Manual/sweep-based-ccd.html)
  * [日本語](/ja/current/Manual/sweep-based-ccd.html)
  * [한국어](/kr/current/Manual/sweep-based-ccd.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sweep-based-ccd.html)
  * [中文](/cn/current/Manual/sweep-based-ccd.html)
  * [日本語](/ja/current/Manual/sweep-based-ccd.html)
  * [한국어](/kr/current/Manual/sweep-based-ccd.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collision detection](collision-detection.html)
  * [Continuous collision detection (CCD)](ContinuousCollisionDetection.html)
  * Sweep-based CCD

[](ContinuousCollisionDetection.html)

Continuous collision detection (CCD)

[](speculative-ccd.html)

Speculative CCD

# Sweep-based CCD

Sweep-based CCD is the CCD algorithm for the **Continuous** and **Continuous
Dynamic** modes.

Use **Continuous** on physics bodies that only collide with stationary static
**colliders** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) (that is, GameObjects that don’t
have a Rigidbody). Use **Continuous Dynamic** on physics bodies that collide
with moving dynamic colliders (that is, GameObjects that have a dynamic
Rigidbody).

**Continuous** and **Continuous Dynamic** are the most accurate **collision**
A collision occurs when the physics engine detects that the colliders of two
GameObjects make contact or overlap, when at least one has a Rigidbody
component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection modes. However, they are
also the most computationally demanding. In addition, they only work for
collisions that occur as a result of linear movement; they can’t detect
collisions that occur as a result of the physics body rotating (for example, a
pinball flipper colliding with a ball when it rotates on its pivot).

## Understand sweep-based CCD

Sweep-based CCD uses a Time-Of-Impact (TOI) algorithm to compute potential
collisions. To do this, the algorithm “sweeps” or detects along the object’s
forward trajectory at the object’s current velocity.

![Sweep-based collision detection, from one timestep to the next. See the
legend below for details.](../uploads/Main/sweep-ccd-1.png) Sweep-based
collision detection, from one timestep to the next. See the legend below for
details.

In the above image:

  * A: Object at starting position
  * B: Predicted area that the object will pass through between now and the next timestep, based on the object’s current velocity
  * C: Object at new position after one physics timestep

If there are contacts along the object’s moving direction, the algorithm
computes the time of impact, and moves the object until that time. The
algorithm can perform sub-steps from that time onwards; most importantly, it
can re-compute the velocity after impact and then re-sweep at the new
trajectory.

![Sweep-based collision detection, when the algorithm detects an obstacle. See
legend below for details.](../uploads/Main/sweep-ccd-2.png) Sweep-based
collision detection, when the algorithm detects an obstacle. See legend below
for details.

In the above image:

  * A: Object at starting position
  * B: Object in position at which the sweep-based CCD algorithm predicts a collision
  * C: Original predicted position after one physics timestep
  * D: Collider interrupting the linear path, detected by the sweep-based CCD algorithm

Sweep-based CCD can have a significant impact on performance, especially when
widely used in a project. If a large number of high-speed objects with sweep-
based CCD are in close proximity, the CCD overhead increases quickly because
the **physics engine** A system that simulates aspects of physical systems so
that objects can accelerate correctly and be affected by collisions, gravity
and other forces. [More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) has to perform more sweeps, and
more CCD sub-steps.

A limitation of sweep-based CCD is that it can only carry out a linear (or
directional) sweep, and not an angular (or rotational) sweep, which means it
cannot predict collisions that might happen if the physics body rotates. For
example, the flipper in a pinball machine is fixed at one end and rotates
around a fixed point; it only has angular motion, and no linear motion. If you
also need to account for an object’s rotation, use speculative CCD.

[](ContinuousCollisionDetection.html)

Continuous collision detection (CCD)

[](speculative-ccd.html)

Speculative CCD

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

