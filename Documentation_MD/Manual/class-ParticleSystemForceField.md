[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ParticleSystemForceField.html)
  * [中文](/cn/current/Manual/class-ParticleSystemForceField.html)
  * [日本語](/ja/current/Manual/class-ParticleSystemForceField.html)
  * [한국어](/kr/current/Manual/class-ParticleSystemForceField.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ParticleSystemForceField.html)
  * [中文](/cn/current/Manual/class-ParticleSystemForceField.html)
  * [日本語](/ja/current/Manual/class-ParticleSystemForceField.html)
  * [한국어](/kr/current/Manual/class-ParticleSystemForceField.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle physics](particle-physics.html)
  * Particle System Force Field component reference

[](configure-particle-trigger.html)

Configure a particle trigger

[](access-particle-system-from-animation.html)

Access the Particle System from the Animation system

# Particle System Force Field component reference

[Switch to Scripting](../ScriptReference/ParticleSystemForceField.html "Go to
ParticleSystemForceField page in the Scripting Reference")

The **Particle System Force Field** component applies forces to particles in
[Particle Systems](class-ParticleSystem.html)A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem).

![](../uploads/Main/PartSysForceFieldInsp.png) **_Property_** | **_Function_**  
---|---  
**Shape**  
| Shape | Select the shape of the area of influence.  
| Start Range | Set the value for the inner point within the shape where the area of influence begins.  
| End Range | Set the value for the outer point of the shape where the area of influence ends.  
| Direction X, Y and Z | Set a linear force to apply to particles along the x-axis, y-axis and z-axis. The higher the value, the greater the force. You can specify a **constant force** A simple component for adding a constant force or torque to game objects with a Rigidbody. [More info](class-ConstantForce.html)  
See in [Glossary](Glossary.html#ConstantForce) or vary the force over time.
See [Varying properties over time](varying-particle-system-properties-over-
time.html) documentation for more information.  
**Gravity**  
| Strength | Set the amount of attraction that particles have towards the focal point within the shape. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more informtion, see [Varying properties over time](varying-particle-system-properties-over-time.html) documentation.  
| Gravity Focus | Set the focal point for gravity to pull particles towards. A value of 0 attracts particles to the center of the shape, and a value of 1 attracts particles to the outer edge of the shape.  
**Rotation**  
| Speed | Set the speed for the Particle System to propel particles around the vortex, which is the center of the force field. The higher the value, the faster the speed. You can specify a constant speed or vary the speed over time. For more information, see the [Varying properties over time](varying-particle-system-properties-over-time.html) documentation.  
| Attraction | Set the strength that particles are dragged into the vortex motion. A value of 1 applies the maximum attraction, and a value of 0 applies no attraction. You can specify a constant attraction or vary the attraction over time. For more information, see the [Varying properties over time](varying-particle-system-properties-over-time.html) documentation.  
| Rotation Randomness | Set a random axes of the shape to propel particles around. A value of 1 applies maximum randomness, and a value of 0 applies no randomness.  
**Drag**  
| Strength | Set the strength of the drag effect which slows particles down. The higher the value, the greater the strength. You can specify a constant strength or vary the strength over time. For more information, see the [Varying properties over time](varying-particle-system-properties-over-time.html) documentation.  
| Multiply Drag by Size | Enable this checkbox to adjust the drag based on the size of the particles.  
| Multiply Drag by Velocity | Enable this checkbox to adjust the drag based on the velocity of the particles.  
**Vector Field** A 3D texture, where each value represents a directional force
that is applied to particles as they move through the field. A vector field is
created in 3D animation software, such as Houdini. [More
info](https://en.wikipedia.org/wiki/Vector_field)  
See in [Glossary](Glossary.html#vectorfield)  
| Volume Texture | Select the texture of the vector field.  
| Speed | Set the speed of the multiplier to apply to particles traveling through the vector field. The higher the value, the faster the speed. You can specify a constant strength or vary the strength over time. See [Varying properties over time](varying-particle-system-properties-over-time.html).  
| Attraction | Set the strength at which Unity drags particles into the vector field motion. The higher the value, the greater the attraction. You can specify a constant attraction or vary the attraction over time. See [Varying properties over time](varying-particle-system-properties-over-time.html).  
  
ParticleSystemForceField

[](configure-particle-trigger.html)

Configure a particle trigger

[](access-particle-system-from-animation.html)

Access the Particle System from the Animation system

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

