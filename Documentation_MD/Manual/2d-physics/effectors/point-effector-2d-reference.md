[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/point-effector-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Effectors 2D](../../2d-physics/effectors/effectors-2d-landing.html)
  * Point Effector 2D reference

[](../../2d-physics/effectors/buoyancy-effector-2d-reference.html)

Buoyancy Effector 2D reference

[](../../2d-physics/effectors/platform-effector-2d-reference.html)

Platform Effector 2D reference

# Point Effector 2D reference

The Point Effector 2D applies forces to attract/repulse against a source point
which can be defined as the position of the rigid-body or the center of a
**collider** An invisible shape that is used to handle physical collisions for
an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) used by the effector. When
another (target) collider comes into contact with the effector then a force is
applied to the target. Where the force is applied and how it is calculated can
be controlled.

Colliders that you use with the effector would typically be set as triggers so
that other colliders can overlap with it to have forces applied however, non-
triggers will still work but forces will only be applied when colliders come
into contact with it.

## Properties

**Property** | **Function**  
---|---  
**Use Collider Mask** | Enable to use the **Collider Mask** property. If disabled, then the global **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) matrix will be used as is the
default for all colliders.  
**Collider Mask** | The mask used to select specific layers allowed to interact with the effector.  
**Force Magnitude** | The magnitude of the force to be applied.  
**Force Variation** | The variation of the magnitude of the force to be applied.  
**Distance Scale** | The scale applied to the distance between the source and target. When calculating the distance, it is scaled by this amount allowing the effective distance to be changed which controls the magnitude of the force applied.  
**Drag** | The linear drag to apply to rigid-bodies.  
**Angular Drag** | The angular drag to apply to rigid-bodies.  
**Force Source** | The force source is the point that attracts or repels target objects. The distance from the target is defined from this point.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Collider** | The source point is defined as the current position of the collider.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;****Rigidbody** A component that allows a
GameObject to be affected by simulated gravity and other forces. [More
info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody)** | The source point is defined as the current position of the rigidbody.  
**Force Target** | The force target is the point on a target object where the effector applies any force. The distance to the source is defined from this point.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Collider** | The target point is defined as the current position of the collider. Applying force here can generate torque (cause the target to rotate) if the collider isn’t positioned at the center-of-mass.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Rigidbody** | The target point is defined as the current center-of-mass of the rigidbody. Applying force here will never generate torque (cause the target to rotate).  
**Force Mode** | How the force is calculated.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Constant** | The force is applied ignoring how far apart the source and target are.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Inverse Linear** | The force is applied as a function of the inverse-linear distance between the source and target. When the source and target are in the same position then the full force is applied but it falls-off linearly as they move apart.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Inverse Squared** | The force is applied as a function of the inverse-squred distance between the source and target. When the source and target are in the same position then the full force is applied but it falls-off squared as they move apart. This is similar to real-world gravity.  
  
PointEffector2D

[](../../2d-physics/effectors/buoyancy-effector-2d-reference.html)

Buoyancy Effector 2D reference

[](../../2d-physics/effectors/platform-effector-2d-reference.html)

Platform Effector 2D reference

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

