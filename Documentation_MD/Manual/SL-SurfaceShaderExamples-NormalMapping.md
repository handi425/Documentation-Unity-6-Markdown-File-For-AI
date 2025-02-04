[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-NormalMapping.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Normal mapping Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples.html)

Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Reflection.html)

Reflection Surface Shader examples in the Built-In Render Pipeline

# Normal mapping Surface Shader example in the Built-In Render Pipeline

![](../uploads/Main/SurfaceShaderDiffuseBump.jpg)

    
    
      Shader "Example/Diffuse Bump" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
          _BumpMap ("Bumpmap", 2D) = "bump" {}
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert
          struct Input {
            float2 uv_MainTex;
            float2 uv_BumpMap;
          };
          sampler2D _MainTex;
          sampler2D _BumpMap;
          void surf (Input IN, inout SurfaceOutput o) {
            o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
            o.Normal = UnpackNormal (tex2D (_BumpMap, IN.uv_BumpMap));
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

[](SL-SurfaceShaderExamples.html)

Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Reflection.html)

Reflection Surface Shader examples in the Built-In Render Pipeline

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

