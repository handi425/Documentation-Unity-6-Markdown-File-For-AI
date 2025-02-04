[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Ambient light shader example in the Built-In Render Pipeline

[](built-in-shader-examples-simple-diffuse-lighting.html)

Simple diffuse lighting shader example in the Built-In Render Pipeline

[](built-in-shader-examples-shadow-casting.html)

Shadow casting shader example in the Built-In Render Pipeline

# Ambient light shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleDiffuseAmbientLighting.png)

The example above does not take any ambient lighting or light probes into
account. Let’s fix this! It turns out we can do this by adding just a single
line of code. Both ambient and [light probe](LightProbes.html)Light probes
store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) data is passed to **shaders** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) in Spherical Harmonics form, and
**ShadeSH9** function from **UnityCG.cginc** [include file](SL-
BuiltinIncludes.html) does all the work of evaluating it, given a world space
normal.

    
    
    Shader "Lit/Diffuse With Ambient"
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
                #include "UnityLightingCommon.cginc"
    
                struct v2f
                {
                    float2 uv : TEXCOORD0;
                    fixed4 diff : COLOR0;
                    float4 vertex : SV_POSITION;
                };
    
                v2f vert (appdata_base v)
                {
                    v2f o;
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    o.uv = v.texcoord;
                    half3 worldNormal = UnityObjectToWorldNormal(v.normal);
                    half nl = max(0, dot(worldNormal, _WorldSpaceLightPos0.xyz));
                    o.diff = nl * _LightColor0;
    
                    // the only difference from previous shader:
                    // in addition to the diffuse lighting from the main light,
                    // add illumination from ambient or light probes
                    // ShadeSH9 function from UnityCG.cginc evaluates it,
                    // using world space normal
                    o.diff.rgb += ShadeSH9(half4(worldNormal,1));
                    return o;
                }
                
                sampler2D _MainTex;
    
                fixed4 frag (v2f i) : SV_Target
                {
                    fixed4 col = tex2D(_MainTex, i.uv);
                    col *= i.diff;
                    return col;
                }
                ENDCG
            }
        }
    }
    

This shader is in fact starting to look very similar to the built-in [Legacy
Diffuse](shader-NormalDiffuse.html) shader!

[](built-in-shader-examples-simple-diffuse-lighting.html)

Simple diffuse lighting shader example in the Built-In Render Pipeline

[](built-in-shader-examples-shadow-casting.html)

Shadow casting shader example in the Built-In Render Pipeline

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

