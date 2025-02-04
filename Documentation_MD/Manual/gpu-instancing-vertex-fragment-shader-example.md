[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [中文](/cn/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [日本語](/ja/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [한국어](/kr/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [中文](/cn/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [日本語](/ja/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)
  * [한국어](/kr/current/Manual/gpu-instancing-vertex-fragment-shader-example.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
  * [Examples of GPU instancing shaders in the Built-In Render Pipeline](gpu-instancing-samples.html)
  * Example of a shader that supports GPU Instancing in the Built-In Render Pipeline

[](gpu-instancing-surface-shader-example.html)

Example of a Surface Shader that supports GPU Instancing in the Built-In
Render Pipeline

[](gpu-instancing-change-data.html)

Example of changing per-instance data at runtime in the Built-In Render
Pipeline

# Example of a shader that supports GPU Instancing in the Built-In Render
Pipeline

The following example demonstrates how to create an instanced vertex and
fragment **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) with different color values for each
instance. Unlike the **surface shader** A streamlined way of writing shaders
for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader), when you create the vertex and
fragment shader you must use UNITY_SETUP_INSTANCE_ID to manually set up an
instance ID.

    
    
    Shader "Custom/SimplestInstancedShader"
    {
        Properties
        {
            _Color ("Color", Color) = (1, 1, 1, 1)
        }
    
        SubShader
        {
            Tags { "RenderType"="Opaque" }
            LOD 100
    
            Pass
            {
                CGPROGRAM
                #pragma vertex vert
                #pragma fragment frag
                #pragma multi_compile_instancing
                #include "UnityCG.cginc"
    
                struct appdata
                {
                    float4 vertex : POSITION;
                    UNITY_VERTEX_INPUT_INSTANCE_ID
                };
    
                struct v2f
                {
                    float4 vertex : SV_POSITION;
                    UNITY_VERTEX_INPUT_INSTANCE_ID // use this to access instanced properties in the fragment shader.
                };
    
                UNITY_INSTANCING_BUFFER_START(Props)
                UNITY_DEFINE_INSTANCED_PROP(float4, _Color)
                UNITY_INSTANCING_BUFFER_END(Props)
    
                v2f vert(appdata v)
                {
                    v2f o;
    
                    UNITY_SETUP_INSTANCE_ID(v);
                    UNITY_TRANSFER_INSTANCE_ID(v, o);
                    o.vertex = UnityObjectToClipPos(v.vertex);
                    return o;
                }
    
                fixed4 frag(v2f i) : SV_Target
                {
                    UNITY_SETUP_INSTANCE_ID(i);
                    return UNITY_ACCESS_INSTANCED_PROP(Props, _Color);
                }
                ENDCG
            }
        }
    }
    

[](gpu-instancing-surface-shader-example.html)

Example of a Surface Shader that supports GPU Instancing in the Built-In
Render Pipeline

[](gpu-instancing-change-data.html)

Example of changing per-instance data at runtime in the Built-In Render
Pipeline

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

