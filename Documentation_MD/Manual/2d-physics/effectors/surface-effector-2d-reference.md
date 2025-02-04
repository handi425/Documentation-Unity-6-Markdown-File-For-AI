[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/effectors/surface-effector-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Effectors 2D](../../2d-physics/effectors/effectors-2d-landing.html)
  * Surface Effector 2D reference

[](../../2d-physics/effectors/platform-effector-2d-reference.html)

Platform Effector 2D reference

[](../../2d-physics/joints/2d-joints-landing.html)

2D joints

# Surface Effector 2D reference

The Surface Effector 2D applies tangent forces along the surfaces of
**colliders** An invisible shape that is used to handle physical collisions
for an object. A collider doesn’t need to be exactly the same shape as the
object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider) used by the effector in an
attempt to match a specified speed along the surface. This is analogous to a
conveyor belt.

Colliders that you use with the effector would typically be set as non-
triggers so that other colliders can come into contact with the surface.

## Properties

**Property** | **Function**  
---|---  
**Use Collider Mask** | Enable this to use the **Collider Mask** property. If this not enabled, the global **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) matrix will be used as the
default for all Collider 2Ds.  
**Collider Mask** | The mask used to select specific Layers allowed to interact with the effector. Note that this option only displays if you have selected **Use Collider Mask**.  
**Speed** | Enter the speed to keep along the surface.  
**Speed Variation** | Enter a value here to apply a random increase in speed, where Unity selects a random number between 0 and the **Speed Variation** value. Entering a negative number here will result in a random reduction in speed instead, where Unity selects a random negative number between 0 and the **Speed Variation** value.  
**Force Scale** | Enter a value to scale the force that’s applied when the effector attempts to meet the specified **Speed** along the surface. If this is 0, then Unity applies no force. If this is 1, then Unity applies full force. **Note:** Entering 1 to apply full force can counteract any other forces being applied to the target object and cause unwanted movement or behavior. It’s recommended to enter a value less than 1 to prevent this issue from happening.  
**Use Contact Force** | Enable this to have Unity apply force at the point of contact between the surface and the target collider. Enabling contact forces can cause the target object to rotate when in contact with a surface.  
**Use Friction** | Enable this to enable friction between the collider and the surface it contacts.  
**Use Bounce** | Enable this to enable bounce between the collider and the surface it contacts.  
  
SurfaceEffector2D

[](../../2d-physics/effectors/platform-effector-2d-reference.html)

Platform Effector 2D reference

[](../../2d-physics/joints/2d-joints-landing.html)

2D joints

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

