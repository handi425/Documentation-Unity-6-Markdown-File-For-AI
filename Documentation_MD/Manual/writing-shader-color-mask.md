[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-color-mask.html)
  * [中文](/cn/current/Manual/writing-shader-color-mask.html)
  * [日本語](/ja/current/Manual/writing-shader-color-mask.html)
  * [한국어](/kr/current/Manual/writing-shader-color-mask.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-color-mask.html)
  * [中文](/cn/current/Manual/writing-shader-color-mask.html)
  * [日本語](/ja/current/Manual/writing-shader-color-mask.html)
  * [한국어](/kr/current/Manual/writing-shader-color-mask.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Set the color channels the GPU renders to

[](writing-shader-blending-modes.html)

Set the blending mode in a shader

[](writing-shader-alpha-to-mask.html)

Reduce aliasing with AlphaToMask mode

# Set the color channels the GPU renders to

By default, the GPU writes to all channels (RGBA). For some effects you might
want to leave certain channels unmodified; for example, you can disable color
rendering to render uncolored shadows. Another common use case is to disable
color writes completely so that you can populate one buffer with data without
writing to others; for example, you might want to populate the **stencil
buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can
use a stencil buffer to flag pixels, and then only render to pixels that pass
the stencil operation. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#stencilbuffer) without writing to the render
target.

## Examples

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Enable writing only to the RGB channels for this Pass, which disables writing to the alpha channel
                  ColorMask RGB
    
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
             // Enable writing only to the RGB channels for this SubShader, which disables writing to the alpha channel
             ColorMask RGB
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [ColorMask command in ShaderLab reference](SL-ColorMask.html)

[](writing-shader-blending-modes.html)

Set the blending mode in a shader

[](writing-shader-alpha-to-mask.html)

Reduce aliasing with AlphaToMask mode

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

