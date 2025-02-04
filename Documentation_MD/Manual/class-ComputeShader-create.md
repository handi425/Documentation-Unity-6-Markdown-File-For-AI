[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ComputeShader-create.html)
  * [中文](/cn/current/Manual/class-ComputeShader-create.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-create.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-create.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ComputeShader-create.html)
  * [中文](/cn/current/Manual/class-ComputeShader-create.html)
  * [日本語](/ja/current/Manual/class-ComputeShader-create.html)
  * [한국어](/kr/current/Manual/class-ComputeShader-create.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Compute shaders](class-ComputeShader.html)
  * Create a compute shader

[](class-ComputeShader-introduction.html)

Introduction to compute shaders

[](class-ComputeShader-hlsl-shaderlab.html)

Use HLSL and ShaderLab in a compute shader

# Create a compute shader

Similar to [shader assets](class-Shader.html), compute **shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) assets are files in your project. with
a _.compute_ file extension. They are written in DirectX 11 style
[HLSL](http://msdn.microsoft.com/en-us/library/windows/desktop/bb509561.aspx)
language, with a minimal number of #pragma compilation directives to indicate
which functions to compile as compute shader kernels.

## Check if a platform supports compute shaders

Compute shader support can be queried at runtime using
[SystemInfo.supportsComputeShaders](../ScriptReference/SystemInfo-
supportsComputeShaders.html).

## Create a compute shader asset

Here’s a basic example of a compute shader file, which fills the output
texture with red:

    
    
    // test.compute
    
    #pragma kernel FillWithRed
    
    RWTexture2D<float4> res;
    
    [numthreads(1,1,1)]
    void FillWithRed (uint3 dtid : SV_DispatchThreadID)
    {
        res[dtid.xy] = float4(1,0,0,1);
    }
    

The language is standard DX11 HLSL, with an additional `#pragma kernel
FillWithRed` directive. One compute shader Asset file must contain at least
one`compute kernel` that can be invoked, and that function is indicated by the
`#pragma directive`. There can be more kernels in the file; just add multiple
`#pragma kernel` lines.

When using multiple `#pragma kernel` lines, note that comments of the style
`// text` are not permitted on the same line as the `#pragma kernel`
directives, and cause compilation errors if used.

The `#pragma kernel` line can optionally be followed by a number of
preprocessor macros to define while compiling that kernel, for example:

    
    
    #pragma kernel KernelOne SOME_DEFINE DEFINE_WITH_VALUE=1337
    #pragma kernel KernelTwo OTHER_DEFINE
    // ...
    

[](class-ComputeShader-introduction.html)

Introduction to compute shaders

[](class-ComputeShader-hlsl-shaderlab.html)

Use HLSL and ShaderLab in a compute shader

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

