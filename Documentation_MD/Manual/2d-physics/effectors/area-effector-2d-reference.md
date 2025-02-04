[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/area-effector-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Effectors 2D](../../2d-physics/effectors/effectors-2d-landing.html)
  * Area Effector 2D reference

[](../../2d-physics/effectors/effectors-2d-landing.html)

Effectors 2D

[](../../2d-physics/effectors/buoyancy-effector-2d-reference.html)

Buoyancy Effector 2D reference

# Area Effector 2D reference

The Area Effector 2D applies forces within an area defined by the attached
**Collider** An invisible shape that is used to handle physical collisions for
an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) 2Ds when another (target)
Collider 2D comes into contact with the Effector 2D. You can configure the
force at any angle with a specific magnitude and random variation on that
magnitude. You can also apply both linear and angular drag forces to slow down
**Rigidbody** A component that allows a GameObject to be affected by simulated
gravity and other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2Ds.

Collider 2Ds that you use with the Area Effector 2D would typically be set as
triggers, so that other Collider 2Ds can overlap with it to have forces
applied. Non-triggers will still work, but forces will only be applied when
Collider 2Ds come into contact with them.

## Properties

**Property** | **Function**  
---|---  
**Use Collider Mask** | Check to enable use of the **Collider Mask** property? If this is not enabled, the Global **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) Matrix will be used as the
default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the Area Effector 2D.  
**Use Global Angle** | Check this to define the **Force Angle** as a global (world-space) angle. If this is not checked, the **Force Angle** is considered a local angle by the **physics engine** A system that simulates aspects of physical systems so that objects can accelerate correctly and be affected by collisions, gravity and other forces. [More info](../../PhysicsSection.html)  
See in [Glossary](../../Glossary.html#PhysicsEngine).  
**Force Angle** | The angle of the force to be applied.  
**Force Magnitude** | The magnitude of the force to be applied.  
**Force Variation** | The variation of the magnitude of the force to be applied.  
**Drag** | The linear drag to apply to Rigidbody 2Ds.  
**Angular Drag** | The angular drag to apply to Rigidbody 2Ds.  
**Force Target** | The point on a target **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) where the Area Effector 2D
applies any force.  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Collider** | The target point is defined as the current position of the Collider 2D. Applying force here can generate torque (rotation) if the Collider 2D isn’t positioned at the **center of mass** Represents the average position of all mass in a Rigidbody for the purposes of physics calculations. By default it is computed from all colliders belonging to the Rigidbody, but can be modified via script. [More info](../../../../../ScriptReference/Rigidbody-centerOfMass.html)  
See in [Glossary](../../Glossary.html#CenterofMass).  
&#nbsp;&#nbsp;&#nbsp;&#nbsp;**Rigidbody** | The target point is defined as the current center-of-mass of the Rigidbody 2D. Applying force here will never generate torque (rotation).  
  
AreaEffector2D

[](../../2d-physics/effectors/effectors-2d-landing.html)

Effectors 2D

[](../../2d-physics/effectors/buoyancy-effector-2d-reference.html)

Buoyancy Effector 2D reference

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

