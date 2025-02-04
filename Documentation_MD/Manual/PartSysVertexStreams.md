[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/PartSysVertexStreams.html)
  * [中文](/cn/current/Manual/PartSysVertexStreams.html)
  * [日本語](/ja/current/Manual/PartSysVertexStreams.html)
  * [한국어](/kr/current/Manual/PartSysVertexStreams.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/PartSysVertexStreams.html)
  * [中文](/cn/current/Manual/PartSysVertexStreams.html)
  * [日本語](/ja/current/Manual/PartSysVertexStreams.html)
  * [한국어](/kr/current/Manual/PartSysVertexStreams.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Custom data streams in Particle Systems](custom-data-streams-particle-systems.html)
  * Particle System custom vertex streams

[](custom-data-streams-particle-systems.html)

Custom data streams in Particle Systems

[](example-particle-system-custom-vertex-streams-standard-shaders.html)

Example of Particle System Standard Shader custom vertex streams

# Particle System custom vertex streams

If you are comfortable writing your own **Shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader), you can use the [Renderer
Module](../ScriptReference/ParticleSystemRenderer.html)’s **Custom Vertex
Streams** feature to configure your **Particle Systems** A component that
simulates fluid entities such as liquids, clouds and flames by generating and
animating large numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) to pass a wider range of data
into your custom Shaders.

There are a number of built-in [data
streams](../ScriptReference/ParticleSystemVertexStream.html) to choose from,
such as velocity, size and center position. Aside from the ability to create
powerful custom Shaders, these streams allow a number of more general
benefits:

  * Use the [Tangent](../ScriptReference/ParticleSystemVertexStream.Tangent.html) stream to support normal mapped particles.
  * You can remove Color and then add the Tangent [UV2](../ScriptReference/ParticleSystemVertexStream.UV2.html) and [AnimBlend](../ScriptReference/ParticleSystemVertexStream.AnimBlend.html) streams to use the Standard Shader on particles.
  * To easily perform linear texture blending of flipbooks, add the UV2 and AnimBlend streams, and attach the Particles/Anim Alpha Blended Shader (see example screenshot below to see how to set this up).

There are also two completely custom per-particle data streams
([ParticleSystemVertexStreams.Custom1](../ScriptReference/ParticleSystemVertexStreams.Custom1.html)
and
[ParticleSystemVertexStreams.Custom2](../ScriptReference/ParticleSystemVertexStreams.Custom2.html)),
which can be populated from script. Call
[SetCustomParticleData](../ScriptReference/ParticleSystem.SetCustomParticleData.html)
and
[GetCustomParticleData](../ScriptReference/ParticleSystem.GetCustomParticleData.html)
with your array of data to use them. There are two ways of using this:

  * To drive custom behavior in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) by attaching your own data to
particles; for example, attaching a “health” value to each particle.

  * To pass this data into a Shader by adding one of the two custom streams, in the same way you would send any other stream to your Shader (see [ParticleSystemRenderer.EnableVertexStreams](../ScriptReference/ParticleSystemRenderer.EnableVertexStreams.html)). To elaborate on the first example, maybe your custom health attribute could now also drive some kind of visual effect, as well as driving script-based game logic.

When adding vertex streams, Unity will provide you with some information in
brackets, next to each item, to help you read the correct data in your shader:

![](../uploads/Main/PartSysVertexStreams-VertexShaders.png)

Each item in brackets corresponds to a **Vertex Shader** A program that runs
on each vertex of a 3D model when the model is being rendered. [More
info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader) input, which you should specify
in your Shader. Here is the correct input structure for this configuration.

    
    
                struct appdata_t {
                    float4 vertex : POSITION;
                    float3 normal : NORMAL;
                    fixed4 color : COLOR;
                    float4 texcoords : TEXCOORD0;
                    float texcoordBlend : TEXCOORD1;
                };
    

Notice that both UV and UV2 are passed in different parts of TEXCOORD0, so we
use a single declaration for both. To access each one in your shader, you
would use the xy and zw swizzles. This allows you to pack your vertex data
efficiently.

## Additional resources

  * [Example of Particle System Standard Shader custom vertex streams](example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [Example of Particle System Surface Shader custom vertex streams](example-particle-system-custom-vertex-streams-surface-shaders.html)

[](custom-data-streams-particle-systems.html)

Custom data streams in Particle Systems

[](example-particle-system-custom-vertex-streams-standard-shaders.html)

Example of Particle System Standard Shader custom vertex streams

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

