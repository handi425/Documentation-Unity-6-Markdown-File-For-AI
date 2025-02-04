[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/target-joint-2d-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [中文](/cn/current/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [日本語](/ja/current/Manual/2d-physics/joints/target-joint-2d-reference.html)
  * [한국어](/kr/current/Manual/2d-physics/joints/target-joint-2d-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [2D Physics](../../2d-physics/2d-physics.html)
  * [2D joints](../../2d-physics/joints/2d-joints-landing.html)
  * [Target Joint 2D](../../2d-physics/joints/target-joint-2d-landing.html)
  * Target Joint 2D

[](../../2d-physics/joints/target-joint-2d-fundamentals.html)

Target Joint 2D fundamentals

[](../../2d-physics/joints/wheel-joint-2d-landing.html)

Wheel Joint 2D

# Target Joint 2D

This **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](../../Joints.html)  
See in [Glossary](../../Glossary.html#joint) connects to a specified target,
rather than another **Rigidbody** A component that allows a GameObject to be
affected by simulated gravity and other forces. [More info](../../class-
Rigidbody.html)  
See in [Glossary](../../Glossary.html#Rigidbody) object as other joints do.
This behaves in a similar way to a spring type joint.

## Properties

**Property** | **Function**  
---|---  
**Anchor** | Define where (in terms of x, y-coordinates on the **Rigidbody 2D**) the end point of the joint connects to this **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject).  
**Target** | Define where (in terms of x, y-coordinates in world space) the other end of the joint attempts to move.  
**Auto Configure Target** | Enable this property to automatically set the other end of the joint to the current position of the GameObject. **Note:** When this option is enabled, the target changes as you move the GameObject but the target will not change if the option is not enabled.  
**Max Force** | Set the force that the joint can apply when attempting to move the object to the **target position** A joint property to set the target position that the joint’s drive force should move it to. [More info](../../class-ConfigurableJoint.html)  
See in [Glossary](../../Glossary.html#TargetPosition). The higher the value,
the higher the maximum force.  
****Damping Ratio** A joint setting to control spring oscillation. A higher
damping ratio means the spring will come to rest faster. [More
info](../../2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](../../Glossary.html#DampingRatio)** | Set the degree to suppress spring oscillation. In the range 0 to 1, the higher the value, the less movement.  
**Frequency** | Set the frequency at which the spring oscillates while the GameObjects are approaching the separation distance you want (measured in cycles per second). In the range 0 to 1,000,000 - the higher the value, the stiffer the spring. **Note:** Setting **Frequency** to zero will create the stiffest spring type joint possible.  
**Break Action** | Set the action taken when either the force or torque threshold is exceeded.  
**Break Force** | Set the force threshold which if exceeded, will cause the joint to perform the selected **Break Action**. The default value is set to **Infinity** , which can never be exceeded and therefore the **Break Action** can never be taken while the threshold remains at this value.  
  
[](../../2d-physics/joints/target-joint-2d-fundamentals.html)

Target Joint 2D fundamentals

[](../../2d-physics/joints/wheel-joint-2d-landing.html)

Wheel Joint 2D

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

