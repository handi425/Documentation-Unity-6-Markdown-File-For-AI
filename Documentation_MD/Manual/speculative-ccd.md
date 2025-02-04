[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/speculative-ccd.html)
  * [中文](/cn/current/Manual/speculative-ccd.html)
  * [日本語](/ja/current/Manual/speculative-ccd.html)
  * [한국어](/kr/current/Manual/speculative-ccd.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/speculative-ccd.html)
  * [中文](/cn/current/Manual/speculative-ccd.html)
  * [日本語](/ja/current/Manual/speculative-ccd.html)
  * [한국어](/kr/current/Manual/speculative-ccd.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collision detection](collision-detection.html)
  * [Continuous collision detection (CCD)](ContinuousCollisionDetection.html)
  * Speculative CCD

[](sweep-based-ccd.html)

Sweep-based CCD

[](joints-section.html)

Joints

# Speculative CCD

Speculative **collision** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection is the CCD algorithm for
**Continuous Speculative** mode.

Speculative **collision detection** An automatic process performed by Unity
which determines whether a moving GameObject with a Rigidbody and collider
component has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) is less computationally
demanding than [sweep-based collision detection](sweep-based-ccd.html). It
also works for collisions that occur as a result of both linear movement (for
example, a ball moving in a straight line) and rotational movement (for
example, a pinball flipper colliding with a ball when it rotates on its
pivot).

However, **Continuous Speculative** can also be less accurate; as well as
missed collisions, “false collisions” can occur, where the algorithm
incorrectly predicts a collision and forces the **colliders** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) off-course.

## Understand speculative CCD

Speculative CCD works by increasing an object’s broad-phase axis-aligned
minimum bounding box (AABB), based on the object’s linear and angular motion.
The algorithm is speculative because it selects all potential contacts during
the next physics step and feeds them into the solver, which makes sure that
all contact constraints are satisfied so that a **Rigidbody** A component that
allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) does not tunnel through any
collision.

![A sphere moving from t0 has an expected position at t1 if there are no walls
in its path. By inflating the AABB with its target pose, the speculative
algorithm detects two contacts with the n1 and n2 normals. The algorithm then
instructs the solver to respect those contacts, so that the sphere doesn’t
tunnel through the walls.](../uploads/Main/SpeculativeCCD2.png) A sphere
moving from **t0** has an expected position at **t1** if there are no walls in
its path. By inflating the AABB with its target pose, the speculative
algorithm detects two contacts with the **n1** and **n2** normals. The
algorithm then instructs the solver to respect those contacts, so that the
sphere doesn’t tunnel through the walls.

An inflated AABB based on the current velocity helps detect all potential
contacts along the moving trajectory, which enables the solver to prevent
missed collisions (“tunneling”).

Speculative CCD is generally less resource-intensive than sweep-based CCD,
because it only computes during the collision detection phase, not during the
solving and integrating phase. Additionally, speculative CCD can find contacts
that sweep-based CCD might miss, because speculative CCD expands the broad-
phase AABB based on both the object’s linear and angular motion.

However, speculative CCD can cause a false collision (or “ghost collision”),
where an object’s motion is affected by a speculative contact point when it
shouldn’t be. This is because speculative CCD collects all potential contacts
based on the closest point algorithm, so the contact normal is less accurate.
This can often make high-speed objects slide along tessellated collision
features and jump up, even though they shouldn’t. For example, in the
following diagram, a sphere starts at **t0** and moves horizontally towards
the right, with a predicted position at **t1** after integration. An inflated
AABB overlaps the boxes **b0** and **b1** , and the CCD yields two speculative
contacts at **c0** and **c1**. Because speculative CCD generates contacts
using the closest point algorithm, **c0** has a very inclined normal, which
the solver assumes to be a ramp.

![The solver assumes that the contact point at c0 is a ramp because the
closest point algorithm generated an inaccurate contact
normal.](../uploads/Main/SpeculativeCCD4.png) The solver assumes that the
contact point at **c0** is a ramp because the closest point algorithm
generated an inaccurate contact normal.

Such an inclined normal causes **t1** to jump upward after integration, rather
than moving straight forward:

![A false collision generated at c0 causes the sphere to erroneously jump up
instead of move straight forward.](../uploads/Main/SpeculativeCCD5.gif) A
false collision generated at c0 causes the sphere to erroneously jump up
instead of move straight forward.

Speculative CCD can also cause missed collisions because speculative contacts
are only computed during the collision detection phase. During contact
solving, if an object gains too much energy from the solver, it might end up
outside the initial inflated AABB after integration. If there are collisions
just outside the AABB, the object tunnels right through.

For example, in the following diagram, a sphere is moving left from **t0**
while a stick rotates clockwise. If the sphere gains too much energy from the
impact, it might end up exiting the inflated AABB (red dotted rectangle) at
**t1**. If there are collisions just outside the AABB, as shown by the blue
box below, the sphere may end up missing the collision and tunneling right
through it. This is because the solver only computes contacts inside the
inflated AABB, and collision detection isn’t performed during the solving and
integrating phase.

![The sphere with inflated AABB using speculative CCD, which only computes
contacts during the collision detection phase, so missed collisions might
occur.](../uploads/Main/SpeculativeCCD6.png) The sphere with inflated AABB
using speculative CCD, which only computes contacts during the collision
detection phase, so missed collisions might occur.

[](sweep-based-ccd.html)

Sweep-based CCD

[](joints-section.html)

Joints

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

