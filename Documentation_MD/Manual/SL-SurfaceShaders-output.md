[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-SurfaceShaders-output.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaders-output.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaders-output.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaders-output.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-SurfaceShaders-output.html)
  * [中文](/cn/current/Manual/SL-SurfaceShaders-output.html)
  * [日本語](/ja/current/Manual/SL-SurfaceShaders-output.html)
  * [한국어](/kr/current/Manual/SL-SurfaceShaders-output.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shaders in the Built-In Render Pipeline](shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
  * [Writing Surface Shaders](writing-surface-shaders.html)
  * Surface Shader output structures in the Built-In Render Pipeline

[](SL-SurfaceShaders.html)

Introduction to surface shaders in the Built-In Render Pipeline

[](SL-RenderPipeline.html)

Surface Shaders and rendering paths in the Built-In Render Pipeline

# Surface Shader output structures in the Built-In Render Pipeline

Standard output structure of surface **shaders** A program that runs on the
GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) is this:

    
    
    struct SurfaceOutput
    {
        fixed3 Albedo;  // diffuse color
        fixed3 Normal;  // tangent space normal, if written
        fixed3 Emission;
        half Specular;  // specular power in 0..1 range
        fixed Gloss;    // specular intensity
        fixed Alpha;    // alpha for transparencies
    };
    

In Unity 5, **surface shaders** A streamlined way of writing shaders for the
Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) can also use physically based
lighting models. Built-in Standard and StandardSpecular lighting models (see
below) use these output structures respectively:

    
    
    struct SurfaceOutputStandard
    {
        fixed3 Albedo;      // base (diffuse or specular) color
        fixed3 Normal;      // tangent space normal, if written
        half3 Emission;
        half Metallic;      // 0=non-metal, 1=metal
        half Smoothness;    // 0=rough, 1=smooth
        half Occlusion;     // occlusion (default 1)
        fixed Alpha;        // alpha for transparencies
    };
    struct SurfaceOutputStandardSpecular
    {
        fixed3 Albedo;      // diffuse color
        fixed3 Specular;    // specular color
        fixed3 Normal;      // tangent space normal, if written
        half3 Emission;
        half Smoothness;    // 0=rough, 1=smooth
        half Occlusion;     // occlusion (default 1)
        fixed Alpha;        // alpha for transparencies
    };
    

[](SL-SurfaceShaders.html)

Introduction to surface shaders in the Built-In Render Pipeline

[](SL-RenderPipeline.html)

Surface Shaders and rendering paths in the Built-In Render Pipeline

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

