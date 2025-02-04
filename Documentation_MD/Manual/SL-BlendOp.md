[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-BlendOp.html)
  * [中文](/cn/current/Manual/SL-BlendOp.html)
  * [日本語](/ja/current/Manual/SL-BlendOp.html)
  * [한국어](/kr/current/Manual/SL-BlendOp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-BlendOp.html)
  * [中文](/cn/current/Manual/SL-BlendOp.html)
  * [日本語](/ja/current/Manual/SL-BlendOp.html)
  * [한국어](/kr/current/Manual/SL-BlendOp.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * BlendOp command in ShaderLab reference

[](SL-Blend.html)

Blend command in ShaderLab reference

[](SL-ColorMask.html)

ColorMask command in ShaderLab reference

# BlendOp command in ShaderLab reference

Specifies the blending operation used by the Blend command. For this command
to have any effect, there must also be a Blend command in the same Pass block
(if this command is in a Pass block) or SubShader block (if this command is in
a SubShader block).

Not all blending operations are supported on all devices, and support depends
on both the graphics API and the hardware. Different graphics APIs handle
unsupported blending operations differently: GL skips unsupported operations,
and Vulkan and Metal fall back to Add operations.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**BlendOp** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
`BlendOp <operation>` | `BlendOp Sub` | Sets the blending operation used by the Blend command.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**operation** | `Add` | Add source and destination together.  
| `Sub` | Subtract destination from source.  
| `RevSub` | Subtract source from destination.  
| `Min` | Use the smaller of source and destination.  
| `Max` | Use the larger of source and destination.  
| `LogicalClear` | Logical operation: `Clear (0)` (1)  
| `LogicalSet` | Logical operation: `Set (1)` (1)  
| `LogicalCopy` | Logical operation: `Copy (s)` (1)  
| `LogicalCopyInverted` | Logical operation: `Copy inverted (!s)` 2  
| `LogicalNoop` | Logical operation: `Noop (d)` (1)  
| `LogicalInvert` | Logical operation: `Invert (!d)` (1)  
| `LogicalAnd` | Logical operation: `And (s & d)` (1)  
| `LogicalNand` | Logical operation: `Nand !(s & d)` (1)  
| `LogicalOr` | Logical operation: `Or (s | d)` (1)  
| `LogicalNor` | Logical operation: `Nor !(s | d)` (1)  
| `LogicalXor` | Logical operation: `Xor (s ^ d)` (1)  
| `LogicalEquiv` | Logical operation: `Equivalence !(s ^ d)` (1)  
| `LogicalAndReverse` | Logical operation: `Reverse And (s & !d)` (1)  
| `LogicalAndInverted` | Logical operation: `Inverted And (!s & d)` (1)  
| `LogicalOrReverse` | Logical operation: `Reverse Or (s | !d)` (1)  
| `LogicalOrInverted` | Logical operation: `Inverted Or (!s | d)` (1)  
| `Multiply` | Advanced OpenGL blending operation: `Multiply` (2)  
| `Screen` | Advanced OpenGL blending operation: `Screen` (2)  
| `Overlay` | Advanced OpenGL blending operation: `Overlay` (2)  
| `Darken` | Advanced OpenGL blending operation: `Darken` (2)  
| `Lighten` | Advanced OpenGL blending operation: `Lighten` (2)  
| `ColorDodge` | Advanced OpenGL blending operation: `ColorDodge` (2)  
| `ColorBurn` | Advanced OpenGL blending operation: `ColorBurn` (2)  
| `HardLight` | Advanced OpenGL blending operation: `HardLight` (2)  
| `SoftLight` | Advanced OpenGL blending operation: `SoftLight` (2)  
| `Difference` | Advanced OpenGL blending operation: `Difference` (2)  
| `Exclusion` | Advanced OpenGL blending operation: `Exclusion` (2)  
| `HSLHue` | Advanced OpenGL blending operation: `HSLHue` (2)  
| `HSLSaturation` | Advanced OpenGL blending operation: `HSLSaturation` (2)  
| `HSLColor` | Advanced OpenGL blending operation: `HSLColor` (2)  
| `HSLLuminosity` | Advanced OpenGL blending operation: `HSLLuminosity` (2)  
  
Notes:

  1. Logical operations require DX 11.1+ or Vulkan.
  2. Advanced OpenGL blending operations require `GLES3.1 AEP+`, `GL_KHR_blend_equation_advanced`, or `GL_NV_blend_equation_advanced`. They can only be used with standard RGBA blending; they are not compatible with separate RGB and alpha blending.

## Examples

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                 // Enable subtractive blending for this Pass
                 Blend SrcAlpha One
                 BlendOp RevSub
                
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
             // Enable subtractive blending for this SubShader
             Blend SrcAlpha One
             BlendOp RevSub
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Set the blending mode in a shader](writing-shader-blending-modes.html)

[](SL-Blend.html)

Blend command in ShaderLab reference

[](SL-ColorMask.html)

ColorMask command in ShaderLab reference

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

