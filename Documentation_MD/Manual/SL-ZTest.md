[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ZTest.html)
  * [中文](/cn/current/Manual/SL-ZTest.html)
  * [日本語](/ja/current/Manual/SL-ZTest.html)
  * [한국어](/kr/current/Manual/SL-ZTest.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ZTest.html)
  * [中文](/cn/current/Manual/SL-ZTest.html)
  * [日本語](/ja/current/Manual/SL-ZTest.html)
  * [한국어](/kr/current/Manual/SL-ZTest.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * ZTest command in ShaderLab reference

[](SL-ZClip.html)

ZClip command in ShaderLab reference

[](SL-ZWrite.html)

ZWrite command in ShaderLab reference

# ZTest command in ShaderLab reference

Sets the conditions under which geometry passes or fails depth testing.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ZTest** | Yes | Yes | Yes | Yes  
  
## Syntax

This command makes a change to the render state. Use it in a `Pass` block to
set the render state for that Pass, or use it in a `SubShader` block to set
the render state for all Passes in that SubShader.

**Signature** | **Example syntax** | **Function**  
---|---|---  
ZTest [operation] | ZTest Less | Set the conditions under which geometry passes or fails depth testing.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
operation  
| Disabled | Disable the depth test.  
| Never | Draw no geometry, regardless of distance.  
| Less | Draw geometry that is in front of existing geometry. Do not draw geometry that is at the same distance as or behind existing geometry.  
| Equal | Draw geometry that is at the same distance as existing geometry. Do not draw geometry that is in front of or behind existing geometry.  
| LEqual | Draw geometry that is in front of or at the same distance as existing geometry. Do not draw geometry that is behind existing geometry.  
  
This is the default value.  
| Greater | Draw geometry that is behind existing geometry. Do not draw geometry that is at the same distance as or in front of existing geometry.  
| NotEqual | Draw geometry that is not at the same distance as existing geometry. Do not draw geometry that is at the same distance as existing geometry.  
| GEqual | Draw geometry that is behind or at the same distance as existing geometry. Do not draw geometry that is in front of existing geometry.  
| Always | No depth testing occurs. Draw all geometry, regardless of distance.  
  
## Additional resources

  * [Set the depth bias in a shader](writing-shader-set-depth-bias.html)
  * [Set the depth clip mode in a shader](writing-shader-set-zclip.html)
  * [Set the depth testing mode in a shader](writing-shader-set-ztest.html)

[](SL-ZClip.html)

ZClip command in ShaderLab reference

[](SL-ZWrite.html)

ZWrite command in ShaderLab reference

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

