[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Fallback.html)
  * [中文](/cn/current/Manual/SL-Fallback.html)
  * [日本語](/ja/current/Manual/SL-Fallback.html)
  * [한국어](/kr/current/Manual/SL-Fallback.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Fallback.html)
  * [中文](/cn/current/Manual/SL-Fallback.html)
  * [日本語](/ja/current/Manual/SL-Fallback.html)
  * [한국어](/kr/current/Manual/SL-Fallback.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Shader in ShaderLab reference](SL-Shader-object.html)
  * Fallback block in ShaderLab reference

[](SL-Properties.html)

Properties block reference in ShaderLab

[](SL-CustomEditor.html)

Custom Editor block in ShaderLab reference

# Fallback block in ShaderLab reference

This page contains information on using a `Fallback` block in your
**ShaderLab** Unity’s language for defining the structure of Shader objects.
[More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code to assign a fallback
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object. For information on how a
**Shader object** An instance of the Shader class, a Shader object is
container for shader programs and GPU instructions, and information that tells
Unity how to use them. Use them with materials to determine the appearance of
your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) works, and how Unity chooses
when to use a fallback, see [Shader objects introduction](shader-
objects.html).

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Fallback block** | Yes | Yes | Yes | Yes  
  
## Syntax

To assign a fallback, you place a `Fallback` block inside a `Shader` block.

**Signature** | **Function**  
---|---  
`Fallback "<name>"` | If no compatible SubShaders are found, use the named Shader object.  
`Fallback Off` | Do not use a fallback Shader object in place of this one. If no compatible SubShaders are found, display the [error shader](shader-error.html).  
  
## Example

This example code demonstrates the syntax for creating a Shader object that
has a named fallback.

    
    
    Shader "Examples/ExampleFallback"
    {
        SubShader
        {
            // Code that defines the SubShader goes here.
    
            Pass
            {                
                  // Code that defines the Pass goes here.
            }
        }
    
        Fallback "ExampleOtherShader"
    }
    

[](SL-Properties.html)

Properties block reference in ShaderLab

[](SL-CustomEditor.html)

Custom Editor block in ShaderLab reference

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

