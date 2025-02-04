[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-pipeline.html)
  * [中文](/cn/current/Manual/writing-shader-tags-pipeline.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-pipeline.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-pipeline.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-pipeline.html)
  * [中文](/cn/current/Manual/writing-shader-tags-pipeline.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-pipeline.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-pipeline.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Set a shader to require URP or HDRP

[](add-shader-tag.html)

Add a shader tag to a SubShader or Pass

[](SL-ShaderCompilationAPIs.html)

Set a shader to require a graphics API or platform

# Set a shader to require URP or HDRP

The `RenderPipeline` tag tells Unity whether a SubShader is compatible with
the Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP) or the High Definition
Render Pipeline (HDRP).

## Example

This example code declares that a SubShader is compatible with URP:

    
    
    Shader "ExampleShader" {
        SubShader {
            Tags { "RenderPipeline" = "UniversalPipeline" }
            Pass {
                …
            }
        }
    }
    

## Additional resources

  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](SL-PassTags.html)

[](add-shader-tag.html)

Add a shader tag to a SubShader or Pass

[](SL-ShaderCompilationAPIs.html)

Set a shader to require a graphics API or platform

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

