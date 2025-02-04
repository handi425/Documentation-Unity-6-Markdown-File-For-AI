[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-AlphaToMask.html)
  * [中文](/cn/current/Manual/SL-AlphaToMask.html)
  * [日本語](/ja/current/Manual/SL-AlphaToMask.html)
  * [한국어](/kr/current/Manual/SL-AlphaToMask.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-AlphaToMask.html)
  * [中文](/cn/current/Manual/SL-AlphaToMask.html)
  * [日本語](/ja/current/Manual/SL-AlphaToMask.html)
  * [한국어](/kr/current/Manual/SL-AlphaToMask.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * AlphaToMask command in ShaderLab reference

[](SL-Commands.html)

GPU render state commands in ShaderLab reference

[](SL-Blend.html)

Blend command in ShaderLab reference

# AlphaToMask command in ShaderLab reference

Enables or disables [alpha-to-
coverage](https://en.wikipedia.org/wiki/Alpha_to_coverage) mode on the GPU.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**AlphaToMask** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
`AlphaToMask <state>` | `AlphaToMask Off` | Enables or disables alpha-to-coverage mode.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**state** | `On` | Enables alpha-to-coverage mode.  
| `Off` | Disables alpha-to-coverage mode.  
  
## Additional resources

  * [Reduce aliasing with AlphaToMask mode](writing-shader-alpha-to-mask.html)

[](SL-Commands.html)

GPU render state commands in ShaderLab reference

[](SL-Blend.html)

Blend command in ShaderLab reference

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

