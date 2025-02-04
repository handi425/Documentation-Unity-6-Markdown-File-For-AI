[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-set-stencil.html)
  * [中文](/cn/current/Manual/writing-shader-set-stencil.html)
  * [日本語](/ja/current/Manual/writing-shader-set-stencil.html)
  * [한국어](/kr/current/Manual/writing-shader-set-stencil.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-set-stencil.html)
  * [中文](/cn/current/Manual/writing-shader-set-stencil.html)
  * [日本語](/ja/current/Manual/writing-shader-set-stencil.html)
  * [한국어](/kr/current/Manual/writing-shader-set-stencil.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Check or write to the stencil buffer in a shader

[](writing-shader-set-zwrite.html)

Disable writing to the depth buffer in a shader

[](writing-shader-blending-modes.html)

Set the blending mode in a shader

# Check or write to the stencil buffer in a shader

The **stencil buffer** A memory store that holds an 8-bit per-pixel value. In
Unity, you can use a stencil buffer to flag pixels, and then only render to
pixels that pass the stencil operation. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#stencilbuffer) stores an 8-bit integer value
for each **pixel** The smallest unit in a computer image. Pixel size depends
on your screen resolution. Pixel lighting is calculated at every screen pixel.
[More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) in the frame buffer. Before executing
the fragment **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) for a given pixel, the GPU can compare
the current value in the stencil buffer against a given reference value. This
is called a stencil test. If the stencil test passes, the GPU performs the
depth test. If the stencil test fails, the GPU skips the rest of the
processing for that pixel. This means that you can use the stencil buffer as a
mask to tell the GPU which pixels to draw, and which pixels to discard.

You would typically use the stencil buffer for special effects such as portals
or mirrors. Additionally, the stencil buffer is sometimes used when rendering
hard shadows, or [constructive solid geometry
(CSG)](https://en.wikipedia.org/wiki/Constructive_solid_geometry?).

You can use the `Stencil` command to do two different things: to configure the
stencil test, and to configure what the GPU writes to the stencil buffer. You
can do both of these things in the same command, but the most common use case
is to create one **Shader object** An instance of the Shader class, a Shader
object is container for shader programs and GPU instructions, and information
that tells Unity how to use them. Use them with materials to determine the
appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) that masks out areas of the
screen that other Shader objects cannot draw to. To do this, you need to
configure the first Shader object to always pass the stencil test and write to
the stencil buffer, and configure the others to perform a stencil test and not
write to the stencil buffer.

Use the `Ref`, `ReadMask`, and `Comp` parameters to configure the stencil
test. Use the `Ref`, `WriteMask`, `Pass`, `Fail`, and `ZFail` parameters to
configure the stencil write operation.

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

The stencil test equation is:

    
    
    (ref & readMask) comparisonFunction (stencilBufferValue & readMask)
    

## Examples

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                 // All pixels in this Pass will pass the stencil test and write a value of 2 to the stencil buffer
                 // You would typically do this if you wanted to prevent subsequent shaders from drawing to this area of the render target or restrict them to render to this area only
                 Stencil
                 {
                     Ref 2
                     Comp Always
                     Pass Replace
                 }            
    
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
                 // All pixels in this SubShader pass the stencil test only if the current value of the stencil buffer is less than 2
                 // You would typically do this if you wanted to only draw to areas of the render target that were not "masked out"
                 Stencil
                 {
                     Ref 2
                     Comp Less
                 }  
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Stencil command in ShaderLab reference](SL-Stencil.html)

[](writing-shader-set-zwrite.html)

Disable writing to the depth buffer in a shader

[](writing-shader-blending-modes.html)

Set the blending mode in a shader

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

