[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ColorMask.html)
  * [中文](/cn/current/Manual/SL-ColorMask.html)
  * [日本語](/ja/current/Manual/SL-ColorMask.html)
  * [한국어](/kr/current/Manual/SL-ColorMask.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ColorMask.html)
  * [中文](/cn/current/Manual/SL-ColorMask.html)
  * [日本語](/ja/current/Manual/SL-ColorMask.html)
  * [한국어](/kr/current/Manual/SL-ColorMask.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * ColorMask command in ShaderLab reference

[](SL-BlendOp.html)

BlendOp command in ShaderLab reference

[](SL-Conservative.html)

Conservative command in ShaderLab reference

# ColorMask command in ShaderLab reference

Sets the color channel writing mask, which prevents the GPU from writing to
channels in the render target.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ColorMask** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
`ColorMask <channels>` | `ColorMask RGB` | Write to the given channels of the default render target.  
`ColorMask <channels> <render target>` | `ColorMask RGB 2` | As above, but for a given render target.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**render target** | Integer, 0 through 7. | The render target index.  
**channels** | `0` | Disables color writes to the R, G, B, and A channels.  
| `R` | Enables color writes to the red channel.  
| `G` | Enables color writes to the green channel.  
| `B` | Enables color writes to the blue channel.  
| `A` | Enables color writes to the alpha channel.  
| Any combination of `R`, `G`, `B`, and `A` without spaces. For example: `RB` | Enables color writes to the given channels.  
  
## Additional resources

  * [Set the color channels the GPU renders to](writing-shader-color-mask.html)

[](SL-BlendOp.html)

BlendOp command in ShaderLab reference

[](SL-Conservative.html)

Conservative command in ShaderLab reference

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

