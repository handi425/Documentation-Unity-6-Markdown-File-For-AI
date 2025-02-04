[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Global illumination Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-ToonRamp.html)

Toon shading Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderTessellation.html)

Tessellation Surface Shader examples in the Built-In Render Pipeline

# Global illumination Surface Shader example in the Built-In Render Pipeline

We’ll start with a **Shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) that mimics Unity’s built-in GI:

    
    
        Shader "Example/CustomGI_ToneMapped" {
            Properties {
                _MainTex ("Albedo (RGB)", 2D) = "white" {}
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                
                CGPROGRAM
                #pragma surface surf StandardDefaultGI
        
                #include "UnityPBSLighting.cginc"
        
                sampler2D _MainTex;
        
                inline half4 LightingStandardDefaultGI(SurfaceOutputStandard s, half3 viewDir, UnityGI gi)
                {
                    return LightingStandard(s, viewDir, gi);
                }
        
                inline void LightingStandardDefaultGI_GI(
                    SurfaceOutputStandard s,
                    UnityGIInput data,
                    inout UnityGI gi)
                {
                    LightingStandard_GI(s, data, gi);
                }
        
                struct Input {
                    float2 uv_MainTex;
                };
        
                void surf (Input IN, inout SurfaceOutputStandard o) {
                    o.Albedo = tex2D(_MainTex, IN.uv_MainTex);
                }
                ENDCG
            }
            FallBack "Diffuse"
        }
    

Now, let’s add some tone mapping on top of the GI:

    
    
        Shader "Example/CustomGI_ToneMapped" {
            Properties {
                _MainTex ("Albedo (RGB)", 2D) = "white" {}
                _Gain("Lightmap tone-mapping Gain", Float) = 1
                _Knee("Lightmap tone-mapping Knee", Float) = 0.5
                _Compress("Lightmap tone-mapping Compress", Float) = 0.33
            }
            SubShader {
                Tags { "RenderType"="Opaque" }
                
                CGPROGRAM
                #pragma surface surf StandardToneMappedGI
        
                #include "UnityPBSLighting.cginc"
        
                half _Gain;
                half _Knee;
                half _Compress;
                sampler2D _MainTex;
        
                inline half3 TonemapLight(half3 i) {
                    i *= _Gain;
                    return (i > _Knee) ? (((i - _Knee)*_Compress) + _Knee) : i;
                }
        
                inline half4 LightingStandardToneMappedGI(SurfaceOutputStandard s, half3 viewDir, UnityGI gi)
                {
                    return LightingStandard(s, viewDir, gi);
                }
        
                inline void LightingStandardToneMappedGI_GI(
                    SurfaceOutputStandard s,
                    UnityGIInput data,
                    inout UnityGI gi)
                {
                    LightingStandard_GI(s, data, gi);
        
                    gi.light.color = TonemapLight(gi.light.color);
                    #ifdef DIRLIGHTMAP_SEPARATE
                        #ifdef LIGHTMAP_ON
                            gi.light2.color = TonemapLight(gi.light2.color);
                        #endif
                        #ifdef DYNAMICLIGHTMAP_ON
                            gi.light3.color = TonemapLight(gi.light3.color);
                        #endif
                    #endif
                    gi.indirect.diffuse = TonemapLight(gi.indirect.diffuse);
                    gi.indirect.specular = TonemapLight(gi.indirect.specular);
                }
        
                struct Input {
                    float2 uv_MainTex;
                };
        
                void surf (Input IN, inout SurfaceOutputStandard o) {
                    o.Albedo = tex2D(_MainTex, IN.uv_MainTex);
                }
                ENDCG
            }
            FallBack "Diffuse"
        }
    

[](SL-SurfaceShaderExamples-ToonRamp.html)

Toon shading Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderTessellation.html)

Tessellation Surface Shader examples in the Built-In Render Pipeline

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

