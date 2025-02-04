[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-Shader.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-Shader.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-Shader.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-Shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-LightProbeProxyVolume-Shader.html)
  * [中文](/cn/current/Manual/class-LightProbeProxyVolume-Shader.html)
  * [日本語](/ja/current/Manual/class-LightProbeProxyVolume-Shader.html)
  * [한국어](/kr/current/Manual/class-LightProbeProxyVolume-Shader.html)

  * [Lighting](LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](lighting-birp.html)
  * [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](LightProbeProxyVolume-landing.html)
  * Add Light Probe Proxy Volume support to a custom shader in the Built-In Render Pipeline

[](class-LightProbeProxyVolume-reference.html)

Light Probe Proxy Volume component reference for the Built-In Render Pipeline

[](blend-reflection-probes-birp.html)

Blend Reflection Probes in the Built-In Render Pipeline

# Add Light Probe Proxy Volume support to a custom shader in the Built-In
Render Pipeline

The following is an example of a particle **shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) using the `ShadeSHPerPixel` function.

    
    
    Shader "Particles/AdditiveLPPV" {
    Properties {
        _MainTex ("Particle Texture", 2D) = "white" {}
        _TintColor ("Tint Color", Color) = (0.5,0.5,0.5,0.5)
    }
    
    Category {
        Tags { "Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" }
        Blend SrcAlpha One
        ColorMask RGB
        Cull Off Lighting Off ZWrite Off
    
        SubShader {
            Pass {
    
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma multi_compile_particles
                #pragma multi_compile_fog
    
                // Specify the target
                #pragma target 3.0
    
                #include "UnityCG.cginc"
    
                // You must include this header to have access to ShadeSHPerPixel
                #include "UnityStandardUtils.cginc"
    
                fixed4 _TintColor;
                sampler2D _MainTex;
    
                struct appdata_t {
                    float4 vertex : POSITION;
                    float3 normal : NORMAL;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
                };
    
                struct v2f {
                    float4 vertex : SV_POSITION;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
                    UNITY_FOG_COORDS(1)
                    float3 worldPos : TEXCOORD2;
                    float3 worldNormal : TEXCOORD3;
                };
    
                float4 _MainTex_ST;
    
                v2f vert (appdata_t v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    o.worldNormal = UnityObjectToWorldNormal(v.normal);
                    o.worldPos = mul(unity_ObjectToWorld, v.vertex).xyz;
                    o.color = v.color;
                    o.texcoord = TRANSFORM_TEX(v.texcoord,_MainTex);
                    UNITY_TRANSFER_FOG(o,o.vertex);
                    return o;
                }
    
                fixed4 frag (v2f i) : SV_Target
                {
                    half3 currentAmbient = half3(0, 0, 0);
                    half3 ambient = ShadeSHPerPixel(i.worldNormal, currentAmbient, i.worldPos);
                    fixed4 col = _TintColor * i.color * tex2D(_MainTex, i.texcoord);
                    col.xyz += ambient;
                    UNITY_APPLY_FOG_COLOR(i.fogCoord, col, fixed4(0,0,0,0)); // fog towards black due to our blend mode
                    return col;
                }
                ENDCG
            }
        }
    }
    }
    

## Additional resources

  * [Precalculating indirect light with Light Probes](LightProbes-landing.html)
  * [Configure an object to sample more light probes](LightProbeProxyVolume-landing.html)

[](class-LightProbeProxyVolume-reference.html)

Light Probe Proxy Volume component reference for the Built-In Render Pipeline

[](blend-reflection-probes-birp.html)

Blend Reflection Probes in the Built-In Render Pipeline

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

