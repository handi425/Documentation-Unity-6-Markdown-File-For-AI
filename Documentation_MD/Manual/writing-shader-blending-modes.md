[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-blending-modes.html)
  * [中文](/cn/current/Manual/writing-shader-blending-modes.html)
  * [日本語](/ja/current/Manual/writing-shader-blending-modes.html)
  * [한국어](/kr/current/Manual/writing-shader-blending-modes.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-blending-modes.html)
  * [中文](/cn/current/Manual/writing-shader-blending-modes.html)
  * [日本語](/ja/current/Manual/writing-shader-blending-modes.html)
  * [한국어](/kr/current/Manual/writing-shader-blending-modes.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Set the blending mode in a shader

[](writing-shader-set-stencil.html)

Check or write to the stencil buffer in a shader

[](writing-shader-color-mask.html)

Set the color channels the GPU renders to

# Set the blending mode in a shader

The `Blend` command determines how the GPU combines the output of the fragment
**shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) with the render target.

The functionality of this command depends on the blending operation, which you
can set using the BlendOp command. Note that while blending itself is
supported on all graphics APIs and hardware, some blending operations have
more limited support.

Enabling blending disables some optimizations on the GPU (mostly hidden
surface removal/Early-Z), which can lead to increased GPU frame times.

## Common blend types

Here is the syntax for the most common blend types:

    
    
    Blend SrcAlpha OneMinusSrcAlpha // Traditional transparency
    Blend One OneMinusSrcAlpha // Premultiplied transparency
    Blend One One // Additive
    Blend OneMinusDstColor One // Soft additive
    Blend DstColor Zero // Multiplicative
    Blend DstColor SrcColor // 2x multiplicative
    

## Examples

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Enable regular alpha blending for this Pass
          Blend SrcAlpha OneMinusSrcAlpha
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

This example code demonstrates the syntax for using this command in a
SubShader block.

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // Enable regular alpha blending for this SubShader
             Blend SrcAlpha OneMinusSrcAlpha
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Blend command in ShaderLab reference](SL-Blend.html)
  * [BlendOp command in ShaderLab reference](SL-BlendOp.html)

[](writing-shader-set-stencil.html)

Check or write to the stencil buffer in a shader

[](writing-shader-color-mask.html)

Set the color channels the GPU renders to

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

