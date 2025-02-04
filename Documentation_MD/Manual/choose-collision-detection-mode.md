[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/choose-collision-detection-mode.html)
  * [中文](/cn/current/Manual/choose-collision-detection-mode.html)
  * [日本語](/ja/current/Manual/choose-collision-detection-mode.html)
  * [한국어](/kr/current/Manual/choose-collision-detection-mode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/choose-collision-detection-mode.html)
  * [中文](/cn/current/Manual/choose-collision-detection-mode.html)
  * [日本語](/ja/current/Manual/choose-collision-detection-mode.html)
  * [한국어](/kr/current/Manual/choose-collision-detection-mode.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collision detection](collision-detection.html)
  * Choose a collision detection mode

[](collision-detection.html)

Collision detection

[](discrete-collision-detection.html)

Discrete collision detection

# Choose a collision detection mode

****Collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) Detection** defines which algorithm
the physics body (Rigidbody or ArticulationBody) uses to detect collisions.
Different algorithms offer different levels of accuracy, but more accurate
algorithms require more computational resources.

There are three algorithms available, represented by four **collision
detection** An automatic process performed by Unity which determines whether a
moving GameObject with a Rigidbody and collider component has come into
contact with any other colliders. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) modes:

**Collision detection mode** | **Algorithm** | **Useful for** | **Not useful for**  
---|---|---|---  
**Discrete** | Discrete | \- Slow-moving collisions. | \- Fast-moving collisions.  
**Continuous Speculative** | Speculative CCD | \- Fast-moving collisions. | \- Some fast-moving collisions that require an especially high degree of accuracy.  
**Continuous** | Sweep CCD | \- Fast-moving linear collisions that require a high degree of accuracy.   
\- Physics bodies that only collide with static colliders. | \- Collisions that happen as a result of the physics body rotating.   
\- Physics bodies that collide with moving colliders.  
**Continuous Dynamic** | Sweep CCD | \- Fast-moving linear collisions that require a high degree of accuracy.   
\- Physics bodies that collide with moving colliders. | \- Collisions that happen as a result of the physics body rotating.  
  
The following decision flow might provide a starting point for selecting a
collision detection type. It starts with the least computationally intensive
mode, and progresses to the most computationally intensive mode.

  1. Try **Discrete** first.
  2. If you notice missed collisions in **Discrete** mode, try **Continuous Speculative**.
  3. If you notice missed collisions or false collisions in **Continuous Speculative** mode, try **Continuous** for collisions with static **colliders** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider), or **Continuous Dynamic** for
collisions with dynamic **Rigidbody** A component that allows a GameObject to
be affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) colliders.

In some cases, you might find that the physics performance relies on a
combination of the collision detection mode and the physics timestep
frequency. Experiment with both and profile the results to find the right
solution for your project.

## Select a collision detection mode

To select an algorithm, set the physics body’s **Collision Detection**
property in one of the following ways:

  * In the Editor: On the Rigidbody or Articulation Body component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), change the **Collision Detection**
property.

  * In code: Use the API properties [Rigidbody.collisionDetectionMode](../ScriptReference/Rigidbody-collisionDetectionMode.html) and [ArticulationBody.collisionDetectionMode](../ScriptReference/ArticulationBody-collisionDetectionMode.html).

[](collision-detection.html)

Collision detection

[](discrete-collision-detection.html)

Discrete collision detection

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

