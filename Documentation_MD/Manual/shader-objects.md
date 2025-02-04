[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shader-objects.html)
  * [中文](/cn/current/Manual/shader-objects.html)
  * [日本語](/ja/current/Manual/shader-objects.html)
  * [한국어](/kr/current/Manual/shader-objects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shader-objects.html)
  * [中文](/cn/current/Manual/shader-objects.html)
  * [日本語](/ja/current/Manual/shader-objects.html)
  * [한국어](/kr/current/Manual/shader-objects.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * Shader object fundamentals

[](SL-ShadingLanguage.html)

Introduction to writing shaders in code

[](SL-landing.html)

Writing a custom shader in ShaderLab and HLSL

# Shader object fundamentals

In Unity, when you work with shaders that are part of the [graphics
pipeline](https://en.wikipedia.org/wiki/Graphics_pipeline), you usually work
with instances of the [Shader](../ScriptReference/Shader.html)A program that
runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) class. An instance of the `Shader`
class is called a ****Shader object****.

A Shader object is a Unity-specific way of working with shader programs; it is
a wrapper for shader programs and other information. It lets you define
multiple shader programs in the same file, and tell Unity how to use them.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Shader objects** | Yes | Yes | Yes | Yes  
  
## Shader object

A Shader object contains shader programs, instructions for changing settings
on the GPU (collectively called the render state), and information that tells
Unity how to use them.

You use Shader objects with [materials](Materials.html)An asset that defines
how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) to determine the appearance of your
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

## Assets

You can create Shader objects in two ways. Each has its own type of asset:

  * You can [write code](writing-shader-writing-shader-programs-hlsl.html) to create a [shader asset](class-Shader.html), which is a text file with the `.shader` extension.
  * You can use [Shader Graph](shader-graph.html) to create a Shader Graph asset.

Whichever way you create your Shader object, Unity represents the results in
the same way internally.

## Inside a Shader object

A Shader object has a nested structure. It organizes information into
structures called **SubShaders** and **Passes**. It organises shader programs
into **shader variants**.

### Shader object

A Shader object contains:

  * Information about itself, such as its name
  * An optional fallback Shader object, which Unity uses if it can’t use this one
  * One or more SubShaders

You can also define additional information such as shared shader code, or
whether to use a [custom editor](editor-CustomEditors.html). For information
on defining a Shader object, see [ShaderLab: defining a Shader object](SL-
Shader.html).

### SubShaders

SubShaders let you separate your Shader object into parts that are compatible
with different hardware, render pipelines, and runtime settings.

A SubShader contains:

  * Information about which hardware, render pipelines, and runtime settings this SubShader is compatible with
  * SubShader tags, which are key-value pairs that provide information about the SubShader
  * One or more Passes

You can also define additional information, such as render state that is
common to all of its Passes. For information on everything you can define in a
SubShader, see [ShaderLab: defining a SubShader](SL-SubShader.html).

### Passes

A Pass contains:

  * Pass tags, which are key-value pairs that provide information about the Pass
  * Instructions for updating the render state before running its shader programs
  * Shader programs, organised into one or more shader variants

You can also define additional information such as a name. For information on
everything you can define in a Pass, see [ShaderLab: defining a Pass](SL-
Pass.html).

### Shader variants

The shader programs that a Pass contains are organised into shader variants.
Shader variants share common code, but have different functionality when a
given keyword is enabled or disabled.

The number of shader variants in a Pass depends on how many keywords you
define in your shader code, and the target platform. Each Pass contains at
least one variant.

For more information, see [Shader variants](shader-variants.html)A verion of a
shader program that Unity generates according to a specific combination of
shader keywords and their status. A Shader object can contain multiple shader
variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#Shadervariant).

[](SL-ShadingLanguage.html)

Introduction to writing shaders in code

[](SL-landing.html)

Writing a custom shader in ShaderLab and HLSL

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

