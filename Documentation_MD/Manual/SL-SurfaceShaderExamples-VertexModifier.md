[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-VertexModifier.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Vertex modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Reflection.html)

Reflection Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-CustomData.html)

Custom data Surface Shader example in the Built-In Render Pipeline

# Vertex modifier Surface Shader example in the Built-In Render Pipeline

![](../uploads/Main/SurfaceShaderNormalExtrusion.jpg)

It is possible to use a “vertex modifier” function that will modify the
incoming vertex data in the vertex **Shader** A program that runs on the GPU.
[More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). This can be used for things like
procedural animation and extrusion along normals. **Surface Shader** A
streamlined way of writing shaders for the Built-in Render Pipeline. [More
info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) compilation directive
`vertex:functionName` is used for that, with a function that takes `inout
appdata_full` parameter.

Here’s a Shader that moves vertices along their normals by the amount
specified in the Material:

    
    
      Shader "Example/Normal Extrusion" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
          _Amount ("Extrusion Amount", Range(-1,1)) = 0.5
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert vertex:vert
          struct Input {
              float2 uv_MainTex;
          };
          float _Amount;
          void vert (inout appdata_full v) {
              v.vertex.xyz += v.normal * _Amount;
          }
          sampler2D _MainTex;
          void surf (Input IN, inout SurfaceOutput o) {
              o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

[](SL-SurfaceShaderExamples-Reflection.html)

Reflection Surface Shader examples in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-CustomData.html)

Custom data Surface Shader example in the Built-In Render Pipeline

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

