[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collider-surfaces.html)
  * [中文](/cn/current/Manual/collider-surfaces.html)
  * [日本語](/ja/current/Manual/collider-surfaces.html)
  * [한국어](/kr/current/Manual/collider-surfaces.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collider-surfaces.html)
  * [中文](/cn/current/Manual/collider-surfaces.html)
  * [日本語](/ja/current/Manual/collider-surfaces.html)
  * [한국어](/kr/current/Manual/collider-surfaces.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * Collider surfaces

[](create-compound-collider.html)

Create a compound collider

[](collider-surface-friction.html)

Collider surface friction

# Collider surfaces

In real-world physics, objects that can collide have different surface
textures and properties that affect how they collide with each other, and how
they interact with each other.

To control how objects collide with each other in the physics simulation, you
can adjust the friction and bounciness of your **colliders** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider). In Unity, you use the [Physics
Material](class-PhysicsMaterial.html)A physics asset for adjusting the
friction and bouncing effects of colliding objects. [More info](class-
PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial) asset to control these
parameters. The Physics Material asset is represented in the API by the
[`PhysicsMaterial`](../ScriptReference/PhysicsMaterial.html) class.

For more detailed information on how PhysX applies friction and bounce, see
the Nvidia PhysX documentation [Rigid Body Dynamics: Friction and
Restitution](https://docs.nvidia.com/gameworks/content/gameworkslibrary/physx/guide/Manual/RigidBodyDynamics.html#friction-
and-restitution).

**Topic** | **Description**  
---|---  
[Collider surface friction](collider-surface-friction.html) | How Unity handles friction on collider surfaces, and how to configure friction properties.  
[Collider surface bounciness](collider-surface-bounce.html) | How Unity handles bounciness on collider surfaces, and how to configure bounce properties.  
[How collider surface values combine](collider-surfaces-combine.html) | How Unity combines the values of surface properties in a collider pair; for example, how it calculates the friction between two colliders that have different friction values.  
[Create and apply a Physics Material](create-apply-physics-material.html) | Create and configure a Physics Material to define a collider’s surface properties, and apply it to a collider.  
[Physics Material component reference](class-PhysicsMaterial.html) | Reference page for the Physics Material asset.  
  
[](create-compound-collider.html)

Create a compound collider

[](collider-surface-friction.html)

Collider surface friction

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

