[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/platform-effector-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Effectors 2D](../../2d-physics/effectors/effectors-2d-landing.html)
  * Platform Effector 2D reference

[](../../2d-physics/effectors/point-effector-2d-reference.html)

Point Effector 2D reference

[](../../2d-physics/effectors/surface-effector-2d-reference.html)

Surface Effector 2D reference

# Platform Effector 2D reference

The Platform Effector 2D applies various platform behavior such as one-way
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More
info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision), removal of side-
friction/bounce and more.

Colliders used with the Effector are typically not set as triggers so that
other **colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) can collide with it.

## Properties

**Property** | **Function**  
---|---  
**Use Collider Mask** | Select this option to indicate the use of the Collider Mask property. If this isn’t selected, the global collision matrix is chosen as the default for all colliders.  
**Collider Mask** | The mask used to select specific layers allowed to interact with the Effector.  
**Use One Way** | Select this option to indicate if one-way collision behavior is used.  
**Use One Way Grouping** | Ensures that all contacts disabled by the one-way behavior act on all colliders. This is useful when using multiple colliders on the object passing through the platform and they all need to act together as a group.  
**Surface Arc** | The angle of an arc centered on the local “up” defines the surface which doesn’t allow colliders to pass. Anything outside of this arc is considered for one-way collision.  
**Use Side Friction** | Select this option to indicate if the friction is used on the platform sides.  
**Use Side Bounce** | Select to indicate if bounce is used on the platform sides.  
**Side Arc** | The angle of an arc that defines the sides of the platform centered on the local “left” and “right” of the Effector. Any collision normals within this arc are considered for the “side” behaviors.  
  
PlatformEffector2D

[](../../2d-physics/effectors/point-effector-2d-reference.html)

Point Effector 2D reference

[](../../2d-physics/effectors/surface-effector-2d-reference.html)

Surface Effector 2D reference

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

