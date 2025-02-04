[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-Reflection.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-Reflection.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-Reflection.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Reflection Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-NormalMapping.html)

Normal mapping Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-VertexModifier.html)

Vertex modifier Surface Shader example in the Built-In Render Pipeline

# Reflection Surface Shader examples in the Built-In Render Pipeline

Here’s a **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that does cubemapped reflection using
built-in `worldRefl` input. It’s very similar to built-in Reflective/Diffuse
Shader:

    
    
      Shader "Example/WorldRefl" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
          _Cube ("Cubemap", CUBE) = "" {}
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert
          struct Input {
              float2 uv_MainTex;
              float3 worldRefl;
          };
          sampler2D _MainTex;
          samplerCUBE _Cube;
          void surf (Input IN, inout SurfaceOutput o) {
              o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb * 0.5;
              o.Emission = texCUBE (_Cube, IN.worldRefl).rgb;
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

Because it assigns the reflection color as **Emission** , we get a very shiny
soldier:

![](../uploads/Main/SurfaceShaderWorldRefl.jpg)

If you want to do reflections that are affected by **normal maps** A type of
Bump Map texture that allows you to add surface detail such as bumps, grooves,
and scratches to a model which catch the light as if they are represented by
real geometry.  
See in [Glossary](Glossary.html#Normalmap), it needs to be slightly more
involved: `INTERNAL_DATA` needs to be added to the `Input` structure, and
`WorldReflectionVector` function used to compute per-pixel reflection vector
after you’ve written the Normal output.

    
    
      Shader "Example/WorldRefl Normalmap" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
          _BumpMap ("Bumpmap", 2D) = "bump" {}
          _Cube ("Cubemap", CUBE) = "" {}
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert
          struct Input {
              float2 uv_MainTex;
              float2 uv_BumpMap;
              float3 worldRefl;
              INTERNAL_DATA
          };
          sampler2D _MainTex;
          sampler2D _BumpMap;
          samplerCUBE _Cube;
          void surf (Input IN, inout SurfaceOutput o) {
              o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb * 0.5;
              o.Normal = UnpackNormal (tex2D (_BumpMap, IN.uv_BumpMap));
              o.Emission = texCUBE (_Cube, WorldReflectionVector (IN, o.Normal)).rgb;
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

Here’s a normal-mapped shiny soldier:

![](../uploads/Main/SurfaceShaderWorldReflNormalmap.jpg)

[](SL-SurfaceShaderExamples-NormalMapping.html)

Normal mapping Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-VertexModifier.html)

Vertex modifier Surface Shader example in the Built-In Render Pipeline

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

