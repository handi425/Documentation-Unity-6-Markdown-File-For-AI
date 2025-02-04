[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/define-custom-data-formats-particles.html)
  * [中文](/cn/current/Manual/define-custom-data-formats-particles.html)
  * [日本語](/ja/current/Manual/define-custom-data-formats-particles.html)
  * [한국어](/kr/current/Manual/define-custom-data-formats-particles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/define-custom-data-formats-particles.html)
  * [中文](/cn/current/Manual/define-custom-data-formats-particles.html)
  * [日本語](/ja/current/Manual/define-custom-data-formats-particles.html)
  * [한국어](/kr/current/Manual/define-custom-data-formats-particles.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Custom data streams in Particle Systems](custom-data-streams-particle-systems.html)
  * Define custom data formats for particles

[](example-particle-system-custom-vertex-streams-surface-shaders.html)

Example of Particle System Surface Shader custom vertex streams

[](particle-system-optimization.html)

Particle System optimization

# Define custom data formats for particles

The [Custom Data](PartSysCustomDataModule.html) module allows you to define
custom data formats in the Editor to be attached to particles. You can also
set this in a script. See documentation on [Particle System vertex
streams](PartSysVertexStreams.html) for more information on how to set custom
data from a script and feed that data into your **shaders** A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

Data can be in the form of a **Vector** , with up to 4
[MinMaxCurve](../ScriptReference/ParticleSystem.MinMaxCurve.html) components,
or a **Color** , which is an HDR-enabled
[MinMaxGradient](../ScriptReference/ParticleSystem.MinMaxGradient.html). Use
this data to drive custom logic in your **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and Shaders.

The default labels for each curve/gradient can be customized by clicking on
them and typing in a contextual name. When passing custom data to shaders, it
is useful to know how that data is used inside the shader. For example, a
curve may be used for custom alpha testing, or a gradient may be used to add a
secondary color to particles. By editing the labels, it is simple to keep a
record in the **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) of the purpose of each custom data entry.

[](example-particle-system-custom-vertex-streams-surface-shaders.html)

Example of Particle System Surface Shader custom vertex streams

[](particle-system-optimization.html)

Particle System optimization

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

