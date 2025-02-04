[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-size.html)
  * [中文](/cn/current/Manual/particle-size.html)
  * [日本語](/ja/current/Manual/particle-size.html)
  * [한국어](/kr/current/Manual/particle-size.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-size.html)
  * [中文](/cn/current/Manual/particle-size.html)
  * [日本語](/ja/current/Manual/particle-size.html)
  * [한국어](/kr/current/Manual/particle-size.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle appearance](particle-appearance.html)
  * Particle size

[](particle-appearance.html)

Particle appearance

[](particle-color.html)

Change particle color

# Particle size

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can change a particle’s size
based on its speed or lifetime.

## Changing particle size based on the particle’s speed

The [Size By Speed Module](PartSysSizeBySpeedModule.html) can create particles
that change size based on their speed in distance units per second.

Some situations will require particles which vary in size depending on their
speed. For example, you would expect small pieces of debris to be accelerated
more by an explosion than larger pieces. You can achieve effects like this
using **Size By Speed** with a simple ramp curve that proportionally increases
the speed as the size of the particle decreases. Note that this should not be
used with the **Limit Velocity Over Lifetime** module, unless you want
particles to change their size as they slow down.

**Speed Range** specifies the range of values that the X (width), Y (height)
and Z (depth) shapes apply to. The Speed Range is only applied when the size
is in one of the curve modes. Fast particles will scale using the values at
the right end of the curve, while slower particles will use values from the
left side of the curve. For example, if you specify a Speed Range between 10
and 100:

  * Speeds below 10 will set the Particle size corresponding with the left-most edge of the curve.
  * Speeds above 100 will set the Particle size corresponding with the right-most edge of the curve.
  * Speeds between 10 and 100 will set the Particle size determined by the point along the curve corresponding to the Speed. In this example, a Speed of 55 would set the size according to the midpoint of the curve.

### Non-uniform particle scaling by speed

![](../uploads/Main/PartSysSizeBySpeed-SepAxes.png)

You can specify how a particle’s width, height and depth size changes by speed
independently. In the **Size by Speed** module, check the **Separate Axes**
checkbox, then choose how the X (width), Y (height) and Z (depth) of the
particle is affected by the speed of the particle. Remember that Z will only
be used for **Mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) particles.

## Changing particle size over the particle’s lifetime

The [Size Over Lifetime](PartSysRotOverLifeModule.html) module can change a
particle’s size based on how long it has existed.

Some particles will typically change in size as they move away from the point
of emission, such as those that represent gases, flames or smoke. For example,
smoke will tend to disperse and occupy a larger volume over time. You can
achieve this by setting the curve for the smoke particle to an upward ramp,
increasing with the particle’s age. You can also further enhance this effect
using the **Color Over Lifetime** module to fade the smoke as it spreads.

For fireballs created by burning fuel, the flame particles will tend to expand
after emission but then fade and shrink as the fuel is used up and the flame
dissipates. In this case, the curve would have a rising “hump” that rises and
then falls back down to a smaller size.

The values specified in the curves are multiplied by the [Start
Size](PartSysMainModule.html) to get the final particle size.

### Non-uniform particle scaling over lifetime

![](../uploads/Main/PartSysSizeOverLife-InspSepAxes.png)

You can specify how a particle’s width, height and depth changes over lifetime
independently. In the **Size over Lifetime** module, check the **Separate
Axes** checkbox, then change the X (width), Y (height) and Z (depth). Remember
that Z will only be used for Mesh particles.

[](particle-appearance.html)

Particle appearance

[](particle-color.html)

Change particle color

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

