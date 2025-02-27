[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [中文](/cn/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/fixed-joint-2d-fundamentals.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Fixed Joint 2D](../../2d-physics/joints/fixed-joint-2d-landing.html)
  * Fixed Joint 2D fundamentals

[](../../2d-physics/joints/fixed-joint-2d-landing.html)

Fixed Joint 2D

[](../../2d-physics/joints/fixed-joint-2d-reference.html)

Fixed Joint 2D component reference

# Fixed Joint 2D fundamentals

The aim of this **joint** A physics component allowing a dynamic connection
between Rigidbody components, usually allowing some degree of movement such as
a hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) is to maintain a relative linear
and angular offset between two points. Those two points can be two
****Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](../../class-Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) 2D** components or a
**Rigidbody 2D** component and a fixed position in the world. (Connect to a
fixed position in the world by setting **Connected Rigidbody** to None).

The linear and angular offsets are based upon the relative positions and
orientations of the two connected points, so you change the offsets by moving
the connected **GameObjects** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) in your **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) view.

The joint applies both linear and torque forces to connected Rigidbody 2D
GameObjects. It uses a simulated spring that is pre-configured to be as stiff
as the simulation can provide. You can change the spring’s value to make it
weaker using the **Frequency** setting.

When the spring applies its force between the GameObjects, it tends to
overshoot the desired distance between them and then rebound repeatedly,
resulting in a continuous oscillation. The **damping ratio** A joint setting
to control spring oscillation. A higher damping ratio means the spring will
come to rest faster. [More info](../../2d-physics/joints/fixed-
joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#DampingRatio) determines how quickly the
oscillation reduces and brings the GameObjects to rest. The frequency is the
rate at which it oscillates either side of the target distance; the higher the
frequency, the stiffer the spring.

Fixed Joint 2D has two simultaneous constraints:

  * Maintain the linear offset between two anchor points on two Rigidbody 2D GameObjects.
  * Maintain the angular offset between two anchor points on two Rigidbody 2D GameObjects.

You can use this joint to construct physical GameObjects that need to react as
if they are rigidly connected. They can’t move away from each other, they
can’t move closer together, and they can’t rotate with respect to each other,
such as a bridge made of sections which hold rigidly together.

You can also use this joint to create a less rigid connection that flexes -
for example, a bridge made of sections which are slightly flexible.

## Comparing Fixed and Relative joints 2D

It is important to know the major differences between **Fixed Joint** A joint
type that is completely constrained, allowing two objects to be held together.
Implemented as a spring so some motion may still occur. [More
info](../../class-FixedJoint.html)  
See in [Glossary](../../Glossary.html#FixedJoint) 2D and **Relative Joint 2D**
A 2D joint that allows two game objects controlled by Rigidbody physics to
maintain in a position based on each other’s location. Use this joint to keep
two objects offset from each other, at a position and angle you decide [More
info](../../2d-physics/joints/relative-joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#RelativeJoint2D):

  * ****Fixed Joint 2D** A 2D joint type which is completely constrained, allowing two objects to be held together. Implemented as a spring so some small motion may still occur. [More info](../../2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#FixedJoint2D)** is a spring-type joint.
**Relative Joint 2D** is a motor-type joint with a maximum force and/or
torque.

  * **Fixed Joint 2D** uses a spring to maintain the relative linear and angular offsets. **Relative Joint 2D** uses a motor. You can configure a joint’s spring or motor.
  * **Fixed Joint 2D** works with anchor points (it’s derived from script **Anchored Joint 2D**); it maintains the relative linear and angular offset between the anchors. **Relative Joint 2D** doesn’t have anchor points (it’s derived directly from script **Joint 2D**).
  * **Fixed Joint 2D** cannot modify the relative linear and angular offsets in real time. **Relative Joint 2D** can.

## Additional resources

  * [Joints 2D](./2d-joints-landing.html)
  * [Fixed Joint 2D component reference](fixed-joint-2d-reference.html)

[](../../2d-physics/joints/fixed-joint-2d-landing.html)

Fixed Joint 2D

[](../../2d-physics/joints/fixed-joint-2d-reference.html)

Fixed Joint 2D component reference

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

