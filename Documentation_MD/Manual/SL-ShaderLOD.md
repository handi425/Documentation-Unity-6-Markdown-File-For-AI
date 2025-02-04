[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-ShaderLOD.html)
  * [中文](/cn/current/Manual/SL-ShaderLOD.html)
  * [日本語](/ja/current/Manual/SL-ShaderLOD.html)
  * [한국어](/kr/current/Manual/SL-ShaderLOD.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-ShaderLOD.html)
  * [中文](/cn/current/Manual/SL-ShaderLOD.html)
  * [日本語](/ja/current/Manual/SL-ShaderLOD.html)
  * [한국어](/kr/current/Manual/SL-ShaderLOD.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [SubShader in ShaderLab reference](SL-SubShader-object.html)
  * LOD directive in ShaderLab reference

[](SL-SubShader.html)

SubShader block in ShaderLab reference

[](SL-SubShaderTags.html)

SubShader tags in ShaderLab reference

# LOD directive in ShaderLab reference

This page contains information on using a `LOD` block in your **ShaderLab**
Unity’s language for defining the structure of Shader objects. [More info](SL-
Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code to assign a **LOD** The _Level
Of Detail_ (LOD) technique is an optimization that reduces the number of
triangles that Unity has to render for a GameObject when its distance from the
Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) (level of detail) value to a SubShader.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: SubShader LOD block** | Yes | Yes | Yes | Yes  
  
## Syntax

In ShaderLab, you assign a LOD value to a SubShader by placing a `LOD` block
inside a `SubShader` block.

**Signature** | **Function**  
---|---  
LOD [value] | Assigns the given LOD value to the SubShader.  
  
## LOD values for Unity’s built-in shaders

In the Built-in Render Pipeline, Unity’s built-in **shaders** A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) have the following LOD values:

**LOD value** | **Shader name**  
---|---  
100 | Unlit/Texture  
Unlit/Color  
Unlit/Transparent  
Unlit/Transparent Cutout  
300 | Standard  
Standard (Specular Setup)  
Autodesk Interactive  
  
## LOD values for legacy shaders

In the Built-in Render Pipeline, Unity’s built-in [legacy shaders](Built-
inShaderGuide.html) have the following LOD values:

**LOD value** | **Shader name**  
---|---  
100 | VertexLit  
150 | Decal  
Reflective VertexLit  
200 | Diffuse  
250 | Diffuse Detail  
Reflective Bumped Unlit  
Reflective Bumped VertexLit  
300 | Bumped  
Specular  
400 | Bumped Specular  
500 | Parallax  
600 | Parallax Specular  
  
## Additional resources

  * [Prioritize lower quality shaders with the LOD command](writing-shader-prioritize-lower-quality-shaders.html)

[](SL-SubShader.html)

SubShader block in ShaderLab reference

[](SL-SubShaderTags.html)

SubShader tags in ShaderLab reference

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

