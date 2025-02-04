[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Fog.html)
  * [中文](/cn/current/Manual/SL-Fog.html)
  * [日本語](/ja/current/Manual/SL-Fog.html)
  * [한국어](/kr/current/Manual/SL-Fog.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Fog.html)
  * [中文](/cn/current/Manual/SL-Fog.html)
  * [日本語](/ja/current/Manual/SL-Fog.html)
  * [한국어](/kr/current/Manual/SL-Fog.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [ShaderLab legacy functionality reference](shader-shaderlab-legacy.html)
  * ShaderLab: legacy fog

[](shader-shaderlab-legacy.html)

ShaderLab legacy functionality reference

[](SL-Material.html)

ShaderLab: legacy lighting

# ShaderLab: legacy fog

**Note** : The **ShaderLab** Unity’s language for defining the structure of
Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) functionality on this page is
legacy, and is documented for backwards compatibility only. If your **shader**
A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) source file includes HLSL code, Unity
ignores these commands completely. If your shader source file does not include
HLSL code, Unity compiles these commands into regular shader programs on
import.

## Render pipeline compatibility

**Feature name** | **Built-in**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline)** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP**  
---|---|---|---|---  
**Legacy fog** | Yes | No | No | No  
  
# Overview

Use the Fog command to enable or disable Unity’s built-in fog, in shaders that
are written using legacy fixed-function style commands.

Configure the **project settings** A broad collection of settings which allow
you to configure how Physics, Audio, Networking, Graphics, Input and many
other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) for the built-in fog effect
using the [RenderSettings](../ScriptReference/RenderSettings.html) class, or
the [Lighting window](lighting-window.html), and then use this command to
enable or disable fog in a given Pass.

Fogging blends the color of the generated pixels down towards a given color,
based on the distance from the **camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Fogging does not modify a blended
**pixel** The smallest unit in a computer image. Pixel size depends on your
screen resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel)’s alpha value, only its RGB components.

## Valid parameter values

**Parameter** | **Value** | **Function**  
---|---|---  
**Mode** | `Off` | Do not apply built-in fog to this Pass.  
| `Global` | Apply built-in fog to this Pass, based on the project settings.  
  
Note that if fog is disabled in the project settings, Unity will not apply it
to this Pass.  
  
## Examples

This example code demonstrates the syntax for using this command in a Pass
block.

    
    
    Shader "Examples/FogExample"
    {
        SubShader
        {
             // The rest of the code that defines the SubShader goes here.
    
            Pass
            {    
                  Fog Off
                
                  // The rest of the code that defines the Pass goes here.
            }
        }
    }
    

[](shader-shaderlab-legacy.html)

ShaderLab legacy functionality reference

[](SL-Material.html)

ShaderLab: legacy lighting

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

