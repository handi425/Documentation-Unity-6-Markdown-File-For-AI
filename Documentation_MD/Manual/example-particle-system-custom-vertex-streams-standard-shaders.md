[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [中文](/cn/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [日本語](/ja/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [한국어](/kr/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [中文](/cn/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [日本語](/ja/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)
  * [한국어](/kr/current/Manual/example-particle-system-custom-vertex-streams-standard-shaders.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * [Custom data streams in Particle Systems](custom-data-streams-particle-systems.html)
  * Example of Particle System Standard Shader custom vertex streams

[](PartSysVertexStreams.html)

Particle System custom vertex streams

[](example-particle-system-custom-vertex-streams-surface-shaders.html)

Example of Particle System Surface Shader custom vertex streams

# Example of Particle System Standard Shader custom vertex streams

Here is an example of an animated flip-book **Shader** A program that runs on
the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader). It uses the default inputs
(**Position** , **Normal** The direction perpendicular to the surface of a
mesh, represented by a Vector. Unity uses normals to determine object
orientation and apply shading. [More info](scripting-vectors.html)  
See in [Glossary](Glossary.html#Normal), **Color** , **UV**), but also uses
two additional streams for the second UV stream (**UV2**) and the flip-book
frame information (**AnimBlend**).

![](../uploads/Main/PartSysVertexStreams-Inspector.png)

    
    
    Shader "Particles/Anim Alpha Blended" {
    Properties {
        _TintColor ("Tint Color", Color) = (0.5,0.5,0.5,0.5)
        _MainTex ("Particle Texture", 2D) = "white" {}
        _InvFade ("Soft Particles Factor", Range(0.01,3.0)) = 1.0
    }
    
    Category {
        Tags { "Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" "PreviewType"="Plane" }
        Blend SrcAlpha OneMinusSrcAlpha
        ColorMask RGB
        Cull Off Lighting Off ZWrite Off
    
        SubShader {
            Pass {
            
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma target 2.0
                #pragma multi_compile_particles
                #pragma multi_compile_fog
                
                #include "UnityCG.cginc"
    
                sampler2D _MainTex;
                fixed4 _TintColor;
                
                struct appdata_t {
                    float4 vertex : POSITION;
                    fixed4 color : COLOR;
                    float4 texcoords : TEXCOORD0;
                    float texcoordBlend : TEXCOORD1;
                    UNITY_VERTEX_INPUT_INSTANCE_ID
                };
    
                struct v2f {
                    float4 vertex : SV_POSITION;
                    fixed4 color : COLOR;
                    float2 texcoord : TEXCOORD0;
                    float2 texcoord2 : TEXCOORD1;
                    fixed blend : TEXCOORD2;
                    UNITY_FOG_COORDS(3)
                    #ifdef SOFTPARTICLES_ON
                    float4 projPos : TEXCOORD4;
                    #endif
                    UNITY_VERTEX_OUTPUT_STEREO
                };
                
                float4 _MainTex_ST;
    
                v2f vert (appdata_t v)
                {
                    v2f o;
                    UNITY_SETUP_INSTANCE_ID(v);
                    UNITY_INITIALIZE_VERTEX_OUTPUT_STEREO(o); 
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    #ifdef SOFTPARTICLES_ON
                    o.projPos = ComputeScreenPos (o.vertex);
                    COMPUTE_EYEDEPTH(o.projPos.z);
                    #endif
                    o.color = v.color * _TintColor;
                    o.texcoord = TRANSFORM_TEX(v.texcoords.xy,_MainTex);
                    o.texcoord2 = TRANSFORM_TEX(v.texcoords.zw,_MainTex);
                    o.blend = v.texcoordBlend;
                    UNITY_TRANSFER_FOG(o,o.vertex);
                    return o;
                }
    
                sampler2D_float _CameraDepthTexture;
                float _InvFade;
                
                fixed4 frag (v2f i) : SV_Target
                {
                    #ifdef SOFTPARTICLES_ON
                    float sceneZ = LinearEyeDepth (SAMPLE_DEPTH_TEXTURE_PROJ(_CameraDepthTexture, UNITY_PROJ_COORD(i.projPos)));
                    float partZ = i.projPos.z;
                    float fade = saturate (_InvFade * (sceneZ-partZ));
                    i.color.a *= fade;
                    #endif
                    
                    fixed4 colA = tex2D(_MainTex, i.texcoord);
                    fixed4 colB = tex2D(_MainTex, i.texcoord2);
                    fixed4 col = 2.0f * i.color * lerp(colA, colB, i.blend);
                    UNITY_APPLY_FOG(i.fogCoord, col);
                    return col;
                }
                ENDCG 
            }
        }   
    }
    }
    

[](PartSysVertexStreams.html)

Particle System custom vertex streams

[](example-particle-system-custom-vertex-streams-surface-shaders.html)

Example of Particle System Surface Shader custom vertex streams

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

