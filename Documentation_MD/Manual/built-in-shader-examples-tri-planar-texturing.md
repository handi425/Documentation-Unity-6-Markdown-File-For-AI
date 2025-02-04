[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-tri-planar-texturing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [中文](/cn/current/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [日本語](/ja/current/Manual/built-in-shader-examples-tri-planar-texturing.html)
  * [한국어](/kr/current/Manual/built-in-shader-examples-tri-planar-texturing.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
  * Tri-planar texturing shader example in the Built-In Render Pipeline

[](built-in-shader-examples-environment-reflections.html)

Normal map texturing shader example in the Built-In Render Pipeline

[](built-in-shader-examples-simple-diffuse-lighting.html)

Simple diffuse lighting shader example in the Built-In Render Pipeline

# Tri-planar texturing shader example in the Built-In Render Pipeline

![](../uploads/SL/ExampleTriPlanar.png)

For complex or procedural meshes, instead of texturing them using the regular
UV coordinates, it is sometimes useful to just “project” texture onto the
object from three primary directions. This is called “tri-planar” texturing.
The idea is to use surface normal to weight the three texture directions.
Here’s the **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader):

    
    
    Shader "Unlit/Triplanar"
    {
        Properties
        {
            _MainTex ("Texture", 2D) = "white" {}
            _Tiling ("Tiling", Float) = 1.0
            _OcclusionMap("Occlusion", 2D) = "white" {}
        }
        SubShader
        {
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #include "UnityCG.cginc"
    
                struct v2f
                {
                    half3 objNormal : TEXCOORD0;
                    float3 coords : TEXCOORD1;
                    float2 uv : TEXCOORD2;
                    float4 pos : SV_POSITION;
                };
    
                float _Tiling;
    
                v2f vert (float4 pos : POSITION, float3 normal : NORMAL, float2 uv : TEXCOORD0)
                {
                    v2f o;
                    o.pos = UnityObjectToClipPos(pos);
                    o.coords = pos.xyz * _Tiling;
                    o.objNormal = normal;
                    o.uv = uv;
                    return o;
                }
    
                sampler2D _MainTex;
                sampler2D _OcclusionMap;
                
                fixed4 frag (v2f i) : SV_Target
                {
                    // use absolute value of normal as texture weights
                    half3 blend = abs(i.objNormal);
                    // make sure the weights sum up to 1 (divide by sum of x+y+z)
                    blend /= dot(blend,1.0);
                    // read the three texture projections, for x,y,z axes
                    fixed4 cx = tex2D(_MainTex, i.coords.yz);
                    fixed4 cy = tex2D(_MainTex, i.coords.xz);
                    fixed4 cz = tex2D(_MainTex, i.coords.xy);
                    // blend the textures based on weights
                    fixed4 c = cx * blend.x + cy * blend.y + cz * blend.z;
                    // modulate by regular occlusion map
                    c *= tex2D(_OcclusionMap, i.uv);
                    return c;
                }
                ENDCG
            }
        }
    }
    

[](built-in-shader-examples-environment-reflections.html)

Normal map texturing shader example in the Built-In Render Pipeline

[](built-in-shader-examples-simple-diffuse-lighting.html)

Simple diffuse lighting shader example in the Built-In Render Pipeline

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

