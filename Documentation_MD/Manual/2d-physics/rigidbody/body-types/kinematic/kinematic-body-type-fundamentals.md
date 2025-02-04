[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-fundamentals.html)

  * [Working in Unity](../../../../working-in-unity.html)
  * [2D in Unity](../../../../Unity2D.html)
  * [2D Physics](../../../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * [Rigidbody 2D body types](../../../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)
  * [Kinematic Body Type](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-landing.html)
  * Kinematic Body Type fundamentals

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
landing.html)

Kinematic Body Type

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
reference.html)

Kinematic Body Type reference

# Kinematic Body Type fundamentals

The Kinematic ****Body Type** Defines a fixed behavior for a 2D Rigidbody. Can
be Dynamic (the body moves under simulation and is affected by forces like
gravity), Kinematic (the body moves under simulation, but and isn’t affected
by forces like gravity) or Static (the body doesn’t move under simulation).
[More info](../../../../2d-physics/rigidbody/introduction-to-
rigidbody-2d.html)  
See in [Glossary](../../../../Glossary.html#BodyType)** **Rigidbody** A
component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](../../../../class-Rigidbody.html)  
See in [Glossary](../../../../Glossary.html#Rigidbody) 2D is designed to move
under simulation, but only under very explicit user control. While a
[Dynamic](../dynamic/dynamic-body-type-reference.html) Rigidbody 2D is
affected by gravity and forces, a Kinematic Rigidbody 2D is not. Because of
this, the Kinematic Rigidbody 2D has a lower demand on system resources than a
Dynamic Rigidbody 2D, allowing it to be simulated faster.

To reposition a Kinematic Rigidbody 2D, it must be repositioned explicitly via
[Rigidbody2D.MovePosition](../../../../../ScriptReference/Rigidbody2D.MovePosition.html)
or
[Rigidbody2D.MoveRotation](../../../../../ScriptReference/Rigidbody2D.MoveRotation.html).
Use physics queries to detect **collisions** A collision occurs when the
physics engine detects that the colliders of two GameObjects make contact or
overlap, when at least one has a Rigidbody component and is in motion. [More
info](../../../../CollidersOverview.html)  
See in [Glossary](../../../../Glossary.html#Collision), and **scripts** A
piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](../../../../creating-scripts.html)  
See in [Glossary](../../../../Glossary.html#Scripts) to decide where and how
the Rigidbody 2D should move.

A Kinematic Rigidbody 2D can still move via its velocity, but the velocity is
not affected by forces or gravity. A Kinematic Rigidbody 2D does not collide
with other Kinematic Rigidbody 2Ds or with Static Rigidbody 2Ds and will only
collide with Dynamic Rigidbody 2Ds.

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
landing.html)

Kinematic Body Type

[](../../../../2d-physics/rigidbody/body-types/kinematic/kinematic-body-type-
reference.html)

Kinematic Body Type reference

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

