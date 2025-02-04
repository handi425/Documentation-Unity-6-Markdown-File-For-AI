[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](SL-SurfaceShaderExamples.html)
  * Wrapped diffuse Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-Decals.html)

Decals Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-ToonRamp.html)

Toon shading Surface Shader example in the Built-In Render Pipeline

# Wrapped diffuse Surface Shader example in the Built-In Render Pipeline

The following example shows **Wrapped Diffuse** , a modification of
**Diffuse** lighting where illumination “wraps around” the edges of objects.
It’s useful for simulating subsurface scattering effects. Only the `CGPROGRAM`
section changes, so once again, the surrounding **Shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code is omitted:

    
    
        ...ShaderLab code...
        CGPROGRAM
        #pragma surface surf WrapLambert
    
        half4 LightingWrapLambert (SurfaceOutput s, half3 lightDir, half atten) {
            half NdotL = dot (s.Normal, lightDir);
            half diff = NdotL * 0.5 + 0.5;
            half4 c;
            c.rgb = s.Albedo * _LightColor0.rgb * (diff * atten);
            c.a = s.Alpha;
            return c;
        }
    
        struct Input {
            float2 uv_MainTex;
        };
        
        sampler2D _MainTex;
            void surf (Input IN, inout SurfaceOutput o) {
            o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
        }
        ENDCG
        ...ShaderLab code...
    

Here’s how it looks like with a Texture and without a Texture, with one
directional Light in the **Scene** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene):

![](../uploads/Main/SurfaceShaderDiffuseWrap.jpg)
![](../uploads/Main/SurfaceShaderDiffuseWrapNoTex.png)

[](SL-SurfaceShaderExamples-Decals.html)

Decals Surface Shader example in the Built-In Render Pipeline

[](SL-SurfaceShaderExamples-ToonRamp.html)

Toon shading Surface Shader example in the Built-In Render Pipeline

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

