[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [中文](/cn/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [日本語](/ja/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [한국어](/kr/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [中文](/cn/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [日本語](/ja/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [한국어](/kr/current/Manual/example-particle-system-gpu-instancing-custom-shader.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Particle System optimization](particle-system-optimization.html)
  * [GPU instancing for Particle Systems](gpu-instancing-particle-systems.html)
  * Example of Particle System GPU instancing in a Custom Shader

[](example-particle-system-gpu-instancing-surface-shader.html)

Example of Particle System GPU instancing in a Surface Shader

[](example-particle-system-gpu-instancing-custom-vertex-streams.html)

Example of Particle System GPU instancing with custom vertex streams

# Example of Particle System GPU instancing in a Custom Shader

Here is a complete working example of a Custom **Shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) using **particle system** A component
that simulates fluid entities such as liquids, clouds and flames by generating
and animating large numbers of small 2D images in the scene. [More
info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) GPU instancing. This custom
shader adds a feature which the standard particle shader does not have - a
fade between the individual frames of a [texture sheet
animation](PartSysTexSheetAnimModule.html).

    
    
    Shader "Instanced/ParticleMeshesCustom"
    {
        Properties
        {
            _MainTex("Albedo", 2D) = "white" {}
            [Toggle(_TSANIM_BLENDING)] _TSAnimBlending("Texture Sheet Animation Blending", Int) = 0
        }
        SubShader
        {
            Tags{ "RenderType" = "Opaque" }
            LOD 100
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma multi_compile __ _TSANIM_BLENDING
                #pragma multi_compile_instancing
                #pragma instancing_options procedural:vertInstancingSetup
                #include "UnityCG.cginc"
                #include "UnityStandardParticleInstancing.cginc"
                struct appdata
                {
                    float4 vertex : POSITION;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
                    UNITY_VERTEX_INPUT_INSTANCE_ID
                };
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
    #ifdef _TSANIM_BLENDING
                    float3 texcoord2AndBlend : TEXCOORD1;   
    #endif
                };
                sampler2D _MainTex;
                float4 _MainTex_ST;
                fixed4 readTexture(sampler2D tex, v2f IN)
                {
                    fixed4 color = tex2D(tex, IN.texcoord);
    #ifdef _TSANIM_BLENDING
                    fixed4 color2 = tex2D(tex, IN.texcoord2AndBlend.xy);
                    color = lerp(color, color2, IN.texcoord2AndBlend.z);
    #endif
                    return color;
                }
                v2f vert(appdata v)
                {
                    v2f o;
                    UNITY_SETUP_INSTANCE_ID(v);
                    o.color = v.color;
                    o.texcoord = v.texcoord;
                    vertInstancingColor(o.color);
    #ifdef _TSANIM_BLENDING
                    vertInstancingUVs(v.texcoord, o.texcoord, o.texcoord2AndBlend);
    #else
                    vertInstancingUVs(v.texcoord, o.texcoord);
    #endif
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    return o;
                }
                fixed4 frag(v2f i) : SV_Target
                {
                    half4 albedo = readTexture(_MainTex, i);
                    return i.color * albedo;
                }
                ENDCG
            }
        }
    }
    

This example contains the same set-up code as the **Surface Shader** A
streamlined way of writing shaders for the Built-in Render Pipeline. [More
info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) for loading the positional
data:

    
    
            #pragma instancing_options procedural:vertInstancingSetup
            #include "UnityStandardParticleInstancing.cginc"
    

The modification to the vertex function is very similar to the Surface Shader
too:

    
    
                    vertInstancingColor(o.color);
    #ifdef _TSANIM_BLENDING
                    vertInstancingUVs(v.texcoord, o.texcoord, o.texcoord2AndBlend);
    #else
                    vertInstancingUVs(v.texcoord, o.texcoord);
    #endif
    

The only difference here, compared with the first example above, is the
texture sheet animation blending. This means that the shader requires an extra
set of texture coordinates to read two frames of the texture sheet animation
instead of just one, and blends them together.

Finally, the fragment shader reads the textures and calculates the final
color.

[](example-particle-system-gpu-instancing-surface-shader.html)

Example of Particle System GPU instancing in a Surface Shader

[](example-particle-system-gpu-instancing-custom-vertex-streams.html)

Example of Particle System GPU instancing with custom vertex streams

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

