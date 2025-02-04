[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-StandardParticleShadersCreate.html)
  * [中文](/cn/current/Manual/shader-StandardParticleShadersCreate.html)
  * [日本語](/ja/current/Manual/shader-StandardParticleShadersCreate.html)
  * [한국어](/kr/current/Manual/shader-StandardParticleShadersCreate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-StandardParticleShadersCreate.html)
  * [中文](/cn/current/Manual/shader-StandardParticleShadersCreate.html)
  * [日本語](/ja/current/Manual/shader-StandardParticleShadersCreate.html)
  * [한국어](/kr/current/Manual/shader-StandardParticleShadersCreate.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
  * [Particle shaders in the Built-In Render Pipeline](shader-StandardParticleShadersLanding.html)
  * Create a particle material in the Built-In Render Pipeline

[](shader-StandardParticleShadersLanding.html)

Particle shaders in the Built-In Render Pipeline

[](shader-StandardParticleShaders.html)

Standard Particle Shaders Material Inspector window reference for the Built-In
Render Pipeline

# Create a particle material in the Built-In Render Pipeline

The Unity Standard Particle Shaders are built-in shaders that enable you to
render a variety of **Particle System** A component that simulates fluid
entities such as liquids, clouds and flames by generating and animating large
numbers of small 2D images in the scene. [More info](class-
ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) effects. These shaders provide
various particle-specific features that aren’t available with the Standard
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).

To use a Particle Shader:

  1. Select the Material you want to apply the shader to. For example, you could apply a Flame Material to a Fire Particle System effect.

  2. In the Material’s **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector), select **Shader Particles**.

  3. Choose the Particle Shader that you want to use, such as **Standard Surface**.

  4. Enable and disable the various Particle Shader properties in the Inspector.

## Types of particle shader

Unity has the following types of particle shader:

  * Standard Particles **Surface Shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) \- This comes with
functionality similar to the Standard Shader, but works especially well with
particles. Like the Standard Shader, it supports **Physically Based Shading**
An advanced lighting model that simulates the interactions between materials
and light in a way that mimics reality. [More info](shader-
StandardShader.html)  
See in [Glossary](Glossary.html#PhysicallyBasedShading). It does not include
features that are unsuitable for dynamic particles, such as lightmapping.

  * Standard Particles Unlit Shader - This simple shader is faster than the Surface Shader. It supports all of the generic particle controls, such as flipbook blending and distortion, but does not perform any lighting calculations.

![An example of billboard particles using the Standard Particle Surface Shader
with a normal map](../uploads/Main/SPSSBillboardParticles.png) An example of
billboard particles using the Standard Particle Surface Shader with a normal
map

[](shader-StandardParticleShadersLanding.html)

Particle shaders in the Built-In Render Pipeline

[](shader-StandardParticleShaders.html)

Standard Particle Shaders Material Inspector window reference for the Built-In
Render Pipeline

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

