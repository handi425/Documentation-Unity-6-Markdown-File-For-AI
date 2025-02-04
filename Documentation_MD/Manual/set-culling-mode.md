[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/set-culling-mode.html)
  * [中文](/cn/current/Manual/set-culling-mode.html)
  * [日本語](/ja/current/Manual/set-culling-mode.html)
  * [한국어](/kr/current/Manual/set-culling-mode.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/set-culling-mode.html)
  * [中文](/cn/current/Manual/set-culling-mode.html)
  * [日本語](/ja/current/Manual/set-culling-mode.html)
  * [한국어](/kr/current/Manual/set-culling-mode.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * [Setting the render state on the GPU](writing-shader-render-state-commands.html)
  * Set the culling mode in a shader

[](writing-shader-conservative-rasterization.html)

Enable conservative rasterization in a shader

[](writing-shader-set-depth-bias.html)

Set the depth bias in a shader

# Set the culling mode in a shader

Culling is the process of determining what not to draw. Culling improves
rendering efficiency, by not wasting GPU time drawing things that would not be
visible in the final image.

By default, the GPU performs back-face culling; this means that it does not
draw polygons that face away from the viewer. In general, the more you can
reduce the rendering workload, the better; you should therefore change this
setting only when necessary.

## Example

    
    
    Shader "Examples/CommandExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  // Disable culling for this Pass.
                  // You would typically do this for special effects, such as transparent objects or double-sided walls.
                  Cull Off
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

## Additional resources

  * [Cull command in ShaderLab reference](SL-Cull.html)

[](writing-shader-conservative-rasterization.html)

Enable conservative rasterization in a shader

[](writing-shader-set-depth-bias.html)

Set the depth bias in a shader

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

