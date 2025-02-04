[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/particle-movement-patterns.html)
  * [中文](/cn/current/Manual/particle-movement-patterns.html)
  * [日本語](/ja/current/Manual/particle-movement-patterns.html)
  * [한국어](/kr/current/Manual/particle-movement-patterns.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/particle-movement-patterns.html)
  * [中文](/cn/current/Manual/particle-movement-patterns.html)
  * [日本語](/ja/current/Manual/particle-movement-patterns.html)
  * [한국어](/kr/current/Manual/particle-movement-patterns.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Configuring particles](configuring-particles.html)
  * [Particle movement](particle-movement.html)
  * Particle movement patterns

[](particle-movement.html)

Particle movement

[](particle-velocity.html)

Particle velocity

# Particle movement patterns

Use the [Noise](PartSysNoiseModule.html) module to add turbulence to particle
movement.

Adding noise to your particles is a simple and effective way to create
interesting patterns and effects. For example, imagine how embers from a fire
move around, or how smoke swirls as it moves. Strong, high frequency noise
could be used to simulate the fire embers, while soft, low frequency noise
would be better suited to modeling a smoke effect.

For maximum control over the noise, you can enable the Separate Axes option.
This allows you to control the strength and remapping on each axis
independently.

The noise algorithm used is based on a technique called Curl Noise, which
internally uses multiple samples of Perlin Noise to create the final noise
field.

The settings on the [Quality](class-QualitySettings.html) window control how
many unique noise samples are generated. When using Medium and Low, less
samples of Perlin Noise are used, and those samples are re-used across
multiple axes but combined in a way to try and hide the re-use. This means
that the noise may look less dynamic and diverse when using lower quality
settings. However, there is a significant performance benefit when using lower
quality settings.

[](particle-movement.html)

Particle movement

[](particle-velocity.html)

Particle velocity

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

