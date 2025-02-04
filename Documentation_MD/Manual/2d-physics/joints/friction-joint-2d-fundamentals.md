[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/friction-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Friction Joint 2D](../../2d-physics/joints/friction-joint-2d-landing.html)
  * Friction Joint 2D fundamentals

[](../../2d-physics/joints/friction-joint-2d-landing.html)

Friction Joint 2D

[](../../2d-physics/joints/friction-joint-2d-reference.html)

Friction Joint 2D component reference

# Friction Joint 2D fundamentals

Use the Friction **Joint** A physics component allowing a dynamic connection
between Rigidbody components, usually allowing some degree of movement such as
a hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) 2D to slow down movement between
two points to a stop. This joint’s aim is to maintain a zero relative linear
and angular offset between two points. Those two points can be two
****Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2D** components or a
**Rigidbody 2D** component and a fixed position in the world. (Connect to a
fixed position in the world by setting **Connected Rigidbody** to None).

## Resistance

The joint applies linear force (**Force**) and angle force (**Torque**) to
both Rigidbody 2D points. It uses a simulated motor that is pre-configured to
have a low motor power (and so, low resistance). You can change the resistance
to make it weaker or stronger.

Strong Resistance:

  * A high (1,000,000 is the highest) **Max Force** creates strong linear resistance. The Rigidbody 2D **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) won’t move in a line
relative to each other very much.

  * A high (1,000,000 is the highest) **Max Torque** creates strong angular resistance. The Rigidbody 2D GameObjects won’t move at an angle relative to each other very much.

Weak Resistance:

  * A low **Max Force** creates weak linear resistance. The Rigidbody 2D GameObjects move easily in a line relative to each other.
  * A low **Max Torque** creates weak angular resistance. The Rigidbody 2D GameObjects move easily at an angle relative to each other.

## Constraints

Friction Joint 2D has two simultaneous constraints:

  * Maintain a zero relative linear velocity between two anchor points on two Rigidbody 2Ds
  * Maintain a zero relative angular velocity between two anchor points on two Rigidbody 2Ds

You can use this joint to construct physical GameObjects that need to behave
as if they have friction. They can resist either linear movement or angular
movement, or both linear and angular movement. For example:

  * A platform that does rotate, but resists applied forces, making it difficult but possible for the player to move it.
  * A ball that resists linear movement. The ball’s friction is related to the GameObject’s velocity and not to any **collisions** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](../../CollidersOverview.html)  
See in [Glossary](../../Glossary.html#Collision). It acts like the **Linear
Drag** and **Angular Drag** which is set in **Rigidbody 2D**. The difference
is that Friction Joint 2D has the option of maximum **Force** and **Torque**
settings.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Friction Joint 2D component reference](friction-joint-2d-reference.html)

[](../../2d-physics/joints/friction-joint-2d-landing.html)

Friction Joint 2D

[](../../2d-physics/joints/friction-joint-2d-reference.html)

Friction Joint 2D component reference

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

