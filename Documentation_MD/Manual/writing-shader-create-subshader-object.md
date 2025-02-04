[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-create-subshader-object.html)
  * [中文](/cn/current/Manual/writing-shader-create-subshader-object.html)
  * [日本語](/ja/current/Manual/writing-shader-create-subshader-object.html)
  * [한국어](/kr/current/Manual/writing-shader-create-subshader-object.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-create-subshader-object.html)
  * [中文](/cn/current/Manual/writing-shader-create-subshader-object.html)
  * [日本語](/ja/current/Manual/writing-shader-create-subshader-object.html)
  * [한국어](/kr/current/Manual/writing-shader-create-subshader-object.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * Add a subshader in a custom shader

[](class-Shader.html)

Create a shader file

[](writing-shader-create-shader-pass.html)

Add a shader pass in a custom shader

# Add a subshader in a custom shader

A **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object contains one or more
SubShaders. SubShaders let you define different GPU settings and shader
programs for different hardware, **render pipelines** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), and runtime settings. Some
**Shader objects** An instance of the Shader class, a Shader object is
container for shader programs and GPU instructions, and information that tells
Unity how to use them. Use them with materials to determine the appearance of
your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) contain only a single SubShader;
others contain multiple SubShaders to support a range of different
configurations.

For information on how a Shader object works, and the relationship between
Shader objects, SubShaders and Passes, see [Shader objects
introduction](shader-objects.html).

In **ShaderLab** Unity’s language for defining the structure of Shader
objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), you define a SubShader by placing
a `SubShader` block inside a `Shader` block.

## Example

This example code demonstrates the syntax for creating a Shader object that
contains a single SubShader, which in turn contains a single Pass.

    
    
    Shader "Examples/SinglePass"
    {
        SubShader
        {
            Tags { "ExampleSubShaderTagKey" = "ExampleSubShaderTagValue" }
            LOD 100
    
             // ShaderLab commands that apply to the whole SubShader go here. 
    
            Pass
            {                
                  Name "ExamplePassName"
                  Tags { "ExamplePassTagKey" = "ExamplePassTagValue" }
    
                  // ShaderLab commands that apply to this Pass go here.
    
                  // HLSL code goes here.
            }
        }
    }
    

## Additional resources

  * [SubShader block in ShaderLab reference](SL-SubShader.html)
  * [SubShader tags in ShaderLab reference](SL-SubShaderTags.html)

[](class-Shader.html)

Create a shader file

[](writing-shader-create-shader-pass.html)

Add a shader pass in a custom shader

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

