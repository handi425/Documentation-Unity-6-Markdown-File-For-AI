[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-lights-trails.html)
  * [中文](/cn/current/Manual/particle-lights-trails.html)
  * [日本語](/ja/current/Manual/particle-lights-trails.html)
  * [한국어](/kr/current/Manual/particle-lights-trails.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-lights-trails.html)
  * [中文](/cn/current/Manual/particle-lights-trails.html)
  * [日本語](/ja/current/Manual/particle-lights-trails.html)
  * [한국어](/kr/current/Manual/particle-lights-trails.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle appearance](particle-appearance.html)
  * Particle lights and trails

[](particle-color.html)

Change particle color

[](particle-rendering-shading.html)

Particle rendering and shading

# Particle lights and trails

Understand how the **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can render lights and trails
on particle effects.

## Lights

The [Lights](PartSysLightsModule.html) module is a fast way to add real-time
lighting to your particle effects. It can be used to make systems cast light
onto their surroundings, for example for a fire, fireworks or lightning. It
also allows you to have the lights inherit a variety of properties from the
particles they are attached to. This can make it more believable that the
particle effect itself is emitting light. For example, this can be achieved by
making the lights fade out with their particles and having them share the same
colors.

This module makes it easy to create a lot of real-time lights very quickly,
and real-time lights have a high performance cost, especially in **Forward
Rendering** A rendering path that renders each object in one or more passes,
depending on lights that affect the object. Lights themselves are also treated
differently by Forward Rendering, depending on their settings and intensity.
[More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) mode. If the lights also
cast shadows, the performance cost is even higher. To help guard against an
accidental tweak to the emission rate and thus causing thousands of real-time
lights to be created, the Maximum Lights property should be used. Creating
more lights than your target hardware is able to manage can cause slowdowns
and unresponsiveness.

## Trails

The [Trails](PartSysTrailsModule.html) module adds trails to a percentage of
your particles. This module shares a number of properties with the [Trail
Renderer](class-TrailRenderer.html)A visual effect that lets you to make
trails behind GameObjects in the Scene as they move. [More info](class-
TrailRenderer.html)  
See in [Glossary](Glossary.html#TrailRenderer) component, but offers the
ability to easily attach Trails to particles, and to inherit various
properties from the particles. Trails can be useful for a variety of effects,
such as bullets, smoke, and magic visuals.

![The Trails module in Particles
mode](../uploads/Main/PartSysTrailsModule.png) The Trails module in Particles
mode ![The Trails module in Ribbon
mode](../uploads/Main/PartSysTrailsModuleRibbon.png) The Trails module in
Ribbon mode

### Tips

  * Use the [Renderer](PartSysRendererModule.html) module to specify the Trail Material.
  * Unity samples colors from the Color Gradient at each vertex, and linearly interpolates colors between each vertex,. Add more vertices to your **Line Renderer** A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer) to get a closer approximation of
a detailed Color Gradient.

[](particle-color.html)

Change particle color

[](particle-rendering-shading.html)

Particle rendering and shading

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

