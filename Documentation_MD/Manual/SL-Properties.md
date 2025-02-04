[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Properties.html)
  * [中文](/cn/current/Manual/SL-Properties.html)
  * [日本語](/ja/current/Manual/SL-Properties.html)
  * [한국어](/kr/current/Manual/SL-Properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Properties.html)
  * [中文](/cn/current/Manual/SL-Properties.html)
  * [日本語](/ja/current/Manual/SL-Properties.html)
  * [한국어](/kr/current/Manual/SL-Properties.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [Shader in ShaderLab reference](SL-Shader-object.html)
  * Properties block reference in ShaderLab

[](SL-Shader.html)

Shader block in ShaderLab reference

[](SL-Fallback.html)

Fallback block in ShaderLab reference

# Properties block reference in ShaderLab

This page contains information on using a `Properties` block in your
**ShaderLab** Unity’s language for defining the structure of Shader objects.
[More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab) code to define material properties
for a **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Properties block** | Yes  
In your HLSL code, you must put per-material variables in the same `CBUFFER` for SRP Batcher compatibility. | Yes  
In your HLSL code, you must put per-material variables in the same `CBUFFER` for SRP Batcher compatibility. | Yes  
In your HLSL code, you must put per-material variables in the same `CBUFFER` for SRP Batcher compatibility. | Yes  
  
## Syntax

**Signature** | **Function**  
---|---  
`Properties`  
`{`  
`<Material property declaration>`  
`<Material property declaration>`  
`}` | Saves the given properties as part of the material asset, and uses the values stored in the material asset during rendering.  
A `Properties` block can contain any number of material property declarations.  
  
### Material property declarations

All material property declarations follow this basic format:

    
    
    [optional: attribute] name("display text in Inspector", type name) = default value
    

The exact syntax varies by type.

This section contains information on:

  * Material property declaration syntax by type.
  * Material property attributes

#### Material property declaration syntax by type

The type name and the syntax for the default value depend on the type of the
property.

In shader code, it is conventional to begin all property names with an
underscore character. The examples on this page follow this convention.

**Type** | **Example syntax** | **Comment**  
---|---|---  
**Integer** | `_ExampleName ("Integer display name", Integer) = 1` | This type is backed by a real integer (unlike the legacy `Int` type described below, which is backed by a float). Use this instead of Int when you want to use an integer.  
**Int** (legacy) | `_ExampleName ("Int display name", Int) = 1` |  **Note:** This legacy type is backed by a float, rather than an integer. It is supported for backwards compatibility reasons only. Use the `Integer` type instead.  
**Float** |  `_ExampleName ("Float display name", Float) = 0.5`  
  
`_ExampleName ("Float with range", Range(0.0, 1.0)) = 0.5` | The maximum and minimum values for the range slider are inclusive.  
**Texture2D** |  `_ExampleName ("Texture2D display name", 2D) = "" {}`  
  
`_ExampleName ("Texture2D display name", 2D) = "red" {}` | Put the following values in the default value string to use one of Unity’s built-in textures: “white” (RGBA: 1,1,1,1), “black” (RGBA: 0,0,0,1), “gray” (RGBA: 0.5,0.5,0.5,1), “bump” (RGBA: 0.5,0.5,1,1) or “red” (RGBA: 1,0,0,1).  
  
If you leave the string empty or enter an invalid value, it defaults to
“gray”.  
  
**Note:** these default textures are not visible in the Inspector.  
**Texture2DArray** | `_ExampleName ("Texture2DArray display name", 2DArray) = "" {}` | For more information, see [Texture arrays](class-Texture2DArray.html).  
**Texture3D** | `_ExampleName ("Texture3D", 3D) = "" {}` | The default value is a “gray” (RGBA: 0.5,0.5,0.5,1) texture.  
****Cubemap** A collection of six square textures that can represent the
reflections in an environment or the skybox drawn behind your geometry. The
six squares form the faces of an imaginary cube that surrounds an object; each
face represents the view along the directions of the world axes (up, down,
left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap)** | `_ExampleName ("Cubemap", Cube) = "" {}` | The default value is a “gray” (RGBA: 0.5,0.5,0.5,1) texture.  
**CubemapArray** | `_ExampleName ("CubemapArray", CubeArray) = "" {}` | See [Cubemap arrays](class-CubemapArray.html).  
**Color** | `_ExampleName("Example color", Color) = (.25, .5, .5, 1)` | This maps to a float4 in your shader code.  
  
The Material Inspector displays a color picker. If you would rather edit the
values as four individual floats, use the Vector type.  
**Vector** | `_ExampleName ("Example vector", Vector) = (.25, .5, .5, 1)` | This maps to a float4 in your shader code.  
  
The Material Inspector displays four individual float fields. If you would
rather edit the values using a color picker, use the Color type.  
  
#### Reserved material property names

Unity has some reserved names for material properties. When you create a
material property with one of these names, Unity performs predefined
operations. Do not use these names unless you intend to use this
functionality.

**Name** | **Example syntax** | **Function**  
---|---|---  
_TransparencyLM | `_TransparencyLM ("Transmissive Texture", 2D) = "white" {}` | Enables custom RGB transparency during lightmapping.  
  
For more information, see [Lightmapping and shaders](MetaPass.html).  
  
### Material property attributes

Material property declarations can have an optional attribute that tells Unity
how to handle them.

In addition to the attributes listed here, you can use the same syntax to add
a [MaterialPropertyDrawer](../ScriptReference/MaterialPropertyDrawer.html) to
a material property. These let you control how material properties appear in
the **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

**Attribute** | **Function**  
---|---  
`[Gamma]` | Indicates that a float or vector property uses sRGB values, which means that it must be converted along with other sRGB values if the color space in your project requires this. For more information, see [Properties in Shader Programs](SL-PropertiesInPrograms.html).  
`[HDR]` | Indicates that a texture or color property uses [high dynamic range (HDR)](hdr-landing.html) values.  
  
For texture properties, the Unity Editor displays a warning if an LDR texture
is assigned. For color properties, the Unity Editor uses the HDR color picker
to edit this value.  
`[HideInInspector]` | Tells the Unity Editor to hide this property in the Inspector.  
`[MainTexture]` | Sets the main texture for a Material, which you can access using [Material.mainTexture](../ScriptReference/Material-mainTexture.html).  
  
By default, Unity considers a texture with the property name name `_MainTex`
as the main texture. Use this attribute if your texture has a different
property name, but you want Unity to consider it the main texture.  
  
If you use this attribute more than once, Unity uses the first property and
ignores subsequent ones.  
  
**Note:** When you set the main texture using this attribute, the texture is
not visible in the Game view when you use the texture mipmap streaming
debugging view mode, or a custom debug tool.  
`[MainColor]` | Sets the main color for a Material, which you can access using [Material.color](../ScriptReference/Material-color.html).  
  
By default, Unity considers a color with the property name name `_Color` as
the main color. Use this attribute if your color has a different property
name, but you want Unity to consider it the main color. If you use this
attribute more than once, Unity uses the first property and ignores subsequent
ones.  
`[NoScaleOffset]` | Tells the Unity Editor to hide tiling and offset fields for this texture property.  
`[Normal]` | Indicates that a texture property expects a normal map.  
  
The Unity Editor displays a warning if you assign an incompatible texture.  
`[PerRendererData]` | Indicates that a texture property will be coming from per-renderer data in the form of a [MaterialPropertyBlock](../ScriptReference/MaterialPropertyBlock.html).  
  
The Material inspector shows these properties as read-only.  
  
## Additional resources

  * [Adding material properties to shaders](writing-shader-change-properties.html)

[](SL-Shader.html)

Shader block in ShaderLab reference

[](SL-Fallback.html)

Fallback block in ShaderLab reference

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

