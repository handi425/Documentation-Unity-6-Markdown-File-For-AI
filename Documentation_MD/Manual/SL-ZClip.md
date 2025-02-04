[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ZClip.html)
  * [中文](/cn/current/Manual/SL-ZClip.html)
  * [日本語](/ja/current/Manual/SL-ZClip.html)
  * [한국어](/kr/current/Manual/SL-ZClip.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ZClip.html)
  * [中文](/cn/current/Manual/SL-ZClip.html)
  * [日本語](/ja/current/Manual/SL-ZClip.html)
  * [한국어](/kr/current/Manual/SL-ZClip.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * ZClip command in ShaderLab reference

[](SL-Stencil.html)

Stencil command in ShaderLab reference

[](SL-ZTest.html)

ZTest command in ShaderLab reference

# ZClip command in ShaderLab reference

Sets the GPU’s depth clip mode, which determines how the GPU handles fragments
that are outside of the near and far planes.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ZClip** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
ZClip [enabled] | ZClip True | Sets the depth clip mode.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
enabled | True | Sets the depth clip mode to clip.  
  
This is the default setting.  
| False | Sets the depth clip mode to clamp.  
  
Fragments closer than the near plane are at the near plane exactly, and
fragments further away than the far plane are at the far plane exactly.  
  
## Additional resources

  * [Set the depth bias in a shader](writing-shader-set-depth-bias.html)
  * [Set the depth clip mode in a shader](writing-shader-set-zclip.html)
  * [Set the depth testing mode in a shader](writing-shader-set-ztest.html)

[](SL-Stencil.html)

Stencil command in ShaderLab reference

[](SL-ZTest.html)

ZTest command in ShaderLab reference

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

