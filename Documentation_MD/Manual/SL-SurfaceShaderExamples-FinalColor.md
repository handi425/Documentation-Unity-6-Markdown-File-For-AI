[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-FinalColor.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Final color modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-CustomData.html)

Custom data Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Decals.html)

Decals Surface Shader example in the Built-In Render Pipeline

# Final color modifier Surface Shader example in the Built-In Render Pipeline

It is possible to use a “final color modifier” function that will modify the
final color computed by the **Shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader).The **Surface Shader** A streamlined
way of writing shaders for the Built-in Render Pipeline. [More info](SL-
SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) compilation directive
`finalcolor:functionName` is used for this, with a function that takes `Input
IN, SurfaceOutput o, inout fixed4 color` parameters.

Here’s a simple Shader that applies tint to the final color. This is different
from just applying tint to the surface Albedo color: this tint will also
affect any color that comes from **Lightmaps** A pre-rendered texture that
contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), **Light Probes** Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) and similar extra sources.

    
    
      Shader "Example/Tint Final Color" {
        Properties {
          _MainTex ("Texture", 2D) = "white" {}
          _ColorTint ("Tint", Color) = (1.0, 0.6, 0.6, 1.0)
        }
        SubShader {
          Tags { "RenderType" = "Opaque" }
          CGPROGRAM
          #pragma surface surf Lambert finalcolor:mycolor
          struct Input {
              float2 uv_MainTex;
          };
          fixed4 _ColorTint;
          void mycolor (Input IN, SurfaceOutput o, inout fixed4 color)
          {
              color *= _ColorTint;
          }
          sampler2D _MainTex;
          void surf (Input IN, inout SurfaceOutput o) {
               o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
          }
          ENDCG
        } 
        Fallback "Diffuse"
      }
    

![](../uploads/Main/SurfaceShaderFinalColorSimple.jpg)

[](SL-SurfaceShaderExamples-CustomData.html)

Custom data Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Decals.html)

Decals Surface Shader example in the Built-In Render Pipeline

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

