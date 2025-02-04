[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ContinuousCollisionDetection.html)
  * [中文](/cn/current/Manual/ContinuousCollisionDetection.html)
  * [日本語](/ja/current/Manual/ContinuousCollisionDetection.html)
  * [한국어](/kr/current/Manual/ContinuousCollisionDetection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ContinuousCollisionDetection.html)
  * [中文](/cn/current/Manual/ContinuousCollisionDetection.html)
  * [日本語](/ja/current/Manual/ContinuousCollisionDetection.html)
  * [한국어](/kr/current/Manual/ContinuousCollisionDetection.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collision detection](collision-detection.html)
  * Continuous collision detection (CCD)

[](discrete-collision-detection.html)

Discrete collision detection

[](sweep-based-ccd.html)

Sweep-based CCD

# Continuous collision detection (CCD)

Continuous **collision** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection (CCD) modes use
predictive algorithms to calculate collisions that happen between physics
timesteps. They are more accurate, but usually require more computational
resources than discrete **collision detection** An automatic process performed
by Unity which determines whether a moving GameObject with a Rigidbody and
collider component has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection).

CCD is supported for Box, Sphere and Capsule **colliders** An invisible shape
that is used to handle physical collisions for an object. A collider doesn’t
need to be exactly the same shape as the object’s mesh - a rough approximation
is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider). It is intended as a safety net to
catch collisions in cases where colliders would otherwise pass through each
other. However, it does not always deliver physically accurate collision
results, so you might still consider decreasing the physics timestep frequency
to make the simulation more precise.

In Unity, there are two CCD algorithms, represented by three **Collision
Detection** mode options.

**Topic** | **Description**  
---|---  
[Speculative CCD](speculative-ccd.html) | Learn about speculative collision detection. **Continuous Speculative** uses speculative collision detection.  
[Sweep-based CCD](sweep-based-ccd.html) | Learn about sweep-based collision detection. Both **Continuous** and **Continuous Dynamic** modes use sweep-based collision detection.  
  
[](discrete-collision-detection.html)

Discrete collision detection

[](sweep-based-ccd.html)

Sweep-based CCD

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

