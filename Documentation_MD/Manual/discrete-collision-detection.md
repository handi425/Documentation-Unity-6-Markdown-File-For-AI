[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/discrete-collision-detection.html)
  * [中文](/cn/current/Manual/discrete-collision-detection.html)
  * [日本語](/ja/current/Manual/discrete-collision-detection.html)
  * [한국어](/kr/current/Manual/discrete-collision-detection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/discrete-collision-detection.html)
  * [中文](/cn/current/Manual/discrete-collision-detection.html)
  * [日本語](/ja/current/Manual/discrete-collision-detection.html)
  * [한국어](/kr/current/Manual/discrete-collision-detection.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collision detection](collision-detection.html)
  * Discrete collision detection

[](choose-collision-detection-mode.html)

Choose a collision detection mode

[](ContinuousCollisionDetection.html)

Continuous collision detection (CCD)

# Discrete collision detection

The **Discrete** **collision** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection mode uses a discrete
**collision detection** An automatic process performed by Unity which
determines whether a moving GameObject with a Rigidbody and collider component
has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) algorithm, which checks
for collisions on each physics timestep.

**Discrete** is the default collision detection mode, and by far the least
computationally demanding. However, it can miss collisions that occur between
physics steps, so it’s usually not suitable for fast-moving collisions.

If your collisions happen too quickly for discrete collision to pick them up,
you can try one or both of the following solutions:

  * Increase the frequency of physics timesteps. This can solve missed collisions for fast-moving objects, but comes with a high performance impact due to the extra calculations required.
  * Use one of the [continuous collision detection (CCD)](ContinuousCollisionDetection.html) modes. These can predict collisions that might occur between physics timesteps, but they also have a higher performance impact.

Experiment with both and profile the results to find the right solution for
your project.

[](choose-collision-detection-mode.html)

Choose a collision detection mode

[](ContinuousCollisionDetection.html)

Continuous collision detection (CCD)

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

