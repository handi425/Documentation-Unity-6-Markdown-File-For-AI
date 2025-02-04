[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/wheel-colliders.html)
  * [中文](/cn/current/Manual/wheel-colliders.html)
  * [日本語](/ja/current/Manual/wheel-colliders.html)
  * [한국어](/kr/current/Manual/wheel-colliders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/wheel-colliders.html)
  * [中文](/cn/current/Manual/wheel-colliders.html)
  * [日本語](/ja/current/Manual/wheel-colliders.html)
  * [한국어](/kr/current/Manual/wheel-colliders.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Collision](collision-section.html)
  * [Collider shapes](collider-shapes.html)
  * Wheel colliders

[](class-MeshCollider.html)

Mesh collider component reference

[](wheel-colliders-introduction.html)

Introduction to Wheel colliders

# Wheel colliders

The **Wheel**collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider)** is a collider for grounded
vehicles. It has built-in **collision** A collision occurs when the physics
engine detects that the colliders of two GameObjects make contact or overlap,
when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection, wheel physics, and a
slip-based tire friction model. It can be used for objects other than wheels,
but it is specifically designed for vehicles with wheels.

Unity’s PhysX integration uses the PhysX 4.1 Vehicles SDK to simulate the
wheel assembly of ground vehicles (that is, the wheels, suspension, and
braking). This documentation covers how to interact with this SDK in Unity;
for details of the SDK itself, see the [PhysX 4.1 Vehicles SDK
documentation](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html).

You don’t need to understand how a real-world vehicle works to build a simple
simulation. However, an understanding of the main elements such as suspension
and wheel behavior can help you work more precisely with the different vehicle
simulation properties available in Unity.

**Topic** | **Description**  
---|---  
[Introduction to wheel colliders](wheel-colliders-introduction.html) | Overview of the concepts and fundamental behaviors of the **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) class and component. This section
includes information on how Unity implements **Wheel colliders** A special
collider for grounded vehicles. It has built-in collision detection, wheel
physics, and a slip-based tire friction model. It can be used for objects
other than wheels, but it is specifically designed for vehicles with wheels.
[More info](class-WheelCollider.html)  
See in [Glossary](Glossary.html#WheelCollider) to simulate ground wheel movement, and how to work with Wheel colliders in the Editor. |   
[Wheel collider friction](wheel-colliders-friction.html) | How Unity simulates friction between the Wheel collider and the surface it travels across.  
[Wheel collider suspension](wheel-colliders-suspension.html) | How Unity simulates a suspension system via the Wheel collider’s position and behavior.  
[Create a vehicle with Wheel colliders](WheelColliderTutorial.html) | Build a ground vehicle with Wheel colliders. This step-by-step walkthrough provides demonstration assets and code samples.  
[Wheel collider component reference](class-WheelCollider.html) | Reference page for the Wheel collider component.  
  
## Additional resources

  * [Nvidia PhysX 4.1 Vehicles SDK documentation](https://gameworksdocs.nvidia.com/PhysX/4.1/documentation/physxguide/Index.html)

[](class-MeshCollider.html)

Mesh collider component reference

[](wheel-colliders-introduction.html)

Introduction to Wheel colliders

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

