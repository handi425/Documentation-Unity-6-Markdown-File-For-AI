[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [中文](/cn/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [日本語](/ja/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)
  * [한국어](/kr/current/Manual/2d-physics/rigidbody/introduction-to-rigidbody-2d.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [Rigidbody 2D](../../2d-physics/rigidbody/rigidbody-2d-landing.html)
  * Introduction to Rigidbody 2D

[](../../2d-physics/rigidbody/rigidbody-2d-landing.html)

Rigidbody 2D

[](../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)

Rigidbody 2D body types

# Introduction to Rigidbody 2D

You can attach a Rigidbody 2D component to a **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) to control it with the
physics system. The Rigidbody 2D shares similar properties with its standard
[Rigidbody](../../class-Rigidbody.html)A component that allows a GameObject to
be affected by simulated gravity and other forces. [More info](../../class-
Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) counterpart, but it’s adapted
to 2D development. For example, GameObjects that have a Rigidbody 2D component
attached to them can only move along the XY plane and can only rotate on an
axis perpendicular to that plane.

## How a Rigidbody 2D works

The Unity Editor’s [Transform](../../class-Transform.html) component defines
how to position, rotate, and scale a GameObject (and its child GameObjects)
within the **Scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). When you change this component,
it updates other components which can affect where they render or the position
of other **colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collider). Unity’s 2D physics system can
move colliders and make them interact with each other, so Unity requires a
method for the physics system to communicate this movement of colliders back
to the Transform components. This movement and connection with colliders is
what a Rigidbody 2D component is for. The Rigidbody 2D component overrides the
**Transform component** A Transform component determines the Position,
Rotation, and Scale of each object in the scene. Every GameObject has a
Transform. [More info](../../class-Transform.html)  
See in [Glossary](../../Glossary.html#TransformComponent) and updates it to
the position and/or rotation it defines instead.

**Note:** You can override the Rigidbody 2D by directly modifying the
Transform component yourself (because Unity exposes all properties on all
components). However, this will cause issues such as unpredictable movement or
GameObjects passing through and into each other.

## Collider 2D and Rigidbody 2D interaction

Any Collider 2D component added to the same GameObject or child GameObject is
implicitly attached to that Rigidbody 2D GameObject, causing the Collider 2D
to move with the Rigidbody 2D. When attached, you should never move the
Collider 2D directly using the Transform or any collider offset; move the
Rigidbody 2D instead. Moving the Rigidbody 2D provides the best performance
and ensures correct **collision** A collision occurs when the physics engine
detects that the colliders of two GameObjects make contact or overlap, when at
least one has a Rigidbody component and is in motion. [More
info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision) detection. Collider 2Ds
attached to the same Rigidbody 2D won’t collide with each other. This means
you can create a set of colliders that act effectively as a single compound
collider, all moving and rotating in sync with the Rigidbody 2D.

Adding a Rigidbody 2D moves a **sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../../sprite/sprite-
landing.html)  
See in [Glossary](../../Glossary.html#Sprite) in a physically convincing way
by applying forces from the scripting API. When you attach the appropriate
collider component to the sprite GameObject, it’s affected by collisions with
other moving GameObjects. Using the Unity physics system can simplify many
common gameplay mechanics and portray realistic behavior with minimal coding.

**Note:** Although Rigidbody 2Ds are often described as colliding with each
other, it’s the Collider 2Ds attached to each of those bodies which collide.
Rigidbody 2Ds can’t collide with each other without Colliders.

## Additional resources

  * [API documentation on Rigidbody2D](../../../ScriptReference/Rigidbody2D.html)
  * [API documentation on Collider2D](../../../ScriptReference/Collider2D.html)

Rigidbody2D

[](../../2d-physics/rigidbody/rigidbody-2d-landing.html)

Rigidbody 2D

[](../../2d-physics/rigidbody/body-types/rigidbody-2d-body-types-landing.html)

Rigidbody 2D body types

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

