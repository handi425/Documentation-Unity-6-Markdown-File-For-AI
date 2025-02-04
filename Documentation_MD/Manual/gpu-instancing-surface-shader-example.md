[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gpu-instancing-surface-shader-example.html)
  * [中文](/cn/current/Manual/gpu-instancing-surface-shader-example.html)
  * [日本語](/ja/current/Manual/gpu-instancing-surface-shader-example.html)
  * [한국어](/kr/current/Manual/gpu-instancing-surface-shader-example.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gpu-instancing-surface-shader-example.html)
  * [中文](/cn/current/Manual/gpu-instancing-surface-shader-example.html)
  * [日本語](/ja/current/Manual/gpu-instancing-surface-shader-example.html)
  * [한국어](/kr/current/Manual/gpu-instancing-surface-shader-example.html)

  * [Rendering](rendering-and-post-processing.html)
  * [Graphics performance and profiling](graphics-performance-profiling.html)
  * [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
  * [Examples of GPU instancing shaders in the Built-In Render Pipeline](gpu-instancing-samples.html)
  * Example of a Surface Shader that supports GPU Instancing in the Built-In Render Pipeline

[](gpu-instancing-samples.html)

Examples of GPU instancing shaders in the Built-In Render Pipeline

[](gpu-instancing-vertex-fragment-shader-example.html)

Example of a shader that supports GPU Instancing in the Built-In Render
Pipeline

# Example of a Surface Shader that supports GPU Instancing in the Built-In
Render Pipeline

The following example demonstrates how to create an instanced Surface
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) with different color values for each
instance.

    
    
    Shader "Custom/InstancedColorSurfaceShader"
    {
    Properties
    {
    _Color ("Color", Color) = (1,1,1,1)
    _MainTex ("Albedo (RGB)", 2D) = "white" {}
    _Glossiness ("Smoothness", Range(0,1)) = 0.5
    _Metallic ("Metallic", Range(0,1)) = 0.0
    }
    
    SubShader
    {
    Tags { "RenderType"="Opaque" }
    LOD 200
    CGPROGRAM
    // Uses the physically based standard lighting model with shadows enabled for all light types.
    #pragma surface surf Standard fullforwardshadows
    // Use Shader model 3.0 target
    #pragma target 3.0
    sampler2D _MainTex;
    struct Input
    {
    float2 uv_MainTex;
    };
    half _Glossiness;
    half _Metallic;
    UNITY_INSTANCING_BUFFER_START(Props)
     UNITY_DEFINE_INSTANCED_PROP(fixed4, _Color)
    UNITY_INSTANCING_BUFFER_END(Props)
    void surf (Input IN, inout SurfaceOutputStandard o) {
    fixed4 c = tex2D (_MainTex, IN.uv_MainTex) * UNITY_ACCESS_INSTANCED_PROP(Props, _Color);
    o.Albedo = c.rgb;
    o.Metallic = _Metallic;
    o.Smoothness = _Glossiness;
    o.Alpha = c.a;
    }
    ENDCG
    }
    FallBack "Diffuse"
    }
    

[](gpu-instancing-samples.html)

Examples of GPU instancing shaders in the Built-In Render Pipeline

[](gpu-instancing-vertex-fragment-shader-example.html)

Example of a shader that supports GPU Instancing in the Built-In Render
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

