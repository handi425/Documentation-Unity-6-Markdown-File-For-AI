[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ShaderCompilationAPIs.html)
  * [中文](/cn/current/Manual/SL-ShaderCompilationAPIs.html)
  * [日本語](/ja/current/Manual/SL-ShaderCompilationAPIs.html)
  * [한국어](/kr/current/Manual/SL-ShaderCompilationAPIs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ShaderCompilationAPIs.html)
  * [中文](/cn/current/Manual/SL-ShaderCompilationAPIs.html)
  * [日本語](/ja/current/Manual/SL-ShaderCompilationAPIs.html)
  * [한국어](/kr/current/Manual/SL-ShaderCompilationAPIs.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Set a shader to require a graphics API or platform

[](writing-shader-tags-pipeline.html)

Set a shader to require URP or HDRP

[](SL-ShaderCompileTargets.html)

Set a shader to require a shader model or GPU feature

# Set a shader to require a graphics API or platform

Some [`#pragma` directives](SL-PragmaDirectives.html) take parameters that
allow you to target specific graphics APIs and platforms. This page contains
information on using those directives, and provides a list of valid parameter
values.

## Including or excluding graphics APIs

By default, Unity compiles all **shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs for each graphics API in the
list for the current build target. Sometimes, you might want to compile
certain shader programs only for certain graphics APIs; for example, if you
use features that are not supported on all platforms.

To compile a shader program only for given APIs, use the `#pragma
only_renderers` directive. You can pass multiple values, space delimited.

This example demonstrates how to compile shaders only for Metal and Vulkan:

    
    
    #pragma only_renderers metal vulkan
    

To exclude shader code from compilation by given compilers, use the `#pragma
exclude_renderers` directive. You can pass multiple values, space delimited.

This example demonstrates how to exclude a shader from compilation for Metal
and Vulkan:

    
    
    #pragma exclude_renderers metal vulkan
    

## Generating shader variants for graphics tiers for a given graphics API

In the Built-in **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), Unity automatically generates
[shader variants](shader-variants.html)A verion of a shader program that Unity
generates according to a specific combination of shader keywords and their
status. A Shader object can contain multiple shader variants. [More
info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant) that correspond to [graphics
tiers](graphics-tiers.html) under certain conditions. You can also force Unity
to generate these variants, if required.

To do this, use the `#pragma hardware_tier_variants` preprocessor directive
and specify the graphics APIs for which you want to generate tier shader
variants.

For example, this instructs Unity to compile tier shader variants for Metal:

    
    
    #pragma hardware_tier_variants metal
    

## List of valid parameter values

Supported values are:

**Value** | **Description**  
---|---  
`d3d11` | DirectX 11 feature level 10 and above, DirectX 12  
`glcore` | OpenGL 3.x, OpenGL 4.x  
`gles3` | OpenGL ES 3.x, **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) 2.0  
`metal` | Metal on iOS or Mac  
`ps4` | PlayStation®4  
`ps5` | PlayStation®5  
`switch` | Nintendo Switch™  
`vulkan` | Vulkan  
`xboxseries` | Xbox Series S|X  
  
## Additional resources

  * [HLSL pragma directives reference](SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](SL-Pragma-target.html)
  * [HLSL pragma require command reference](SL-Pragma-require.html)
  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](SL-PassTags.html)

[](writing-shader-tags-pipeline.html)

Set a shader to require URP or HDRP

[](SL-ShaderCompileTargets.html)

Set a shader to require a shader model or GPU feature

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

