[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-set-ztest.html)
  * [中文](/cn/current/Manual/writing-shader-set-ztest.html)
  * [日本語](/ja/current/Manual/writing-shader-set-ztest.html)
  * [한국어](/kr/current/Manual/writing-shader-set-ztest.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-set-ztest.html)
  * [中文](/cn/current/Manual/writing-shader-set-ztest.html)
  * [日本語](/ja/current/Manual/writing-shader-set-ztest.html)
  * [한국어](/kr/current/Manual/writing-shader-set-ztest.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Set the depth testing mode in a shader

[](writing-shader-set-zclip.html)

Set the depth clip mode in a shader

[](writing-shader-set-zwrite.html)

Disable writing to the depth buffer in a shader

# Set the depth testing mode in a shader

Depth testing allows GPUs that have “Early-Z” functionality to reject geometry
early in the pipeline, and also ensures correct ordering of the geometry. You
can change the conditions of depth testing to achieve visual effects such as
object occlusion.

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
                  // Sets the depth test operation to Equal for all pixels in this Pass
                  // You would typically do this if you want to render the geometry exactly where already rendered geometry is
                  ZTest Equal
                
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
            // Sets the depth test operation to Equal for all pixels in this Pass
            // You would typically do this if you want to render the geometry exactly where already rendered geometry is
            ZTest Equal
    
             // The rest of the code that defines the SubShader goes here.        
    
            Pass
            {    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [ZTest command in ShaderLab reference](SL-ZTest.html)

[](writing-shader-set-zclip.html)

Set the depth clip mode in a shader

[](writing-shader-set-zwrite.html)

Disable writing to the depth buffer in a shader

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

