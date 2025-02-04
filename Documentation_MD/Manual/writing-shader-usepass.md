[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-usepass.html)
  * [中文](/cn/current/Manual/writing-shader-usepass.html)
  * [日本語](/ja/current/Manual/writing-shader-usepass.html)
  * [한국어](/kr/current/Manual/writing-shader-usepass.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-usepass.html)
  * [中文](/cn/current/Manual/writing-shader-usepass.html)
  * [日本語](/ja/current/Manual/writing-shader-usepass.html)
  * [한국어](/kr/current/Manual/writing-shader-usepass.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
  * Include a shader pass with the UsePass command

[](writing-shader-create-shader-pass.html)

Add a shader pass in a custom shader

[](writing-shader-writing-shader-programs-hlsl.html)

Writing HLSL shader programs

# Include a shader pass with the UsePass command

The UsePass command inserts a named Pass from another **Shader** A program
that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object. You can use this command to
reduce code duplication in shader source files.

## Example

This example code creates a **Shader object** An instance of the Shader class,
a Shader object is container for shader programs and GPU instructions, and
information that tells Unity how to use them. Use them with materials to
determine the appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) called ContainsNamedPass, which
contains a Pass called ExampleNamedPass.

    
    
    Shader "Examples/ContainsNamedPass"
    {
        SubShader
        {
            Pass
            {    
                  Name "ExampleNamedPass"
                
                  // The rest of the Pass contents go here.
            }
        }
    }
    

This example code creates a Shader object called UseNamedPass, which uses the
named Pass from the example code above.

    
    
    Shader "Examples/UsesNamedPass"
    {
        SubShader
        {
            UsePass "Examples/ContainsNamedPass/EXAMPLENAMEDPASS"
        }
    }
    

## Additional resources

  * [UsePass directive in ShaderLab reference](SL-UsePass.html)

[](writing-shader-create-shader-pass.html)

Add a shader pass in a custom shader

[](writing-shader-writing-shader-programs-hlsl.html)

Writing HLSL shader programs

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

