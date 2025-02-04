[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-unlit.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-unlit.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-unlit.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-unlit.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-unlit.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-unlit.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-unlit.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-unlit.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Simple unlit shader example in the Built-In Render Pipeline

[](built-in-shader-examples-checkerboard.html)

Checkerboard pattern shader example in the Built-In Render Pipeline

[](built-in-shader-examples-mesh-normals.html)

Mesh normals shader example in the Built-In Render Pipeline

# Simple unlit shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleUnlitTextured.png)

    
    
    Shader "Unlit/SimpleUnlitTexturedShader"
    {
        Properties
        {
            // we have removed support for texture tiling/offset,
            // so make them not be displayed in material inspector
            [NoScaleOffset] _MainTex ("Texture", 2D) = "white" {}
        }
        SubShader
        {
            Pass
            {
                CGPROGRAM
                // use "vert" function as the vertex shader
                #pragma vertex vert
                // use "frag" function as the pixel (fragment) shader
                #pragma fragment frag
    
                // vertex shader inputs
                struct appdata
                {
                    float4 vertex : POSITION; // vertex position
                    float2 uv : TEXCOORD0; // texture coordinate
                };
    
                // vertex shader outputs ("vertex to fragment")
                struct v2f
                {
                    float2 uv : TEXCOORD0; // texture coordinate
                    float4 vertex : SV_POSITION; // clip space position
                };
    
                // vertex shader
                v2f vert (appdata v)
                {
                    v2f o;
                    // transform position to clip space
                    // (multiply with model*view*projection matrix)
                    o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);
                    // just pass the texture coordinate
                    o.uv = v.uv;
                    return o;
                }
                
                // texture we will sample
                sampler2D _MainTex;
    
                // pixel shader; returns low precision ("fixed4" type)
                // color ("SV_Target" semantic)
                fixed4 frag (v2f i) : SV_Target
                {
                    // sample texture and return it
                    fixed4 col = tex2D(_MainTex, i.uv);
                    return col;
                }
                ENDCG
            }
        }
    }
    

[](built-in-shader-examples-checkerboard.html)

Checkerboard pattern shader example in the Built-In Render Pipeline

[](built-in-shader-examples-mesh-normals.html)

Mesh normals shader example in the Built-In Render Pipeline

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

