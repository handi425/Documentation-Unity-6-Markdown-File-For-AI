[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [中文](/cn/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [日本語](/ja/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [한국어](/kr/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [中文](/cn/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [日本語](/ja/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [한국어](/kr/current/Manual/example-particle-system-gpu-instancing-surface-shader.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System optimization](particle-system-optimization.html)
  * [GPU instancing for Particle Systems](gpu-instancing-particle-systems.html)
  * Example of Particle System GPU instancing in a Surface Shader

[](PartSysInstancing.html)

Apply GPU instancing for a Particle System

[](example-particle-system-gpu-instancing-custom-shader.html)

Example of Particle System GPU instancing in a Custom Shader

# Example of Particle System GPU instancing in a Surface Shader

Here is a complete working example of Surface **Shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) using **Particle System** A component
that simulates fluid entities such as liquids, clouds and flames by generating
and animating large numbers of small 2D images in the scene. [More
info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) GPU Instancing:

    
    
    Shader "Instanced/ParticleMeshesSurface" {
        Properties {
            _Color ("Color", Color) = (1,1,1,1)
            _MainTex ("Albedo (RGB)", 2D) = "white" {}
            _Glossiness ("Smoothness", Range(0,1)) = 0.5
            _Metallic ("Metallic", Range(0,1)) = 0.0
        }
        SubShader {
            Tags { "RenderType"="Opaque" }
            LOD 200
    
            CGPROGRAM
            // Physically based Standard lighting model, and enable shadows on all light types
            // And generate the shadow pass with instancing support
            #pragma surface surf Standard nolightmap nometa noforwardadd keepalpha fullforwardshadows addshadow vertex:vert
            // Enable instancing for this shader
            #pragma multi_compile_instancing
            #pragma instancing_options procedural:vertInstancingSetup
            #pragma exclude_renderers gles
            #include "UnityStandardParticleInstancing.cginc"
            sampler2D _MainTex;
            struct Input {
                float2 uv_MainTex;
                fixed4 vertexColor;
            };
            fixed4 _Color;
            half _Glossiness;
            half _Metallic;
            void vert (inout appdata_full v, out Input o)
            {
                UNITY_INITIALIZE_OUTPUT(Input, o);
                vertInstancingColor(o.vertexColor);
                vertInstancingUVs(v.texcoord, o.uv_MainTex);
            }
    
            void surf (Input IN, inout SurfaceOutputStandard o) {
                // Albedo comes from a texture tinted by color
                fixed4 c = tex2D (_MainTex, IN.uv_MainTex) * IN.vertexColor * _Color;
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
    

There are a number of small differences to a regular [Surface Shader](SL-
SurfaceShaders.html)A streamlined way of writing shaders for the Built-in
Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) in the above example, which
make it work with particle instancing.

Firstly, you must add the following two lines to enable Procedural Instancing,
and specify the built-in vertex setup function. This function lives in
UnityStandardParticleInstancing.cginc, and loads the per-instance (per-
particle) positional data:

    
    
            #pragma instancing_options procedural:vertInstancingSetup
            #include "UnityStandardParticleInstancing.cginc"
    

The other modification in the example is to the Vertex function, which has two
extra lines that apply per-instance attributes, specifically, particle colors
and [Texture Sheet Animation](PartSysTexSheetAnimModule.html) texture
coordinates:

    
    
                vertInstancingColor(o.vertexColor);
                vertInstancingUVs(v.texcoord, o.uv_MainTex);
    

[](PartSysInstancing.html)

Apply GPU instancing for a Particle System

[](example-particle-system-gpu-instancing-custom-shader.html)

Example of Particle System GPU instancing in a Custom Shader

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

