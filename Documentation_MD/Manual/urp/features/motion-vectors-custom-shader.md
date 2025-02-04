[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors-custom-shader.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-custom-shader.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-custom-shader.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-custom-shader.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors-custom-shader.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors-custom-shader.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors-custom-shader.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors-custom-shader.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Output a motion vector texture in a custom shader in URP

[](../../urp/features/motion-vectors-render-pass.html)

Motion vectors render pass in URP

[](../../urp/features/motion-vectors-sample.html)

Sample motion vectors in a shader in URP

# Output a motion vector texture in a custom shader in URP

For URP to render the **MotionVectors** pass for a **ShaderLab** Unity’s
language for defining the structure of Shader objects. [More info](../../SL-
Shader.html)  
See in [Glossary](../../Glossary.html#ShaderLab) **shader** A program that
runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader), make sure that its active
SubShader contains a pass with the following [LightMode tag](../urp-
shaders/urp-shaderlab-pass-tags.html#lightmode):

    
    
    Tags { "LightMode" = "MotionVectors" }
    

For example:

    
    
    Shader “Example/MyCustomShaderWithPerObjectMotionVectors"
    {
        SubShader
        {
            // ...other passes, SubShader tags and commands
        
            Pass
            {
                Tags { "LightMode" = "MotionVectors" }
                ColorMask RG
                
                HLSLPROGRAM
                
                // Your shader code goes here.
                
                ENDHLSL
            }
        }
    }
    

For an example of adding motion vector pass support for features such as alpha
clipping, **LOD** The _Level Of Detail_ (LOD) technique is an optimization
that reduces the number of triangles that Unity has to render for a GameObject
when its distance from the Camera increases. [More
info](../../LevelOfDetail.html)  
See in [Glossary](../../Glossary.html#LOD) cross-fade, or alembic animation,
refer to the implementation of the `MotionVectors` pass in URP pre-built
ShaderLab shaders, for example, the `Unlit.shader` file. The rendering of your
`MotionVectors` pass should match your non-motion-vector passes and should
reflect any custom deformation and/or vertex animation a pass is performing.

If a custom shader is only intended for objects with transform motion or
skinned animation, without using alpha clipping, LOD cross-fade, alembic
animation, custom deformation, or vertex animation, the motion vector fallback
shader provided by URP might be enough. To add the pre-built fallback shader,
add the following ShaderLab command to your SubShader blocks:

    
    
    Shader “Example/MyCustomShaderWithPerObjectMotionVectorFallback"
    {
        SubShader
        {
            // ...other passes, SubShader tags, and commands
        
            UsePass "Hidden/Universal Render Pipeline/ObjectMotionVectorFallback/MOTIONVECTORS"
        }
    }
    

**Note:** In Unity versions earlier than 2023.2, URP would automatically use
the fallback pass for all SubShader blocks which don’t have a pass tagged with
the `MotionVectors` [LightMode tag](../urp-shaders/urp-shaderlab-pass-
tags.html). Starting from Unity 2023.2, this fallback logic is disabled for
the following reasons:

  * The fallback logic was only an initial implementation detail meant for URP’s own Materials.
  * URP Materials now use material-type-specific motion vector passes to support features like alpha clip, LOD cross-fade, or alembic animation, making the fallback obsolete.
  * The fallback logic was causing unintended visual artifacts for content which it was not applicable to (for example, decals which should not draw any object motion vectors).

[](../../urp/features/motion-vectors-render-pass.html)

Motion vectors render pass in URP

[](../../urp/features/motion-vectors-sample.html)

Sample motion vectors in a shader in URP

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

