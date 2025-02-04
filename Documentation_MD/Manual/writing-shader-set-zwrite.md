[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-set-zwrite.html)
  * [中文](/cn/current/Manual/writing-shader-set-zwrite.html)
  * [日本語](/ja/current/Manual/writing-shader-set-zwrite.html)
  * [한국어](/kr/current/Manual/writing-shader-set-zwrite.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-set-zwrite.html)
  * [中文](/cn/current/Manual/writing-shader-set-zwrite.html)
  * [日本語](/ja/current/Manual/writing-shader-set-zwrite.html)
  * [한국어](/kr/current/Manual/writing-shader-set-zwrite.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Disable writing to the depth buffer in a shader

[](writing-shader-set-ztest.html)

Set the depth testing mode in a shader

[](writing-shader-set-stencil.html)

Check or write to the stencil buffer in a shader

# Disable writing to the depth buffer in a shader

`ZWrite` sets whether the **depth buffer** A memory store that holds the
z-value depth of each pixel in an image, where the z-value is the depth for
each rendered pixel from the projection plane. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#depthbuffer) contents are updated during
rendering. Normally, ZWrite is enabled for opaque objects and disabled for
semi-transparent ones.

Disabling ZWrite can lead to incorrect depth ordering. In this case, you need
to sort geometry on the CPU.

## Examples

This example code demonstrates the syntax for using this command in a Pass
block.

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Disables writing to the depth buffer for this Pass
                  ZWrite Off
                
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
             // Disables writing to the depth buffer for this SubShader
             ZWrite Off
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional Resources

  * [ZWrite command in ShaderLab reference](SL-ZWrite.html)

[](writing-shader-set-ztest.html)

Set the depth testing mode in a shader

[](writing-shader-set-stencil.html)

Check or write to the stencil buffer in a shader

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

