[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/slider-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Slider Joint 2D](../../2d-physics/joints/slider-joint-2d-landing.html)
  * Slider Joint 2D fundamentals

[](../../2d-physics/joints/slider-joint-2d-landing.html)

Slider Joint 2D

[](../../2d-physics/joints/slider-joint-2d-reference.html)

Slider Joint 2D

# Slider Joint 2D fundamentals

Use this **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) slide **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) by maintaining the position
of two points on a configurable line that extends to infinity. Those two
points can be two **Rigidbody2D** components, or a **Rigidbody2D** component
and a fixed position in the world (by setting **Connected Rigidbody** to
**None**).

The joint applies a linear force to both connected **Rigidbody** A component
that allows a GameObject to be affected by simulated gravity and other forces.
[More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) objects to keep them on the
line. It also has a simulated linear motor that applies linear force to move
the Rigidbody GameObjects along the line. You can turn the motor off or on.
Although the line is infinite, you can specify just a segment of the line that
you want to use, using the **Translation Limits** option.

This joint has three simultaneous constraints. All are optional:

  * Maintain a relative linear distance away from a specified line between two anchor points on two Rigidbody objects.
  * Maintain a linear speed between two anchor points on two Rigidbody objects along a specified line. (The speed is limited with a maximum force.)
  * Maintain a linear distance between two points along the specified line.

You can use this joint to construct physical objects that need to react as if
they are connected together on a line. For example:

  * A platform which can move up or down. The platform reacts by moving down when something lands on it but must never move sideways. You can use this joint to ensure platform to never moves up or down beyond certain limits. Use the motor to make the platform move up.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Slider Joint 2D component reference](slider-joint-2d-reference.html)

SliderJoint2D

[](../../2d-physics/joints/slider-joint-2d-landing.html)

Slider Joint 2D

[](../../2d-physics/joints/slider-joint-2d-reference.html)

Slider Joint 2D

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

