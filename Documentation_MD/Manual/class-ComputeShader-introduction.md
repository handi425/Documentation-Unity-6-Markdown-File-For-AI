[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ComputeShader-introduction.html)
  * [中文](/cn/current/Manual/class-ComputeShader-introduction.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-introduction.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-introduction.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ComputeShader-introduction.html)
  * [中文](/cn/current/Manual/class-ComputeShader-introduction.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-introduction.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-introduction.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Compute shaders](class-ComputeShader.html)
  * Introduction to compute shaders

[](class-ComputeShader.html)

Compute shaders

[](class-ComputeShader-create.html)

Create a compute shader

# Introduction to compute shaders

Compute shaders are **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs that run on the GPU, outside
of the normal rendering pipeline.

They can be used for massively parallel GPGPU algorithms, or to accelerate
parts of game rendering. In order to efficiently use them, an in-depth
knowledge of GPU architectures and parallel algorithms is often needed; as
well as knowledge of [DirectCompute](http://msdn.microsoft.com/en-
us/library/windows/desktop/ff476331.aspx), [OpenGL
Compute](https://www.khronos.org/opengl/wiki/Compute_Shader),
[CUDA](http://en.wikipedia.org/wiki/CUDA), or
[OpenCL](http://en.wikipedia.org/wiki/OpenCL).

Compute shaders in Unity closely match [
DirectX](https://en.wikipedia.org/wiki/DirectX) 11 DirectCompute technology.
Platforms where compute shaders work:

  * Windows and Windows Store, with a DirectX 11 or DirectX 12 graphics API and Shader Model 5.0 GPU

  * macOS and iOS using [Metal graphics](https://developer.apple.com/metal/) API

  * Android, Linux and Windows platforms with [Vulkan](https://www.khronos.org/vulkan/) API

  * Modern [OpenGL](https://www.opengl.org/) platforms (OpenGL 4.3 on Linux or Windows; OpenGL ES 3.1 on Android). Note that Mac OS X does not support OpenGL 4.3

  * Modern consoles

## Cross-platform support

As with regular shaders, Unity is capable of [translating](shader-
compilation.html) compute shaders from HLSL to other shader languages.
Therefore, for the easiest cross-platform builds, you should write compute
shaders in HLSL. However, there are some factors that need to be considered
when doing this.

[](class-ComputeShader.html)

Compute shaders

[](class-ComputeShader-create.html)

Create a compute shader

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

