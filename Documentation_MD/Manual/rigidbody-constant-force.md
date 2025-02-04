[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/rigidbody-constant-force.html)
  * [中文](/cn/current/Manual/rigidbody-constant-force.html)
  * [日本語](/ja/current/Manual/rigidbody-constant-force.html)
  * [한국어](/kr/current/Manual/rigidbody-constant-force.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/rigidbody-constant-force.html)
  * [中文](/cn/current/Manual/rigidbody-constant-force.html)
  * [日本語](/ja/current/Manual/rigidbody-constant-force.html)
  * [한국어](/kr/current/Manual/rigidbody-constant-force.html)

  * [Physics](PhysicsSection.html)
  * [Built-in 3D Physics](PhysicsOverview.html)
  * [Rigidbody physics](rigidbody-physics-section.html)
  * Apply constant force to a Rigidbody

[](rigidbody-configure-colliders.html)

Configure Rigidbody Colliders

[](rigidbody-interpolation.html)

Apply interpolation to a Rigidbody

# Apply constant force to a Rigidbody

To apply a constant linear or rotational force to a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s **Rigidbody** A component that
allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody), add the **Constant Force** A
simple component for adding a constant force or torque to game objects with a
Rigidbody. [More info](class-ConstantForce.html)  
See in [Glossary](Glossary.html#ConstantForce) component (represented by the
API class [`ConstantForce`](../ScriptReference/ConstantForce.html)) to your
GameObject. See [Constant Force component reference](class-ConstantForce.html)
for details on how to configure the properties on the component.

## Set maximum velocity limitations

Constant force is not the same as constant speed. When you apply a constant
force, the speed of movement accelerates over time based on the value of the
force. In real life, this acceleration continues indefinitely. By default in
Unity’s physics simulation, linear acceleration continues indefinitely, and
angular acceleration continues until the Rigidbody reaches a max velocity of
50 rad/s. You can change these maximum velocities in code, via the properties
[`Rigidbody.maxLinearVelocity`](../ScriptReference/Rigidbody-
maxLinearVelocity.html) and
[`Rigidbody.maxAngularVelocity`](../ScriptReference/Rigidbody-
maxAngularVelocity.html).

## Configure constant forward acceleration

To make a GameObject constantly accelerate forward (for example, to make it
behave like a rocket), do the following:

  1. Add a Constant Force component to the GameObject.
  2. On the Constant Force component, set the **Relative Force** Z axis to a positive value.
  3. On the Rigidbody, disable **Use Gravity**. This ensures that there is no competing gravitational force acting upon the GameObject.
  4. On the Rigidbody component, set the **Drag** property so that the Rigidbody does not exceed your preferred maximum velocity (the higher the drag, the lower the maximum velocity will be). This might require some trial and error to get the effect you want.

[](rigidbody-configure-colliders.html)

Configure Rigidbody Colliders

[](rigidbody-interpolation.html)

Apply interpolation to a Rigidbody

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

