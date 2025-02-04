[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Conservative.html)
  * [中文](/cn/current/Manual/SL-Conservative.html)
  * [日本語](/ja/current/Manual/SL-Conservative.html)
  * [한국어](/kr/current/Manual/SL-Conservative.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Conservative.html)
  * [中文](/cn/current/Manual/SL-Conservative.html)
  * [日本語](/ja/current/Manual/SL-Conservative.html)
  * [한국어](/kr/current/Manual/SL-Conservative.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * Conservative command in ShaderLab reference

[](SL-ColorMask.html)

ColorMask command in ShaderLab reference

[](SL-Cull.html)

Cull command in ShaderLab reference

# Conservative command in ShaderLab reference

Enables or disables conservative **rasterization** The process of generating
an image by calculating pixels for each polygon or triangle in the geometry.
This is an alternative to ray tracing.  
See in [Glossary](Glossary.html#Rasterization).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Conservative** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
`Conservative <enabled>` | `Conservative True` | Enables or disables conservative rasterization.  
  
Requires DX 11.3+, or GL_NV_conservative_raster.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**enabled** | `True` | Enables conservative rasterization.  
| `False` | Disables conservative rasterization.  
  
## Additional resources

  * [Enable conservative rasterization in a shader](writing-shader-conservative-rasterization.html)

[](SL-ColorMask.html)

ColorMask command in ShaderLab reference

[](SL-Cull.html)

Cull command in ShaderLab reference

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

