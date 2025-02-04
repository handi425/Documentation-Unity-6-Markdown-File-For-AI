[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/RagdollStability.html)
  * [中文](/cn/current/Manual/RagdollStability.html)
  * [日本語](/ja/current/Manual/RagdollStability.html)
  * [한국어](/kr/current/Manual/RagdollStability.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/RagdollStability.html)
  * [中文](/cn/current/Manual/RagdollStability.html)
  * [日本語](/ja/current/Manual/RagdollStability.html)
  * [한국어](/kr/current/Manual/RagdollStability.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Ragdoll physics](ragdoll-physics-section.html)
  * Joint and Ragdoll stability

[](wizard-RagdollWizard.html)

Create a ragdoll

[](class-Cloth.html)

Cloth

# Joint and Ragdoll stability

This page provides tips for improving [Joint](Joints.html)A physics component
allowing a dynamic connection between Rigidbody components, usually allowing
some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) and [Ragdoll](wizard-
RagdollWizard.html) stability.

  * Avoid small Joint angles of **Angular Y Limit** and **Angular Z Limit**. Depending on your setup, the minimum angles should be around 5 to 15 degrees in order to be stable. Instead of using a small angle, try setting the angle to zero. This locks the axis and provide a stable simulation.
  * Uncheck the Joint’s **Enable Preprocessing** property. Disabling preprocessing can help prevent Joints from separating or moving erratically if they are forced into situations where there is no possible way to satisfy the Joint constraints. This can occur if [Rigidbody](class-Rigidbody.html)A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components connected by Joints are
pulled apart by static **collision** A collision occurs when the physics
engine detects that the colliders of two GameObjects make contact or overlap,
when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) geometry (for example, spawning a
Ragdoll partially inside a wall).

  * Under extreme circumstances (such as spawning partially inside a wall or pushed with a large force), the joint solver is unable to keep the Rigidbody components of a Ragdoll together. This can result in stretching. To handle this, enable projection on the Joints using either [ConfigurableJoint.projectionMode](../ScriptReference/ConfigurableJoint-projectionMode.html) or [CharacterJoint.enableProjection](../ScriptReference/CharacterJoint-enableProjection.html).
  * If Rigidbody components connected with Joints are jittering, open the [Physics](class-PhysicsManager.html) window (**Edit** > **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings), then select the **Physics**
category) and try increasing the **Default Solver Iterations** value to
between 10 and 20.

  * If Rigidbody components connected with Joints are not accurately responding to bounces, open the [Physics](class-PhysicsManager.html) window (**Edit** > **Project Settings** , then select the **Physics__category) and try increasing the** Default Solver Velocity Iterations__ value to between 10 and 20.
  * Never use direct Transform access with Kinematic Rigidbody components connected by Joints to other Rigidbody components. Doing so skips the step where PhysX computes internal velocities of corresponding Rigidbody components, making the solver provide unwanted results. A common example of bad practice is using direct Transform access in 2D projects to flip characters, by altering [Transform.TransformDirection](../ScriptReference/Transform.TransformDirection.html) on the root bone of the rig. This behaves much better if you use [Rigidbody2D.MovePosition](../ScriptReference/Rigidbody2D.MovePosition.html) and [Rigidbody2D.MoveRotation](../ScriptReference/Rigidbody2D.MoveRotation.html) instead.
  * Avoid large differences in the masses between Rigidbody components connected by Joints. It’s okay to have one Rigidbody with twice as much mass as another, but when one mass is ten times larger than the other, the simulation can become jittery.
  * Try to avoid scaling different from 1 in the Transform containing Rigidbody or the Joint. The scaling might not be robust in all cases.
  * If Rigidbody components are overlapping when inserted into the world, and you cannot avoid the overlap, try lowering the [Rigidbody.maxDepenetrationVelocity](../ScriptReference/Rigidbody-maxDepenetrationVelocity.html) to make the Rigidbody components exit each other more smoothly.

[](wizard-RagdollWizard.html)

Create a ragdoll

[](class-Cloth.html)

Cloth

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

