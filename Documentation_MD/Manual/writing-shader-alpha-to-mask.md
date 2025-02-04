[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-alpha-to-mask.html)
  * [中文](/cn/current/Manual/writing-shader-alpha-to-mask.html)
  * [日本語](/ja/current/Manual/writing-shader-alpha-to-mask.html)
  * [한국어](/kr/current/Manual/writing-shader-alpha-to-mask.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-alpha-to-mask.html)
  * [中文](/cn/current/Manual/writing-shader-alpha-to-mask.html)
  * [日本語](/ja/current/Manual/writing-shader-alpha-to-mask.html)
  * [한국어](/kr/current/Manual/writing-shader-alpha-to-mask.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Reduce aliasing with AlphaToMask mode

[](writing-shader-color-mask.html)

Set the color channels the GPU renders to

[](SL-Other.html)

Group commands with the Category block

# Reduce aliasing with AlphaToMask mode

Alpha-to-coverage mode can reduce the excessive aliasing that occurs when you
use multisample anti-aliasing (MSAA) with shaders that use alpha testing, such
as vegetation shaders. To do this, it modifies the multisample coverage mask
proportionally to the alpha value in the output of the fragment **shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) result.

This command is intended for use with MSAA. If you enable alpha-to-coverage
mode when you are not using MSAA, the results can be unpredictable; different
graphics APIs and GPUs handle this differently.

## Examples

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Enable alpha-to-coverage mode for this Pass
                  AlphaToMask On
                
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
             // Enable alpha-to-coverage mode for this SubShader
             AlphaToMask On
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [AlphaToMask command in ShaderLab reference](SL-AlphaToMask.html)

[](writing-shader-color-mask.html)

Set the color channels the GPU renders to

[](SL-Other.html)

Group commands with the Category block

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

