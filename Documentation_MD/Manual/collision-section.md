[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/collision-section.html)
  * [中文](/cn/current/Manual/collision-section.html)
  * [日本語](/ja/current/Manual/collision-section.html)
  * [한국어](/kr/current/Manual/collision-section.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/collision-section.html)
  * [中文](/cn/current/Manual/collision-section.html)
  * [日本語](/ja/current/Manual/collision-section.html)
  * [한국어](/kr/current/Manual/collision-section.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * Collision

[](class-ConstantForce.html)

Constant Force component reference

[](CollidersOverview.html)

Introduction to collision

# Collision

To configure **collision** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) between GameObjects in Unity, you
need to use colliders. colliders define the shape of a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) for the purposes of physical
collisions. You can then use these colliders to manage collision events. You
can configure collisions via **collider** An invisible shape that is used to
handle physical collisions for an object. A collider doesn’t need to be
exactly the same shape as the object’s mesh - a rough approximation is often
more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) components, or their corresponding
C# class.

This documentation describes how to configure collisions and collision events,
and how colliders interact with each other and their environment.

**Topic** | **Description**  
---|---  
[Introduction to collision](CollidersOverview.html) | Overview of the fundamental concepts around physics collision in Unity.  
[Introduction to collider types](collider-types-introduction.html) | The different collider types (static, kinematic, and dynamic), and how collider behaviour differs depending on the collider’s physics body configuration.  
[Collider shapes](collider-shapes.html) | The different collider shapes available, and how collider shape complexity affects performance.  
[Collider surfaces](collider-surfaces.html) | How PhysX handles friction and bounciness on a collider’s surface, and how to configure surface properties for each collider.  
[Collider interactions and events](collider-interactions.html) | How collisions can call events and functions to trigger changes at run time.  
[Collision detection](collision-detection.html)An automatic process performed
by Unity which determines whether a moving GameObject with a Rigidbody and
collider component has come into contact with any other colliders. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#CollisionDetection) | How PhysX detects collisions in Unity, and how to select the right algorithm depending on your collider configuration for optimal performance.  
  
[](class-ConstantForce.html)

Constant Force component reference

[](CollidersOverview.html)

Introduction to collision

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

