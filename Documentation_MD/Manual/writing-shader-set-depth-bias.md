[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-set-depth-bias.html)
  * [中文](/cn/current/Manual/writing-shader-set-depth-bias.html)
  * [日本語](/ja/current/Manual/writing-shader-set-depth-bias.html)
  * [한국어](/kr/current/Manual/writing-shader-set-depth-bias.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-set-depth-bias.html)
  * [中文](/cn/current/Manual/writing-shader-set-depth-bias.html)
  * [日本語](/ja/current/Manual/writing-shader-set-depth-bias.html)
  * [한국어](/kr/current/Manual/writing-shader-set-depth-bias.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Set the depth bias in a shader

[](set-culling-mode.html)

Set the culling mode in a shader

[](writing-shader-set-zclip.html)

Set the depth clip mode in a shader

# Set the depth bias in a shader

Depth bias, also called depth offset, is a setting on the GPU that determines
the depth at which it draws geometry. Adjust the depth bias to force the GPU
to draw geometry on top of other geometry that is at the same depth. This can
help you to avoid unwanted visual effects such as z-fighting and shadow acne.

To set the depth bias for specific geometry, use this command or a
[RenderStateBlock](../ScriptReference/Rendering.RenderStateBlock.html). To set
the global depth bias, which affects all geometry, use
[CommandBuffer.SetGlobalDepthBias](../ScriptReference/Rendering.CommandBuffer.SetGlobalDepthBias.html).
The GPU applies the depth bias for specific geometry in addition to the global
depth bias.

To reduce shadow acne, you can achieve a similar visual effect with the
**light bias** settings; however, these settings work differently, and they do
not change the state on the GPU. For more information, see [Shadow
troubleshooting](ShadowPerformance.html).

# Example

This example code demonstrates the syntax for using this command in a Pass
block.

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Sets the depth offset for this geometry so that the GPU draws this geometry closer to the camera
                  // You would typically do this to avoid z-fighting
                  Offset -1, -1
    
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Offset command in ShaderLab reference](SL-Offset.html)

[](set-culling-mode.html)

Set the culling mode in a shader

[](writing-shader-set-zclip.html)

Set the depth clip mode in a shader

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

