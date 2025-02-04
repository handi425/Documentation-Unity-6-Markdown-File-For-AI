[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [中文](/cn/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [日本語](/ja/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [한국어](/kr/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [中文](/cn/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [日本語](/ja/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)
  * [한국어](/kr/current/Manual/example-particle-system-custom-vertex-streams-surface-shaders.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Custom data streams in Particle Systems](custom-data-streams-particle-systems.html)
  * Example of Particle System Surface Shader custom vertex streams

[](example-particle-system-custom-vertex-streams-standard-shaders.html)

Example of Particle System Standard Shader custom vertex streams

[](define-custom-data-formats-particles.html)

Define custom data formats for particles

# Example of Particle System Surface Shader custom vertex streams

It’s possible to use Surface **Shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) with custom vertex streams, although
there are some extra things to be aware of:

  * The input structure to your surface function is not the same as the input structure to the **vertex Shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](Glossary.html#vertexshader). You need to provide your own
vertex Shader input structure. See below for an example, where it is called
`appdata_particles`.

  * When **surface Shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) are built, there is automatic
handling of variables whose names begin with certain tokens. The most notable
one is `uv`. To prevent the automatic handling from causing problems here, be
sure to give your UV inputs different names (for example, “texcoord”).

Here is the same functionality as the Standard Shader, but in a Surface
Shader:

    
    
    Shader "Particles/Anim Alpha Blend Surface" {
        Properties {
            _Color ("Color", Color) = (1,1,1,1)
            _MainTex ("Albedo (RGB)", 2D) = "white" {}
            _Glossiness ("Smoothness", Range(0,1)) = 0.5
            _Metallic ("Metallic", Range(0,1)) = 0.0
        }
        SubShader {
            Tags {"Queue"="Transparent" "RenderType"="Transparent"}
            Blend SrcAlpha OneMinusSrcAlpha
            ZWrite off
            LOD 200
            
            CGPROGRAM
            // Physically based Standard lighting model, and enable shadows on all light types
            #pragma surface surf Standard alpha vertex:vert
    
            // Use shader model 3.0 target, to get nicer looking lighting
            #pragma target 3.0
    
            sampler2D _MainTex;
    
             struct appdata_particles {
                float4 vertex : POSITION;
                float3 normal : NORMAL;
                float4 color : COLOR;
                float4 texcoords : TEXCOORD0;
                float texcoordBlend : TEXCOORD1;
                };
    
    
            struct Input {
                float2 uv_MainTex;
                float2 texcoord1;
                float blend;
                float4 color;
            };
    
    
            void vert(inout appdata_particles v, out Input o) {
                UNITY_INITIALIZE_OUTPUT(Input,o);
                o.uv_MainTex = v.texcoords.xy;
                o.texcoord1 = v.texcoords.zw;
                o.blend = v.texcoordBlend;
                o.color = v.color;
              }
    
    
            half _Glossiness;
            half _Metallic;
            fixed4 _Color;
    
    
            void surf (Input IN, inout SurfaceOutputStandard o) {
                fixed4 colA = tex2D(_MainTex, IN.uv_MainTex);
                fixed4 colB = tex2D(_MainTex, IN.texcoord1);
                fixed4 c = 2.0f * IN.color * lerp(colA, colB, IN.blend) * _Color;
                     
                o.Albedo = c.rgb;
                // Metallic and smoothness come from slider variables
                o.Metallic = _Metallic;
                o.Smoothness = _Glossiness;
                o.Alpha = c.a;
            }
            ENDCG
        }
        FallBack "Diffuse"
    }
    
    

[](example-particle-system-custom-vertex-streams-standard-shaders.html)

Example of Particle System Standard Shader custom vertex streams

[](define-custom-data-formats-particles.html)

Define custom data formats for particles

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

