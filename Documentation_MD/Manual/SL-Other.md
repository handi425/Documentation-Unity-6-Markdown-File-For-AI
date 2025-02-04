[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Other.html)
  * [中文](/cn/current/Manual/SL-Other.html)
  * [日本語](/ja/current/Manual/SL-Other.html)
  * [한국어](/kr/current/Manual/SL-Other.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Other.html)
  * [中文](/cn/current/Manual/SL-Other.html)
  * [日本語](/ja/current/Manual/SL-Other.html)
  * [한국어](/kr/current/Manual/SL-Other.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Group commands with the Category block

[](writing-shader-alpha-to-mask.html)

Reduce aliasing with AlphaToMask mode

[](writing-shader-change-properties.html)

Adding material properties to shaders

# Group commands with the Category block

Use the **Category** block to group commands that set the render state, so
that you can “inherit” the grouped rendering state within the block.

For example, your **Shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object might have multiple
[SubShaders](SL-SubShader.html), each of which requires [blending](SL-
Blend.html) set to additive. You can use the Category block for that:

    
    
    Shader "example" {
    Category {
        Blend One One
        SubShader {
            // ...
        }
        SubShader {
            // ...
        }
        // ...
    }
    }
    

The Category block does not have an impact on shader performance; it is
essentially the same as copy-pasting the code.

[](writing-shader-alpha-to-mask.html)

Reduce aliasing with AlphaToMask mode

[](writing-shader-change-properties.html)

Adding material properties to shaders

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

