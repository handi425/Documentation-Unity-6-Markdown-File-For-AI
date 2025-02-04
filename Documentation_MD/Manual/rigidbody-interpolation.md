[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/rigidbody-interpolation.html)
  * [中文](/cn/current/Manual/rigidbody-interpolation.html)
  * [日本語](/ja/current/Manual/rigidbody-interpolation.html)
  * [한국어](/kr/current/Manual/rigidbody-interpolation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/rigidbody-interpolation.html)
  * [中文](/cn/current/Manual/rigidbody-interpolation.html)
  * [日本語](/ja/current/Manual/rigidbody-interpolation.html)
  * [한국어](/kr/current/Manual/rigidbody-interpolation.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Rigidbody physics](rigidbody-physics-section.html)
  * Apply interpolation to a Rigidbody

[](rigidbody-constant-force.html)

Apply constant force to a Rigidbody

[](class-Rigidbody.html)

Rigidbody component reference

# Apply interpolation to a Rigidbody

Interpolation provides a way to manage the appearance of jitter in the
movement of your [Rigidbody](RigidbodiesOverview.html)A component that allows
a GameObject to be affected by simulated gravity and other forces. [More
info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) at run time.

Jitter can happen when the rate of physics simulation updates (determined by
the [Fixed Timestep](class-TimeManager.html)A customizable frame-rate-
independent interval that dictates when physics calculations and FixedUpdate()
events are performed. [More info](class-TimeManager.html)  
See in [Glossary](Glossary.html#FixedTimestep)) is slower than the
application’s frame rate. It is most noticeable if you have a Rigidbody with
physics-based movement that the **camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) tracks at run time.

Unity’s PhysX system provides a way to implement interpolation. The
**Interpolate** setting on a Rigidbody provides two options to smooth the
appearance of a Rigidbody’s motion if it appears jittery at run time. These
options are **Interpolate** and **Extrapolate**.

Both interpolation and extrapolation calculate the pose of the Rigidbody (that
is, the position and rotation) between physics updates. Which one you should
choose depends on which option produces the best visual outcome for your use
case.

You should only use interpolation or extrapolation if you see jitter in your
Rigidbody’s movement. **Interpolate** is set to **None** by default.

When interpolation or extrapolation is enabled, the physics system takes
control of the Rigidbody’s transform. For this reason, you should follow any
direct (non-physics) change to the transform with a
[Physics.SyncTransforms](../ScriptReference/Physics.SyncTransforms.html) call.
Otherwise, Unity ignores any transform change that does not originate from the
physics system.

## Interpolate

Use the pose of the Rigidbody from the previous two physics updates to
calculate and apply the pose of the Rigidbody in the current frame.

Interpolate makes the Rigidbody appear to move slightly behind where it should
be. This is because interpolation delays the Rigidbody’s pose by one physics
update, so that it has two points to use for its calculation, and enough time
to move the Rigidbody to the new pose.

Interpolation is more accurate than extrapolation, but it has a time lag of
one physics update.

Interpolate is usually the best option for situations where the Rigidbody’s
velocity varies, or if there are other physics elements that influence the
Rigidbody’s movement.

Interpolate is represented by the API property
[`RigidbodyInterpolation.Interpolate`](../ScriptReference/RigidbodyInterpolation.Interpolate.html).

## Extrapolate

Use the pose of the Rigidbody from the previous physics update, and predict
the pose of the Rigidbody in the next physics update, to calculate and predict
the pose in the current frame.

Extrapolate makes the Rigidbody appear to move slightly ahead of where it
should be. This is because extrapolation uses the Rigidbody’s current velocity
to predict the Rigidbody’s pose in the next physics update, so that it has two
points to use for its calculation.

Extrapolation is often less accurate, and might visibly overshoot
**collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) bounds (and then correct itself in
the next frame, after the next physics update). This is because the
extrapolation calculation does not take into account future physics forces or
calculations.

Extrapolate is usually only a good option for situations where accuracy is not
important; for example, if the Rigidbody moves at a constant velocity, and
there are no other physics elements that influence the Rigidbody’s movement.

Extrapolate is represented by the API property
[`RigidbodyInterpolation.Extrapolate`](../ScriptReference/RigidbodyInterpolation.Extrapolate.html).

[](rigidbody-constant-force.html)

Apply constant force to a Rigidbody

[](class-Rigidbody.html)

Rigidbody component reference

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

