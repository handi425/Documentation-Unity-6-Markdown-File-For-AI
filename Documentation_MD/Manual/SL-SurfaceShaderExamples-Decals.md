[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-Decals.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-Decals.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-Decals.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Decals Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-FinalColor.html)

Final color modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-WrappedDiffuse.html)

Wrapped diffuse Surface Shader example in the Built-In Render Pipeline

# Decals Surface Shader example in the Built-In Render Pipeline

Decals are commonly used to add details to Materials at run time (for example,
bullet impacts). They are especially useful in deferred rendering, because
they alter the GBuffer before it is lit, therefore saving on performance.

In a typical scenario, Decals should be rendered after the opaque objects and
should not be shadow casters, as seen in the **ShaderLab** Unity’s language
for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) “Tags” in the example below.

    
    
    Shader "Example/Decal" {
      Properties {
        _MainTex ("Base (RGB)", 2D) = "white" {}
      }
      SubShader {
        Tags { "RenderType"="Opaque" "Queue"="Geometry+1" "ForceNoShadowCasting"="True" }
        LOD 200
        Offset -1, -1
        
        CGPROGRAM
        #pragma surface surf Lambert decal:blend
        
        sampler2D _MainTex;
        
        struct Input {
          float2 uv_MainTex;
        };
        
        void surf (Input IN, inout SurfaceOutput o) {
            half4 c = tex2D (_MainTex, IN.uv_MainTex);
            o.Albedo = c.rgb;
            o.Alpha = c.a;
          }
        ENDCG
        }
    }
    

[](SL-SurfaceShaderExamples-FinalColor.html)

Final color modifier Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-WrappedDiffuse.html)

Wrapped diffuse Surface Shader example in the Built-In Render Pipeline

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

