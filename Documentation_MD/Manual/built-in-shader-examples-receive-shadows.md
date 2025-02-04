[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-receive-shadows.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-receive-shadows.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-receive-shadows.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-receive-shadows.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-receive-shadows.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-receive-shadows.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-receive-shadows.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-receive-shadows.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Receiving shadows shader example in the Built-In Render Pipeline

[](built-in-shader-examples-shadow-casting.html)

Shadow casting shader example in the Built-In Render Pipeline

[](built-in-shader-examples-fog.html)

Fog shader example in the Built-In Render Pipeline

# Receiving shadows shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleShadowReceiving.png)

Implementing support for receiving shadows will require compiling the base
lighting pass into several variants, to handle cases of “directional light
without shadows” and “directional light with shadows” properly. **#pragma
multi_compile_fwdbase** directive does this (see [multiple shader
variants](SL-MultipleProgramVariants.html) for details). In fact it does a lot
more: it also compiles variants for the different **lightmap** A pre-rendered
texture that contains the effects of light sources on static objects in the
scene. Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) types, **Enlighten** A lighting
system by Geomerics used in Unity for Enlighten Realtime Global Illumination.
[More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) being on or off etc.
Currently we don’t need all that, so we’ll explicitly skip these variants.

Then to get actual shadowing computations, we’ll **#include
“AutoLight.cginc”** **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) [include file](SL-
BuiltinIncludes.html) and use SHADOW_COORDS, TRANSFER_SHADOW,
SHADOW_ATTENUATION macros from it.

Here’s the shader:

    
    
    Shader "Lit/Diffuse With Shadows"
    {
        Properties
        {
            [NoScaleOffset] _MainTex ("Texture", 2D) = "white" {}
        }
        SubShader
        {
            Pass
            {
                Tags {"LightMode"="ForwardBase"}
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #include "UnityCG.cginc"
                #include "Lighting.cginc"
    
                // compile shader into multiple variants, with and without shadows
                // (we don't care about any lightmaps yet, so skip these variants)
                #pragma multi_compile_fwdbase nolightmap nodirlightmap nodynlightmap novertexlight
                // shadow helper functions and macros
                #include "AutoLight.cginc"
    
                struct v2f
                {
                    float2 uv : TEXCOORD0;
                    SHADOW_COORDS(1) // put shadows data into TEXCOORD1
                    fixed3 diff : COLOR0;
                    fixed3 ambient : COLOR1;
                    float4 pos : SV_POSITION;
                };
                v2f vert (appdata_base v)
                {
                    v2f o;
                    o.pos = UnityObjectToClipPos(v.vertex);
                    o.uv = v.texcoord;
                    half3 worldNormal = UnityObjectToWorldNormal(v.normal);
                    half nl = max(0, dot(worldNormal, _WorldSpaceLightPos0.xyz));
                    o.diff = nl * _LightColor0.rgb;
                    o.ambient = ShadeSH9(half4(worldNormal,1));
                    // compute shadows data
                    TRANSFER_SHADOW(o)
                    return o;
                }
    
                sampler2D _MainTex;
    
                fixed4 frag (v2f i) : SV_Target
                {
                    fixed4 col = tex2D(_MainTex, i.uv);
                    // compute shadow attenuation (1.0 = fully lit, 0.0 = fully shadowed)
                    fixed shadow = SHADOW_ATTENUATION(i);
                    // darken light's illumination with shadow, keep ambient intact
                    fixed3 lighting = i.diff * shadow + i.ambient;
                    col.rgb *= lighting;
                    return col;
                }
                ENDCG
            }
    
            // shadow casting support
            UsePass "Legacy Shaders/VertexLit/SHADOWCASTER"
        }
    }
    

Look, we have shadows now!

[](built-in-shader-examples-shadow-casting.html)

Shadow casting shader example in the Built-In Render Pipeline

[](built-in-shader-examples-fog.html)

Fog shader example in the Built-In Render Pipeline

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

