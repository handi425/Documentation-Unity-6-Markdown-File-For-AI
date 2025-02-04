[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CharacterControllers.html)
  * [中文](/cn/current/Manual/CharacterControllers.html)
  * [日本語](/ja/current/Manual/CharacterControllers.html)
  * [한국어](/kr/current/Manual/CharacterControllers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CharacterControllers.html)
  * [中文](/cn/current/Manual/CharacterControllers.html)
  * [日本語](/ja/current/Manual/CharacterControllers.html)
  * [한국어](/kr/current/Manual/CharacterControllers.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Character control](character-control-section.html)
  * Introduction to character control

[](character-control-section.html)

Character control

[](class-CharacterController.html)

Character Controller component reference

# Introduction to character control

The character in a first- or third-person game usually needs some collision-
based physics so that it doesn’t fall through the floor or walk through walls.
In many applications, the character’s acceleration and movement are
intentionally not physically realistic, so that the character can accelerate,
brake and change direction almost instantly and without being affected by
momentum.

In 3D physics, this type of behaviour can be created using a **Character
Controller** A simple, capsule-shaped collider component with specialized
features for behaving as a character in a game. Unlike true collider
components, a Rigidbody is not needed and the momentum effects are not
realistic. [More info](class-CharacterController.html)  
See in [Glossary](Glossary.html#CharacterController). This component gives the
character a simple, capsule-shaped **collider** An invisible shape that is
used to handle physical collisions for an object. A collider doesn’t need to
be exactly the same shape as the object’s mesh - a rough approximation is
often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) that is always upright. The
controller has its own special functions to set the object’s speed and
direction but unlike true colliders, a **rigidbody** A component that allows a
GameObject to be affected by simulated gravity and other forces. [More
info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) is not needed and the momentum
effects are not realistic.

A character controller cannot walk through static colliders in a **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), and so will follow floors and be
obstructed by walls. It can push rigidbody objects aside while moving but will
not be accelerated by incoming **collisions** A collision occurs when the
physics engine detects that the colliders of two GameObjects make contact or
overlap, when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision). This means that you can use the
standard 3D colliders to create a scene around which the controller will walk
but you are not limited by realistic physical behaviour on the character
itself.

You can find out more about character controllers on the [reference
page](class-CharacterController.html).

[](character-control-section.html)

Character control

[](class-CharacterController.html)

Character Controller component reference

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

