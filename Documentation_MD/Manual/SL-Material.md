[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Material.html)
  * [中文](/cn/current/Manual/SL-Material.html)
  * [日本語](/ja/current/Manual/SL-Material.html)
  * [한국어](/kr/current/Manual/SL-Material.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Material.html)
  * [中文](/cn/current/Manual/SL-Material.html)
  * [日本語](/ja/current/Manual/SL-Material.html)
  * [한국어](/kr/current/Manual/SL-Material.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [ShaderLab legacy functionality reference](shader-shaderlab-legacy.html)
  * ShaderLab: legacy lighting

[](SL-Fog.html)

ShaderLab: legacy fog

[](SL-AlphaTest.html)

ShaderLab: legacy alpha testing

# ShaderLab: legacy lighting

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
**Legacy lighting** | Yes | No | No | No  
  
## Overview

The material and lighting parameters are used to control the built-in vertex
lighting. Vertex lighting is the standard Direct3D/OpenGL lighting model that
is computed for each vertex. **Lighting on** turns it on. Lighting is affected
by **Material** An asset that defines how a surface should be rendered. [More
info](class-Material.html)  
See in [Glossary](Glossary.html#Material) block, **ColorMaterial** and
**SeparateSpecular** commands.

Vertex Coloring & Lighting is the first effect to be calculated for any
rendered geometry. It operates on the vertex level, and calculates the base
color that is used before textures are applied.

## Syntax

The top level commands control whether to use fixed function lighting or not,
and some configuration options. The main setup is in the **Material Block** ,
detailed further below.

### Color

    
    
        Color color
    

Sets the object to a solid color. A color is either four RGBA values in
parenthesis, or a color property name in square brackets.

### Material

    
    
        Material {Material Block}
    

The Material block is used to define the material properties of the object.

### Lighting

    
    
        Lighting On | Off
    

For the settings defined in the Material block to have any effect, you must
enable Lighting with the _Lighting On_ command. If lighting is off instead,
the color is taken straight from the _Color_ command.

### SeparateSpecular

    
    
        SeparateSpecular On | Off
    

This command makes specular lighting be added to the end of the shader pass,
so specular lighting is unaffected by texturing. Only has effect when
_Lighting On_ is used.

### ColorMaterial

    
    
        ColorMaterial AmbientAndDiffuse | Emission
    

Makes per-vertex color be used instead of the colors set in the material.
**AmbientAndDiffuse** replaces Ambient and Diffuse values of the material;
**Emission** replaces Emission value of the material.

### Material Block

This contains settings for how the material reacts to the light. Any of these
properties can be left out, in which case they default to black (i.e. have no
effect).

**Diffuse color:** The diffuse color component. This is an object’s base
color.

**Ambient color:** The ambient color component. This is the color the object
has when it’s hit by the **ambient light** Light that doesn’t come from any
specific direction, and contributes equal light in all directions to the
Scene. [More info](lighting-window.html)  
See in [Glossary](Glossary.html#Ambientlight) set in the [Lighting
Window](lighting-window.html).

****Specular color** The color of a specular highlight.  
See in [Glossary](Glossary.html#specularcolor):** The color of the object’s
specular highlight.

**Shininess number:** The sharpness of the highlight, between 0 and 1. At 0
you get a huge highlight that looks a lot like diffuse lighting, at 1 you get
a tiny speck.

**Emission color:** The color of the object when it is not hit by any light.

The full color of lights hitting the object is:

**Ambient** * [Lighting Window’s Ambient Intensity setting](lighting-
window.html) \+ (Light Color * **Diffuse** \+ Light Color * **Specular**) +
**Emission**

The light parts of the equation (within parenthesis) is repeated for all
lights that hit the object.

Typically you want to keep the Diffuse and Ambient colors the same (all built-
in shaders do this).

## Examples

Always render object in pure red:

    
    
    Shader "Solid Red" {
        SubShader {
            Pass { Color (1,0,0,0) }
        }
    }
    

Basic Shader that colors the object white and applies vertex lighting:

    
    
    Shader "VertexLit White" {
        SubShader {
            Pass {
                Material {
                    Diffuse (1,1,1,1)
                    Ambient (1,1,1,1)
                }
                Lighting On
            }
        }
    }
    

An extended version that adds material color as a property visible in Material
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector):

    
    
    Shader "VertexLit Simple" {
        Properties {
            _Color ("Main Color", COLOR) = (1,1,1,1)
        }
        SubShader {
            Pass {
                Material {
                    Diffuse [_Color]
                    Ambient [_Color]
                }
                Lighting On
            }
        }
    }
    

And finally, a full fledged vertex-lit shader (see also [SetTexture](SL-
SetTexture.html) reference page):

    
    
    Shader "VertexLit" {
        Properties {
            _Color ("Main Color", Color) = (1,1,1,0)
            _SpecColor ("Spec Color", Color) = (1,1,1,1)
            _Emission ("Emmisive Color", Color) = (0,0,0,0)
            _Shininess ("Shininess", Range (0.01, 1)) = 0.7
            _MainTex ("Base (RGB)", 2D) = "white" {}
        }
        SubShader {
            Pass {
                Material {
                    Diffuse [_Color]
                    Ambient [_Color]
                    Shininess [_Shininess]
                    Specular [_SpecColor]
                    Emission [_Emission]
                }
                Lighting On
                SeparateSpecular On
                SetTexture [_MainTex] {
                    Combine texture * primary DOUBLE, texture * primary
                }
            }
        }
    }
    

[](SL-Fog.html)

ShaderLab: legacy fog

[](SL-AlphaTest.html)

ShaderLab: legacy alpha testing

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

