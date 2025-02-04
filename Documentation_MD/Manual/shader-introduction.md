[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-introduction.html)
  * [中文](/cn/current/Manual/shader-introduction.html)
  * [日本語](/ja/current/Manual/shader-introduction.html)
  * [한국어](/kr/current/Manual/shader-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-introduction.html)
  * [中文](/cn/current/Manual/shader-introduction.html)
  * [日本語](/ja/current/Manual/shader-introduction.html)
  * [한국어](/kr/current/Manual/shader-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * Introduction to shaders

[](Shaders.html)

Shaders

[](shader-built-in-landing.html)

Prebuilt shaders

# Introduction to shaders

A **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) program, commonly referred to as a
shader, is a program that runs on a GPU.

## Types of shader

In Unity, shaders are divided into three broad categories. You use each
category for different things, and work with them differently.

  * Shaders that are part of the [graphics pipeline](https://en.wikipedia.org/wiki/Graphics_pipeline) are the most common type of shader. They perform calculations that determine the color of **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) on the screen. In Unity, you usually
work with this type of shader by using [Shader objects](shader-objects.html)An
instance of the Shader class, a Shader object is container for shader programs
and GPU instructions, and information that tells Unity how to use them. Use
them with materials to determine the appearance of your scene. [More
info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject).

  * [Compute shaders](class-ComputeShader.html) perform calculations on the GPU, outside of the regular graphics pipeline.
  * **Ray tracing** The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing  
See in [Glossary](Glossary.html#Raytracing) shaders perform calculations
related to ray tracing.

## Terminology

The terminology around shaders can be confusing; people commonly use the word
“shader” to mean different things.

In this documentation, the terminology is as follows:

  * **shader** or **shader program** \- a program that runs on a GPU. Unless otherwise specified, this means shader programs that are part of the graphics pipeline.
  * **Shader object** \- an instance of the `Shader` class. A Shader object is a wrapper for shader programs and other information.
  * ****ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab)** \- a Unity-specific language for
writing shaders.

  * **Shader Graph** \- a tool for creating shaders without writing code.
  * **shader asset** \- a file with the `.shader` extension in your Unity project. It defines a Shader object.
  * **Shader Graph asset** \- a file in your Unity project. It defines a Shader object.

[](Shaders.html)

Shaders

[](shader-built-in-landing.html)

Prebuilt shaders

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

