[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-include-directives.html)
  * [中文](/cn/current/Manual/shader-include-directives.html)
  * [日本語](/ja/current/Manual/shader-include-directives.html)
  * [한국어](/kr/current/Manual/shader-include-directives.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-include-directives.html)
  * [中文](/cn/current/Manual/shader-include-directives.html)
  * [日本語](/ja/current/Manual/shader-include-directives.html)
  * [한국어](/kr/current/Manual/shader-include-directives.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * Include another HLSL file in a shader

[](SL-SamplerStates.html)

Texture samplers

[](writing-shader-programs-pragma-directives.html)

Pass information to the shader compiler in HLSL

# Include another HLSL file in a shader

In HLSL, `#include` directives are a type of [preprocessor directive](writing-
shader-programs-pragma-directives.html). They instruct the compiler to include
the contents of one HLSL file inside another. The file that they include is
called an **include file**.

In Unity, regular `#include` directives work the same as in standard HLSL. For
more information on regular `#include` directives, see the HLSL documentation:
[include Directive](https://docs.microsoft.com/en-
us/windows/win32/direct3dhlsl/dx-graphics-hlsl-appendix-pre-include).

Unity also provides an additional, Unity-specific `#include_with_pragmas`
directive. The `#include_with_pragmas` directive works the same as a regular
`#include` directive, but it also allows you to use `#pragma` directives in
the include file. This means that the `#include_with_pragmas` directive allows
you to share `#pragma` directives between multiple files.

## Using the include_with_pragmas directive

**Note:** To use `#include_with_pragmas` directives, you must enable the
[Caching Shader Preprocessor](shader-compilation.html#preprocessor).

This example demonstrates how to use the Unity-specific
`#include_with_pragmas` directive to enable a common workflow improvement: the
ability to toggle **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) debugging on and off for multiple
shaders, without needing to edit every shader source file every time.

The following line demonstrates the contents of the include file. It contains
a single pragma directive that enables shader debugging:

    
    
    // Comment out the following line to disable shader debugging
    #pragma enable_d3d11_debug_symbols
    

In each shader that you want to debug, add an `#include_with_pragmas`
directive that points to the include file. Put the directive near the other
`#pragma` directives, like this:

    
    
    // Example pragma directives
    #pragma target 4.0
    #pragma vertex vert
    #pragma fragment frag
    
    // Replace path-to-include-file with the path to the include file 
    #include_with_pragmas "path-to-include-file"
    
    // The rest of the HLSL code goes here
    

Now, when you want to toggle shader debugging on and off for all shaders that
use the include file, you only need to change a single line in the include
file. When Unity recompiles the shaders, it includes the amended line.

**Note:** If a shader file uses `#include` to import a file that contains an
`#include_with_pragmas` directive, Unity ignores the `#pragma` directives in
the file the `#include_with_pragmas` directive references.

[](SL-SamplerStates.html)

Texture samplers

[](writing-shader-programs-pragma-directives.html)

Pass information to the shader compiler in HLSL

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

