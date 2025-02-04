[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-include-shader-program.html)
  * [中文](/cn/current/Manual/writing-shader-include-shader-program.html)
  * [日本語](/ja/current/Manual/writing-shader-include-shader-program.html)
  * [한국어](/kr/current/Manual/writing-shader-include-shader-program.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-include-shader-program.html)
  * [中文](/cn/current/Manual/writing-shader-include-shader-program.html)
  * [日本語](/ja/current/Manual/writing-shader-include-shader-program.html)
  * [한국어](/kr/current/Manual/writing-shader-include-shader-program.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Writing HLSL shader programs](writing-shader-writing-shader-programs-hlsl.html)
  * Duplicate HLSL in multiple programs

[](writing-shader-add-shader-program.html)

Add an HLSL shader program

[](writing-shader-shader-input.html)

Shader input

# Duplicate HLSL in multiple programs

To include HLSL code in other `HLSLPROGRAM` sections, you can use the
`HLSLINCLUDE` directive.

## Example

    
    
    Shader "Examples/ExampleShader"
    {
        SubShader
        {
    
            HLSLINCLUDE
                // HLSL code that you want to share goes here
            ENDHLSL
    
            Pass
            {                
                  Name "ExampleFirstPassName"
                  Tags { "LightMode" = "ExampleLightModeTagValue" }
    
                  // ShaderLab commands to set the render state go here
    
                  HLSLPROGRAM
                    // This HLSL shader program automatically includes the contents of the HLSLINCLUDE block above
                    // HLSL shader code goes here
                  ENDHLSL
            }
    
            Pass
            {                
                  Name "ExampleSecondPassName"
                  Tags { "LightMode" = "ExampleLightModeTagValue" }
    
                  // ShaderLab commands to set the render state go here
    
                  HLSLPROGRAM
                    // This HLSL shader program automatically includes the contents of the HLSLINCLUDE block above
                    // HLSL shader code goes here
                  ENDHLSL
            }
    
        }
    }
    

## Additional resources

  * [ShaderLab: adding shader programs](shader-shaderlab-code-blocks.html)

[](writing-shader-add-shader-program.html)

Add an HLSL shader program

[](writing-shader-shader-input.html)

Shader input

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

