[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-add-shader-program.html)
  * [中文](/cn/current/Manual/writing-shader-add-shader-program.html)
  * [日本語](/ja/current/Manual/writing-shader-add-shader-program.html)
  * [한국어](/kr/current/Manual/writing-shader-add-shader-program.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-add-shader-program.html)
  * [中文](/cn/current/Manual/writing-shader-add-shader-program.html)
  * [日本語](/ja/current/Manual/writing-shader-add-shader-program.html)
  * [한국어](/kr/current/Manual/writing-shader-add-shader-program.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * Add an HLSL shader program

[](writing-shader-programs-introduction.html)

Shader program fundamentals

[](writing-shader-include-shader-program.html)

Duplicate HLSL in multiple programs

# Add an HLSL shader program

To add HLSL code, you can use the `HLSLPROGRAM` directive.

## Example

    
    
    Shader "Examples/ExampleShader"
    {
        SubShader
        {
            Pass
            {                
                  Name "ExamplePassName"
                  Tags { "LightMode" = "ExampleLightModeTagValue" }
    
                  // ShaderLab commands to set the render state go here
    
                  HLSLPROGRAM
                    // HLSL shader code goes here
                  ENDHLSL
            }
        }
    }
    

## Additional resources

  * [ShaderLab: adding shader programs](shader-shaderlab-code-blocks.html)

[](writing-shader-programs-introduction.html)

Shader program fundamentals

[](writing-shader-include-shader-program.html)

Duplicate HLSL in multiple programs

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

