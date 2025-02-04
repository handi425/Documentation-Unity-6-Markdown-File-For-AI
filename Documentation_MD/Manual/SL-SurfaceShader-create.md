[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShader-create.html)
  * [中文](/cn/current/Manual/SL-SurfaceShader-create.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShader-create.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShader-create.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShader-create.html)
  * [中文](/cn/current/Manual/SL-SurfaceShader-create.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShader-create.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShader-create.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * Create a surface shader in the Built-In Render Pipeline

[](SL-RenderPipeline.html)

Surface Shaders and rendering paths in the Built-In Render Pipeline

[](SL-SurfaceShaderLighting.html)

Set the lighting model in a Surface Shader in the Built-In Render Pipeline

# Create a surface shader in the Built-In Render Pipeline

Surface **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) is placed inside `CGPROGRAM..ENDCG`
block, just like any other shader. The differences are:

  * It must be placed inside [SubShader](SL-SubShader.html) block, not inside [Pass](SL-Pass.html). **Surface shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) will compile into multiple
passes itself.

  * It uses `#pragma surface ...` directive to indicate it’s a surface shader.

The `#pragma surface` directive is:

    
    
    #pragma surface surfaceFunction lightModel [optionalparams]
    

## Example

    
    
      Shader "Example/Diffuse Simple" {
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert
          struct Input {
              float4 color : COLOR;
          };
          void surf (Input IN, inout SurfaceOutput o) {
              o.Albedo = 1;
          }
          ENDCG
        }
        Fallback "Diffuse"
      }
    

Here’s how it looks like on a model with two [Lights](class-Light.html) set
up:

![](../uploads/Main/SurfaceShaderSimple.jpg)

[](SL-RenderPipeline.html)

Surface Shaders and rendering paths in the Built-In Render Pipeline

[](SL-SurfaceShaderLighting.html)

Set the lighting model in a Surface Shader in the Built-In Render Pipeline

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

